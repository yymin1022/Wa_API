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
    pass

def messageHa():
    pass

def messageIreon():
    pass

def messageMooYaHo():
    pass

def messageReal():
    pass

def messageSalute():
    pass

def messageStop():
    pass

def messageWa():
    randInt = random.randrange(0, 5)
    messageStr = ""

    if randInt == 0:
        messageStr = "갑부;;"
    elif randInt == 1:
        messageStr = "기만;;"
    elif randInt == 2:
        messageStr = "ㄹㅇ;;"
    elif randInt == 3:
        messageStr = "마스터;;"
    elif randInt == 4:
        messageStr = "역시;;"

def messageWaSans():
    pass

def messageZara():
    pass

def messageZayazi():
    pass