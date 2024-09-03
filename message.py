from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context
from dotenv import load_dotenv

import certifi
import datetime
import json
import os
import random
import requests
import time
import xmltodict
import base64

import google.generativeai as genai

CIPHERS = (
    'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
    'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES:!aNULL:'
    '!eNULL:!MD5'
    ':HIGH:!DH:!aNULL'
)

load_dotenv()
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
GEMINI_GENERATION_CONFIG = {
  "candidate_count": 1,
  "max_output_tokens": 256,
  "temperature": 1.0,
  "top_p": 0.7,
}
GEMINI_SAFETY_CONFIG=[
  {
    "category": "HARM_CATEGORY_DANGEROUS",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  },
]

genai.configure(
    api_key=GEMINI_API_KEY
)
model = genai.GenerativeModel(
    model_name='gemini-1.0-pro-latest',
    generation_config=GEMINI_GENERATION_CONFIG,
    safety_settings=GEMINI_SAFETY_CONFIG
)

class DESAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).proxy_manager_for(*args, **kwargs)

def getReplyMessage(message, room, sender):
    strResult = ""

    if "!뉴스" in message:
        strResult = messageFakeNews(message)
    elif "!base64d" in message:
        strResult = messageBase64Decode(message)
    elif "!base64e" in message:
        strResult = messageBase64Encode(message)
    elif "!날씨" in message:
        loc = message.split("!날씨")
        if(loc == "!날씨"):
            strResult = messageWeather()
        else:
            lat, lon = getlatlon(loc)
            strResult(messageWeather(lat, lon))
    elif "!기억" in message:
        strResult = messageRemember(message, room)
    elif "!날짜" in message:
        if "더하기" in message:
            strResult = messageCalDay(1, message)
        elif "빼기" in message:
            strResult = messageCalDay(0, message)
    elif "!메모" in message:
        strResult = messageMemo(message, sender)
    elif "!택배" in message:
        strResult = messageLogisticsParser(message)
    elif "!통관" in message:
        strResult = messageCustomTracker(message)
    elif "마법의 소라고동이시여" in message:
        strResult = messageSora(message)
    elif "!시간" in message:
        strResult = messageTimezone(message)
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
    elif "학식" in message:
        if "아침" in message or "조식" in message:
            strResult = messageCAUMeal("10", "내일" in message)
        elif "점심" in message or "중식" in message:
            strResult = messageCAUMeal("20", "내일" in message)
        elif "저녁" in message or "석식" in message:
            strResult = messageCAUMeal("40", "내일" in message)
        elif "대림대" in message:
            strResult = messageDaelimMeal()
        elif "안양대" in message:
            strResult = messageAnyangMeal()
        elif "남샤" in message:
            strResult = messageNSUMeal()
        else:
            strResult = messageCAUMeal("")
    elif "개발해야" in message or "코딩해야" in message or "과제해야" in message:
        strResult = messageCoding()
    elif ("ㅠ" in message or "ㅜ" in message) and getCryCount(message) >= 3:
        strResult = messageCry()
    elif "!디데이" in message or "!day" in message:
        strResult = messageDDay(message)
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
    elif ("ㅋ" in message or "ㅎ" in message) and getLaughCount(message) >= 20:
        strResult = messageLaugh()
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
    elif ";" in message and getStressCount(message) >= 4:
        strResult = messageStress()
    elif "어.." in message:
        strResult = messageUh()
    elif "와.." in message:
        strResult = messageWa()
    elif "와!" in message:
        strResult = messageWaSans()
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
    elif "유용민" in message:
        if "바보" in message:
            strResult = messageStupidYongmin(0)
        elif "천재" in message:
            strResult = messageStupidYongmin(1)
        else:
            strResult = messageStupidYongmin(2)
    return strResult

def getCryCount(message):
    count = message.count("ㅠ")
    count += message.count("ㅜ")

    return count

def getLaughCount(message):
    count = message.count("ㅋ")
    count += message.count("ㄱ")
    count += message.count("ㄲ")
    count += message.count("ㄴ")
    count += message.count("ㅌ")
    count += message.count("ㅎ")

    return count

def getStressCount(message):
    count = message.count(";")
    count += message.count(":")
    count += message.count(",")
    count += message.count(".")

    return count

def messageAh():
    messages = ["글쿤..", "그래요..", "그렇군요..", "안돼..", "..메리카노", "..에이오우", "..아르키메데스의 원리"]
    return random.choice(messages)

