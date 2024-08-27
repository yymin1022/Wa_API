import message
import os
import json

inputMessage = input("테스트 할 Message를 입력하세요: ")
replyMessage = message.getReplyMessage(inputMessage, "Test_Room1", "Test_Sender1")

if replyMessage == "":
    replyMessage = "None WA Bot Message Found"
elif "\\m" in replyMessage:
    replyMessage = replyMessage.replace("\\m", "\n")

print(replyMessage)