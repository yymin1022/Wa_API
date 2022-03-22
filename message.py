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
    elif "응애" in message:
        strResult = messageBaby()
    elif "불편" in message:
        strResult = messageBoolpyeon()
    elif "개발해야" in message or "코딩해야" in message or "과제해야" in message:
        strResult = messageCoding()
    elif ("코로나" in message or "확진자" in message) and "몇" in message:
        if "지역별" in message:
            strResult = messageCoronaCity()
        else:
            strResult = messageCorona()
    elif "방역" in message and ("수칙" in message or "지침" in message):
        strResult = messageCoronaRule()
    elif ("ㅠ" in message or "ㅜ" in message) and getCryCount(message) >= 3:
        strResult = messageCry()
    elif "뭐먹" in message:
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
    elif "저누님" in message:
        strResult = messageJeonwoo()
    elif ("ㅋ" in message or "ㅎ" in message) and getLaughCount(message) >= 10:
        strResult = messageLaugh()
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
    elif "ㄹㅇㅋㅋ" in message:
        strResult = messageReal()
    elif "^^7" in message:
        strResult = messageSalute()
    elif "나스" in message or "폴리오" in message:
        strResult = messageSaseyo()
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
    elif "근무" in message:
        if "오늘" in message:
            strResult = messageWorkToday()
        elif "내일" in message:
            strResult = messageWorkTomorrow()
        elif "월" in message and "일" in message:
            year = datetime.date.today().year
            if "년" in message:
                year = message.split("년")[0]
            month = message.split("월")[0].split()[-1]
            day = message.split("월")[1].split("일")[0].split()[-1]
            strResult = messageWorkDate(year, month, day)
    elif "용민" in message:
        if "전역" in message:
            strResult = messageYongminGraduate()
        else:
            strResult = messageYongmin()
    elif "자라" in message:
        strResult = messageZara()
    elif "자야" in message:
        strResult = messageZayazi()

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

def messageCoding():
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0:
        strMessage = "구라ㅡㅡ;;"
    elif randInt == 1:
        strMessage = "ㅋ"

    return strMessage

def messageCorona():
    curDate = datetime.date.today().strftime("%Y년 %m월 %d일")
    curTimestamp = str(time.time())

    url = f"https://apiv3.corona-live.com/domestic/stat.json?timestamp={curTimestamp}"
    response = requests.get(url)
    jsonData = json.loads(response.content)["overview"]

    dataConfirmed = jsonData["confirmed"]
    dataCritical = jsonData["confirmedCritical"]
    dataDeceased = jsonData["deceased"]
    dataHospitalised = jsonData["hospitalised"]
    dataRecovered = jsonData["recovered"]

    strConfirmed = f"확진자 : {format(dataConfirmed[1], ',')}명 (누적 {format(dataConfirmed[0], ',')}명)"
    strCritical = f"위중증 : {format(dataCritical[0], ',')}명 "
    if int(dataCritical[1]) < 0:
        strCritical += f"(-{format(int(dataCritical[1]) * -1, ',')})"
    else:
        strCritical += f"(+{format(dataCritical[1], ',')})"

    strDeceased = f"사망자 : {format(dataDeceased[0], ',')}명 "
    if int(dataDeceased[1]) < 0:
        strDeceased += f"(-{format(int(dataDeceased[1]) * -1, ',')})"
    else:
        strDeceased += f"(+{format(dataDeceased[1], ',')})"

    strHospitalised = f"입원환자 : {format(dataHospitalised[0], ',')}명 "
    if int(dataHospitalised[1]) < 0:
        strHospitalised += f"(-{format(int(dataHospitalised[1]) * -1, ',')})"
    else:
        strHospitalised += f"(+{format(dataHospitalised[1], ',')})"

    strRecovered = f"완치자 : {format(dataRecovered[0], ',')}명 "
    if int(dataRecovered[1]) < 0:
        strRecovered += f"(-{format(int(dataRecovered[1]) * -1, ',')})"
    else:
        strRecovered += f"(+{format(dataRecovered[1], ',')})"

    url = f"https://apiv3.corona-live.com/domestic/live.json?timestamp={curTimestamp}"
    response = requests.get(url)
    jsonData = json.loads(response.content)["live"]

    dataConfirmedLive = jsonData["today"]
    dataConfirmedLiveYesterday = jsonData["yesterday"]

    strConfirmedLive = f"실시간 : {format(dataConfirmedLive, ',')}명"
    strConfirmedLiveYesterday = f"어제 동시간대 : {format(dataConfirmedLiveYesterday, ',')}명"

    strMessage = f"{curDate} 코로나19 현황\n{strConfirmedLive}\n{strConfirmedLiveYesterday}\n\n어제까지\n{strConfirmed}\n{strCritical}\n{strHospitalised}\n{strRecovered}\n{strDeceased}"

    return strMessage

