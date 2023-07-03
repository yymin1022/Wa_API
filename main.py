from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
from waitress import serve

import message

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

    replyMessage = message.getReplyMessage(inputMessage, inputRoom, inputSender)
    replyRoom = inputRoom
    replySender = inputSender

    if(replyMessage == ""):
        errCode = 100
        errMessage = "None WA Bot Message Found"

    replyData = dict([("RESULT", dict([("RESULT_CODE", errCode), ("RESULT_MSG", errMessage)])), ("DATA", dict([("msg", replyMessage), ("room", replyRoom), ("sender", replySender)]))])

    return jsonify(replyData)
 
if __name__ == "__main__":
    serve(flaskApp, host="0.0.0.0", port=80)