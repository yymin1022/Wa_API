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
from message_util.message_onoff import message_onoff


def get_wa_reply(message, room, sender):
    # Special Command Messages
    result_message = message_command(message, room, sender)
    if result_message is not None:
        return result_message
    result_message = message_datetime(message, room, sender)
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
    return None