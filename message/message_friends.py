import random


def message_friends(message, room, sends):
    if "동훈" in message:
        return message_donghoon()
    elif "민석" in message:
        return message_minseok()
    elif "민식" in message:
        return message_minsik()
    elif "상윤" in message:
        return message_sangyoon()
    elif "상혁" in message:
        return message_sanghyuk()
    elif "서건1우" in message:
        return message_sgw()
    elif "수현" in message or "수휫" in message:
        if "임수현" in message or "수휫" in message:
            return message_limsoo()
        else:
            return message_soohyun()
    elif "여진" in message or "김여진" in message:
        return message_yeojin()
    elif "유용민" in message:
        if "바보" in message:
            return message_stupidYongmin(0)
        elif "천재" in message:
            return message_stupidYongmin(1)
        else:
            return message_stupidYongmin(2)
    elif "용민" in message:
        return message_yongmin()
    elif "유빈" in message or "서유빈" in message:
        return message_vini()
    elif "주형" in message:
        return message_joohyeong()
    elif "준섭" in message:
        return message_junseob()
    elif "태환" in message:
        return messageTaehwan()
    elif "호규" in message:
        return message_hokyu()
    elif "훈의" in message:
        return message_hoon()
    elif "GDG" in message:
        return message_gdg()
    elif "GDSC" in message:
        return message_not_gdsc()

def message_donghoon():
    messages=[
        "ㅋㅋ 동훈이 바보",
        "상윤이는 내꺼야.",
        "땅유나 따랑해",
        "똥후니는 똑똑하고 귀엽고 잘생기고 멋지고 착해. 구치 애두랍~?",
        "예. 저는 대졸입니다.",
        "대학원 올래?"
    ]
    return random.choice(messages)

def message_hokyu():
    messages = [
        "필승! 전문-38기 하사 김호규입니다!",
        "예! 하사 김호규!",
        "ㅍ승!",
        "안녕하세요? 전역하지 않기로 한 김호규입니다.",
        "팬택 핥짝",
        "베가 핥짝 핥짝",
        "호구",
        "K2C1 핥짝핥짝",
        "감사합니다. 314대대 통신반 김호규 하사입니다. 머슼타드일까요?",
        "악! 소위 김호규!",
        "아...\\m전역하기 싫다...",
        "SFF 핥짝핥짝"
    ]
    return random.choice(messages)

def message_hoon():
    messages = ["여진이는 어딨어?", "주먹밥", "멋쟁이 기획 부장", "세콤의 얼굴", "훈이야 ~ 놀자 ~", "한화 최고"]
    return random.choice(messages)

def message_joohyeong():
    strMessage = "예! 2025년도 CECOM 회장 이주형!"

    return strMessage

def message_junseob():
    messages = [
        "준섭아 컴공인 척 하지마",
        "준섭이는 유명한 납땜러",
        "준섭아 이상한거 좀 그만 사...",
        "준섭이가 사주는 술 마시러 갈사람~",
        "김준섭 박사기원 N일차",
        "그거 아세요? 준섭이가 미래의 CECOM 회장이래요",
        "준섭이는 미래의 코딩의 신",
        "준섭아 맛있는거 만들어줘",
    ]
    return random.choice(messages)

def message_limsoo():
    messages = ["임수현이 졸업했는데 왜 찾아?","안녕티비 ㅋㅋ","아 진짜?","넹구리","엥?","수현이는 혼자서도 잘 살아요"]
    return random.choice(messages)

def message_minseok():
    strMessage = "와봇은 민석이가 지배했다!"

    return strMessage

def message_minsik():
    strMessage = "민식아 그래서 학교는 언제와?"

    return strMessage

def message_sanghyuk():
    messages = ["대.상.혁", "상혁아 이거 어떻게 해?", "적분의 신", "대대대", "누나 미워"]
    return random.choice(messages)

def message_sangyoon():
    messages=[
        "상윤아 트월킹 춰 줘",
        "상윤아 잠 좀 자",
        "상윤아 커피 좀 그만 마셔",
        "알파 메일 김상윤!",
        "똥훈아 따랑해",
        "동훈이 보러가자!"
    ]
    return random.choice(messages)

def message_sgw():
    messages = ["좀 나가라;;", "뭐하냐;", "좀 꺼라;", "이미 차단당한 유저입니다."]
    return random.choice(messages)

def message_soohyun():
    strMessage = "수현이? 무슨 수현이?"
    return strMessage

def message_stupidYongmin(type):
    strMessage = ""
    if type == 0:
        strMessage = "그렇지~"
    elif type == 1:
        strMessage = "겠냐?"
    elif type == 2:
        strMessage = "바보~"

    return strMessage

def messageTaehwan():
    messages = ["와..~ 용민형님","용민형님 기다리고 있었습니다","굿아이디어","그게 맞지","뭔지 알지","그건 틀렸어","헉..","와! 알바메일 권태환!"]
    return random.choice(messages)

def message_vini():
    messages = ["|￣￣￣￣￣￣￣￣￣|\\n| *ﾟ 방금 서유빈 +    |\\n|　 왜 불렀지... .　 ﾟ  |\\n|＿＿＿＿　＿＿＿＿|\\n　　 ∧　∧||∧　∧\\n　　(｡･Α･∩∩･∀･｡)\\n　　 Οu_ΟΘ_uΘ","안녕하세용가리","우리 유빈이 즐~대 디자이너 아입니다!","┌───────────────┐\\n        방금 유빈이 부른 사람\\n└───────────────┘\\n　　ᕱ ᕱ ||\\n　 ( ･ω･ ||\\n　 /　つΦ\\n"," ⋆͛*͛ ͙͛ ⁑͛⋆͛*͛ ͙͛(๑•﹏•)⋆͛*͛ ͙͛ ⁑͛⋆͛*͛ ͙͛ "]
    return random.choice(messages)

def message_yeojin():
    messages = ["오나핑 여진이",
              "여진이 바빠요",
              "2024 GDG 오거나이저!\\m김여진!",
              "여지니 왜 불러요?\\m난 왜 안 찾아?"
    ]

    return random.choice(messages)

def message_yongmin():
    strMessage = "집가고싶다"

    return strMessage

def message_gdg():
    strMessage = "GDG on Campus: CAU 최고 ~!~!~!~!@"
    return strMessage

def message_not_gdsc():
    strMessage = ["아뇨. GDG 인데요.", "이제 GDG라니깐요?!", "GDG입니다.", "GDSC는 이제 없어요.", "GDG! GDG!! GDG!@!@!@!"]
    return random.choice(strMessage)