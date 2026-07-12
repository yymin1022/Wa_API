import random

import certifi
import requests

from models import WaMessage


def message_meme(wa_message: WaMessage):
    message = wa_message.msg
    room = wa_message.room
    sender = wa_message.sender
    if "아.." in message:
        return message_ah()
    elif "안사요" in message or "안 사요" in message or "사지말까" in message or "사지 말까" in message or "안살래" in message or "안 살래" in message:
        return message_ahnsa()
    elif "응애" in message:
        return message_baby()
    elif "비트코인" in message:
        return message_bitcoin()
    elif "불편" in message:
        return message_boolpyeon()
    elif "사고싶" in message or "사야" in message or "살까" in message or "샀어" in message or "샀다" in message or "샀네" in message or "사버렸" in message:
        return message_buy()
    elif "개발해야" in message or "코딩해야" in message or "과제해야" in message:
        return message_coding()
    elif "뭐먹" in message or "머먹" in message:
        return message_eat()
    elif "거북이" in message:
        return message_ggobugi()
    elif ("제발" in message or "하고 싶다" in message) and "졸업" in message:
        return message_graduate()
    elif "하.." in message:
        return message_ha()
    elif "배고파" in message or "배고프" in message:
        return message_hungry()
    elif "이런.." in message:
        return message_ireon()
    elif "과제" in message or "집가고싶다" in message:
        return message_minsik_booreop()
    elif "ㅡㅡ" in message:
        return message_mm()
    elif ("앎" in message or "아는사람" in message) or "알아" in message:
        return message_moloo()
    elif "무야호" in message:
        return message_mooyaho()
    elif "꺼라" in message:
        return message_off()
    elif "오호" in message or "호오" in message:
        return message_oho(message)
    elif "오.." in message:
        return message_oh()
    elif "오케이" in message:
        return message_okay()
    elif "퇴근" in message:
        return message_outwork()
    elif "ㄹㅇㅋㅋ" in message:
        return message_real()
    elif "^^7" in message:
        return message_salute()
    elif "나스" in message:
        return message_saseyo()
    elif "슈슉" in message:
        return message_shuk()
    elif "졸려" in message or "잠와" in message or "피곤해" in message:
        return message_sleepy()
    elif "마법의 소라고동이시여" in message:
        return message_sora(message)
    elif "멈춰" in message:
        return message_stop()
    elif "어.." in message:
        return message_uh()
    elif "럭키" in message or "운세" in message:
        return message_viki()
    elif "와.." in message:
        return message_wa()
    elif "와!" in message:
        return message_wa_sans()
    elif "자라" in message:
        return message_zara()
    elif "자야" in message or "잘까" in message:
        return message_zayazi()
    return None

def message_ah():
    messages = ["글쿤..",
                "그래요..",
                "그렇군요..",
                "안돼..",
                "..메리카노",
                "..에이오우",
                "..아르키메데스의 원리"]
    return random.choice(messages)

def message_ahnsa():
    messages = ["이걸 안 사?",
                "왜요;;",
                "그거 사면 진짜 좋을텐데..",
                "아..",
                "헐..",
                "너한테 안 팔아;;"]
    return random.choice(messages)

def message_baby():
    messages = ["귀여운척 하지 마세요;;",
                "응애 나 애기",
                "응애 나 아기 코린이"]
    return random.choice(messages)

def message_bitcoin():
    request_url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
    try:
        response = requests.get(request_url, verify = certifi.where())
        response.raise_for_status()
        data = response.json()
        current_price = data[0]["trade_price"]
        str_message = f"와! 비트코인 현재가 : {current_price}원! 지금 사요?"
    except requests.exceptions.RequestException:
        str_message = "비트코인 가격을 불러오는 중 오류가 발생했습니다."

    return str_message

def message_boolpyeon():
    str_message = "불편해?\\m불편하면 자세를 고쳐앉아!\\m보는 자세가 불편하니깐 그런거아냐!!"
    return str_message

def message_buy():
    messages = ["축하합니다!!!",
                "그걸 샀네;;",
                "개부자;;",
                "와 샀네",
                "이걸 산다고?",
                "ㅋㅋ",
                "왜요",
                "그거 살 돈이면 차라리..\\m.........",
                "ㅋㅋ 그걸 누가 삼"]
    return random.choice(messages)

