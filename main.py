from flask import Flask

flaskApp = Flask (__name__)
 
@flaskApp.route("/")
def main():
    return "Hello, World!"

@flaskApp.route("/getMessage")
def main():
    return "Hello, World! This is getMessage Function!"
 
if __name__ == "__main__":
    flaskApp.run(host = "0.0.0.0", port = 80)