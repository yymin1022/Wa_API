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
    todayDate = datetime.date.today()
    numDate = todayDate.weekday()

    if numDate >= 5:
        return "금일은 학식을 운영하지 않습니다"

    mealUrl = "https://www.anyang.ac.kr/main/activities/school-cafeteria.do"

    requestSession = requests.Session()
    requestSession.mount(mealUrl, DESAdapter())
    mealResponse = requestSession.get(mealUrl, verify=certifi.where()).text

    bs = BeautifulSoup(mealResponse, 'html.parser')
    mealData = json.loads(bs.find("input", id="mealList").get("value"))

    strDate = ["mon", "tue", "wed", "thu", "fri"]
    strMessage = f"{todayDate.strftime('%Y.%m.%d.')} 안양대학교 학식메뉴\n"
    strMessage += f"{mealData[f'{strDate[numDate]}Main02']}"
    for item in mealData[f'{strDate[numDate]}Sub02']:
        strMessage += f"\n{item}"

    return strMessage

def message_meal_cau(mealTypeID, isTomorrow):
    if mealTypeID == "10":
        mealType = "조식"
    elif mealTypeID == "20":
        mealType = "중식"
    elif mealTypeID == "40":
        mealType = "석식"
    else:
        strMessage = "중앙대학교 학식메뉴\n\n사용법 : 학식 키워드와 함께 아침 / 점심 / 저녁 / 조식 / 중식 / 석식 키워드 언급"
        return strMessage

    mealUrl = "https://mportal.cau.ac.kr/portlet/p005/p005.ajax"
    mealData = {
        "daily": (1 if isTomorrow else 0),
        "tabs": "1",
        "tabs2": mealTypeID
    }

    requestSession = requests.Session()
    requestSession.mount(mealUrl, DESAdapter())
    mealResponse = requestSession.post(mealUrl, json=mealData, verify=certifi.where()).json()
    mealList = mealResponse["list"]

    strMessage = f"{mealList[0]['date']}. 중앙대학교 학식메뉴({mealType})\n"
    for mealItem in mealList:
        strMenu = mealItem['menuDetail']
        if strMenu == None:
            strMenu = "정보가 없습니다."
        strMessage += f"\n{mealItem['rest']} : {strMenu}"

    return strMessage

def message_meal_daelim():
    todayDate = datetime.date.today()
    mealUrl = "https://www.daelim.ac.kr/ajaxf/FrBistroSvc/BistroCarteInfo.do"
    mealInput = f"MENU_ID=1470&BISTRO_SEQ=1&START_DAY={todayDate.strftime('%Y.%m.%d')}&END_DAY={todayDate.strftime('%Y.%m.%d')}"

    mealHeader = {"Content-Type": "application/x-www-form-urlencoded"}
    requestSession = requests.Session()
    requestSession.mount(mealUrl, DESAdapter())
    mealResponse = requestSession.post(mealUrl, data=mealInput, headers=mealHeader, verify=certifi.where()).json()

    strDate = todayDate.weekday() + 1
    strMessage = f"{todayDate.strftime('%Y.%m.%d.')} 대림대학교 학식메뉴\n"
    if strDate < 6:
        for idx in range(1, 10):
            try:
                strMessage += f">> {mealResponse['data'][f'CNM1{idx}']} <<\n{mealResponse['data'][f'CCT{strDate}{idx}'].strip()}\n"
            except:
                pass
    else:
        strMessage += "금일은 학식을 운영하지 않습니다"

    return strMessage

def message_meal_nsu():
    try:
        strMessage = ""
        MealList0 = []
        MealList1 = []
        MealList2 = []

        day = datetime.date.today().weekday()
        if day == 0:
            pass
        elif day > 0 and day <= 4:
            day += 2
        else:
            raise

        strUrl = "https://nsu.ac.kr/api/user/board/getBoardContentSummaryList"
        bokji_data = "boardIdList=467&includeProperties=1&parentBoardContentId=-1&isAvailable=1&isPrivate=0&isAlwaysOnTop=0&isDeleted=0&orderByCode=4"
        cafe_data = "boardIdList=468&includeProperties=1&parentBoardContentId=-1&isAvailable=1&isPrivate=0&isAlwaysOnTop=0&isDeleted=0&orderByCode=4"

        bokji_response = requests.post(strUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=bokji_data).json()
        bokji_response = dict(bokji_response)
        mealDate = bokji_response["body"]["list"][0]["title"]
        bokji_list = bokji_response["body"]["list"][0]["properties"]["food_list"][0]
        for mealData in bokji_list.items():
            MealList0.append((f"{mealData[1]}\n"))

        cafe_response = requests.post(strUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=cafe_data).json()
        cafe_response = dict(cafe_response)
        cafe0_list = cafe_response["body"]["list"][0]["properties"]["food_list"][0]
        cafe1_list = cafe_response["body"]["list"][0]["properties"]["food_list"][1]
        for mealData in cafe0_list.items():
            MealList1.append((f"{mealData[1]}\n"))

        for mealData in cafe1_list.items():
            MealList2.append((f"{mealData[1]}\n"))

        strMessage = "남서울대학교 " + mealDate + " 식단표" + "\n" + ">> 천원의 아침밥 <<\n" + MealList1[day] + "\n>> 오늘의 메뉴 <<\n" + MealList0[day] + "\n>> 멀베리 <<\n" + MealList2[day]
    except:
        strMessage = "오늘은 학식을 운영하지 않습니다."
    return strMessage