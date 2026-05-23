from message import get_wa_reply


input_message = input("테스트 할 Message를 입력하세요: ")
reply_message = get_wa_reply(input_message, "Test_Room1", "Test_Sender1")

if reply_message is None:
    reply_message = "None WA Bot Message Found"
else:
    reply_message = reply_message.replace("\\m", "\n")

print(reply_message)