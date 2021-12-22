from flask import Flask, jsonify, redirect, request

flaskApp = Flask(__name__)
 
@flaskApp.route("/")
def main():
    return "Hello, CECOM!"

if __name__ == "__main__":
    flaskApp.run(host="0.0.0.0", port=80)