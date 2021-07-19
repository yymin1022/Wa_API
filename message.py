import random

def getReplyMessage(message):
    strResult = message

    return strResult

def messageAh():
    randInt = random.randrange(0, 5)
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
    pass

def messageWaSans():
    pass

def messageZara():
    pass

def messageZayazi():
    pass