from flask import Flask, jsonify, request

import message

flaskApp = Flask (__name__)
 
@flaskApp.route("/")
def main():
    return "Hello, World!"

@flaskApp.route("/getMessage", methods = ["POST"])
def getMessage():
    inputData = request.get_json()

    inputMessage = inputData["msg"]
    inputRoom = inputData["room"]
    inputSender = inputData["sender"]

    replyMessage = message.getReplyMessage(inputMessage)
    replyRoom = inputRoom
    replySender = inputSender

    replyData = dict(zip(("msg", replyMessage), ("room", replyRoom), ("sender", replySender)))

    return jsonify(replyData)
 
if __name__ == "__main__":
    flaskApp.run(host = "0.0.0.0", port = 80)