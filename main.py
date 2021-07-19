from flask import Flask, jsonify, request

flaskApp = Flask (__name__)
 
@flaskApp.route("/")
def main():
    return "Hello, World!"

@flaskApp.route("/getMessage", methods = ["POST"])
def getMessage():
    inputData = request.get_json()
    return jsonify(inputData)
 
if __name__ == "__main__":
    flaskApp.run(host = "0.0.0.0", port = 80)