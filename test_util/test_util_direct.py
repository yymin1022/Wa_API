from message import get_wa_reply
from models import WaMessage


input_message = input("테스트 할 Message를 입력하세요: ")
wa_message = WaMessage(
    msg = input_message,
    room = "Test_Room1",
    sender = "Test_Sender1"
)
reply_message = get_wa_reply(wa_message)

if reply_message is None:
    reply_message = "None WA Bot Message Found"
else:
    reply_message = reply_message.replace("\\m", "\n")

print(reply_message)