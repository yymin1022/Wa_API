import ast
import datetime

import certifi
import requests

from models import WaMessage


def message_library(wa_message: WaMessage):
    message = wa_message.msg
    room = wa_message.room
    sender = wa_message.sender
    if "학사일정" in message:
        return message_calendar_cau()
    elif "열람실" in message:
        if "서울" in message:
            return message_library_cau(1)
        elif "법학" in message:
            return message_library_cau(2)
        elif "안성" in message:
            return message_library_cau(3)
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

    cal_response = ast.literal_eval(requests.post(cal_url, json = cal_data, verify = certifi.where()).json())
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

    lib_response = requests.post(lib_url, json = lib_data, verify = certifi.where()).json()

    lib_list = lib_response["gridData"]

    str_message = f"중앙대학교 열람실 좌석현황({lib_type})\n"
    for lib_item in lib_list:
       str_message += f"\n{lib_item['roomName']} : 여석 {lib_item['remainCnt']}석 ({lib_item['useCnt']}석 사용중)"

    return str_message
