from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
from waitress import serve

import os
import json

from message import get_wa_reply

flaskApp = Flask(__name__)
CORS(flaskApp, resources = {r"*": {"origins": "*"}})
 
@flaskApp.route("/")
def main_page():
    return redirect("https://github.com/yymin1022/Wa_API", code = 302)

@flaskApp.route("/getMessage", methods = ["POST"])
def get_message():
    err_code = 0
    err_message = "RESULT OK"

    try:
        input_data = request.get_json()
        input_message = input_data["msg"]
        input_room = input_data["room"]
        input_sender = input_data["sender"]
    except Exception as err_data:
        err_code = 200
        err_message = repr(err_data)
        reply_data = dict([("RESULT",
                            dict([("RESULT_CODE", err_code),
                                    ("RESULT_MSG", err_message)])),
                            ("DATA",
                             dict([("msg", ""),
                                   ("room", ""),
                                   ("sender", "")]))])
        return jsonify(reply_data)

    reply_message = None
    if os.path.isfile("power.json"):
        with open('power.json', 'r', encoding='utf-8') as f:
            power_dict = json.load(f)
            if power_dict.get(input_room) is None:
                reply_message = get_wa_reply(input_message, input_room, input_sender)
            elif power_dict[input_room] == "0":
                if "와봇" in input_message:
                    reply_message = get_wa_reply(input_message, input_room, input_sender)
            else:
                reply_message = get_wa_reply(input_message, input_room, input_sender)
    else:
        reply_message = get_wa_reply(input_message, input_room, input_sender)

    if reply_message is None:
        err_code = 100
        err_message = "None WA Bot Message Found"

    reply_data = dict([("RESULT",
                        dict([("RESULT_CODE", err_code),
                              ("RESULT_MSG", err_message)])),
                       ("DATA",
                        dict([("msg", reply_message),
                              ("room", input_room),
                              ("sender", input_sender)]))])
    return jsonify(reply_data)
 
if __name__ == "__main__":
    serve(flaskApp, host="0.0.0.0", port=80)