def messageAhnsa():
    messages = ["이걸 안 사?", "왜요;;", "그거 사면 진짜 좋을텐데..", "아..", "헐..", "너한테 안 팔아;;"]
    return random.choice(messages)

def messageAnyangMeal():
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
        response = requestSession.get(url)
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

def messageCAUMeal(mealTypeID, isTomorrow):
    strMessage = mealTypeID

    mealData = {
        "daily": (1 if isTomorrow else 0),
        "tabs": "1",
        "tabs2": mealTypeID
    }
    mealType = ""
    mealUrl = "https://mportal.cau.ac.kr/portlet/p005/p005.ajax"

    if mealTypeID == "10":
        mealType = "조식"
    elif mealTypeID == "20":
        mealType = "중식"
    elif mealTypeID == "40":
        mealType = "석식"
    else:
        strMessage = "중앙대학교 학식메뉴\n\n사용법 : 학식 키워드와 함께 아침 / 점심 / 저녁 / 조식 / 중식 / 석식 키워드 언급"
        return strMessage

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

def messageCalDay(cal, message):
    strMessage = ""
    weekly = 0
    day = datetime.datetime.now()
    try:
        if "주" in message:
            weekly = 1
        message = message.replace("!날짜더하기", "").replace("!날짜빼기", "").replace(" ", "").replace("일", "").replace("주", "")
        if message.isdigit() == False:
            raise
        if cal == 1:
            if weekly == 1:
                dday = day + datetime.timedelta(days=int(message) * 7)
                strMessage = "오늘을 기준으로 %s주 후는 %s년 %s월 %s일입니다." % (message, dday.year, dday.month, dday.day)
            else:
                dday = day + datetime.timedelta(days=int(message))
                strMessage = "오늘을 기준으로 %s일 후는 %s년 %s월 %s일입니다." % (message, dday.year, dday.month, dday.day)
        elif cal == 0:
            if weekly == 1:
                dday = day - datetime.timedelta(days=int(message) * 7)
                strMessage = "오늘을 기준으로 %s주 전은 %s년 %s월 %s일입니다." % (message, dday.year, dday.month, dday.day)
            else:
                dday = day - datetime.timedelta(days=int(message))
                strMessage = "오늘을 기준으로 %s일 전은 %s년 %s월 %s일입니다." % (message, dday.year, dday.month, dday.day)
    except:
        strMessage = "존재하지 않는 날짜이거나 사용 불가능한 형식입니다.\\mex) !날짜더하기 100일 or !날짜빼기 16주"
    return strMessage

def messageChalsGraduate():
    strMessage = "찰스가 입대한지 %d일, 전역한지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2020,12,7)).days, (datetime.date.today() - datetime.date(2022,9,1)).days)

    return strMessage

def messageCoding():
    messages = ["구라ㅡㅡ;;", "ㅋ", "밤새도 못 할 듯?ㅋㅋ"]
    return random.choice(messages)

def messageCry():
    messages = ["뭘 울어요;;", "왜 우시는 거예요?", "ㅋㅋ얘 운다"]
    return random.choice(messages)

def messageCustomTracker(message):
    strMessage = ""
    try:
        message = message.replace('!통관', '').replace(" ", "")
        key = os.environ['CUSTOM_API_KEY']
        year = datetime.date.today().year
        url = 'https://unipass.customs.go.kr:38010/ext/rest/cargCsclPrgsInfoQry/retrieveCargCsclPrgsInfo?crkyCn=%s&blYy=%s&hblNo=%s' % (key, year, message)
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "xml")
        name = soup.find('prnm')
        customs_name = soup.find('etprCstm')
        status = soup.find('prgsStts')
        process_time = datetime.datetime.strptime(str(soup.find('prcsDttm').text), "%Y%m%d%H%M%S").strftime("%Y.%m.%d %H:%M:%S")
        strMessage = "/// 관세청 UNIPASS 통관 조회 ///\n\n품명: %s\n입항세관: %s\n통관진행상태: %s\n처리일시: %s" % (name.text, customs_name.text, status.text, process_time)
    except:
        strMessage = "존재하지 않는 운송장번호이거나 잘못된 형식 혹은 아직 입항하지 않은 화물입니다.\\m사용법: !통관 123456789"

    return strMessage

def messageDaelimMeal():
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

