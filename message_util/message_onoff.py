import json
import os
import random


def message_onoff(message, room, sender):
    if "와봇" in message:
        if "꺼" in message or "끄" in message:
            return message_wabot_power(0, room)
        elif "켜" in message or "키" in message:
            return message_wabot_power(1, room)

def message_wabot_power(is_on, room):
    if os.path.isfile("power.json"):
        with open("power.json", "r", encoding = "utf-8") as f:
            power_dict = json.load(f)
        room_power = power_dict.get(room)
        if room_power is not None:
            if (is_on == 0 and room_power == "0") or (is_on == 1 and room_power == "1"):
                return None
        else:
            if is_on == 1:
                return None
    else:
        power_dict = {}
    rand_int = random.randrange(0, 4)
    if rand_int == 0:
        if is_on == 0:
            power_dict[room] = "0"
            json_data = json.dumps(power_dict, ensure_ascii = False, indent = 4)
            str_message = "와봇이 종료되었습니다."
        else:
            power_dict[room] = "1"
            json_data = json.dumps(power_dict, ensure_ascii = False, indent = 4)
            str_message = "와봇이 시작되었습니다."
        with open("power.json", "w", encoding = "utf-8") as f:
            f.write(json_data)
        return str_message
    elif rand_int == 1:
        return "싫은데? ^^"
    elif rand_int == 2:
        return "네~"
    elif rand_int == 3:
        return "ㅋㅋ"
    return None