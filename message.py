from message_util.message_command import message_command
from message_util.message_cry_laugh_stress import message_cry_laugh_stress
from message_util.message_friends import message_friends
from message_util.message_gemini import message_gemini
from message_util.message_graduate import message_graduate
from message_util.message_logistics import message_logistics
from message_util.message_meal import message_meal
from message_util.message_meme import message_meme
from message_util.message_memory import message_memory
from message_util.message_onoff import message_onoff
from util.cipher_util import DESAdapter

import certifi
import datetime
import requests


def getReplyMessage(message, room, sender):
    # Special Command Messages
    result_message = message_command(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_gemini(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_logistics(message, room, sender)
    if result_message is not None:
        return result_message

    # Normal Text Messages
    result_message = message_cry_laugh_stress(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_friends(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_graduate(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_meal(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_meme(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_memory(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_onoff(message, room, sender)
    if result_message is not None:
        return result_message

    if "학사일정" in message:
        strResult = messageCAUCalendar()
    elif "열람실" in message:
        if "서울" in message:
            strResult = messageCAULibrary("1")
        elif "법학" in message:
            strResult = messageCAULibrary("2")
        elif "안성" in message:
            strResult = messageCAULibrary("3")
        elif "남샤" in message:
            strResult = messageNSULibrary()
        else:
            strResult = messageCAULibrary("")
    elif "비트코인" in message:
        strResult = messageBitcoin()
    return strResult

def messageBitcoin():
    strMessage = ""

    requestSession = requests.Session()
    url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
    requestSession.mount(url, DESAdapter())

    try:
        response = requestSession.get(url, verify=certifi.where())
        response.raise_for_status()
        data = response.json()
        current_price = data[0]['trade_price']
        strMessage = f"와! 비트코인 현재가 : {current_price}원! 지금 사요?"
    except requests.exceptions.RequestException as e:
        strMessage = "비트코인 가격을 불러오는 중 오류가 발생했습니다."

    return strMessage

def messageCAUCalendar():
    strMessage = ""

    calData = datetime.date.today()
    calMonth = calData.month
    calYear = calData.year

    calData = {
        "active": True,
        "month": calMonth,
        "title": f"{calMonth}월",
        "year": calYear
    }
    calUrl = "https://mportal.cau.ac.kr/portlet/p014/p014List.ajax"

    requestSession = requests.Session()
    requestSession.mount(calUrl, DESAdapter())
    calResponse = eval(requestSession.post(calUrl, json=calData, verify=certifi.where()).json())
    calList = calResponse["data"]

    strMessage = f"중앙대학교 {calMonth}월 학사일정\n"
    for calItem in calList:
        strMessage += f"\n{calItem['TITLE']} : {calItem['TDAY']}"

    return strMessage

def messageCAULibrary(libTypeID):
    strMessage = libTypeID

    libData = {
       "tabNo": libTypeID
    }
    libType = ""
    libUrl = "https://mportal.cau.ac.kr/portlet/p017/p017.ajax"

    if libTypeID == "1":
       libType = "서울"
    elif libTypeID == "2":
       libType = "법학"
    elif libTypeID == "3":
       libType = "안성"
    else:
        strMessage = "중앙대학교 열람실 좌석현황\n\n사용법 : 열람실 키워드와 함께 서울 / 안성 / 법학 키워드 언급"
        return strMessage

    requestSession = requests.Session()
    requestSession.mount(libUrl, DESAdapter())
    libResponse = requestSession.post(libUrl, json=libData, verify=certifi.where()).json()

    libList = libResponse["gridData"]

    strMessage = f"중앙대학교 열람실 좌석현황({libType})\n"
    for libItem in libList:
       strMessage += f"\n{libItem['roomName']} : 여석 {libItem['remainCnt']}석 ({libItem['useCnt']}석 사용중)"

    return strMessage

def messageNSULibrary():
    strMessage = ""
    strUrl = "http://220.68.191.20/setting"
    requestSession = requests.Session()
    Response = requestSession.get(strUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=certifi.where()).json()
    Response = dict(Response)
    first = "제1 자유열람실 : 여석 %s석 (%s석 사용중)\n" % (str(357 - int(Response['data']['data'][0]['inUse']) - int(Response['data']['data'][0]['fix']) - int(Response['data']['data'][0]['disabled'])), Response['data']['data'][0]['inUse'])
    second = "제2 자유열람실 : 여석 %s석 (%s석 사용중)\n" % (str(265 - int(Response['data']['data'][1]['inUse']) - int(Response['data']['data'][1]['fix']) - int(Response['data']['data'][1]['disabled'])), Response['data']['data'][1]['inUse'])
    third = "제3 자유열람실 : 여석 %s석 (%s석 사용중)" % (str(324 - int(Response['data']['data'][2]['inUse']) - int(Response['data']['data'][2]['fix']) - int(Response['data']['data'][2]['disabled'])), Response['data']['data'][2]['inUse'])

    strMessage = "남서울대학교 열람실 좌석현황(성암기념중앙도서관)\n\n" + first + second + third

    return strMessage