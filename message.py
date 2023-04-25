from bs4 import BeautifulSoup

import datetime
import json
import random
import requests
import time
import xmltodict

def getReplyMessage(message):
    strResult = ""

    if "아.." in message:
        strResult = messageAh()
    elif "안사요" in message or "안 사요" in message or "사지말까" in message or "사지 말까" in message or "안살래" in message or "안 살래" in message:
        strResult = messageAhnsa()
    elif "응애" in message:
        strResult = messageBaby()
    elif "병희 전역" in message:
        strResult = messageBHGraduate()  
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
        else:
            strResult = messageCAULibrary("")
    elif "학식" in message:
        if "아침" in message or "조식" in message:
            strResult = messageCAUMeal("10")
        elif "점심" in message or "중식" in message:
            strResult = messageCAUMeal("20")
        elif "저녁" in message or "석식" in message:
            strResult = messageCAUMeal("40")
        elif "대림대" in message:
            strResult = messageDaelimMeal()
        elif "안양대" in message:
            strResult = messageAnyangMeal()
        else:
            strResult = messageCAUMeal("")
    elif "창환 전역" in message:
        strResult = messageChalsGraduate()
    elif "개발해야" in message or "코딩해야" in message or "과제해야" in message:
        strResult = messageCoding()
    elif ("ㅠ" in message or "ㅜ" in message) and getCryCount(message) >= 3:
        strResult = messageCry()
    elif "뭐먹" in message or "머먹" in message:
        strResult = messageEat()
    elif ("제발" in message or "하고 싶다" in message) and "졸업" in message:
        strResult = messageGraduate()
    elif "하.." in message:
        strResult = messageHa()
    elif "한수 소해" in message:
        strResult = messageHansuGraduate()
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
    elif "과제" in message or "집가고싶다" in message:
        strResult = messageMinsikBooreop()
    elif "ㅡㅡ" in message:
        strResult = messageMM()
    elif ("앎" in message or "아는사람" in message) or "알아" in message:
        strResult = messageMoloo()
    elif "무야호" in message:
        strResult = messageMooYaHo()
    elif "남샤" in message:
        if "1층" in message:
            strResult = messageNSUMeal("465")
        elif "2층" in message:
            strResult = messageNSUMeal("466")
        elif "3층" in message:
            strResult = messageNSUMeal("467")
        elif "카페" in message:
            strResult = messageNSUMeal("468")
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
    elif "성민 소해" in message:
        strResult = messageSeongminGraduate()
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
    elif "!날씨" in message:
        strResult = messageWeather()
    elif "용민" in message:
        strResult = messageYongmin()
    elif "자라" in message:
        strResult = messageZara()
    elif "자야" in message or "잘까" in message:
        strResult = messageZayazi() 
    elif "!뉴스" in message:
        strResult = messageFakeNews(message)

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
    randInt = random.randrange(0, 6)
    strMessage = ""

    if randInt == 0:
        strMessage = "글쿤.."
    elif randInt == 1:
        strMessage = "그래요.."
    elif randInt == 2:
        strMessage = "그렇군요.."
    elif randInt == 3:
        strMessage = "안돼.."
    elif randInt == 4:
        strMessage = "..메리카노"
    elif randInt == 5:
        strMessage = "..에이오우"
    
    return strMessage

def messageAhnsa():
    randInt = random.randrange(0, 5)
    strMessage = ""

    if randInt == 0:
        strMessage = "이걸 안 사?"
    elif randInt == 1:
        strMessage = "왜요;;"
    elif randInt == 2:
        strMessage = "그거 사면 진짜 좋을텐데.."
    elif randInt == 3:
        strMessage = "아.."
    elif randInt == 4:
        strMessage = "헐.."

    return strMessage

def messageAnyangMeal():
    todayDate = datetime.date.today()
    numDate = todayDate.weekday()

    if numDate >= 5:
        return "금일은 학식을 운영하지 않습니다"

    mealUrl = "https://www.anyang.ac.kr/main/activities/school-cafeteria.do"

    mealResponse = requests.post(mealUrl).text

    bs = BeautifulSoup(mealResponse, 'html.parser')
    mealData = json.loads(bs.find("input", id="mealList").get("value"))

    strDate = ["mon", "tue", "wed", "thu", "fri"]
    strMessage = f"{todayDate.strftime('%Y.%m.%d.')} 안양대학교 학식메뉴\n"
    strMessage += f"{mealData[f'{strDate[numDate]}Main02']}"
    for item in mealData[f'{strDate[numDate]}Sub02']:
        strMessage += f"\n{item}"

    return strMessage

