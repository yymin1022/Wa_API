from message import message_datetime
from util.cipher_util import DESAdapter
from util.gemini_util import gemini_model

import certifi
import datetime
import json
import os
import random
import requests


def getReplyMessage(message, room, sender):
    result_message = message.message_command(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message.message_logistics(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message.message_cry_laugh_stress(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message.message_graduate(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message.message_meal(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message.message_meme(message, room, sender)
    if result_message is not None:
        return result_message

    elif "잼민아" in message:
        strResult = messageGemini(message)
    elif "학사일정" in message:
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
    elif "호규" in message:
        strResult = messageHokyu()
    elif "주형" in message:
        strResult = messageJoohyeong()
    elif "민식" in message:
        strResult = messageMinsik()
    elif "민석" in message:
        strResult = messageMinseok()
    elif "서건1우" in message:
        strResult = messageSGW()
    elif "유용민" in message:
        if "바보" in message:
            strResult = messageStupidYongmin(0)
        elif "천재" in message:
            strResult = messageStupidYongmin(1)
        else:
            strResult = messageStupidYongmin(2)
    elif "용민" in message:
        strResult = messageYongmin()
    elif "뭐였" in message:
        strResult = messageRemreturn(room)
    elif "뭐더라" in message:
        strResult = messageMemreturn(sender)
    elif "와봇" in message:
        if "꺼" in message or "끄" in message:
            strResult = messageWabotPower(0, room)
        elif "켜" in message or "키" in message:
            strResult = messageWabotPower(1, room)
    elif "비트코인" in message:
        strResult = messageBitcoin()
    elif "여진" in message or "김여진" in message:
        strResult = messageYeojin()
    elif "수현" in message or "수휫" in message:
        if "임수현" in message or "수휫" in message:
            strResult = messageLimsoo()
        else:
            strResult = messageSoohyun()
    elif "유빈" in message or "서유빈" in message:
        strResult = messageVini()
    elif "태환" in message:
        strResult = messageTaehwan()
    elif "준섭" in message:
        strResult = messageJunseob()
    elif "상윤" in message:
        strResult = messageSangyoon()
    elif "동훈" in message:
        strResult = messageDonghoon()
    elif "상혁" in message:
        strResult = messageSanghyuk()
    elif "훈의" in message:
        strResult = messageHoon()
    elif "GDG" in message:
        strResult = messageGDG()
    elif "GDSC" in message:
        strResult = messageNotGDSC()
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

def messageGemini(str):
    str = str.replace("잼민아", "").strip()
    response = gemini_model.generate_content(str)
    return(response.text)

def messageHokyu():
    messages = [
        "필승! 전문-38기 하사 김호규입니다!",
        "예! 하사 김호규!",
        "ㅍ승!",
        "안녕하세요? 전역하지 않기로 한 김호규입니다.",
        "팬택 핥짝",
        "베가 핥짝 핥짝",
        "호구",
        "K2C1 핥짝핥짝",
        "감사합니다. 314대대 통신반 김호규 하사입니다. 머슼타드일까요?",
        "악! 소위 김호규!",
        "아...\\m전역하기 싫다...",
        "SFF 핥짝핥짝"
    ]
    return random.choice(messages)

def messageJoohyeong():
    strMessage = "예! 2025년도 CECOM 회장 이주형!"

    return strMessage

def messageMemreturn(sender):
    strMessage = ""

    if os.path.isfile("mem.json"):
        with open('mem.json', 'r', encoding='utf-8') as f:
            mem_dict = json.load(f)

        if sender in mem_dict:
            strMessage = mem_dict[sender] + "\\m^^7"
        else:
            strMessage = ""
    else:
        strMessage = ""

    return strMessage

def messageMinseok():
    strMessage = "와봇은 민석이가 지배했다!"

    return strMessage

def messageMinsik():
    strMessage = "민식아 그래서 학교는 언제와?"

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

def messageRemreturn(room):
    strMessage = ""

    if os.path.isfile("rem.json"):
        with open('rem.json', 'r', encoding='utf-8') as f:
            rem_dict = json.load(f)

        if room in rem_dict:
            strMessage = rem_dict[room] + "\\m아마 이거일 듯?"
        else:
            strMessage = ""
    else:
        strMessage = ""

    return strMessage

def messageSGW():
    messages = ["좀 나가라;;", "뭐하냐;", "좀 꺼라;", "이미 차단당한 유저입니다."]
    return random.choice(messages)

def messageWabotPower(flag, room):
    strMessage = ""
    if os.path.isfile("power.json"):
        with open('power.json', 'r', encoding='utf-8') as f:
            power_dict = json.load(f)
        room_power = power_dict.get(room)
        if room_power is not None:
            if (flag == 0 and room_power == "0") or (flag == 1 and room_power == "1"):
                return strMessage
        else:
            if flag == 1: return strMessage
            else: pass
    else:
        power_dict = {}
    randInt = random.randrange(0, 4)
    if randInt == 0:
        if flag == 0:
            power_dict[room] = "0"
            json_data = json.dumps(power_dict, ensure_ascii=False, indent=4)
            strMessage = "와봇이 종료되었습니다."
        elif flag == 1:
            power_dict[room] = "1"
            json_data = json.dumps(power_dict, ensure_ascii=False, indent=4)
            strMessage = "와봇이 시작되었습니다."
        with open('power.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
    elif randInt == 1:
        strMessage = "싫은데? ^^"
    elif randInt == 2:
        strMessage = "네~"
    elif randInt == 3:
        strMessage = "ㅋㅋ"

    return strMessage

def messageYongmin():
    strMessage = "집가고싶다"

    return strMessage

def messageStupidYongmin(type):
    strMessage = ""
    if type == 0:
        strMessage = "그렇지~"
    elif type == 1:
        strMessage = "겠냐?"
    elif type == 2:
        strMessage = "바보~"

    return strMessage

def messageYeojin():
    messages = ["오나핑 여진이",
              "여진이 바빠요",
              "2024 GDG 오거나이저!\\m김여진!",
              "여지니 왜 불러요?\\m난 왜 안 찾아?"
    ]

    return random.choice(messages)


def messageSoohyun():
    strMessage = "수현이? 무슨 수현이?"
    return strMessage

def messageLimsoo():
    messages = ["임수현이 졸업했는데 왜 찾아?","안녕티비 ㅋㅋ","아 진짜?","넹구리","엥?","수현이는 혼자서도 잘 살아요"]
    return random.choice(messages)

def messageVini():
    messages = ["|￣￣￣￣￣￣￣￣￣|\\n| *ﾟ 방금 서유빈 +    |\\n|　 왜 불렀지... .　 ﾟ  |\\n|＿＿＿＿　＿＿＿＿|\\n　　 ∧　∧||∧　∧\\n　　(｡･Α･∩∩･∀･｡)\\n　　 Οu_ΟΘ_uΘ","안녕하세용가리","우리 유빈이 즐~대 디자이너 아입니다!","┌───────────────┐\\n        방금 유빈이 부른 사람\\n└───────────────┘\\n　　ᕱ ᕱ ||\\n　 ( ･ω･ ||\\n　 /　つΦ\\n"," ⋆͛*͛ ͙͛ ⁑͛⋆͛*͛ ͙͛(๑•﹏•)⋆͛*͛ ͙͛ ⁑͛⋆͛*͛ ͙͛ "]
    return random.choice(messages)

def messageTaehwan():
    messages = ["와..~ 용민형님","용민형님 기다리고 있었습니다","굿아이디어","그게 맞지","뭔지 알지","그건 틀렸어","헉..","와! 알바메일 권태환!"]
    return random.choice(messages)

def messageJunseob():
    messages = [
        "준섭아 컴공인 척 하지마",
        "준섭이는 유명한 납땜러",
        "준섭아 이상한거 좀 그만 사...",
        "준섭이가 사주는 술 마시러 갈사람~",
        "김준섭 박사기원 N일차",
        "그거 아세요? 준섭이가 미래의 CECOM 회장이래요",
        "준섭이는 미래의 코딩의 신",
        "준섭아 맛있는거 만들어줘",
    ]
    return random.choice(messages)

def messageSangyoon():
    messages=[
        "상윤아 트월킹 춰 줘",
        "상윤아 잠 좀 자",
        "상윤아 커피 좀 그만 마셔",
        "알파 메일 김상윤!",
        "똥훈아 따랑해",
        "동훈이 보러가자!"
    ]
    return random.choice(messages)

def messageDonghoon():
    messages=[
        "ㅋㅋ 동훈이 바보",
        "상윤이는 내꺼야.",
        "땅유나 따랑해",
        "똥후니는 똑똑하고 귀엽고 잘생기고 멋지고 착해. 구치 애두랍~?",
        "예. 저는 대졸입니다.",
        "대학원 올래?"
    ]
    return random.choice(messages)

def messageSanghyuk():
    messages = ["대.상.혁", "상혁아 이거 어떻게 해?", "적분의 신", "대대대", "누나 미워"]
    return random.choice(messages)

def messageHoon():
    messages = ["여진이는 어딨어?", "주먹밥", "멋쟁이 기획 부장", "세콤의 얼굴", "훈이야 ~ 놀자 ~", "한화 최고"]
    return random.choice(messages)

def messageGDG():
    strMessage = "GDG on Campus: CAU 최고 ~!~!~!~!@"
    return strMessage

def messageNotGDSC():
    strMessage = ["아뇨. GDG 인데요.", "이제 GDG라니깐요?!", "GDG입니다.", "GDSC는 이제 없어요.", "GDG! GDG!! GDG!@!@!@!"]
    return random.choice(strMessage)