def messageCoronaCity():
    curDate = datetime.date.today().strftime("%Y년 %m월 %d일")
    curTimestamp = str(time.time())

    url = f"https://apiv3.corona-live.com/domestic/live.json?timestamp={curTimestamp}"
    response = requests.get(url)
    jsonData = json.loads(response.content)["cities"]

    domesticList = ["서울", "부산", "인천", "대구", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "경북", "경남", "전북", "전남", "제주", "입국 검역소"]

    strDomestic = ""
    for i in range(18):
        dataCurDomestic = jsonData[str(i)]
        strDomestic += f"{domesticList[i]} {format(dataCurDomestic[0], ',')}명 "
        if(int(dataCurDomestic[1]) < 0):
            strDomestic += f"(-{format(int(dataCurDomestic[1]) * -1, ',')})\n"
        else:
            strDomestic += f"(+{format(dataCurDomestic[1], ',')})\n"

    strMessage = f"{curDate} 코로나19 지역별 현황\n{strDomestic}".rstrip()

    return strMessage

def messageCoronaRule():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    url = "https://o-bang.kr/"

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, features="html.parser")

    divParent = soup.find_all("div")[0]
    divFrame = divParent.find_all("div")[4]
    divContainer = divFrame.find_all("div")[2]
    divTerm = divContainer.find_all("div")[2]
    divPerson = divContainer.find_all("div")[5]
    divTime = divContainer.find_all("div")[8]
    divPass = divContainer.find_all("div")[11]

    strTerm = divTerm.text
    strPerson = divPerson.text
    strTime = divTime.text
    strPass = divPass.text

    strMessage = f"현행 코로나19 방역수칙\n\n인원제한 - {strPerson}\n시간제한 - {strTime}\n방역패스 - {strPass}\n\n적용기간 {strTerm}"

    return strMessage

def messageCry():
    strMessage = "뭘 울어요;;"

    return strMessage

def messageEat():
    randInt = random.randrange(0, 5)
    if randInt == 0:
    	strMessage = "돼지"
    elif randInt == 1:
    	strMessage = "또 먹어?"
    elif randInt == 2:
    	strMessage = "살쪄"
    elif randInt == 3:
    	strMessage = "그만 먹어;;"
    elif randInt == 4:
        strMessage = "고기!!"

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
    
    randInt = random.randrange(0, 9)
    if randInt == 0:
        strMessage = "필승! 833기 일병 김호규입니다!"
    elif randInt == 1:
        strMessage = "예! 일병 김호규!"
    elif randInt == 2:
        strMessage = "필승!"
    elif randInt == 3:
        strMessage = "안녕하세요? 전역하고 싶은 김호규입니다."
    elif randInt == 4:
        strMessage = "팬택 핥짝"
    elif randInt == 5:
        strMessage = "베가 핥짝 핥짝"
    elif randInt == 6:
        strMessage = "호구"
    elif randInt == 7:
        strMessage = "K2C1 핥짝핥짝"
    elif randInt == 8:
        strMessage = "감사합니다. 314대대 통신반 일병 김호규입니다. 머슼타드일까요?"
    
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

def messageJeonwoo():
    randInt = random.randrange(0, 4)
    strMessage = ""

    if randInt == 0:
        strMessage = "코딩좀 하십쇼;;"
    elif randInt == 1:
        strMessage = "공부좀 하십쇼;;"
    elif randInt == 2:
        strMessage = "일좀 하십쇼;;"
    elif randInt == 3:
        strMessage = "근무좀 하십쇼;;"
    
    return strMessage;

