import datetime
import random

from message_util import message_datetime


def message_graduate(message, room, sender):
    if "소해" in message or "졸업" in message or "전역" in message:
        if "병희" in message:
            return message_bh_graduate()
        elif "창환" in message:
            return message_chals_graduate()
        elif "한수" in message:
            return message_hansu_graduate()
        elif "호규" in message:
            return message_hokyu_graduate()
        elif "재민" in message:
            return message_jaemin_graduate()
        elif "성민" in message:
            return message_seongmin_graduate()
        elif "승범" in message:
            return message_seungbeom_graduate()
        elif "수필" in message:
            return message_supil_graduate()
        elif "태식" in message:
            return message_tjo_graduate()
    return None

def message_bh_graduate():
    strMessage = ""

    randInt = random.randrange(0,2)
    if randInt == 0: strMessage = "임병희씨가 입대한지 %d일, 전역한지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2020,6,30)).days, (datetime.date.today() - datetime.date(2021,12,29)).days)
    elif randInt == 1: strMessage = "임병희씨의 예비군 소집해제일까지 %d일 남았습니다."%((datetime.date(2029,12,31) - datetime.date.today()).days)
    return strMessage

def message_chals_graduate():
    strMessage = "찰스가 입대한지 %d일, 전역한지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2020,12,7)).days, (datetime.date.today() - datetime.date(2022,9,1)).days)

    return strMessage

def message_hansu_graduate():
    strMessage = ""
    randInt = random.randrange(0,2)
    if randInt == 0: strMessage = "이한수씨가 소집된지 %d일, 해제된지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2022,12,1)).days, (datetime.date.today() - datetime.date(2024,8,31)).days)
    elif randInt == 1: strMessage = "이한수씨의 민방위 소집해제일까지 %d일 남았습니다."%((datetime.date(2039,1,1) - datetime.date.today()).days)

    return strMessage

def message_hokyu_graduate():
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

def message_jaemin_graduate():
    randInt = random.randrange(0, 2)
    strMessage = ""

    if randInt == 0: strMessage = "재민이가 입대한지 %d일, 전역한지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2021,5,9)).days, (datetime.date.today() - datetime.date(2024,3,8)).days)
    elif randInt == 1: strMessage = "재민이의 예비군 소집해제일까지 %d일 남았습니다."%((datetime.date(2031,12,31) - datetime.date.today()).days)

    return strMessage

def message_seungbeom_graduate():
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

def message_supil_graduate():
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

def message_seongmin_graduate():
    strMessage = ""
    randInt = random.randrange(0,2)
    if randInt == 0: strMessage = "지성민씨가 소집된지 %d일, 소해된지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2022,5,22)).days, (datetime.date.today() - datetime.date(2024,2,22)).days)
    elif randInt == 1: strMessage = "지성민씨의 예비군 소집해제일까지 %d일 남았습니다."%((datetime.date(2031,12,31) - datetime.date.today()).days)
    return strMessage

def message_tjo_graduate():
    strMessage = "zz"

    return strMessage