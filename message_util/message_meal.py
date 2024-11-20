from bs4 import BeautifulSoup

import datetime
import json

import certifi
import requests

from util.cipher_util import DESAdapter


def message_meal(message, room, sender):
    if "학식" in message:
        if "아침" in message or "조식" in message:
            return message_meal_cau("10", "내일" in message)
        elif "점심" in message or "중식" in message:
            return message_meal_cau("20", "내일" in message)
        elif "저녁" in message or "석식" in message:
            return message_meal_cau("40", "내일" in message)
        elif "대림대" in message:
            return message_meal_daelim()
        elif "안양대" in message:
            return message_meal_anyang()
        elif "남샤" in message:
            return message_meal_nsu()
        else:
            return message_meal_cau("", False)

def message_meal_anyang():
    today_date = datetime.date.today()
    num_date = today_date.weekday()

    if num_date >= 5:
        return "금일은 학식을 운영하지 않습니다"

    meal_url = "https://www.anyang.ac.kr/main/activities/school-cafeteria.do"

    request_session = requests.Session()
    request_session.mount(meal_url, DESAdapter())
    meal_response = request_session.get(meal_url, verify = certifi.where()).text

    bs = BeautifulSoup(meal_response, "html.parser")
    meal_data = json.loads(bs.find("input", id = "mealList").get("value"))

    str_date = ["mon", "tue", "wed", "thu", "fri"]
    str_message = f"{today_date.strftime("%Y.%m.%d.")} 안양대학교 학식메뉴\n"
    str_message += f"{meal_data[f"{str_date[num_date]}Main02"]}"
    for item in meal_data[f"{str_date[num_date]}Sub02"]:
        str_message += f"\n{item}"

    return str_message

def message_meal_cau(meal_type_id, is_tomorrow):
    if meal_type_id == "10":
        meal_type = "조식"
    elif meal_type_id == "20":
        meal_type = "중식"
    elif meal_type_id == "40":
        meal_type = "석식"
    else:
        str_message = "중앙대학교 학식메뉴\n\n사용법 : 학식 키워드와 함께 아침 / 점심 / 저녁 / 조식 / 중식 / 석식 키워드 언급"
        return str_message

    meal_url = "https://mportal.cau.ac.kr/portlet/p005/p005.ajax"
    meal_data = {
        "daily": (1 if is_tomorrow else 0),
        "tabs": "1",
        "tabs2": meal_type_id
    }

    request_session = requests.Session()
    request_session.mount(meal_url, DESAdapter())
    meal_response = request_session.post(meal_url, json=meal_data, verify=certifi.where()).json()
    meal_list = meal_response["list"]

    str_message = f"{meal_list[0]["date"]}. 중앙대학교 학식메뉴({meal_type})\n"
    for meal_item in meal_list:
        str_menu = meal_item["menuDetail"]
        if str_menu is None:
            str_menu = "정보가 없습니다."
        str_message += f"\n{meal_item["rest"]} : {str_menu}"

    return str_message

def message_meal_daelim():
    today_date = datetime.date.today()

    meal_header = {"Content-Type": "application/x-www-form-urlencoded"}
    meal_input = f"MENU_ID=1470&BISTRO_SEQ=1&START_DAY={today_date.strftime("%Y.%m.%d")}&END_DAY={today_date.strftime("%Y.%m.%d")}"
    meal_url = "https://www.daelim.ac.kr/ajaxf/FrBistroSvc/BistroCarteInfo.do"

    request_session = requests.Session()
    request_session.mount(meal_url, DESAdapter())
    meal_response = request_session.post(meal_url, data=meal_input, headers=meal_header, verify=certifi.where()).json()

    str_date = today_date.weekday() + 1
    str_message = f"{today_date.strftime("%Y.%m.%d.")} 대림대학교 학식메뉴\n"
    if str_date < 6:
        for idx in range(1, 10):
            try:
                str_message += f">> {meal_response["data"][f"CNM1{idx}"]} <<\n{meal_response["data"][f"CCT{str_date}{idx}"].strip()}\n"
            except (IndexError, TypeError):
                pass
    else:
        str_message += "금일은 학식을 운영하지 않습니다"

    return str_message

def message_meal_nsu():
    try:
        meal_list_0 = []
        meal_list_1 = []
        meal_list_2 = []

        day = datetime.date.today().weekday()
        if day == 0:
            pass
        elif 0 < day <= 4:
            day += 2
        else:
            raise IndexError

        meal_url = "https://nsu.ac.kr/api/user/board/getBoardContentSummaryList"
        bokji_data = "boardIdList=467&includeProperties=1&parentBoardContentId=-1&isAvailable=1&isPrivate=0&isAlwaysOnTop=0&isDeleted=0&orderByCode=4"
        cafe_data = "boardIdList=468&includeProperties=1&parentBoardContentId=-1&isAvailable=1&isPrivate=0&isAlwaysOnTop=0&isDeleted=0&orderByCode=4"

        bokji_response = requests.post(meal_url, headers={"Content-Type": "application/x-www-form-urlencoded"}, data=bokji_data).json()
        bokji_response = dict(bokji_response)
        meal_date = bokji_response["body"]["list"][0]["title"]
        bokji_list = bokji_response["body"]["list"][0]["properties"]["food_list"][0]
        for meal_data in bokji_list:
            meal_list_0.append(f"{meal_data[1]}\n")

        cafe_response = requests.post(meal_url, headers={"Content-Type": "application/x-www-form-urlencoded"}, data=cafe_data).json()
        cafe_response = dict(cafe_response)
        cafe0_list = cafe_response["body"]["list"][0]["properties"]["food_list"][0]
        cafe1_list = cafe_response["body"]["list"][0]["properties"]["food_list"][1]
        for meal_data in cafe0_list:
            meal_list_1.append(f"{meal_data[1]}\n")

        for meal_data in cafe1_list:
            meal_list_2.append(f"{meal_data[1]}\n")

        str_message = f"남서울대학교 {meal_date} 식단표\n>> 천원의 아침밥 <<\n{meal_list_1[day]}\n>> 오늘의 메뉴 <<\n{meal_list_0[day]}\n>> 멀베리 <<\n{meal_list_2[day]}"
    except (IndexError, TypeError):
        str_message = "오늘은 학식을 운영하지 않습니다."
    return str_message