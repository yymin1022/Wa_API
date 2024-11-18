from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
from waitress import serve

import message_util
import os
import json

flaskApp = Flask(__name__)
CORS(flaskApp, resources={r"*": {"origins": "*"}})
 
@flaskApp.route("/")
def mainPage():
    return redirect("https://github.com/yymin1022/Wa_API", code=302)

@flaskApp.route("/getMessage", methods = ["POST"])
def getMessage():
    errCode = 0
    errMessage = "RESULT OK"

    inputData = ""
    inputMessage = ""
    inputRoom = ""
    inputSender = ""

    try:
        inputData = request.get_json()

        inputMessage = inputData["msg"]
        inputRoom = inputData["room"]
        inputSender = inputData["sender"]
    except Exception as errContent:
        errCode = 200
        errMessage = repr(errContent)

        replyData = dict([("RESULT", dict([("RESULT_CODE", errCode), ("RESULT_MSG", errMessage)])), ("DATA", dict([("msg", ""), ("room", ""), ("sender", "")]))])

        return jsonify(replyData)

    if os.path.isfile("power.json"):
        with open('power.json', 'r', encoding='utf-8') as f:
            power_dict = json.load(f)
            if power_dict.get(inputRoom) == None:
                replyMessage = message_util.getReplyMessage(inputMessage, inputRoom, inputSender)
            elif power_dict[inputRoom] == "0":
                if "와봇" in inputMessage:
                    replyMessage = message_util.getReplyMessage(inputMessage, inputRoom, inputSender)
                else:
                    replyMessage = ""
            else:
                replyMessage = message_util.getReplyMessage(inputMessage, inputRoom, inputSender)
    else:
        replyMessage = message_util.getReplyMessage(inputMessage, inputRoom, inputSender)

    replyRoom = inputRoom
    replySender = inputSender

    if(replyMessage == ""):
        errCode = 100
        errMessage = "None WA Bot Message Found"

    replyData = dict([("RESULT", dict([("RESULT_CODE", errCode), ("RESULT_MSG", errMessage)])), ("DATA", dict([("msg", replyMessage), ("room", replyRoom), ("sender", replySender)]))])

    return jsonify(replyData)
 
if __name__ == "__main__":
    serve(flaskApp, host="0.0.0.0", port=80)