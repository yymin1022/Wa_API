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
    weekly = 0
    day = datetime.datetime.now()
    try:
        if "주" in message:
            weekly = 1
        message = message.replace("!날짜더하기", "").replace("!날짜빼기", "").replace(" ", "").replace("일", "").replace("주", "")
        if not message.isdigit():
            raise
        if cal == 1:
            if weekly == 1:
                dday = day + datetime.timedelta(days=int(message) * 7)
                return f"오늘을 기준으로 {message}주 후는 {dday.year}년 {dday.month}월 {dday.day}일입니다."
            else:
                dday = day + datetime.timedelta(days=int(message))
                return f"오늘을 기준으로 {message}일 후는 {dday.year}년 {dday.month}월 {dday.day}일입니다."
        elif cal == 0:
            if weekly == 1:
                dday = day - datetime.timedelta(days=int(message) * 7)
                return f"오늘을 기준으로 {message}주 전은 {dday.year}년 {dday.month}월 {dday.day}일입니다."
            else:
                dday = day - datetime.timedelta(days=int(message))
                return f"오늘을 기준으로 {message}일 전은 {dday.year}년 {dday.month}월 {dday.day}일입니다."
    except TypeError:
        return "존재하지 않는 날짜이거나 사용 불가능한 형식입니다.\\mex) !날짜더하기 100일 or !날짜빼기 16주"
    return None

def message_date_calculator(y, m, d):
    date_end = datetime.date(y,m,d)
    date_today = datetime.date.today()
    now = datetime.datetime.now()
    left_days = (date_end - date_today).days
    left_hours = 24 - now.hour - 1
    left_minutes = 60 - now.minute - 1
    left_seconds = 60 - now.second - 1
    left_seconds_wa = ((left_days - 1) * 24 * 60 * 60) + (left_hours * 60 * 60) + (left_minutes * 60) + left_seconds
    return left_days, left_hours, left_minutes, left_seconds, left_seconds_wa

def message_dday(message):
    try:
        message = message.replace("!디데이", "").replace("!day", "").replace(" ", "")
        if message.strip()[-1] == '.': message = message[:-1]
        if message.count('-') == 2 or message.count('.') == 2:
            if "-" in message:
                message = message.split("-")
            elif "." in message:
                message = message.split(".")
            if len(str(message[0])) == 2:
                message[0] = "20" + message[0]
            y, m, d = int(message[0]), int(message[1]), int(message[2])
            message_date_calculator(y, m, d)
            left_days, left_hours, left_minutes, left_seconds, left_seconds_wa = message_date_calculator(y, m, d)
            if left_days < 0:
                return f"{message[0]}년 {message[1]}월 {message[2]}일을 기준으로 오늘은 {format(int(left_days * -1), ',')}일이 지났으며, 이를 초 단위로 환산하면 {format(int(left_seconds_wa * -1), ',')}초입니다."
            elif left_days == 0:
                return "D-DAY입니다!"
            else:
                return f"{message[0]}년 {message[1]}월 {message[2]}일까지는 {format(left_days, ',')}일이 남았으며, 이를 초 단위로 환산하면 {format(left_seconds_wa, ',')}초입니다."
        else: raise
    except TypeError:
        return "존재하지 않는 날짜이거나 사용 불가능한 형식입니다.\\mex) !day 2023.9.8 or !디데이 23.12.31"

def message_timezone(message):
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
        str_message = f"현재 UTC{message}의 시간은 ", adjusted_time.strftime('%Y-%m-%d %H:%M:%S') , "입니다."
    except TypeError:
        str_message = "사용 형식이 잘못됐거나 존재하지 않는 시간대입니다.\\m사용법: !시간 +9 or !시간 -11"
    return str_message