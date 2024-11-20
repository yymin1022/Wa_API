import json
import os


def message_memory(message, room, sender):
    if "!기억" in message:
        return message_remem(message, room)
    if "뭐였" in message:
        return message_remem_return(room)
    if "뭐더라" in message:
        return message_mem_return(sender)

def message_remem(message, room):
    message = message.replace("!기억해", "").replace("!기억", "").strip()

    if len(message) != 0:
        if os.path.isfile("rem.json"):
            with open("rem.json", "r", encoding = "utf-8") as f:
                rem_dict = json.load(f)
        else:
            rem_dict = {}
        rem_dict[room] = message
        json_data = json.dumps(rem_dict, ensure_ascii = False, indent = 4)
        with open("rem.json", "w", encoding = "utf-8") as f:
            f.write(json_data)
    return None

def message_mem_return(sender):
    if os.path.isfile("mem.json"):
        with open("mem.json", "r", encoding = "utf-8") as f:
            mem_dict = json.load(f)
        if sender in mem_dict:
            return f"{mem_dict[sender]}\\m^^7"
    return None

def message_remem_return(room):
    if os.path.isfile("rem.json"):
        with open("rem.json", "r", encoding = "utf-8") as f:
            rem_dict = json.load(f)
        if room in rem_dict:
            return f"{rem_dict[room]}\\m아마 이거일 듯?"
    return None