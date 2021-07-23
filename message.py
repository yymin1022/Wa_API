import random

def getReplyMessage(message):
    strResult = ""

    if "아.." in message:
        strResult = messageAh()
    elif "코딩해야" in message:
        strResult = messageCoding()
    elif "하.." in message:
        strResult = messageHa()
    elif "이런.." in message:
        strResult = messageIreon()
    elif "무야호" in message:
        strResult = messageMooYaHo()
    elif "ㄹㅇㅋㅋ" in message:
        strResult = messageReal()
    elif "^^7" in message:
        strResult = messageSalute()
    elif "멈춰" in message:
        strResult = messageStop()
    elif "와.." in message:
        strResult = messageWa()
    elif "와!" in message:
        strResult = messageWaSans()
    elif "자라" in message:
        strResult = messageZara()
    elif "자야" in message:
        strResult = messageZayazi()
    elif "응애" in message:
        strResult = messageBaby()

    return strResult

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
    strMessage = "구라ㅡㅡ;;"

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

def messageMooYaHo():
    strMessage = "그만큼 신나신다는거지~"

    return strMessage

def messageReal():
    strMessage = "ㄹㅇㅋㅋ"

    return strMessage

def messageSalute():
    strMessage = "^^7"

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
    strMessage = "샌즈!<br/>아시는구나!<br/>이거 겁.나.어.렵.습.니.다."

    return strMessage

def messageZara():
    strMessage = "전기요금 아깝다;;"

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
