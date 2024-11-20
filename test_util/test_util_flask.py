import requests


url = "http://localhost/getMessage"
json_data = {
    "msg": "!택배 6091439711728",
    "room": "아 1집가고싶다",
    "sender": "Changhwan"
}

response = requests.post(url, json=json_data)
data = response.json()

print('msg:', data['DATA']['msg'])
print('room:', data['DATA']['room'])
print('sender:', data['DATA']['sender'])