import datetime

import certifi
import requests

from util.cipher_util import DESAdapter


def message_library(message, room, sender):
    if "학사일정" in message:
        return message_calendar_cau()
    elif "열람실" in message:
        if "서울" in message:
            return message_library_cau("1")
        elif "법학" in message:
            return message_library_cau("2")
        elif "안성" in message:
            return message_library_cau("3")
        elif "남샤" in message:
            return message_library_nsu()
        else:
            return message_library_cau("")

def message_calendar_cau():
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

def message_library_cau(libTypeID):
    if libTypeID == "1":
       libType = "서울"
    elif libTypeID == "2":
       libType = "법학"
    elif libTypeID == "3":
       libType = "안성"
    else:
        strMessage = "중앙대학교 열람실 좌석현황\n\n사용법 : 열람실 키워드와 함께 서울 / 안성 / 법학 키워드 언급"
        return strMessage

    libData = {
       "tabNo": libTypeID
    }
    libUrl = "https://mportal.cau.ac.kr/portlet/p017/p017.ajax"

    requestSession = requests.Session()
    requestSession.mount(libUrl, DESAdapter())
    libResponse = requestSession.post(libUrl, json=libData, verify=certifi.where()).json()

    libList = libResponse["gridData"]

    strMessage = f"중앙대학교 열람실 좌석현황({libType})\n"
    for libItem in libList:
       strMessage += f"\n{libItem['roomName']} : 여석 {libItem['remainCnt']}석 ({libItem['useCnt']}석 사용중)"

    return strMessage

def message_library_nsu():
    strUrl = "http://220.68.191.20/setting"
    requestSession = requests.Session()
    Response = requestSession.get(strUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=certifi.where()).json()
    Response = dict(Response)
    first = "제1 자유열람실 : 여석 %s석 (%s석 사용중)\n" % (str(357 - int(Response['data']['data'][0]['inUse']) - int(Response['data']['data'][0]['fix']) - int(Response['data']['data'][0]['disabled'])), Response['data']['data'][0]['inUse'])
    second = "제2 자유열람실 : 여석 %s석 (%s석 사용중)\n" % (str(265 - int(Response['data']['data'][1]['inUse']) - int(Response['data']['data'][1]['fix']) - int(Response['data']['data'][1]['disabled'])), Response['data']['data'][1]['inUse'])
    third = "제3 자유열람실 : 여석 %s석 (%s석 사용중)" % (str(324 - int(Response['data']['data'][2]['inUse']) - int(Response['data']['data'][2]['fix']) - int(Response['data']['data'][2]['disabled'])), Response['data']['data'][2]['inUse'])

    strMessage = "남서울대학교 열람실 좌석현황(성암기념중앙도서관)\n\n" + first + second + third

    return strMessage