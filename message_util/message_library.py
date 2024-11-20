import datetime

import certifi
import requests

from util.cipher_util import DESAdapter


def message_library(message, room, sender):
    if "학사일정" in message:
        return message_calendar_cau()
    elif "열람실" in message:
        if "서울" in message:
            return message_library_cau(1)
        elif "법학" in message:
            return message_library_cau(2)
        elif "안성" in message:
            return message_library_cau(3)
        elif "남샤" in message:
            return message_library_nsu()
        else:
            return message_library_cau(0)

def message_calendar_cau():
    cal_data = datetime.date.today()
    cal_month = cal_data.month
    cal_year = cal_data.year

    cal_data = {
        "active": True,
        "month": cal_month,
        "title": f"{cal_month}월",
        "year": cal_year
    }
    cal_url = "https://mportal.cau.ac.kr/portlet/p014/p014List.ajax"

    request_session = requests.Session()
    request_session.mount(cal_url, DESAdapter())
    cal_response = eval(request_session.post(cal_url, json = cal_data, verify = certifi.where()).json())
    cal_list = cal_response['data']

    str_message = f"중앙대학교 {cal_month}월 학사일정\n"
    for calItem in cal_list:
        str_message += f"\n{calItem['TITLE']} : {calItem['TDAY']}"

    return str_message

def message_library_cau(lib_type_id):
    if lib_type_id == 1:
       lib_type = "서울"
    elif lib_type_id == 2:
       lib_type = "법학"
    elif lib_type_id == 3:
       lib_type = "안성"
    else:
        str_message = "중앙대학교 열람실 좌석현황\n\n사용법 : 열람실 키워드와 함께 서울 / 안성 / 법학 키워드 언급"
        return str_message

    lib_data = {"tabNo": lib_type_id}
    lib_url = "https://mportal.cau.ac.kr/portlet/p017/p017.ajax"

    request_session = requests.Session()
    request_session.mount(lib_url, DESAdapter())
    lib_response = request_session.post(lib_url, json = lib_data, verify = certifi.where()).json()

    lib_list = lib_response["gridData"]

    str_message = f"중앙대학교 열람실 좌석현황({lib_type})\n"
    for lib_item in lib_list:
       str_message += f"\n{lib_item['roomName']} : 여석 {lib_item['remainCnt']}석 ({lib_item['useCnt']}석 사용중)"

    return str_message

def message_library_nsu():
    str_url = "http://220.68.191.20/setting"
    request_session = requests.Session()
    request_response = dict(request_session.get(str_url, headers={"Content-Type": "application/x-www-form-urlencoded"}, verify=certifi.where()).json())
    lib_first = f"제1 자유열람실 : 여석 {str(357 - int(request_response['data']['data'][0]['inUse']) - int(request_response['data']['data'][0]['fix']) - int(request_response['data']['data'][0]['disabled']))}석 ({request_response['data']['data'][0]['inUse']}석 사용중)\n"
    lib_second = f"제2 자유열람실 : 여석 {str(265 - int(request_response['data']['data'][1]['inUse']) - int(request_response['data']['data'][1]['fix']) - int(request_response['data']['data'][1]['disabled']))}석 ({request_response['data']['data'][1]['inUse']}석 사용중)\n"
    lib_third = f"제3 자유열람실 : 여석 {str(324 - int(request_response['data']['data'][2]['inUse']) - int(request_response['data']['data'][2]['fix']) - int(request_response['data']['data'][2]['disabled']))}석 ({request_response['data']['data'][2]['inUse']}석 사용중)"

    str_message = f"남서울대학교 열람실 좌석현황(성암기념중앙도서관)\n\n{lib_first}{lib_second}{lib_third}"

    return str_message