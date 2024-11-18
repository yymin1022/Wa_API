import message_util
import os
import json

from message import getReplyMessage

inputMessage = input("테스트 할 Message를 입력하세요: ")
replyMessage = getReplyMessage(inputMessage, "Test_Room1", "Test_Sender1")

if replyMessage == "":
    replyMessage = "None WA Bot Message Found"
elif "\\m" in replyMessage:
    replyMessage = replyMessage.replace("\\m", "\n")

print(replyMessage)