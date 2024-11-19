from message import get_wa_reply

inputMessage = input("테스트 할 Message를 입력하세요: ")
replyMessage = get_wa_reply(inputMessage, "Test_Room1", "Test_Sender1")

if replyMessage == "":
    replyMessage = "None WA Bot Message Found"
elif "\\m" in replyMessage:
    replyMessage = replyMessage.replace("\\m", "\n")

print(replyMessage)