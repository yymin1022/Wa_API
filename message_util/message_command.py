import datetime
import re

from bs4 import BeautifulSoup, Comment

import base64
import json
import os

import certifi
import dotenv
import requests

from models import WaMessage

dotenv.load_dotenv()

def message_command(wa_message: WaMessage):
    message = wa_message.msg
    room = wa_message.room
    sender = wa_message.sender
    if message.startswith("!base64d"):
        return message_base64_decode(message)
    if message.startswith("!base64e"):
        return message_base64_encode(message)

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

    response = requests.post(chopchop_url, data=data)

    if "등록된 데이터가 없습니다" in response.text:
        return "등록된 데이터가 없습니다. 다시 확인해주세요."

    soup = BeautifulSoup(response.text, "html.parser")

    def get_td_value(s, label):
        target = s.find('td', string=lambda t: t and label in t)
        if target:
            sibling = target.find_next_sibling('td')
            if sibling:
                return sibling.get_text(strip=True)
        return None

    str_status = get_td_value(soup, '업무진행상황')
    if str_status is None:
        str_status = '알수없음'

    str_message = f"업무진행상황: {str_status}\n" \
                  f"통신사/유형: {get_td_value(soup, '통신사/유형') or '알수없음'}\n" \
                  f"모델명: {get_td_value(soup, '모델명') or '알수없음'}\n" \
                  f"색상: {get_td_value(soup, '색상') or '알수없음'}\n" \
                  f"요금제: {get_td_value(soup, '요금제') or '알수없음'}\n" \
                  f"약정: {get_td_value(soup, '약정') or '알수없음'}\n"

    maint_period = get_td_value(soup, '회선유지기간')
    plan_period = get_td_value(soup, '요금제유지기간')

    if not maint_period or not plan_period:
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            if "회선유지기간" in comment or "요금제유지기간" in comment:
                c_soup = BeautifulSoup(comment, "html.parser")
                if not maint_period:
                    maint_period = get_td_value(c_soup, '회선유지기간')
                if not plan_period:
                    plan_period = get_td_value(c_soup, '요금제유지기간')

    if str_status == "개통완료":
        str_message += f"회선유지기간: {maint_period or '정보없음'}\n" \
                        f"요금제유지기간: {plan_period or '정보없음'}"
    else:
        str_message += f"배송정보: {get_td_value(soup, '배송정보') or get_td_value(soup, '배송등록') or '정보없음'}"

    return str_message.strip()

def message_currency():
    today_date = datetime.date.today()
    currency_url = f"http://www.smbs.biz/Flash/TodayExRate_flash.jsp?tr_date={today_date.strftime('%Y-%m-%d')}"

    response = requests.get(currency_url, verify=certifi.where())

    parse_data = re.findall(r"([A-Z]+)=([\d.,]+)", response.text)
    str_message = f"{today_date.strftime('%m월 %d일')} 환율 정보"
    for data in parse_data:
        str_message += f"\\n1 {data[0]} : {data[1].replace(',', '')} KRW"

    return str_message

def message_fake_news(message):
    fake_news_url = os.environ["FAKE_NEWS_URL"]
    keyword = message.split("!뉴스:")[1]
    response = requests.post(fake_news_url, json={"message_util":keyword, "len":64}, verify=certifi.where())
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
