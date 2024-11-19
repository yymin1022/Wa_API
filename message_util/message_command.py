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
        if(loc == "!날씨"):
            return message_weather()
        else:
            lat, lon = get_weather_lat_lon(loc)
            return message_weather(lat, lon)
    if "!뉴스" in message:
        return message_fake_news(message)
    if "!메모" in message:
        return message_memo(message, sender)
    if "!촙촙" in message:
        return message_chopchop(message)
    return None

def message_base64_decode(message):
    msg = message.split("!base64d ")
    return base64.b64decode(msg[1]).decode('utf8')

def message_base64_encode(message):
    msg = message.split("!base64e ")[1]
    return base64.b64encode(msg.encode('utf8')).decode('utf8')

def message_chopchop(message):
    chopchopUrl = 'http://check.bboo.co.kr/check.bboo.co.kr.html'

    if len(message.split()) != 3:
        return "사용법: !촙촙 <가입자 이름> <회선 번호>"

    r_name = message.split()[1]
    r_hp = message.split()[2]

    data = {
        'r_name': r_name,
        'r_hp': r_hp
    }

    requestSession = requests.Session()
    requestSession.mount(chopchopUrl, DESAdapter())
    response = requestSession.post(chopchopUrl, data=data)

    if "등록된 데이터가 없습니다" in response.text:
        return "등록된 데이터가 없습니다. 다시 확인해주세요."

    soup = BeautifulSoup(response.text, "html.parser")
    strStatus = soup.find("td", text="업무진행상황").find_next_sibling("td").get_text(strip=True)

    strMessage = f"업무진행상황: {strStatus}\n" \
                    f"통신사/유형: {soup.find('td', text='통신사/유형').find_next_sibling('td').get_text(strip=True)}\n" \
                    f"모델명: {soup.find('td', text='모델명').find_next_sibling('td').get_text(strip=True)}\n" \
                    f"색상: {soup.find('td', text='색상').find_next_sibling('td').get_text(strip=True)}\n" \
                    f"요금제: {soup.find('td', text='요금제').find_next_sibling('td').get_text(strip=True)}\n" \
                    f"약정: {soup.find('td', text='약정').find_next_sibling('td').get_text(strip=True)}\n"

    if strStatus == "개통완료":
        strMessage += f"회선유지기간: {soup.find('td', text='회선유지기간').find_next_sibling('td').get_text(strip=True)}\n" \
                        f"요금제유지기간: {soup.find('td', text='요금제유지기간').find_next_sibling('td').get_text(strip=True)}"
    else:
        strMessage += f"배송정보: {soup.find('td', text='배송등록').find_next_sibling('td').get_text(strip=True)}"

    return strMessage



def message_fake_news(message):
    fake_news_url = os.environ['FAKE_NEWS_URL']
    keyword = message.split("!뉴스:")[1]
    requestSession = requests.Session()
    requestSession.mount(fake_news_url, DESAdapter())
    response = requestSession.post(fake_news_url, json={'message_util':keyword, 'len':64}, verify=certifi.where())
    return '\\m'.join(response.text.split('\n')[2:-4])

def message_memo(message, sender):
    message = message.replace("!메모", "").strip()

    if len(message) != 0:
        if os.path.isfile("mem.json"):
            with open('mem.json', 'r', encoding='utf-8') as f:
                mem_dict = json.load(f)
        else:
            mem_dict = {}

        mem_dict[sender] = message
        json_data = json.dumps(mem_dict, ensure_ascii=False, indent=4)

        with open('mem.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
    else:
        pass

    strMessage = ""
    return strMessage

def message_weather():
    appid = "ea9e5f8d8e4aa2c798f8eb78f361d1b4"
    id = 1835847
    weatherAPIUrl = "https://api.openweathermap.org/data/2.5/weather?id={id}&appid={appid}".format(id=id, appid = appid)

    requestSession = requests.Session()
    requestSession.mount(weatherAPIUrl, DESAdapter())
    text = requestSession.get(weatherAPIUrl, verify=certifi.where())
    text = text.text
    jsonData = json.loads(text)

    strMessage = "현재온도: {}K\\n구름: {}%".format(str(jsonData["main"]["temp"]), str(jsonData["clouds"]["all"]))
    strMessage +="\\n압력: {}Pa\\n습도: {}%".format(str(jsonData["main"]["pressure"]), str(jsonData["main"]["humidity"]))
    strMessage +="\\m서울의 날씨 {}".format(str(jsonData["weather"]["description"]))
    return strMessage

def message_weather(lat, lon, loc):
    apikey = "ea9e5f8d8e4aa2c798f8eb78f361d1b4"
    weatherAPIUrl = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}".format(lat=lat, lon=lon, key = apikey)

    requestSession = requests.Session()
    requestSession.mount(weatherAPIUrl, DESAdapter())
    text = requestSession.get(weatherAPIUrl, verify=certifi.where())
    text = text.text
    jsonData = json.loads(text)

    strMessage = "현재온도: {}K\\n구름: {}%".format(str(jsonData["main"]["temp"]), str(jsonData["clouds"]["all"]))
    strMessage +="\\n압력: {}Pa\\n습도: {}%".format(str(jsonData["main"]["pressure"]), str(jsonData["main"]["humidity"]))
    strMessage +="\\m{}의 날씨 {}".format(loc, str(jsonData["weather"]["description"]))

    return strMessage

def get_weather_lat_lon(location):
    apikey = "ea9e5f8d8e4aa2c798f8eb78f361d1b4"
    weatherAPIUrl = "http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={key}".format(city_name=location, key=apikey)

    requestSession = requests.Session()
    requestSession.mount(weatherAPIUrl, DESAdapter())
    text = requestSession.get(weatherAPIUrl, verify=certifi.where())
    text = text.text
    jsonData = json.loads(text)

    lat = jsonData["lat"]
    lon = jsonData["lon"]

    if "cod" in jsonData:
        return "지역이 잘못되었습니다", "지역이 잘못되었습니다"
    else:
        return lat, lon