def messageBaby():
    randInt = random.randrange(0, 3)
    strMessage = ""
    
    if randInt == 0:
        strMessage = "귀여운척 하지 마세요;;"
    elif randInt == 1:
        strMessage = "응애 나 애기"
    elif randInt == 2:
        strMessage = "응애 나 코린이"

    return strMessage

def messageBoolpyeon():
    strMessage = "불편해?\\m불편하면 자세를 고쳐앉아!\\m보는 자세가 불편하니깐 그런거아냐!!"

    return strMessage

def messageBuy():
    randInt = random.randrange(0, 8)
    strMessage = ""

    if randInt == 0:
        strMessage = "축하합니다!!!"
    elif randInt == 1:
        strMessage = "그걸 샀네;;"
    elif randInt == 2:
        strMessage = "개부자;;"
    elif randInt == 3:
        strMessage = "와 샀네"
    elif randInt == 4:
        strMessage = "이걸 산다고?"
    elif randInt == 5:
        strMessage = "ㅋㅋ"
    elif randInt == 6:
        strMessage = "왜요"
    elif randInt == 7:
        strMessage = "그거 살 돈이면 차라리..\\m........."

    return strMessage

def messageBHGraduate():
    dateEnd = datetime.date(2021,12,29)
    dateToday = datetime.date.today()
    leftDays = (dateToday - dateEnd).days
    strMessage = "임병희씨가 전역한지 %d일이 지났습니다."%(leftDays)
    
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

    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "ALL:@SECLEVEL=1"
    calResponse = eval(requests.post(calUrl, json=calData).json())
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

    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "ALL:@SECLEVEL=1"
    libResponse = requests.post(libUrl, json=libData).json()

    libList = libResponse["gridData"]

    strMessage = f"중앙대학교 열람실 좌석현황({libType})\n"
    for libItem in libList:
       strMessage += f"\n{libItem['roomName']} : 여석 {libItem['remainCnt']}석 ({libItem['useCnt']}석 사용중)"

    return strMessage