def messageDateCalculator(y, m, d):
    dateEnd = datetime.date(y,m,d)
    dateToday = datetime.date.today()
    now = datetime.datetime.now()
    leftdays = (dateEnd - dateToday).days
    lefthours = 24 - now.hour - 1
    leftminutes = 60 - now.minute - 1
    leftseconds = 60 - now.second - 1
    leftseconds_wa = ((leftdays - 1) * 24 * 60 * 60) + (lefthours * 60 * 60) + (leftminutes * 60) + leftseconds

    return leftdays, lefthours, leftminutes, leftseconds, leftseconds_wa

def messageDDay(message):
    try:
        strMessage = ""
        message = message.replace("!디데이", "").replace("!day", "").replace(" ", "")
        if message.strip()[-1] == '.': message = message[:-1]
        if message.count('-') == 2 or message.count('.') == 2:
            if "-" in message: message = message.split("-")
            elif "." in message: message = message.split(".")
            if len(str(message[0])) == 2:
                message[0] = "20" + message[0]
            y, m, d = int(message[0]), int(message[1]), int(message[2])
            messageDateCalculator(y, m, d)
            leftdays, lefthours, leftminutes, leftseconds, leftseconds_wa = messageDateCalculator(y, m, d)
            if leftdays < 0: strMessage = "%s년 %s월 %s일을 기준으로 오늘은 %s일이 지났으며, 이를 초 단위로 환산하면 %s초입니다."%(message[0], message[1], message[2], format(int(leftdays * -1), ','), format(int(leftseconds_wa * -1), ','))
            elif leftdays == 0: strMessage = "D-DAY입니다!"
            else: strMessage = "%s년 %s월 %s일까지는 %s일이 남았으며, 이를 초 단위로 환산하면 %s초입니다."%(message[0], message[1], message[2], format(leftdays, ','), format(leftseconds_wa, ','))
        else: raise
    except:
        strMessage = "존재하지 않는 날짜이거나 사용 불가능한 형식입니다.\\mex) !day 2023.9.8 or !디데이 23.12.31"

    return strMessage

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
    response = model.generate_content(f"지금부터 대한민국의 초등학생의 말투로 대답해줘. 맞춤법도 조금 틀려서 해주면 좋을 것 같아. 조금 바보같은 말투로 대답하면 돼. {str}")
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

def messageLaugh():
    messages = ["뭘 웃어요;;", "안웃긴데;;", "이게 웃겨요?"]
    return random.choice(messages)

def messageLogisticsParser(message):
    strMessage = ""
    message = message.replace("!택배", "").replace(" ", "")
    if message == "":
        strMessage = "///택배 운송장조회 사용 방법///\\m사용 예시: !택배[운송장번호]\nex)!택배1234567890\n지원중인 택배사: 우체국택배, 대한통운(CJ, 대통), 로젠택배, 롯데택배, 한진택배"
        return strMessage

    logistics = [
        messageLogisticsParser_CJ,
        messageLogisticsParser_HJ,
        messageLogisticsParser_KP,
        messageLogisticsParser_LG,
        messageLogisticsParser_LT
    ]

    for parser in logistics:
        strMessage = parser(message)
        if strMessage: return strMessage

    strMessage = "미집하된 화물이거나 존재하지 않는 운송장 번호입니다.\\m사용 예시: !택배[운송장번호]\nex)!택배1234567890\n지원중인 택배사: 우체국택배, 대한통운(CJ, 대통), 로젠택배, 롯데택배, 한진택배"

    return strMessage

