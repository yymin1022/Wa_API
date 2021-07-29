from bs4 import BeautifulSoup

import datetime
import random
import requests

def getReplyMessage(message):
    strResult = ""

    if "아.." in message:
        strResult = messageAh()
    elif "응애" in message:
        strResult = messageBaby()
    elif "개발해야" in message or "코딩해야" in message or "과제해야" in message:
        strResult = messageCoding()
    elif ("코로나" in message or "확진자" in message) and "몇" in message:
        strResult = messageCorona()
    elif "뭐먹" in message:
        strResult = messageEat()
    elif ("제발" in message or "하고 싶다" in message) and "졸업" in message:
        strResult = messageGraduate()
    elif "하.." in message:
        strResult = messageHa()
    elif "호규" in message:
        strResult = messageHokyu()
    elif "배고파" in message:
        strResult = messageHungry()
    elif "이런.." in message:
        strResult = messageIreon()
    elif ("ㅋ" in message or "ㅎ" in message) and getLaughCount(message) >= 10:
        strResult = messageLaugh()
    elif "무야호" in message:
        strResult = messageMooYaHo()
    elif "꺼라" in message:
        strResult = messageOff()
    elif "오케이" in message:
        strResult = messageOkay()
    elif "ㄹㅇㅋㅋ" in message:
        strResult = messageReal()
    elif "^^7" in message:
        strResult = messageSalute()
    elif "나스" in message or "폴리오" in message:
        strResult = messageSaseyo()
    elif "슉" in message or "슈슉" in message:
        strResult = messageShuk()
    elif "멈춰" in message:
        strResult = messageStop()
    elif (";" in message or "," in message) and getStressCount(message) >= 4:
        strResult = messageStress()
    elif "와.." in message:
        strResult = messageWa()
    elif "와!" in message:
        strResult = messageWaSans()
    elif "오늘" in message and "근무" in message:
        strResult = messageWork()
    elif "용민" in message:
        strResult = messageYongmin()
    elif "자라" in message:
        strResult = messageZara()
    elif "자야" in message:
        strResult = messageZayazi()

    return strResult

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
    randInt = random.randrange(0, 8)
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
        strMessage = "메리카노.."
    elif randInt == 5:
        strMessage = "냄새나요;"
    elif randInt == 6:
        strMessage = "흑우가 또.."
    elif randInt == 7:
        strMessage = "정신 나갈 거 같애.."
    
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

def messageCoding():
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0:
        strMessage = "구라ㅡㅡ;;"
    elif randInt == 1:
        strMessage = "ㅋ"

    return strMessage

def messageCorona():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    url = "http://ncov.mohw.go.kr/"

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, features="html.parser")

    divTable = soup.find("div", class_="liveboard_layout")
    divLive = divTable.find("div", class_="liveNumOuter")
    divData = divLive.find("div", class_="liveNum")
    strDate = divLive.find("span", class_="livedate").text
    strTotal = divData.find_all("span", class_="num")[0].text.split(")")[1]
    strToday = divData.find_all("span", class_="before")[0].text.split(" ")[2][:-1]

    strMessage = "어제 %s명\\n누적 %s명\\n%s"%(strToday, strTotal, strDate)

    return strMessage

def messageEat():
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
        strMessage = "어림도 없지"

    return strMessage

def messageHa():
    strMessage = "코딩하기 싫다.."

    return strMessage
    
def messageHokyu():
    dateStart = datetime.date(2021,7,19)
    dateEnd = datetime.date(2023,1,18)
    dateToday = datetime.date.today()
    strMessage = ""
    
    leftDays = (dateEnd - dateToday).days
    goneDays = (dateToday - dateStart).days
    
    randInt = random.randrange(0, 4)
    if randInt == 0:
        strMessage = "안녕하십니까? 아미타이거 육군 김호규입니다."
    elif randInt == 1:
        strMessage = "응애 나 애기 호규."
    elif randInt == 2:
        strMessage = "돔황챠!"
    elif randInt == 3:
        strMessage = "안녕하세요? 민간인 김호규입니다."
        
# 입대 시 변경 바람
#    elif randInt == 2:
#        strMessage = "호규는 2021년 7월 19일 입대했습니다. 2023년 1월 18일 전역 예정입니다. %d일 남았습니다."%(leftDays)
#    elif randInt == 3:
#        strMessage = "호규가 입대한 지 %d일 되었습니다."%(goneDays)
    
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
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0:
        strMessage = "안됐군요.."
    elif randInt == 1:
        strMessage = "안타깝네요.."
    
    return strMessage