def message_coding():
    messages = ["구라ㅡㅡ;;",
                "ㅋ",
                "밤새도 못 할 듯?ㅋㅋ"]
    return random.choice(messages)

def message_eat():
    messages = ["돼지", "또 먹어?", "살쪄", "그만 먹어;;", "된장찌개!!", "부리또!!", "김볶밥!!",
                "김치찌개!!", "햄버거!!", "부찌!!", "불고기!!", "삼겹살!!", "돼지갈비!!", "황금볶음밥!!",
                "미역국!!", "닭갈비!!", "떡볶이!!", "순두부찌개!!", "돈까스!!", "곱창!!", "콩나물국!!",
                "짜장면!!", "감자전!!", "짬뽕!!", "해물탕!!", "감자탕!!", "치킨!!", "라면!!",
                "샌드위치!!", "피자!!", "파스타!!", "햄버거!!", "샐러드!!", "쌈밥!!",
                "고무장갑 구이!!", "화분 케이크!!", "민트 초코맛 라면!!", "콜라에 밥 말아먹기!!",
                "플라스틱 튀김!!", "LED 광케이블 라조냐!!", "아이폰 스파게티!!",
                "바질리카 소스를 곁들인 크림리 소프트 쉘 크랩 파스타!!",
                "천천히 구운 로즈메리 향이 나는 양갈비와 민트 소스!!",
                "풍미 가득 허브와 치즈가 어우러진 랙 오브 램!!",
                "더블 초콜릿 퍼지 브라우니와 바닐라 아이스크림!!",
                "바다의 맛이 느껴지는 신선한 랍스터 테르미도르!!"]
    return random.choice(messages)

def message_ggobugi():
    rand_int = random.randrange(0, 3)
    str_message = ""

    if rand_int == 0:
        return "자라"

    if random.randrange(0, 2) == 0:
        ggobugi_message = "효과는 굉장했다!"
    else:
        ggobugi_message = "효과가 별로인 듯하다..."

    if rand_int == 1:
        str_message = f"꼬부기는 몸통박치기를 사용했다.\\m{ggobugi_message}"
    elif rand_int == 2:
        str_message = f"꼬부기는 물대포를 사용했다.\\m{ggobugi_message}"

    return str_message

def message_graduate():
    messages = ["대학원 가셔야죠 ㅋㅋ",
                "졸업은 무슨",
                "노예 하셔야죠 ㅋㅋ",
                "어림도 없지 ㅋㅋ",
                "졸업은 무슨 ㅋㅋ",
                "박사도 해야죠 ㅋㅋ"]
    return random.choice(messages)

def message_ha():
    messages = ["코딩하기 싫다..",
                "과제하기 싫다..",
                "걍 놀고 싶다..",
                "걍 자고 싶다..",
                "걍 쉬고 싶다..",
                "퇴근하고 싶다..",
                "집 가고 싶다..",
                "퇴사하고 싶다.."]
    return random.choice(messages)

def message_hungry():
    messages = ["돼지",
                "또 먹어?",
                "살쪄",
                "그만 먹어;;",
                "아까 먹었잖아"]
    return random.choice(messages)

def message_ireon():
    messages = ["안됐군요..",
                "안타깝네요..",
                "눈물이 납니다..",
                "유감입니다..",
                "불쌍하네요..",
                "아쉽네요..",
                "저런.."]
    return random.choice(messages)

def message_minsik_booreop():
    str_message = "2023-1학기 복학한 민식아 이제 안부럽다"
    return str_message

def message_moloo():
    str_message = "몰?루"
    return str_message

def message_mooyaho():
    str_message = "그만큼 신나신다는거지~"
    return str_message

def message_mm():
    str_message = "정색하지 마세요;;"
    return str_message

def message_off():
    str_message = "전기세 아깝다ㅡㅡ;;"
    return str_message

def message_oh():
    messages = ["..레오", "..렌지쥬스", "..필승 코리아", "..카리나", "..리 꽥꽥"]
    return random.choice(messages)

def message_outwork():
    messages = ["출근하세요", "평생 쉬세요~", "집가고싶다", "어딜 쉬러가요", "오늘 야근이에요"]
    return random.choice(messages)

def message_oho(message):
    str_message = message[::-1]
    return str_message

def message_okay():
    str_message = "땡큐! 4딸라!"
    return str_message

