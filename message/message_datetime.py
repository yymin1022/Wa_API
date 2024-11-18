import datetime


def message_datetime(message, room, sender):
    if "!날짜" in message:
        if "더하기" in message:
            return message_cal_day(1, message)
        elif "빼기" in message:
            return message_cal_day(0, message)
    if "!디데이" in message or "!day" in message:
        return message_dday(message)
    if "!시간" in message:
        return message_timezone(message)
    return None

def message_cal_day(cal, message):
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

def message_date_calculator(y, m, d):
    dateEnd = datetime.date(y,m,d)
    dateToday = datetime.date.today()
    now = datetime.datetime.now()
    leftdays = (dateEnd - dateToday).days
    lefthours = 24 - now.hour - 1
    leftminutes = 60 - now.minute - 1
    leftseconds = 60 - now.second - 1
    leftseconds_wa = ((leftdays - 1) * 24 * 60 * 60) + (lefthours * 60 * 60) + (leftminutes * 60) + leftseconds

    return leftdays, lefthours, leftminutes, leftseconds, leftseconds_wa

def message_dday(message):
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
            message_date_calculator(y, m, d)
            leftdays, lefthours, leftminutes, leftseconds, leftseconds_wa = message_date_calculator(y, m, d)
            if leftdays < 0: strMessage = "%s년 %s월 %s일을 기준으로 오늘은 %s일이 지났으며, 이를 초 단위로 환산하면 %s초입니다."%(message[0], message[1], message[2], format(int(leftdays * -1), ','), format(int(leftseconds_wa * -1), ','))
            elif leftdays == 0: strMessage = "D-DAY입니다!"
            else: strMessage = "%s년 %s월 %s일까지는 %s일이 남았으며, 이를 초 단위로 환산하면 %s초입니다."%(message[0], message[1], message[2], format(leftdays, ','), format(leftseconds_wa, ','))
        else: raise
    except:
        strMessage = "존재하지 않는 날짜이거나 사용 불가능한 형식입니다.\\mex) !day 2023.9.8 or !디데이 23.12.31"

    return strMessage

def message_timezone(message):
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