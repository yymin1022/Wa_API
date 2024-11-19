from message_util.message_command import message_command
from message_util.message_cry_laugh_stress import message_cry_laugh_stress
from message_util.message_friends import message_friends
from message_util.message_gemini import message_gemini
from message_util.message_graduate import message_graduate
from message_util.message_library import message_library
from message_util.message_logistics import message_logistics
from message_util.message_meal import message_meal
from message_util.message_meme import message_meme
from message_util.message_memory import message_memory
from message_util.message_onoff import message_onoff
from util.cipher_util import DESAdapter

import certifi
import requests


def getReplyMessage(message, room, sender):
    # Special Command Messages
    result_message = message_command(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_gemini(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_logistics(message, room, sender)
    if result_message is not None:
        return result_message

    # Normal Text Messages
    result_message = message_cry_laugh_stress(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_friends(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_graduate(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_library(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_meal(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_meme(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_memory(message, room, sender)
    if result_message is not None:
        return result_message

    result_message = message_onoff(message, room, sender)
    if result_message is not None:
        return result_message

    if "비트코인" in message:
        strResult = messageBitcoin()
    return strResult

def messageBitcoin():
    strMessage = ""

    requestSession = requests.Session()
    url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
    requestSession.mount(url, DESAdapter())

    try:
        response = requestSession.get(url, verify=certifi.where())
        response.raise_for_status()
        data = response.json()
        current_price = data[0]['trade_price']
        strMessage = f"와! 비트코인 현재가 : {current_price}원! 지금 사요?"
    except requests.exceptions.RequestException as e:
        strMessage = "비트코인 가격을 불러오는 중 오류가 발생했습니다."

    return strMessage