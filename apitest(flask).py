# 이 코드를 실행하기 전에 먼저 Wa API를 구동해야 합니다.
import requests
import json

def post():
    url = "http://localhost/getMessage"
    json_data = {
        "msg": "와!",
        "room": "아 1집가고싶다",
        "sender": "Changhwan"
    }
    response = requests.post(url, json=json_data)
    with open('./data.json', 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)

post()