def messageLaugh():
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0:
        strMessage = "뭘 웃어요;;"
    elif randInt == 1:
        strMessage = "안웃긴데;;"

    return strMessage

def messageMooYaHo():
    strMessage = "그만큼 신나신다는거지~"

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
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0:
        strMessage = "사세요"
    elif randInt == 1:
        strMessage = "안 사도 돼요"

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

def messageWorkDate(year, month, day):
    try:
        year = int(year)
        month = int(month)
        day = int(day)

        dateStart = datetime.date(2021,3,1)
        dateToday = datetime.date(year, month, day)

        countDays = (dateToday - dateStart).days
        
        strMessage = "%s 근무현황\\n%s"%(dateToday.strftime("%Y년 %m월 %d일"), calcWork(countDays))
    except:
        strMessage = "그게 날짜냐?"
    
    return strMessage

def messageWorkToday():
    dateStart = datetime.date(2021,3,1)
    dateToday = datetime.date.today()
    
    countDays = (dateToday - dateStart).days

    strMessage = "%s 근무현황\\n%s"%(dateToday.strftime("%Y년 %m월 %d일"), calcWork(countDays))

    return strMessage

def messageWorkTomorrow():
    dateStart = datetime.date(2021,3,1)
    dateToday = datetime.date.today() + datetime.timedelta(days=1)
    
    countDays = (dateToday - dateStart).days

    strMessage = "%s 근무현황\\n%s"%(dateToday.strftime("%Y년 %m월 %d일"), calcWork(countDays))

    return strMessage

def messageYongmin():
    randInt = random.randrange(0, 3)
    strMessage = ""
    
    if randInt == 0:
        strMessage = "감사합니다. MCC 병장 유용민입니다. 머슼타드일까요?"
    elif randInt == 1:
        strMessage = "감사합니다. 체계운영실 병장 유용민입니다. 머슼타드일까요?"
    elif randInt == 2:
        strMessage = "감사합니다. 운영중대 병장 유용민입니다. 머슼타드일까요?"

    return strMessage

def messageYongminGraduate():
    randInt = random.randrange(0, 3)
    strMessage = ""
    
    if randInt == 0:
        strMessage = "819기가 벌써 전역 따질 짬인가??"
    elif randInt == 1:
        strMessage = "404 Not Found"
    elif randInt == 2:
        dateGraduate = datetime.date(2022,7,12)
        dateToday = datetime.date.today()
        
        countDays = (dateGraduate - dateToday).days - 1
        strMessage = "전역까지 %d일 남았습니다."%(countDays)

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

def calcWork(days):
    calcValue = days % 5
    strResult = ""
    
    if calcValue == 0:
        strResult = "1조 2BRK\\n2조 MID(23:40 ~ 07:20)/SWI(17:40 ~ 23:50)\\n3조 1BRK\\n4조 MOR(07:10 ~ 12:10)\\n5조 AFT(12:00 ~ 17:50)"
    elif calcValue == 1:
        strResult = "1조 MOR(07:10 ~ 12:10)\\n2조 AFT(12:00 ~ 17:50)\\n3조 2BRK\\n4조 MID(23:40 ~ 07:20)/SWI(17:40 ~ 23:50)\\n5조 1BRK"
    elif calcValue == 2:
        strResult = "1조 MID(23:40 ~ 07:20)/SWI(17:40 ~ 23:50)\\n2조 1BRK\\n3조 MOR(07:10 ~ 12:10)\\n4조 AFT(12:00 ~ 17:50)\\n5조 2BRK"
    elif calcValue == 3:
        strResult = "1조 AFT(12:00 ~ 17:50)\\n2조 2BRK\\n3조 MID(23:40 ~ 07:20)/SWI(17:40 ~ 23:50)\\n4조 1BRK\\n5조 MOR(07:10 ~ 12:10)"
    elif calcValue == 4:
        strResult = "1조 1BRK\\n2조 MOR(07:10 ~ 12:10)\\n3조 AFT(12:00 ~ 17:50)\\n4조 2BRK\\n5조 MID(23:40 ~ 07:20)/SWI(17:40 ~ 23:50)"
    
    return strResult