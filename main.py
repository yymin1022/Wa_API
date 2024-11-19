from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
from waitress import serve

import os
import json

from message import get_wa_reply

flaskApp = Flask(__name__)
CORS(flaskApp, resources={r"*": {"origins": "*"}})
 
@flaskApp.route("/")
def mainPage():
    return redirect("https://github.com/yymin1022/Wa_API", code=302)

@flaskApp.route("/getMessage", methods = ["POST"])
def getMessage():
    errCode = 0
    errMessage = "RESULT OK"

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

    reply_message = None
    if os.path.isfile("power.json"):
        with open('power.json', 'r', encoding='utf-8') as f:
            power_dict = json.load(f)
            if power_dict.get(inputRoom) == None:
                reply_message = get_wa_reply(inputMessage, inputRoom, inputSender)
            elif power_dict[inputRoom] == "0":
                if "와봇" in inputMessage:
                    reply_message = get_wa_reply(inputMessage, inputRoom, inputSender)
            else:
                reply_message = get_wa_reply(inputMessage, inputRoom, inputSender)
    else:
        reply_message = get_wa_reply(inputMessage, inputRoom, inputSender)

    replyRoom = inputRoom
    replySender = inputSender

    if reply_message is None:
        errCode = 100
        errMessage = "None WA Bot Message Found"

    replyData = dict([("RESULT", dict([("RESULT_CODE", errCode), ("RESULT_MSG", errMessage)])), ("DATA", dict([("msg", reply_message), ("room", replyRoom), ("sender", replySender)]))])

    return jsonify(replyData)
 
if __name__ == "__main__":
    serve(flaskApp, host="0.0.0.0", port=80)