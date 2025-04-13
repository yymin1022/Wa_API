import datetime
import re

from bs4 import BeautifulSoup

import base64
import json
import os

import certifi
import dotenv
import requests

from util.cipher_util import DESAdapter

dotenv.load_dotenv()

def message_command(message, room, sender):
    if message.startswith("!base64d"):
        return message_base64_decode(message)
    if message.startswith("!base64e"):
        return message_base64_encode(message)
    if message.startswith("!날씨"):
        loc = message.split("!날씨")
        if len(loc) == 1:
            return message_weather()
        else:
            lat, lon = get_weather_lat_lon(loc)
            return message_weather_latlon(lat, lon, loc)
    if message.startswith("!뉴스"):
        return message_fake_news(message)
    if message.startswith("!메모"):
        return message_memo(message, sender)
    if message.startswith("!촙촙"):
        return message_chopchop(message)
    if message.startswith("!환율"):
        return message_currency()
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
    str_status = soup.find('td', text='업무진행상황').find_next_sibling('td').get_text(strip=True)

    str_message = f"업무진행상황: {str_status}\n" \
                    f"통신사/유형: {soup.find('td', text='통신사/유형').find_next_sibling('td').get_text(strip=True)}\n" \
                    f"모델명: {soup.find('td', text='모델명').find_next_sibling('td').get_text(strip=True)}\n" \
                    f"색상: {soup.find('td', text='색상').find_next_sibling('td').get_text(strip=True)}\n" \
                    f"요금제: {soup.find('td', text='요금제').find_next_sibling('td').get_text(strip=True)}\n" \
                    f"약정: {soup.find('td', text='약정').find_next_sibling('td').get_text(strip=True)}\n"

    if str_status == "개통완료":
        str_message += f"회선유지기간: {soup.find('td', text='회선유지기간').find_next_sibling('td').get_text(strip=True)}\n" \
                        f"요금제유지기간: {soup.find('td', text='요금제유지기간').find_next_sibling('td').get_text(strip=True)}"
    else:
        str_message += f"배송정보: {soup.find('td', text='배송등록').find_next_sibling('td').get_text(strip=True)}"

    return str_message

def message_currency():
    today_date = datetime.date.today()
    currency_url = f"http://www.smbs.biz/Flash/TodayExRate_flash.jsp?tr_date={today_date.strftime('%Y-%m-%d')}"

    request_session = requests.Session()
    request_session.mount(currency_url, DESAdapter())
    response = request_session.get(currency_url, verify=certifi.where())

    parse_data = re.findall(r"([A-Z]+)=([\d.,]+)", response.text)
    str_message = f"{today_date.strftime('%m월 %d일')} 환율 정보"
    for data in parse_data:
        str_message += f"\\n1 {data[0]} : {data[1].replace(',', '')} KRW"

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
    return None

def message_weather():
    app_id = "ea9e5f8d8e4aa2c798f8eb78f361d1b4"
    api_id = 1835847
    weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?id={api_id}&appid={app_id}"

    request_session = requests.Session()
    request_session.mount(weather_api_url, DESAdapter())
    text = request_session.get(weather_api_url, verify=certifi.where())
    text = text.text
    json_data = json.loads(text)

    try:
        return f"현재온도: {str(json_data['main']['temp'])}K\\n구름: {str(json_data['clouds']['all'])}%\\n"\
                  f"압력: {str(json_data['main']['pressure'])}Pa\\n습도: {str(json_data['main']['humidity'])}%\\m"\
                  f"서울의 날씨 {str(json_data['weather']['description'])}"
    except KeyError:
        return None

def message_weather_latlon(lat, lon, loc):
    apikey = os.environ.get("WEATHER_API_KEY")
    weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}"

    request_session = requests.Session()
    request_session.mount(weather_api_url, DESAdapter())
    text = request_session.get(weather_api_url, verify=certifi.where())
    text = text.text
    json_data = json.loads(text)

    try:
        return f"현재온도: {str(json_data['main']['temp'])}K\\n구름: {str(json_data['clouds']['all'])}%\\n"\
                  f"압력: {str(json_data['main']['pressure'])}Pa\\n습도: {str(json_data['main']['humidity'])}%\\m"\
                  f"{loc}의 날씨 {str(json_data['weather']['description'])}"
    except KeyError:
        return None

def get_weather_lat_lon(location):
    apikey = "ea9e5f8d8e4aa2c798f8eb78f361d1b4"
    weather_api_url = "http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={key}".format(city_name=location, key=apikey)

    request_session = requests.Session()
    request_session.mount(weather_api_url, DESAdapter())
    text = request_session.get(weather_api_url, verify=certifi.where())
    text = text.text
    json_data = json.loads(text)

    try:
        lat = json_data["lat"]
        lon = json_data["lon"]

        if "cod" in json_data:
            return "지역이 잘못되었습니다", "지역이 잘못되었습니다"
        else:
            return lat, lon
    except TypeError:
        return None, None