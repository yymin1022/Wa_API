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
    elif "하.." in message:
        strResult = messageHa()
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
    elif "멈춰" in message:
        strResult = messageStop()
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

def messageAh():
    randInt = random.randrange(0, 7)
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

    strMessage = "어제 %s명\\n\\n누적 %s명\\n\\n%s"%(strToday, strTotal, strDate)

    return strMessage

def messageEat():
    strMessage = "고기!!"

    return strMessage

def messageHa():
    strMessage = "코딩하기 싫다.."

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

def messageStop():
    strMessage = "멈춰!!"

    return strMessage

def messageWa():
    randInt = random.randrange(0, 7)
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

    return strMessage

def messageWaSans():
    strMessage = "샌즈!\\n\\n아시는구나!\\n\\n이거 겁.나.어.렵.습.니.다."

    return strMessage

def messageWork():
    dateStart = datetime.date(2021,3,1)
    dateToday = datetime.date.today()
    
    countDays = (dateToday - dateStart).days

    strMessage = "병사<br/>%s<br/><br/>간부<br/>%s"%(calcByeongsa(countDays), calcGanbu(countDays))

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

def messageOkay():
    strMessage = "땡큐! 4딸라!"

    return strMessage

def calcByeongsa(days):
    calcValue = days % 5
    strResult = ""
    
    if calcValue == 0:
        strResult = "1조 2BRK<br/>2조 MID(23:40 ~ 07:20)/SWI(17:40 ~ 23:50)<br/>3조 1BRK<br/>4조 MOR(07:10 ~ 12:10)<br/>5조 AFT(12:00 ~ 17:50)"
    elif calcValue == 1:
        strResult = "1조 MOR(07:10 ~ 12:10)<br/>2조 AFT(12:00 ~ 17:50)<br/>3조 2BRK<br/>4조 MID(23:40 ~ 07:20)/SWI(17:40 ~ 23:50)<br/>5조 1BRK"
    elif calcValue == 2:
        strResult = "1조 MID(23:40 ~ 07:20)/SWI(17:40 ~ 23:50)<br/>2조 1BRK<br/>3조 MOR(07:10 ~ 12:10)<br/>4조 AFT(12:00 ~ 17:50)<br/>5조 2BRK"
    elif calcValue == 3:
        strResult = "1조 AFT(12:00 ~ 17:50)<br/>2조 2BRK<br/>3조 MID(23:40 ~ 07:20)/SWI(17:40 ~ 23:50)<br/>4조 1BRK<br/>5조 MOR(07:10 ~ 12:10)"
    elif calcValue == 4:
        strResult = "1조 1BRK<br/>2조 MOR(07:10 ~ 12:10)<br/>3조 AFT(12:00 ~ 17:50)<br/>4조 2BRK<br/>5조 MID(23:40 ~ 07:20)/SWI(17:40 ~ 23:50)"
    
    return strResult

def calcGanbu(days):
    calcValue = days % 8
    strResult = ""
    
    if calcValue == 0:
        strResult = "A조 S/B<br/>B조 2MID(23:20 ~ 07:30)/1SWI(17:00 ~ 23:30)<br/>C조 1BRK<br/>D조 1DAY(07:20 ~ 17:10)"
    elif calcValue == 1:
        strResult = "A조 1MID(23:20 ~ 07:30)<br/>B조 2SWI(17:00 ~ 23:30)<br/>C조 2BRK<br/>D조 2DAY(07:20 ~ 17:10)"
    elif calcValue == 2:
        strResult = "A조 2MID(23:20 ~ 07:30)/1SWI(17:00 ~ 23:30)<br/>B조 1BRK<br/>C조 1DAY(07:20 ~ 17:10)<br/>D조 S/B"
    elif calcValue == 3:
        strResult = "A조 2SWI(17:00 ~ 23:30)<br/>B조 2BRK<br/>C조 2DAY(07:20 ~ 17:10)<br/>D조 1MID(23:20 ~ 07:30)"
    elif calcValue == 4:
        strResult = "A조 1BRK<br/>B조 1DAY(07:20 ~ 17:10)<br/>C조 S/B<br/>D조 2MID(23:20 ~ 07:30)/1SWI(17:00 ~ 23:30)"
    elif calcValue == 5:
        strResult = "A조 2BRK<br/>B조 2DAY(07:20 ~ 17:10)<br/>C조 1MID(23:20 ~ 07:30)<br/>D조 2SWI(17:00 ~ 23:30)"
    elif calcValue == 6:
        strResult = "A조 1DAY(07:20 ~ 17:10)<br/>B조 S/B<br/>C조 2MID(23:20 ~ 07:30)/1SWI(17:00 ~ 23:30)<br/>D조 1BRK"
    elif calcValue == 7:
        strResult = "A조 2DAY(07:20 ~ 17:10)<br/>B조 1MID(23:20 ~ 07:30)<br/>C조 2SWI(17:00 ~ 23:30)<br/>D조 2BRK"
    
    return strResult