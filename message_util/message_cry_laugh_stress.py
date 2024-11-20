import random


def message_cry_laugh_stress(message, room, sender):
    if "ㅠ" in message or "ㅜ" in message:
        return message_cry(message)
    elif "ㅋ" in message or "ㅎ" in message:
        return message_laugh(message)
    elif ";" in message:
        return message_stress(message)
    return None

def message_cry(message):
    messages = ["뭘 울어요;;",
                "왜 우시는 거예요?",
                "ㅋㅋ얘 운다"]
    if sum(message.count(char) for char in "ㅠㅜ") >= 3:
        return random.choice(messages)
    return None

def message_laugh(message):
    messages = ["뭘 웃어요;;",
                "안웃긴데;;",
                "이게 웃겨요?"]
    if sum(message.count(char) for char in "ㅋㄱㄲㄴㅌㅎ") >= 20:
        return random.choice(messages)
    return None

def message_stress(message):
    if sum(message.count(char) for char in ";:,.") >= 4:
        return "어림도 없지"
    return None