import util.cipher_util
from models import WaMessage
from message_util.message_command import message_command
from message_util.message_cry_laugh_stress import message_cry_laugh_stress
from message_util.message_datetime import message_datetime
from message_util.message_friends import message_friends
from message_util.message_gemini import message_gemini
from message_util.message_graduate import message_graduate
from message_util.message_library import message_library
from message_util.message_logistics import message_logistics
from message_util.message_meal import message_meal
from message_util.message_meme import message_meme
from message_util.message_memory import message_memory
from message_util.message_onoff import check_onoff, message_onoff


def get_wa_reply(wa_message: WaMessage):
    # Check for disabled room
    if check_onoff(wa_message.msg, wa_message.room) is False:
        return None

    # Special Command Messages
    result_message = message_command(wa_message)
    if result_message is not None:
        return result_message
    
    result_message = message_datetime(wa_message)
    if result_message is not None:
        return result_message

    result_message = message_gemini(wa_message)
    if result_message is not None:
        return result_message

    result_message = message_logistics(wa_message)
    if result_message is not None:
        return result_message

    # Normal Text Messages
    result_message = message_cry_laugh_stress(wa_message)
    if result_message is not None:
        return result_message

    result_message = message_friends(wa_message)
    if result_message is not None:
        return result_message

    result_message = message_graduate(wa_message)
    if result_message is not None:
        return result_message

    result_message = message_library(wa_message)
    if result_message is not None:
        return result_message

    result_message = message_meal(wa_message)
    if result_message is not None:
        return result_message

    result_message = message_meme(wa_message)
    if result_message is not None:
        return result_message

    result_message = message_memory(wa_message)
    if result_message is not None:
        return result_message

    result_message = message_onoff(wa_message)
    if result_message is not None:
        return result_message
    return None