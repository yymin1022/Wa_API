# 이 코드를 실행하기 전에 먼저 Wa API를 구동해야 합니다.
import requests
import json

url = "http://localhost/getMessage"
json_data = {
    "msg": "!택배 533467568432",
    "room": "아 1집가고싶다",
    "sender": "Changhwan"
}

response = requests.post(url, json=json_data)
data = response.json()

print('msg:', data['DATA']['msg'])
print('room:', data['DATA']['room'])
print('sender:', data['DATA']['sender'])