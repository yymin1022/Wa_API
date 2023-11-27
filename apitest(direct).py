import message
import os
import json

# Room과 Sender를 매번 입력받으려면 input()으로 문장을 고치세요.
inputRoom = "Test_Room1"
inputSender = "Test_User1"

inputMessage = input("테스트 할 Message를 입력하세요: ")
replyMessage = message.getReplyMessage(inputMessage, inputRoom, inputSender)

if replyMessage == "":
    replyMessage = "None"
elif "\\m" in replyMessage:
    replyMessage = replyMessage.replace("\\m", "\n")

print(replyMessage)