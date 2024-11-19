import json
import os
import random


def message_onoff(message, room, sender):
    if "와봇" in message:
        if "꺼" in message or "끄" in message:
            return messageWabotPower(0, room)
        elif "켜" in message or "키" in message:
            return messageWabotPower(1, room)

def messageWabotPower(flag, room):
    strMessage = ""
    if os.path.isfile("power.json"):
        with open('power.json', 'r', encoding='utf-8') as f:
            power_dict = json.load(f)
        room_power = power_dict.get(room)
        if room_power is not None:
            if (flag == 0 and room_power == "0") or (flag == 1 and room_power == "1"):
                return strMessage
        else:
            if flag == 1: return strMessage
            else: pass
    else:
        power_dict = {}
    randInt = random.randrange(0, 4)
    if randInt == 0:
        if flag == 0:
            power_dict[room] = "0"
            json_data = json.dumps(power_dict, ensure_ascii=False, indent=4)
            strMessage = "와봇이 종료되었습니다."
        elif flag == 1:
            power_dict[room] = "1"
            json_data = json.dumps(power_dict, ensure_ascii=False, indent=4)
            strMessage = "와봇이 시작되었습니다."
        with open('power.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
    elif randInt == 1:
        strMessage = "싫은데? ^^"
    elif randInt == 2:
        strMessage = "네~"
    elif randInt == 3:
        strMessage = "ㅋㅋ"

    return strMessage