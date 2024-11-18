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

    result_message = message.message_cry_laugh_stress(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message.message_logistics(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message.message_meal(message, room, sender)
    if result_message is not None:
        return result_message

    elif "마법의 소라고동이시여" in message:
        strResult = messageSora(message)
    elif "잼민아" in message:
        strResult = messageGemini(message)
    elif "아.." in message:
        strResult = messageAh()
    elif "안사요" in message or "안 사요" in message or "사지말까" in message or "사지 말까" in message or "안살래" in message or "안 살래" in message:
        strResult = messageAhnsa()
    elif "응애" in message:
        strResult = messageBaby()
    elif "불편" in message:
        strResult = messageBoolpyeon()
    elif "사고싶" in message or "사야" in message or "살까" in message or "샀어" in message or "샀다" in message or "샀네" in message or "사버렸" in message:
        strResult = messageBuy()
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
    elif "개발해야" in message or "코딩해야" in message or "과제해야" in message:
        strResult = messageCoding()
    elif "뭐먹" in message or "머먹" in message:
        strResult = messageEat()
    elif ("제발" in message or "하고 싶다" in message) and "졸업" in message:
        strResult = messageGraduate()
    elif "하.." in message:
        strResult = messageHa()
    elif "호규" in message:
        if "전역" in message:
            strResult = messageHokyuGraduate()
        else:
            strResult = messageHokyu()
    elif "배고파" in message or "배고프" in message:
        strResult = messageHungry()
    elif "이런.." in message:
        strResult = messageIreon()
    elif "주형" in message:
        strResult = messageJoohyeong()
    elif "민식" in message:
        strResult = messageMinsik()
    elif "민석" in message:
        strResult = messageMinseok()
    elif "과제" in message or "집가고싶다" in message:
        strResult = messageMinsikBooreop()
    elif "ㅡㅡ" in message:
        strResult = messageMM()
    elif ("앎" in message or "아는사람" in message) or "알아" in message:
        strResult = messageMoloo()
    elif "무야호" in message:
        strResult = messageMooYaHo()
    elif "꺼라" in message:
        strResult = messageOff()
    elif "오호" in message or "호오" in message:
        strResult = messageOho(message)
    elif "오.." in message:
        strResult = messageOh()
    elif "오케이" in message:
        strResult = messageOkay()
    elif "퇴근" in message:
        strResult = messageOutwork()
    elif "ㄹㅇㅋㅋ" in message:
        strResult = messageReal()
    elif "^^7" in message:
        strResult = messageSalute()
    elif "나스" in message:
        strResult = messageSaseyo()
    elif "소해" in message or "졸업" in message or "전역" in message:
        if "승범" in message:
            strResult = messageSeungbeomGraduate()
        elif "성민" in message:
            strResult = messageSeongminGraduate()
        elif "수필" in message:
            strResult = messageSupilGraduate()
        elif "재민" in message:
            strResult = messageJaeminGraduate()
        elif "한수" in message:
            strResult = messageHansuGraduate()
        elif "병희" in message:
            strResult = messageBHGraduate()
        elif "창환" in message:
            strResult = messageChalsGraduate()
        elif "태식" in message:
            strResult = messageTjoGraduate()
    elif "서건1우" in message:
        strResult = messageSGW()
    elif "슈슉" in message:
        strResult = messageShuk()
    elif "졸려" in message or "잠와" in message or "피곤해" in message:
        strResult = messageSleepy()
    elif "멈춰" in message:
        strResult = messageStop()
    elif "어.." in message:
        strResult = messageUh()
    elif "와.." in message:
        strResult = messageWa()
    elif "와!" in message:
        strResult = messageWaSans()
    elif "유용민" in message:
        if "바보" in message:
            strResult = messageStupidYongmin(0)
        elif "천재" in message:
            strResult = messageStupidYongmin(1)
        else:
            strResult = messageStupidYongmin(2)
    elif "용민" in message:
        strResult = messageYongmin()
    elif "자라" in message:
        strResult = messageZara()
    elif "거북이" in message:
        strResult = messageGgobugi()
    elif "자야" in message or "잘까" in message:
        strResult = messageZayazi()
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
    elif "GDG" in message:
        strResult = messageGDG()
    elif "GDSC" in message:
        strResult = messageNotGDSC()
    elif "여진" in message or "김여진" in message:
        strResult = messageYeojin()
    elif "수현" in message or "수휫" in message:
        if "임수현" in message or "수휫" in message:
            strResult = messageLimsoo()
        else:
            strResult = messageSoohyun()
    elif "유빈" in message or "서유빈" in message:
        strResult = messageVini()
    elif "럭키" in message or "운세" in message:
        strResult = messageViki()
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
    return strResult

def messageAh():
    messages = ["글쿤..", "그래요..", "그렇군요..", "안돼..", "..메리카노", "..에이오우", "..아르키메데스의 원리"]
    return random.choice(messages)

def messageAhnsa():
    messages = ["이걸 안 사?", "왜요;;", "그거 사면 진짜 좋을텐데..", "아..", "헐..", "너한테 안 팔아;;"]
    return random.choice(messages)



def messageBaby():
    messages = ["귀여운척 하지 마세요;;", "응애 나 애기", "응애 나 아기 코린이"]
    return random.choice(messages)

def messageBoolpyeon():
    strMessage = "불편해?\\m불편하면 자세를 고쳐앉아!\\m보는 자세가 불편하니깐 그런거아냐!!"

    return strMessage

def messageBuy():
    messages = ["축하합니다!!!", "그걸 샀네;;", "개부자;;", "와 샀네",
                "이걸 산다고?", "ㅋㅋ", "왜요", "그거 살 돈이면 차라리..\\m.........",
                "ㅋㅋ 그걸 누가 삼"]
    return random.choice(messages)

def messageBHGraduate():
    strMessage = ""

    randInt = random.randrange(0,2)
    if randInt == 0: strMessage = "임병희씨가 입대한지 %d일, 전역한지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2020,6,30)).days, (datetime.date.today() - datetime.date(2021,12,29)).days)
    elif randInt == 1: strMessage = "임병희씨의 예비군 소집해제일까지 %d일 남았습니다."%((datetime.date(2029,12,31) - datetime.date.today()).days)
    return strMessage

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

def messageChalsGraduate():
    strMessage = "찰스가 입대한지 %d일, 전역한지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2020,12,7)).days, (datetime.date.today() - datetime.date(2022,9,1)).days)

    return strMessage



def messageCoding():
    messages = ["구라ㅡㅡ;;", "ㅋ", "밤새도 못 할 듯?ㅋㅋ"]
    return random.choice(messages)

def messageEat():
    messages = [
        "돼지", "또 먹어?", "살쪄", "그만 먹어;;", "된장찌개!!", "부리또!!", "김볶밥!!",
        "김치찌개!!", "햄버거!!", "부찌!!", "불고기!!", "삼겹살!!", "돼지갈비!!", "황금볶음밥!!",
        "미역국!!", "닭갈비!!", "떡볶이!!", "순두부찌개!!", "돈까스!!", "곱창!!", "콩나물국!!",
        "짜장면!!", "감자전!!", "짬뽕!!", "해물탕!!", "감자탕!!", "치킨!!", "라면!!",
        "샌드위치!!", "피자!!", "파스타!!", "햄버거!!", "샐러드!!", "쌈밥!!",
        "고무장갑 구이!!", "화분 케이크!!", "민트 초코맛 라면!!", "콜라에 밥 말아먹기!!",
        "플라스틱 튀김!!", "LED 광케이블 라조냐!!", "아이폰 스파게티!!",
        "바질리카 소스를 곁들인 크림리 소프트 쉘 크랩 파스타!!",
        "천천히 구운 로즈메리 향이 나는 양갈비와 민트 소스!!",
        "풍미 가득 허브와 치즈가 어우러진 랙 오브 램!!",
        "더블 초콜릿 퍼지 브라우니와 바닐라 아이스크림!!",
        "바다의 맛이 느껴지는 신선한 랍스터 테르미도르!!"
    ]
    return random.choice(messages)

def messageGemini(str):
    str = str.replace("잼민아", "").strip()
    response = gemini_model.generate_content(str)
    return(response.text)

def messageGgobugi():
    randInt = random.randrange(0, 3)
    strMessage = ""

    if randInt == 1 or randInt == 2 :
        ggobugiInt = random.randrange(0, 2)
        ggobugiMessage = ""

        if ggobugiInt == 0:
            ggobugiMessage = "효과는 굉장했다!"
        elif ggobugiInt == 1:
            ggobugiMessage = "효과가 별로인 듯하다..."

    if randInt == 0:
        strMessage = "자라"
    elif randInt == 1:
        strMessage = "꼬부기는 몸통박치기를 사용했다.\\m" + ggobugiMessage
    elif randInt == 2:
        strMessage = "꼬부기는 물대포를 사용했다.\\m" + ggobugiMessage

    return strMessage

def messageGraduate():
    messages = [
        "대학원 가셔야죠 ㅋㅋ",
        "졸업은 무슨",
        "노예 하셔야죠 ㅋㅋ",
        "어림도 없지 ㅋㅋ",
        "졸업은 무슨 ㅋㅋ",
        "박사도 해야죠 ㅋㅋ",
    ]
    return random.choice(messages)

def messageHa():
    messages = [
        "코딩하기 싫다..",
        "과제하기 싫다..",
        "걍 놀고 싶다..",
        "걍 자고 싶다..",
        "걍 쉬고 싶다..",
        "퇴근하고 싶다..",
        "집 가고 싶다..",
        "퇴사하고 싶다.."
    ]
    return random.choice(messages)

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

def messageHokyuGraduate():
    strMessage = ""
    randInt = random.randrange(0, 6)

    if randInt == 0:
        strMessage = "호규의 부사후 249기 지원을 응원합니다!"
    elif randInt == 1:
        strMessage = "호규의 학사 152기 지원을 응원합니다!"
    elif randInt == 2:
        strMessage = "호규의 예비군 소집해제일까지 %d일 남았습니다."%((datetime.date(2030,12,31) - datetime.date.today()).days -1)
    elif randInt == 3:
        strMessage = "호규의 민방위 소집해제일까지 %d일 남았습니다."%((datetime.date(2041,4,28) - datetime.date.today()).days -1)
    elif randInt == 4:
        strMessage = "예비군 1년차는 좀..."
    elif randInt == 5:
        strMessage = "하사 김호규의 임기제부사관 만기복무일까지 %d일 남았습니다."%((datetime.date(2027,8,26) - datetime.date.today()).days -1)

    return strMessage

def messageHansuGraduate():
    strMessage = ""
    randInt = random.randrange(0,2)
    if randInt == 0: strMessage = "이한수씨가 소집된지 %d일, 해제된지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2022,12,1)).days, (datetime.date.today() - datetime.date(2024,8,31)).days)
    elif randInt == 1: strMessage = "이한수씨의 민방위 소집해제일까지 %d일 남았습니다."%((datetime.date(2039,1,1) - datetime.date.today()).days)

    return strMessage

def messageHungry():
    messages = ["돼지", "또 먹어?", "살쪄", "그만 먹어;;", "아까 먹었잖아"]
    return random.choice(messages)

def messageIreon():
    messages = ["안됐군요..", "안타깝네요..", "눈물이 납니다..", "유감입니다..", "불쌍하네요..",
                "아쉽네요..", "저런.."]
    return random.choice(messages)

def messageJaeminGraduate():
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0: strMessage = "재민이가 입대한지 %d일, 전역한지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2021,5,9)).days, (datetime.date.today() - datetime.date(2024,3,8)).days)
    elif randInt == 1: strMessage = "재민이의 예비군 소집해제일까지 %d일 남았습니다."%((datetime.date(2031,12,31) - datetime.date.today()).days)

    return strMessage

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


def messageMinsikBooreop():
    strMessage = "2023-1학기 복학한 민식아 이제 안부럽다"

    return strMessage

def messageMoloo():
    strMessage = "몰?루"

    return strMessage

def messageMooYaHo():
    strMessage = "그만큼 신나신다는거지~"

    return strMessage

def messageMM():
    strMessage = "정색하지 마세요;;"

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



def messageOff():
    strMessage = "전기세 아깝다ㅡㅡ;;"

    return strMessage

def messageOh():
    messages = ["..레오", "..렌지쥬스", "..필승 코리아", "..카리나", "..리 꽥꽥"]
    return random.choice(messages)

def messageOutwork():
    messages = ["출근하세요", "평생 쉬세요~", "집가고싶다", "어딜 쉬러가요", "오늘 야근이에요"]
    return random.choice(messages)

def messageOho(message):
    strMessage = message[::-1]

    return strMessage

def messageOkay():
    strMessage = "땡큐! 4딸라!"

    return strMessage

def messageReal():
    messages = ["ㄹㅇㅋㅋ", "아닌데요", "ㄹㅇ임ㅋㅋ"]
    return random.choice(messages)



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

def messageSalute():
    messages = ["필승! ^^7", "충성! ^^7", "훈련병들은 충성! ^^7", "훈련병들은 필승! ^^7"]
    return random.choice(messages)

def messageSaseyo():
    messages = ["사세요", "안 사도 돼요", "나스는 역시 시놀로지죠~", "나스는 역시 큐냅이죠~"]
    return random.choice(messages)

def messageSeungbeomGraduate():
    randInt = random.randrange(0, 3)
    strMessage = ""
    y, m, d = 2031, 2, 28
    message_datetime.message_date_calculator(y, m, d)
    leftdays, lefthours, leftminutes, leftseconds, leftseconds_wa = message_datetime.message_date_calculator(y, m, d)

    if randInt == 0:
        strMessage = "승범아 대학원 가야지?"
    elif randInt == 1:
        strMessage = "승범이가 박사과정을 마치기까지 %d일 %d시간 %d분 %d초 남았습니다."%(leftdays - 1, abs(lefthours), leftminutes, leftseconds)
    elif randInt == 2:
        strMessage = "승범이가 박사과정을 마치기까지 " + format(leftseconds_wa, ',') + "초 남았습니다."
    return strMessage

def messageSupilGraduate():
    randInt = random.randrange(0, 5)
    strMessage = ""

    y, m, d = 2024, 11, 27
    message_datetime.message_date_calculator(y, m, d)
    leftdays, lefthours, leftminutes, leftseconds, leftseconds_wa = message_datetime.message_date_calculator(y, m, d)

    if randInt == 0:
        strMessage = "24년은 오지 않습니다..."
    elif randInt == 1:
        strMessage = "그런거 물어볼 시간에 일이나 하세요."
    elif randInt == 2:
        strMessage = "박수필씨의 소집해제일까지 %d일이 남았습니다."%(leftdays)
    elif randInt == 3:
        strMessage = "박수필씨의 소집해제일까지 %d일 %d시간 %d분 %d초 남았습니다."%(leftdays - 1, abs(lefthours), leftminutes, leftseconds)
    elif randInt == 4:
        strMessage = "당신이 민간인이 될 때까지 " + format(leftseconds_wa, ',') + "초 남았습니다."

    return strMessage

def messageSeongminGraduate():
    strMessage = ""
    randInt = random.randrange(0,2)
    if randInt == 0: strMessage = "지성민씨가 소집된지 %d일, 소해된지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2022,5,22)).days, (datetime.date.today() - datetime.date(2024,2,22)).days)
    elif randInt == 1: strMessage = "지성민씨의 예비군 소집해제일까지 %d일 남았습니다."%((datetime.date(2031,12,31) - datetime.date.today()).days)
    return strMessage

def messageShuk():
    strMessage = "슈슉"
    messages = [".슉.슈슉.시.발럼", ".슈슉.슉.슉시",
                ".슈발놈아.슉.시발.슈슉.슉", ".슈슉.시발.럼아.슉.슈슉.슉.슉슉.슈슉.시.발놈아"]
    return strMessage + random.choice(messages) + ".슉"

def messageSleepy():
    messages = ["자라;;", "구라;;", "자야지;;", "자야겠다;;", "자야겠다..", "졸린게 말이 돼?", "그만 좀 자라;;"]
    return random.choice(messages)

def messageSora(message):
    question = message.replace("마법의 소라고동이시여", "").strip()

    if not question:
        strMessage = "말 해"
    else:
        strMessage = random.choice(["그럼", "아마", "안 돼", "다시 한번 물어봐"])

    return strMessage

def messageStop():
    strMessage = "멈춰!!"

    return strMessage

def messageSGW():
    messages = ["좀 나가라;;", "뭐하냐;", "좀 꺼라;", "이미 차단당한 유저입니다."]
    return random.choice(messages)



def messageTjoGraduate():
    strMessage = "zz"

    return strMessage

def messageUh():
    messages = ["..이가없네;;", "..피치", "..기여차"]
    return random.choice(messages)

def messageWa():
    messages = ["갑부;;", "기만;;", "ㄹㅇ;;", "마스터;;", "역시;;",
                "이건 좀;;", "극혐;;", "플;;", "이파이;;", "내가 봐도 선 넘었네;;", "사비;;"]
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

def messageWaSans():
    strMessage = "샌즈!\\m아시는구나!\\m이거 겁.나.어.렵.습.니.다."

    return strMessage

def messageYongmin():
    strMessage = "집가고싶다"

    return strMessage

def messageZara():
    messages = [
        "전기세 아깝다ㅡㅡ;;",
        "거북이",
        "..투스트라는 이렇게 말했다.",
        "..ZARA는 스페인에 본사를 둔 글로벌 패션 그룹 인디텍스를 모회사로 두고 있는 SPA 브랜드로, SPA 브랜드 중 세계 최대 매출을 기록하고 있습니다.",
        "잘 자라^^",
        "자라는 토끼랑 달리기 경주 중",
    ]
    return random.choice(messages)

def messageZayazi():
    strMessage = "구라ㅡㅡ;;"

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

def messageGDG():
    strMessage = "GDG on Campus: CAU 최고 ~!~!~!~!@"
    return strMessage

def messageNotGDSC():
    strMessage = ["아뇨. GDG 인데요.", "이제 GDG라니깐요?!", "GDG입니다.", "GDSC는 이제 없어요.", "GDG! GDG!! GDG!@!@!@!"]
    return random.choice(strMessage)

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

def messageViki():
    messages = ["오늘의 운세는 이븐~하게 익지 않았어요.","오늘의 운세는 이븐~하게 익지 않았어요.",".....∧_∧\\n.. ( ̳• ·̫ • ̳) \\n┏ー∪∪━━━━━━━━┓\\n  °•. 오늘운세구려요.. . .•°\\n┗━--━━━━━•━━━┛",".....∧_∧\\n.. ( ̳• ·̫ • ̳) \\n┏ー∪∪━━━━━━━━┓\\n  °•. 오늘운세구려요.. . .•°\\n┗━--━━━━━•━━━┛",". /)_/)\\n( ̳• ·̫ • ̳)   럭키. .ꕥ 할지도\\n/>ꕥ<","＿人人人人人人人人＿\\n＞ 오늘 운세 낫배드! ＜\\n￣Y^Y^Y^Y^Y^Y^Y^Y￣\\n　 _n　( ｜　 ハ_ハ\\n　 ＼＼ ( ‘-^　)\\n　　 ＼￣￣　 )\\n　　　 ７　　/","오늘은 평범-한 날이예요","오늘 당신 초-럭키༘˚⋆𐙚｡ \\n 동방에 방문하면 좋은 일이 생길지도⋆𖦹.✧˚", "♡ ♡ ♡ ₍ᐢɞ̴̶̷.̮ɞ̴̶̷ᐢ₎ ♡ ♡ ♡\\n┏━♡━ U U━♡━━┓\\n♡오늘의 운세는···     ♡\\n♡초초초럭키-예요!   ♡\\n┗━♡━━━━♡━━┛"]
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