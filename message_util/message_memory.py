import json
import os


def message_memory(message, room, sender):
    if "!기억" in message:
        return message_remember(message, room)
    if "뭐였" in message:
        return messageRemreturn(room)
    if "뭐더라" in message:
        return messageMemreturn(sender)

def message_remember(message, room):
    message = message.replace("!기억해", "").replace("!기억", "").strip()

    if len(message) != 0:
        if os.path.isfile("rem.json"):
            with open('rem.json', 'r', encoding='utf-8') as f:
                rem_dict = json.load(f)
        else:
            rem_dict = {}

        rem_dict[room] = message
        json_data = json.dumps(rem_dict, ensure_ascii=False, indent=4)

        with open('rem.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
    else:
        pass

    strMessage = ""
    return strMessage

def messageMemreturn(sender):
    if os.path.isfile("mem.json"):
        with open('mem.json', 'r', encoding='utf-8') as f:
            mem_dict = json.load(f)

        if sender in mem_dict:
            strMessage = mem_dict[sender] + "\\m^^7"
        else:
            strMessage = ""
    else:
        strMessage = ""

    return strMessage

def messageRemreturn(room):
    strMessage = ""

    if os.path.isfile("rem.json"):
        with open('rem.json', 'r', encoding='utf-8') as f:
            rem_dict = json.load(f)

        if room in rem_dict:
            strMessage = rem_dict[room] + "\\m아마 이거일 듯?"
        else:
            strMessage = ""
    else:
        strMessage = ""

    return strMessage