def message_real():
    messages = ["ㄹㅇㅋㅋ", "아닌데요", "ㄹㅇ임ㅋㅋ"]
    return random.choice(messages)

def message_salute():
    messages = ["필승! ^^7", "충성! ^^7", "훈련병들은 충성! ^^7", "훈련병들은 필승! ^^7"]
    return random.choice(messages)

def message_saseyo():
    messages = ["사세요", "안 사도 돼요", "나스는 역시 시놀로지죠~", "나스는 역시 큐냅이죠~"]
    return random.choice(messages)

def message_shuk():
    str_message = "슈슉"
    messages = [".슉.슈슉.시.발럼",
                ".슈슉.슉.슉시",
                ".슈발놈아.슉.시발.슈슉.슉",
                ".슈슉.시발.럼아.슉.슈슉.슉.슉슉.슈슉.시.발놈아"]
    return f"{str_message}{random.choice(messages)}.슉"

def message_sleepy():
    messages = ["자라;;",
                "구라;;",
                "자야지;;",
                "자야겠다;;",
                "자야겠다..",
                "졸린게 말이 돼?",
                "그만 좀 자라;;"]
    return random.choice(messages)

def message_sora(message):
    question = message.replace("마법의 소라고동이시여", "").strip()
    if not question:
        return "말 해"
    else:
        messages = ["그럼",
                    "아마",
                    "안 돼",
                    "다시 한번 물어봐"]
        return random.choice(messages)

def message_stop():
    str_message = "멈춰!!"
    return str_message

def message_uh():
    messages = ["..이가없네;;",
                "..피치",
                "..기여차"]
    return random.choice(messages)

def message_viki():
    messages = ["오늘의 운세는 이븐~하게 익지 않았어요.",
                "오늘의 운세는 이븐~하게 익지 않았어요.",
                ".....∧_∧\\n.. ( ̳• ·̫ • ̳) \\n┏ー∪∪━━━━━━━━┓\\n  °•. 오늘운세구려요.. . .•°\\n┗━--━━━━━•━━━┛",
                ".....∧_∧\\n.. ( ̳• ·̫ • ̳) \\n┏ー∪∪━━━━━━━━┓\\n  °•. 오늘운세구려요.. . .•°\\n┗━--━━━━━•━━━┛",
                ". /)_/)\\n( ̳• ·̫ • ̳)   럭키. .ꕥ 할지도\\n/>ꕥ<",
                "＿人人人人人人人人＿\\n＞ 오늘 운세 낫배드! ＜\\n￣Y^Y^Y^Y^Y^Y^Y^Y￣\\n　 _n　( ｜　 ハ_ハ\\n　 ＼＼ ( ‘-^　)\\n　　 ＼￣￣　 )\\n　　　 ７　　/",
                "오늘은 평범-한 날이예요","오늘 당신 초-럭키༘˚⋆𐙚｡ \\n 동방에 방문하면 좋은 일이 생길지도⋆𖦹.✧˚",
                "♡ ♡ ♡ ₍ᐢɞ̴̶̷.̮ɞ̴̶̷ᐢ₎ ♡ ♡ ♡\\n┏━♡━ U U━♡━━┓\\n♡오늘의 운세는···     ♡\\n♡초초초럭키-예요!   ♡\\n┗━♡━━━━♡━━┛"]
    return random.choice(messages)

def message_wa():
    messages = ["갑부;;",
                "기만;;",
                "ㄹㅇ;;",
                "마스터;;",
                "역시;;",
                "이건 좀;;",
                "극혐;;",
                "플;;",
                "이파이;;",
                "내가 봐도 선 넘었네;;",
                "사비;;"]
    return random.choice(messages)

def message_wa_sans():
    str_message = "샌즈!\\m아시는구나!\\m이거 겁.나.어.렵.습.니.다."
    return str_message

def message_zara():
    messages = ["전기세 아깝다ㅡㅡ;;",
                "거북이",
                "..투스트라는 이렇게 말했다.",
                "..ZARA는 스페인에 본사를 둔 글로벌 패션 그룹 인디텍스를 모회사로 두고 있는 SPA 브랜드로, SPA 브랜드 중 세계 최대 매출을 기록하고 있습니다.",
                "잘 자라^^",
                "자라는 토끼랑 달리기 경주 중"]
    return random.choice(messages)

def message_zayazi():
    str_message = "구라ㅡㅡ;;"
    return str_message