def messageCAUMeal(mealTypeID):
    strMessage = mealTypeID

    mealData = {
        "daily": 0,
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

    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "ALL:@SECLEVEL=1"
    mealResponse = requests.post(mealUrl, json=mealData).json()
    mealList = mealResponse["list"]

    strMessage = f"{mealList[0]['date']}. 중앙대학교 학식메뉴({mealType})\n"
    for mealItem in mealList:
        strMenu = mealItem['menuDetail']
        if strMenu == None:
            strMenu = "정보가 없습니다."
        strMessage += f"\n{mealItem['rest']} : {strMenu}"

    return strMessage

def messageChalsGraduate():
    randInt = random.randrange(0, 2)
    strMessage = ""

    dateStart = datetime.date(2020,12,7)
    dateEnd = datetime.date(2022,9,1)
    dateToday = datetime.date.today()
    goneDays = (dateToday - dateStart).days
    leftDays = (dateToday - dateEnd).days

    if randInt == 0:
        strMessage = "찰스가 입대한지 %d일이 됐습니다."%(goneDays)
    elif randInt == 1:
        strMessage = "찰스가 전역한지 %d일이 지났습니다."%(leftDays)

    return strMessage

def messageCoding():
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0:
        strMessage = "구라ㅡㅡ;;"
    elif randInt == 1:
        strMessage = "ㅋ"

    return strMessage

def messageCry():
    strMessage = "뭘 울어요;;"

    return strMessage

def messageDaelimMeal():
    todayDate = datetime.date.today()
    mealUrl = "https://www.daelim.ac.kr/ajaxf/FrBistroSvc/BistroCarteInfo.do"
    mealInput = f"MENU_ID=1470&BISTRO_SEQ=1&START_DAY={todayDate.strftime('%Y.%m.%d')}&END_DAY={todayDate.strftime('%Y.%m.%d')}"

    mealHeader = {"Content-Type": "application/x-www-form-urlencoded"}
    mealResponse = requests.post(mealUrl, data=mealInput, headers=mealHeader).json()

    strDate = todayDate.weekday() + 1
    strMessage = f"{todayDate.strftime('%Y.%m.%d.')} 대림대학교 학식메뉴\n"
    if strDate < 6:
        strMessage += f"* Corner1\n{mealResponse['data'][f'CCT{strDate}1'].strip()}\n"
        strMessage += f"* Corner3\n{mealResponse['data'][f'CCT{strDate}3'].strip()}\n"
        strMessage += f"* Corner6\n{mealResponse['data'][f'CCT{strDate}6'].strip()}\n"
        strMessage += f"* Daelim Cook\n{mealResponse['data'][f'CCT{strDate}7'].strip()}"
    else:
        strMessage += "금일은 학식을 운영하지 않습니다"

    return strMessage

def messageEat():
    randInt = random.randrange(0, 28)
    if randInt == 0:
    	strMessage = "돼지"
    elif randInt == 1:
    	strMessage = "또 먹어?"
    elif randInt == 2:
    	strMessage = "살쪄"
    elif randInt == 3:
    	strMessage = "그만 먹어;;"
    elif randInt == 4:
        strMessage = "삼겹살에 쐬주 한 잔?"
    elif randInt == 5:
        strMessage = "부리또!!"
    elif randInt == 6:
        strMessage = "김볶밥!!"
    elif randInt == 7:
        strMessage = "소고기!!"
    elif randInt == 8:
        strMessage = "햄버거!!"
    elif randInt == 9:
        strMessage = "부찌!!"
    elif randInt == 10:
        strMessage = "치폴!!"
    elif randInt == 11:
        strMessage = "아웃백!!"
    elif randInt == 12:
        strMessage = "빕스!!"
    elif randInt == 13:
        strMessage = "황금볶음밥!!"
    elif randInt == 14:
        strMessage = "마라탕!!"
    elif randInt == 15:
        strMessage = "슈하스코!!"
    elif randInt == 16:
        strMessage = "떡볶이!!"
    elif randInt == 17:
        strMessage = "학식!!"
    elif randInt == 18:
        strMessage = "돈까스!!"
    elif randInt == 19:
        strMessage = "곱창!!"
    elif randInt == 20:
        strMessage = "삼계탕!!"
    elif randInt == 21:
        strMessage = "짜장면!!"
    elif randInt == 22:
        strMessage = "양꼬치!!"
    elif randInt == 23:
        strMessage = "피탕!!"
    elif randInt == 24:
        strMessage = "피맥!!"
    elif randInt == 25:
        strMessage = "감자탕!!"
    elif randInt == 26:
        strMessage = "치킨!!"
    elif randInt == 27:
        strMessage = "C₂₈H₃₄N₂O₃!!"
    return strMessage

def messageGraduate():
    randInt = random.randrange(0, 4)
    strMessage = ""
    
    if randInt == 0:
        strMessage = "대학원 가셔야죠 ㅋㅋ"
    elif randInt == 1:
        strMessage = "졸업은 무슨"
    elif randInt == 2:
        strMessage = "노예 하셔야죠 ㅋㅋ"
    elif randInt == 3:
        strMessage = "어림도 없지 ㅋㅋ"

    return strMessage

def messageHa():
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0:
        strMessage = "코딩하기 싫다.."
    elif randInt == 1:
        strMessage = "과제하기 싫다.."

    return strMessage
    
def messageHokyu():
    strMessage = ""
    
    randInt = random.randrange(0, 10)
    if randInt == 0:
        strMessage = "필승! 833기 병장(진) 김호규입니다!"
    elif randInt == 1:
        strMessage = "예! 하사(진) 김호규!"
    elif randInt == 2:
        strMessage = "필승!"
    elif randInt == 3:
        strMessage = "안녕하세요? 전역하고 싶지 않은 김호규입니다."
    elif randInt == 4:
        strMessage = "팬택 핥짝"
    elif randInt == 5:
        strMessage = "베가 핥짝 핥짝"
    elif randInt == 6:
        strMessage = "호구"
    elif randInt == 7:
        strMessage = "K2C1 핥짝핥짝"
    elif randInt == 8:
        strMessage = "감사합니다. 314대대 통신반 병장(진) 김호규입니다. 머슼타드일까요?"
    elif randInt == 9:
        strMessage = "악! 소위 김호규!"
    
    return strMessage

def messageHokyuGraduate():
    strMessage = ""
    dateStart = datetime.date(2021,12,6)
    dateEnd = datetime.date(2023,8,27)
    dateToday = datetime.date.today()

    leftDays = (dateEnd - dateToday).days - 1
    goneDays = (dateToday - dateStart).days

    randInt = random.randrange(0, 4)
    if randInt == 0:
        strMessage = "호규는 전역할 때까지 %d일 남았습니다"%(leftDays)
    elif randInt == 1:
        strMessage = "호규가 입대한 지 %d일 되었습니다."%(goneDays)
    elif randInt == 2:
        strMessage = "833기가 벌써 전역 따질 짬인가?"
    elif randInt == 3:
        strMessage = "404 Not Found"

    return strMessage

def messageHansuGraduate():
    randInt = random.randrange(0, 3)
    strMessage = ""
    
    dateEnd = datetime.date(2024,8,31)
    dateToday = datetime.date.today()
    now = datetime.datetime.now()
    leftdays = (dateEnd - dateToday).days
    lefthours = 24 - now.hour - 10
    leftminutes = 60 - now.minute - 1
    leftseconds = 60 - now.second - 1
    leftseconds_wa = (leftdays * 24 * 60 * 60 - 1) + (lefthours * 60 * 60) + (leftminutes * 60) + leftseconds
    if randInt == 0:
        strMessage = "404 Not Found"
    elif randInt == 1:
        strMessage = "이한수씨의 소집해제일까지 %d일 %d시간 %d분 %d초 남았습니다."%(leftdays - 1, abs(lefthours), leftminutes, leftseconds)
    elif randInt == 2:
        strMessage = "이한수씨의 소집해제일까지 " + format(leftseconds_wa, ',') + "초 남았습니다."
    
    return strMessage

def messageHungry():
    strMessage = ""
    
    randInt = random.randrange(0, 4)
    if randInt == 0:
    	strMessage = "돼지"
    elif randInt == 1:
    	strMessage = "또 먹어?"
    elif randInt == 2:
    	strMessage = "살쪄"
    elif randInt == 3:
    	strMessage = "그만 먹어;;"
    	
    return strMessage

def messageIreon():
    randInt = random.randrange(0, 5)
    strMessage = ""

    if randInt == 0:
        strMessage = "안됐군요.."
    elif randInt == 1:
        strMessage = "안타깝네요.."
    elif randInt == 2:
        strMessage = "눈물이 납니다.."
    elif randInt == 3:
        strMessage = "유감입니다.."
    elif randInt == 4:
        strMessage = "불쌍하네요.."
    
    return strMessage

def messageJoohyeong():
    strMessage = "예! 2025년도 CECOM 회장 이주형!"

    return strMessage

def messageLaugh():
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0:
        strMessage = "뭘 웃어요;;"
    elif randInt == 1:
        strMessage = "안웃긴데;;"

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

def messageNSUMeal(NSU_BAP):
    strMessage = ""
    strUrl = "https://nsu.ac.kr/api/user/board/getBoardContentSummaryList"
    mealResponse = requests.post(strUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data="boardIdList=%d&includeProperties=1&parentBoardContentId=-1&isAvailable=1&isPrivate=0&isAlwaysOnTop=0&isDeleted=0&orderByCode=4" % int(NSU_BAP)).json()
    mealResponse = dict(mealResponse)
    mealList = mealResponse["body"]["list"][0]["properties"]["food_list"][0]

    mealList['// 월요일 //'], mealList['// 화요일 //'], mealList['// 수요일 //'], mealList['// 목요일 //'], mealList['// 금요일 //'], = mealList['field1'], mealList['field2'], mealList['field3'], mealList['field4'], mealList['field5']
    del(mealList['corner'], mealList['field1'], mealList['field2'], mealList['field3'], mealList['field4'], mealList['field5'])

    for mealData in mealList.items():
        strMessage += (f"{mealData[0]}\n{mealData[1]}\n")
    return strMessage

def messageOff():
    strMessage = "전기세 아깝다ㅡㅡ;;"

    return strMessage

def messageOh():
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0:
        strMessage = "..레오"
    elif randInt == 1:
        strMessage = "..렌지쥬스"
    
    return strMessage

def messageOutwork():
    randInt = random.randrange(0, 3)
    strMessage = ""

    if randInt == 0:
        strMessage = "출근하세요"
    elif randInt == 1:
        strMessage = "평생 쉬세요~"
    elif randInt == 2:
        strMessage = "집가고싶다"

    return strMessage

def messageOho(message):
    strMessage = message[::-1]
    
    return strMessage

def messageOkay():
    strMessage = "땡큐! 4딸라!"

    return strMessage

def messageReal():
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0:
        strMessage = "ㄹㅇㅋㅋ"
    elif randInt == 1:
        strMessage = "아닌데요"

    return strMessage

def messageSalute():
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0:
        strMessage = "필승! ^^7"
    elif randInt == 1:
        strMessage = "충성! ^^7"

    return strMessage

def messageSaseyo():
    randInt = random.randrange(0, 4)
    strMessage = ""

    if randInt == 0:
        strMessage = "사세요"
    elif randInt == 1:
        strMessage = "안 사도 돼요"
    elif randInt == 2:
        strMessage = "나스는 역시 시놀로지죠~"
    elif randInt == 3:
        strMessage = "나스는 역시 큐냅이죠~"

    return strMessage

def messageSeongminGraduate():
    randInt = random.randrange(0, 3)
    strMessage = ""

    dateEnd = datetime.date(2024,2,22)
    dateToday = datetime.date.today()
    leftdays = (dateEnd - dateToday).days

    if randInt == 0:
        strMessage = "24년은 오지 않습니다..."
    if randInt == 1:
        strMessage = "지성민씨의 소집해제일은 29년 12월 32일입니다."
    elif randInt == 2:
        strMessage = "지성민씨의 소집해제일까지 %d일이 남았습니다."%(leftdays)
    
    return strMessage

def messageShuk():
    randInt = random.randrange(0, 4)
    strMessage = "슈슉"
    
    while randInt != 4:
        if randInt == 0:
            strMessage += ".슉.슈슉.시.발럼"
        elif randInt == 1:
            strMessage += ".슈슉.슉.슉시"
        elif randInt == 2:
            strMessage += ".슈발놈아.슉.시발.슈슉.슉"
        elif randInt == 3:
            strMessage += ".슈슉.시발.럼아.슉.슈슉.슉.슉슉.슈슉.시.발놈아"
        
        randInt = random.randrange(0, 5)

    strMessage += ".슉"

    return strMessage

def messageSleepy():
    randInt = random.randrange(0, 2)
    strMessage = ""
    
    if randInt == 0:
        strMessage = "자라;;"
    elif randInt == 1:
        strMessage = "구라;;"
    
    return strMessage

def messageStop():
    strMessage = "멈춰!!"

    return strMessage

def messageStress():
    strMessage = "어림도 없지"

    return strMessage

def messageSGW():
    randInt = random.randrange(0, 4)
    strMessage = ""

    if randInt == 0:
        strMessage = "좀 나가라;;"
    elif randInt == 1:
        strMessage = "뭐하냐;"
    elif randInt == 2:
        strMessage = "좀 꺼라;"
    elif randInt == 3:
        strMessage = "이미 차단당한 유저입니다."
    
    return strMessage

def messageUh():
    randInt = random.randrange(0, 3)
    strMessage = ""

    if randInt == 0:
        strMessage = "..이가없네;;"
    elif randInt == 1:
        strMessage = "..피치"
    elif randInt == 2:
        strMessage = "..기여차"

    return strMessage

def messageWa():
    randInt = random.randrange(0, 9)
    strMessage = ""

    if randInt == 0:
        strMessage = "갑부;;"
    elif randInt == 1:
        strMessage = "기만;;"
    elif randInt == 2:
        strMessage = "ㄹㅇ;;"
    elif randInt == 3:
        strMessage = "마스터;;"
    elif randInt == 4:
        strMessage = "역시;;"
    elif randInt == 5:
        strMessage = "이건 좀;;"
    elif randInt == 6:
        strMessage = "극혐;;"
    elif randInt == 7:
        strMessage = "플;;"
    elif randInt == 8:
        strMessage = "이파이;;"

    return strMessage

def messageWaSans():
    strMessage = "샌즈!\\m아시는구나!\\m이거 겁.나.어.렵.습.니.다."

    return strMessage

def messageYongmin():
    strMessage = "집가고싶다"
    
    return strMessage

def messageZara():
    randInt = random.randrange(0, 2)
    strMessage = ""
    
    if randInt == 0:
        strMessage = "전기세 아깝다ㅡㅡ;;"
    elif randInt == 1:
        strMessage = "거북이"
        
    return strMessage

def messageZayazi():
    strMessage = "구라ㅡㅡ;;"

    return strMessage

def messageFakeNews(message):
    fake_news_url = os.environ['FAKE_NEWS_URL']
    keyword = message.split("!뉴스:")[1]
    response = requests.post(fake_news_url, json={'message':keyword, 'len':64})
    strResult = response.text.split('\n')
    
    return strResult

def messageWeather():

    weatherAPIUrl = "https://api.openweathermap.org/data/2.5/weather?id=1835847&appid=ea9e5f8d8e4aa2c798f8eb78f361d1b4"
    text = requests.get(weatherAPIUrl)
    text = text.text
    jsonData = json.loads(text)
    
    strMessage = "현재온도: " + str((jsonData["main"]["temp"])) + "구름: " + str((jsonData["clouds"]["all"]))
    return strMessage