def messageLogisticsParser_CJ(message):
    strMessage = ""
    infom = []
    i = 1
    temp = ""
    try:
        if message.isdigit() == False: raise
        request_headers = {
        'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'), }
        strUrl = "https://trace.cjlogistics.com/tracking/jsp/cmn/Tracking_new.jsp?QueryType=3&pTdNo=" + message
        requestSession = requests.Session()
        Response = requests.get(strUrl, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(Response.text, 'html.parser')

        while True:
            info = soup.select('#content > div > table.tepTb02.tepDep02 > tbody > tr:nth-child(%d)' % i)
            if not info:
                info = soup.select('#content > div > table.tepTb02.tepDep02 > tbody > tr:nth-child(%d)' % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        goods_name = soup.select('#content > div > table.tepTb02.tepDep > tbody > tr:nth-child(6) > td:nth-child(2)')
        goods_name = goods_name[0].get_text().strip()
        goods_name = goods_name.replace('[<td>제품,', '').replace('</td>]', '')
        infom = temp.split('\n')
        for _ in range(len(infom)):
            if infom[_] == "\xa0":
                infom[_] = infom[_].replace(u'\xa0', u'(정보 없음)')
            elif "인수자 : " in infom[_]:
                infom[_] = infom[_].replace('인수자 : ', '')
        strMessage = "/// CJ대한통운 배송조회 ///\n\n품목: %s\n처리장소: %s\n전화번호: %s\n구분: %s\n처리일자: %s\n상대장소(배송장소): %s" % (goods_name, infom[1], infom[2], infom[3], infom[4], infom[5])
    except:
        strMessage = ""
    return strMessage

def messageLogisticsParser_HJ(message):
    strMessage = ""
    infom = []
    i = 1
    temp = ""
    try:
        if message.isdigit() == False: raise
        request_headers = {
        'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'), }
        strUrl = "https://www.hanjin.com/kor/CMS/DeliveryMgr/WaybillResult.do?mCode=MN038&wblnum=" + message + "&schLang=KR"
        requestSession = requests.Session()
        Response = requests.get(strUrl, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(Response.text, 'html.parser')
        while True:
            info = soup.select('#delivery-wr > div > div.waybill-tbl > table > tbody > tr:nth-child(%d)' % i)
            if not info:
                info = soup.select('#delivery-wr > div > div.waybill-tbl > table > tbody > tr:nth-child(%d)' % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        infom = temp.split('\n')
        for _ in range(len(infom)):
            if infom[7] == '':
                infom[7] = "(정보 없음)"
        goods_name = soup.select('#delivery-wr > div > table > tbody > tr > td:nth-child(1)')
        goods_name = goods_name[0].get_text().strip()
        strMessage = "/// 한진택배 배송조회 ///\n\n상품명: %s\n날짜: %s\n시간: %s\n상품위치: %s\n배송 진행상황: %s\n전화번호: %s" % (goods_name, infom[1], infom[2], infom[3], infom[5], infom[7])
    except:
        strMessage = ""
    return strMessage

def messageLogisticsParser_KP(message):
    strMessage = ""
    infom = []
    i = 1
    temp = ""
    try:
        if message.isdigit() == False: raise
        request_headers = {
        'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'), }
        strUrl = "https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm?sid1=" + message
        requestSession = requests.Session()
        Response = requests.get(strUrl, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(Response.text, 'html.parser')
        while True:
            info = soup.select('#processTable > tbody > tr:nth-child(%d)' % i)
            if not info:
                info = soup.select('#processTable > tbody > tr:nth-child(%d)' % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        infom = temp.split('\n')
        for _ in range(len(infom)):
            if '\t' in infom[_]: infom[_] = infom[_].replace('\t', '')
        if infom[5] == '            ': infom[5] = '배달준비'
        strMessage = "/// 우체국택배 배송조회 ///\n\n날짜: %s\n시간: %s\n발생국: %s\n처리현황: %s" % (infom[1], infom[2], infom[3], infom[5])
    except:
        strMessage = ""
    return strMessage

def messageLogisticsParser_LG(message):
    strMessage = ""
    infom = []
    i = 1
    temp = ""
    try:
        if message.isdigit() == False:
            raise
        request_headers = {
        'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'), }
        strUrl = "https://www.ilogen.com/web/personal/trace/" + message
        requestSession = requests.Session()
        Response = requests.get(strUrl, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(Response.text, 'html.parser')
        while True:
            info = soup.select('body > div.contents.personal.tkSearch > section > div > div.tab_container > div > table.data.tkInfo > tbody > tr:nth-child(%d)' % i)
            if not info:
                info = soup.select('body > div.contents.personal.tkSearch > section > div > div.tab_container > div > table.data.tkInfo > tbody > tr:nth-child(%d)' % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        infom = temp.split('\n')
        for _ in range(len(infom)):
            if '\t' in infom[_]: infom[_] = infom[_].replace('\t', '')
        infom = [v for v in infom if v]
        temp = ''
        if "전달" in infom[3]:
            temp = '\n인수자: ' + infom[5]
        elif "배달 준비" in infom[3]:
            temp = '\n배달 예정 시간: ' + infom[5]
        strMessage = "/// 로젠택배 배송조회 ///\n\n날짜: %s\n사업장: %s\n배송상태: %s\n배송내용: %s" % (infom[0], infom[1], infom[2], infom[3]) + temp
    except:
        strMessage = ""
    return strMessage

def messageLogisticsParser_LT(message):
    strMessage = ""
    infom = []
    i = 1
    temp = ""
    try:
        if message.isdigit() == False:
            raise
        request_headers = {
        'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'), }
        strUrl = "https://www.lotteglogis.com/mobile/reservation/tracking/linkView?InvNo=" + message
        requestSession = requests.Session()
        Response = requests.get(strUrl, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(Response.text, 'html.parser')
        info = soup.find("div", "scroll_date_table")
        for tag in info:
            temp += tag.get_text()
        infom = temp.split('\n')
        for _ in range(len(infom)):
            infom[_] = infom[_].replace('\t', '').replace('\r', '').replace(' ', '').replace(u'\xa0', '')
        infom = [v for v in infom if v]
        infom[6] = infom[6][:10] + ' ' + infom[6][10:]
        strMessage = "/// 롯데택배 배송조회 ///\n\n단계: %s\n시간: %s\n현위치: %s\n처리현황: %s" % (infom[5], infom[6], infom[7], infom[8])
    except:
        strMessage = ""
    return strMessage

def messageMemo(message, sender):
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

def messageNSUMeal():
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

def messageRemember(message, room):
    message = message.replace("!기억해", "").replace("!기억", "").strip()

    if len(message) != 0:
        if os.path.isfile("rem.json"):
            with open('rem.json', 'r', encoding='utf-8') as f:
                rem_dict = json.load(f)
        else:
            rem_dict = {}

        rem_dict[room] = message
        json_data = json.dumps(rem_dict, ensure_ascii=False, indent=4)

        with open('rem.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
    else:
        pass

    strMessage = ""
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
    messageDateCalculator(y, m, d)
    leftdays, lefthours, leftminutes, leftseconds, leftseconds_wa = messageDateCalculator(y, m, d)

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
    messageDateCalculator(y, m, d)
    leftdays, lefthours, leftminutes, leftseconds, leftseconds_wa = messageDateCalculator(y, m, d)

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

def messageStress():
    strMessage = "어림도 없지"

    return strMessage

def messageSGW():
    messages = ["좀 나가라;;", "뭐하냐;", "좀 꺼라;", "이미 차단당한 유저입니다."]
    return random.choice(messages)

def messageTimezone(message):
    strMessage = ""
    try:
        message = message.replace("!시간 ", "").replace(" ", "")
        if message.startswith('+') or message.startswith('-'):
            if int(message) > 12 or int(message) < -11:
                raise
            offset = datetime.timedelta(hours=int(message))
        else:
            hours, minutes = map(int, message.split(':'))
            offset = datetime.timedelta(hours=hours, minutes=minutes)
        adjusted_time = datetime.datetime.now(datetime.timezone.utc) + offset
        strMessage = f"현재 UTC{message}의 시간은 ", adjusted_time.strftime('%Y-%m-%d %H:%M:%S') , "입니다."
    except:
        strMessage = "사용 형식이 잘못됐거나 존재하지 않는 시간대입니다.\\m사용법: !시간 +9 or !시간 -11"
    return strMessage

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

def messageFakeNews(message):
    fake_news_url = os.environ['FAKE_NEWS_URL']
    keyword = message.split("!뉴스:")[1]
    requestSession = requests.Session()
    requestSession.mount(fake_news_url, DESAdapter())
    response = requestSession.post(fake_news_url, json={'message':keyword, 'len':64}, verify=certifi.where())
    strMessage = '\\m'.join(response.text.split('\n')[2:-4])

    return strMessage

def messageWeather():
    appid = "ea9e5f8d8e4aa2c798f8eb78f361d1b4"
    id = 1835847    ###서울 디폴트
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


def getlatlon(location):
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

def messageWeather(lat, lon, loc):
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

def messageStupidYongmin(type):
    strMessage = ""
    if type == 0:
        strMessage = "그렇지~"
    elif type == 1:
        strMessage = "겠냐?"
    elif type == 2:
        strMessage = "바보~"

    return strMessage

def messageBase64Encode(message):
    msg = message.split("!base64e ")[1]
    return base64.b64encode(msg.encode('utf8')).decode('utf8')
def messageBase64Decode(message):
    msg = message.split("!base64d ")
    return base64.b64decode(msg[1]).decode('utf8')
