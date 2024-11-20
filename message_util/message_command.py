from bs4 import BeautifulSoup

import base64
import json
import os

import certifi
import requests

from util.cipher_util import DESAdapter


def message_command(message, room, sender):
    if "!base64d" in message:
        return message_base64_decode(message)
    if "!base64e" in message:
        return message_base64_encode(message)
    if "!날씨" in message:
        loc = message.split("!날씨")
        if len(loc) == 1:
            return message_weather()
        else:
            lat, lon = get_weather_lat_lon(loc)
            return message_weather_latlon(lat, lon, loc)
    if "!뉴스" in message:
        return message_fake_news(message)
    if "!메모" in message:
        return message_memo(message, sender)
    if "!촙촙" in message:
        return message_chopchop(message)
    return None

def message_base64_decode(message):
    msg = message.split("!base64d ")
    return base64.b64decode(msg[1]).decode("utf8")

def message_base64_encode(message):
    msg = message.split("!base64e ")[1]
    return base64.b64encode(msg.encode("utf8")).decode("utf8")

def message_chopchop(message):
    chopchop_url = "http://check.bboo.co.kr/check.bboo.co.kr.html"

    if len(message.split()) != 3:
        return "사용법: !촙촙 <가입자 이름> <회선 번호>"

    r_name = message.split()[1]
    r_hp = message.split()[2]

    data = {
        "r_name": r_name,
        "r_hp": r_hp
    }

    request_session = requests.Session()
    request_session.mount(chopchop_url, DESAdapter())
    response = request_session.post(chopchop_url, data=data)

    if "등록된 데이터가 없습니다" in response.text:
        return "등록된 데이터가 없습니다. 다시 확인해주세요."

    soup = BeautifulSoup(response.text, "html.parser")
    str_status = soup.find("td", text="업무진행상황").find_next_sibling("td").get_text(strip=True)

    str_message = f"업무진행상황: {str_status}\n" \
                    f"통신사/유형: {soup.find("td", text="통신사/유형").find_next_sibling("td").get_text(strip=True)}\n" \
                    f"모델명: {soup.find("td", text="모델명").find_next_sibling("td").get_text(strip=True)}\n" \
                    f"색상: {soup.find("td", text="색상").find_next_sibling("td").get_text(strip=True)}\n" \
                    f"요금제: {soup.find("td", text="요금제").find_next_sibling("td").get_text(strip=True)}\n" \
                    f"약정: {soup.find("td", text="약정").find_next_sibling("td").get_text(strip=True)}\n"

    if str_status == "개통완료":
        str_message += f"회선유지기간: {soup.find("td", text="회선유지기간").find_next_sibling("td").get_text(strip=True)}\n" \
                        f"요금제유지기간: {soup.find("td", text="요금제유지기간").find_next_sibling("td").get_text(strip=True)}"
    else:
        str_message += f"배송정보: {soup.find("td", text="배송등록").find_next_sibling("td").get_text(strip=True)}"

    return str_message



def message_fake_news(message):
    fake_news_url = os.environ["FAKE_NEWS_URL"]
    keyword = message.split("!뉴스:")[1]
    request_session = requests.Session()
    request_session.mount(fake_news_url, DESAdapter())
    response = request_session.post(fake_news_url, json={"message_util":keyword, "len":64}, verify=certifi.where())
    return "\\m".join(response.text.split("\n")[2:-4])

def message_memo(message, sender):
    message = message.replace("!메모", "").strip()

    if len(message) != 0:
        if os.path.isfile("mem.json"):
            with open("mem.json", "r", encoding="utf-8") as f:
                mem_dict = json.load(f)
        else:
            mem_dict = {}

        mem_dict[sender] = message
        json_data = json.dumps(mem_dict, ensure_ascii=False, indent=4)

        with open("mem.json", "w", encoding="utf-8") as f:
            f.write(json_data)
    else:
        pass

    str_message = ""
    return str_message

def message_weather():
    app_id = "ea9e5f8d8e4aa2c798f8eb78f361d1b4"
    api_id = 1835847
    weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?id={api_id}&appid={app_id}"

    request_session = requests.Session()
    request_session.mount(weather_api_url, DESAdapter())
    text = request_session.get(weather_api_url, verify=certifi.where())
    text = text.text
    json_data = json.loads(text)

    str_message = "현재온도: {}K\\n구름: {}%".format(str(json_data["main"]["temp"]), str(json_data["clouds"]["all"]))
    str_message +="\\n압력: {}Pa\\n습도: {}%".format(str(json_data["main"]["pressure"]), str(json_data["main"]["humidity"]))
    str_message +="\\m서울의 날씨 {}".format(str(json_data["weather"]["description"]))
    return str_message

def message_weather_latlon(lat, lon, loc):
    apikey = "ea9e5f8d8e4aa2c798f8eb78f361d1b4"
    weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}"

    request_session = requests.Session()
    request_session.mount(weather_api_url, DESAdapter())
    text = request_session.get(weather_api_url, verify=certifi.where())
    text = text.text
    json_data = json.loads(text)

    str_message = "현재온도: {}K\\n구름: {}%".format(str(json_data["main"]["temp"]), str(json_data["clouds"]["all"]))
    str_message +="\\n압력: {}Pa\\n습도: {}%".format(str(json_data["main"]["pressure"]), str(json_data["main"]["humidity"]))
    str_message +="\\m{}의 날씨 {}".format(loc, str(json_data["weather"]["description"]))

    return str_message

def get_weather_lat_lon(location):
    apikey = "ea9e5f8d8e4aa2c798f8eb78f361d1b4"
    weather_api_url = "http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={key}".format(city_name=location, key=apikey)

    request_session = requests.Session()
    request_session.mount(weather_api_url, DESAdapter())
    text = request_session.get(weather_api_url, verify=certifi.where())
    text = text.text
    json_data = json.loads(text)

    lat = json_data["lat"]
    lon = json_data["lon"]

    if "cod" in json_data:
        return "지역이 잘못되었습니다", "지역이 잘못되었습니다"
    else:
        return lat, lon