def messageLaugh():
    strMessage = "뭘 웃어요;;"

    return strMessage

def messageMooYaHo():
    strMessage = "그만큼 신나신다는거지~"

    return strMessage

def messageOff():
    strMessage = "전기세 아깝다ㅡㅡ;;"

    return strMessage

def messageOkay():
    strMessage = "땡큐! 4딸라!"

    return strMessage

def messageReal():
    strMessage = "ㄹㅇㅋㅋ"

    return strMessage

def messageSalute():
    strMessage = "^^7"

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

def messageStop():
    strMessage = "멈춰!!"

    return strMessage

def messageStress():
    strMessage = "어림도 없지"

    return strMessage

def messageWa():
    randInt = random.randrange(0, 8)
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
        strMessage = "흑우;;"
    elif randInt == 7:
        strMessage = "돼지;;"

    return strMessage

def messageWaSans():
    strMessage = "샌즈!\\m아시는구나!\\m이거 겁.나.어.렵.습.니.다."

    return strMessage

def messageWork():
    dateStart = datetime.date(2021,3,1)
    dateToday = datetime.date.today()
    
    countDays = (dateToday - dateStart).days

    strMessage = "병사\\n%s\\n\\n간부\\n%s"%(calcByeongsa(countDays), calcGanbu(countDays))

    return strMessage

def messageYongmin():
    randInt = random.randrange(0, 3)
    strMessage = ""
    
    if randInt == 0:
        strMessage = "감사합니다. MCC 상병 유용민입니다. 머슼타드일까요?"
    elif randInt == 1:
        strMessage = "감사합니다. 체계운영실 상병 유용민입니다. 머슼타드일까요?"
    elif randInt == 2:
        strMessage = "감사합니다. 보라매 바동 1생활관 생활관장 상병 유용민입니다. 머슼타드일까요?"

    return strMessage

def messageZara():
    strMessage = "전기세 아깝다ㅡㅡ;;"
    return strMessage

def messageZayazi():
    strMessage = "구라ㅡㅡ;;"

    return strMessage

def calcByeongsa(days):
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

def calcGanbu(days):
    calcValue = days % 8
    strResult = ""
    
    if calcValue == 0:
        strResult = "A조 S/B\\nB조 2MID(23:20 ~ 07:30)/1SWI(17:00 ~ 23:30)\\nC조 1BRK\\nD조 1DAY(07:20 ~ 17:10)"
    elif calcValue == 1:
        strResult = "A조 1MID(23:20 ~ 07:30)\\nB조 2SWI(17:00 ~ 23:30)\\nC조 2BRK\\nD조 2DAY(07:20 ~ 17:10)"
    elif calcValue == 2:
        strResult = "A조 2MID(23:20 ~ 07:30)/1SWI(17:00 ~ 23:30)\\nB조 1BRK\\nC조 1DAY(07:20 ~ 17:10)\\nD조 S/B"
    elif calcValue == 3:
        strResult = "A조 2SWI(17:00 ~ 23:30)\\nB조 2BRK\\nC조 2DAY(07:20 ~ 17:10)\\nD조 1MID(23:20 ~ 07:30)"
    elif calcValue == 4:
        strResult = "A조 1BRK\\nB조 1DAY(07:20 ~ 17:10)\\nC조 S/B\\nD조 2MID(23:20 ~ 07:30)/1SWI(17:00 ~ 23:30)"
    elif calcValue == 5:
        strResult = "A조 2BRK\\nB조 2DAY(07:20 ~ 17:10)\\nC조 1MID(23:20 ~ 07:30)\\nD조 2SWI(17:00 ~ 23:30)"
    elif calcValue == 6:
        strResult = "A조 1DAY(07:20 ~ 17:10)\\nB조 S/B\\nC조 2MID(23:20 ~ 07:30)/1SWI(17:00 ~ 23:30)\\nD조 1BRK"
    elif calcValue == 7:
        strResult = "A조 2DAY(07:20 ~ 17:10)\\nB조 1MID(23:20 ~ 07:30)\\nC조 2SWI(17:00 ~ 23:30)\\nD조 2BRK"
    
    return strResult
