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
    messages = ["임병희씨가 입대한지 %d일, 전역한지는 %d일이 됐습니다." %((datetime.date.today() - datetime.date(2020,6,30)).days, (datetime.date.today() - datetime.date(2021,12,29)).days),
                "임병희씨의 예비군 소집해제일까지 %d일 남았습니다." %(datetime.date(2029, 12, 31) - datetime.date.today()).days]
    return random.choice(messages)

def message_chals_graduate():
    str_message = "찰스가 입대한지 %d일, 전역한지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2020,12,7)).days, (datetime.date.today() - datetime.date(2022,9,1)).days)

    return str_message

def message_hansu_graduate():
    messages = ["이한수씨가 소집된지 %d일, 해제된지는 %d일이 됐습니다." %((datetime.date.today() - datetime.date(2022,12,1)).days, (datetime.date.today() - datetime.date(2024,8,31)).days),
                "이한수씨의 민방위 소집해제일까지 %d일 남았습니다." %(datetime.date(2039, 1, 1) - datetime.date.today()).days]
    return random.choice(messages)

def message_hokyu_graduate():
    messages = ["호규의 부사후 249기 지원을 응원합니다!",
                "호규의 학사 152기 지원을 응원합니다!",
                "호규의 예비군 소집해제일까지 %d일 남았습니다."%((datetime.date(2030,12,31) - datetime.date.today()).days -1),
                "호규의 민방위 소집해제일까지 %d일 남았습니다."%((datetime.date(2041,4,28) - datetime.date.today()).days -1),
                "예비군 1년차는 좀...",
                "하사 김호규의 임기제부사관 만기복무일까지 %d일 남았습니다."%((datetime.date(2027,8,26) - datetime.date.today()).days -1)]
    return random.choice(messages)

def message_jaemin_graduate():
    messages = ["재민이가 입대한지 %d일, 전역한지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2021,5,9)).days, (datetime.date.today() - datetime.date(2024,3,8)).days),
                "재민이의 예비군 소집해제일까지 %d일 남았습니다."%(datetime.date(2031,12,31) - datetime.date.today()).days]
    return random.choice(messages)

def message_seungbeom_graduate():
    y, m, d = 2031, 2, 28
    message_datetime.message_date_calculator(y, m, d)
    left_days, left_hours, left_minutes, left_seconds, left_seconds_wa = message_datetime.message_date_calculator(y, m, d)

    messages = ["승범아 대학원 가야지?",
                "승범이가 박사과정을 마치기까지 %d일 %d시간 %d분 %d초 남았습니다."%(left_days - 1, abs(left_hours), left_minutes, left_seconds),
                "승범이가 박사과정을 마치기까지 " + format(left_seconds_wa, ',') + "초 남았습니다."]
    return random.choice(messages)

def message_supil_graduate():
    y, m, d = 2024, 11, 27
    message_datetime.message_date_calculator(y, m, d)
    left_days, left_hours, left_minutes, left_seconds, left_seconds_wa = message_datetime.message_date_calculator(y, m, d)

    messages = ["24년은 오지 않습니다...",
                "그런거 물어볼 시간에 일이나 하세요.",
                "박수필씨의 소집해제일까지 %d일이 남았습니다."%(left_days),
                "박수필씨의 소집해제일까지 %d일 %d시간 %d분 %d초 남았습니다."%(left_days - 1, abs(left_hours), left_minutes, left_seconds),
                "당신이 민간인이 될 때까지 " + format(left_seconds_wa, ',') + "초 남았습니다."]
    return random.choice(messages)

def message_seongmin_graduate():
    messages = ["지성민씨가 소집된지 %d일, 소해된지는 %d일이 됐습니다."%((datetime.date.today() - datetime.date(2022,5,22)).days, (datetime.date.today() - datetime.date(2024,2,22)).days),
                "지성민씨의 예비군 소집해제일까지 %d일 남았습니다."%(datetime.date(2031,12,31) - datetime.date.today()).days]
    return random.choice(messages)

def message_tjo_graduate():
    str_message = "zz"

    return str_message