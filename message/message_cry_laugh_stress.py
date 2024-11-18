import random

def message_cry_laugh_stress(message):
    if ("ㅠ" in message or "ㅜ" in message) and get_cry_count(message) >= 3:
        return message_cry()
    elif ("ㅋ" in message or "ㅎ" in message) and get_laugh_count(message) >= 20:
        return message_laugh()
    elif ";" in message and get_stress_count(message) >= 4:
        return message_stress()
    return None

def get_cry_count(message):
    count = message.count("ㅠ")
    count += message.count("ㅜ")

    return count

def get_laugh_count(message):
    count = message.count("ㅋ")
    count += message.count("ㄱ")
    count += message.count("ㄲ")
    count += message.count("ㄴ")
    count += message.count("ㅌ")
    count += message.count("ㅎ")

    return count

def get_stress_count(message):
    count = message.count(";")
    count += message.count(":")
    count += message.count(",")
    count += message.count(".")

    return count

def message_cry():
    messages = ["뭘 울어요;;", "왜 우시는 거예요?", "ㅋㅋ얘 운다"]
    return random.choice(messages)

def message_laugh():
    messages = ["뭘 웃어요;;", "안웃긴데;;", "이게 웃겨요?"]
    return random.choice(messages)

def message_stress():
    strMessage = "어림도 없지"

    return strMessage