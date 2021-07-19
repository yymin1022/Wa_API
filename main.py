from flask import Flask

flaskApp = Flask (__name__)
 
@flaskApp.route("/")
def main():
    return "Hello, World!"
 
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80)