from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from message import get_wa_reply

fastApiApp = FastAPI()
fastApiApp.add_middleware(
    CORSMiddleware,
    allow_credentials = True,
    allow_headers = ["*"],
    allow_methods = ["*"],
    allow_origins = ["*"]
)

@fastApiApp.get("/")
def main_page():
    return RedirectResponse(url = "https://github.com/yymin1022/Wa_API")

@fastApiApp.post("/getMessage")
def get_message(request: Request):
    reply_data = dict([("RESULT",
                        dict([("RESULT_CODE", 0),
                                ("RESULT_MSG", "RESULT OK")])),
                        ("DATA",
                         dict([("msg", ""),
                               ("room", ""),
                               ("sender", "")]))])

    # Message Input Parse
    try:
        input_data = request.json()
        input_message = input_data["msg"]
        input_room = input_data["room"]
        input_sender = input_data["sender"]
    except Exception as err_data:
        reply_data["RESULT"]["RESULT_CODE"] = 200
        reply_data["RESULT"]["RESULT_MSG"] = repr(err_data)
        return JSONResponse(content = reply_data)

    # Get Message
    reply_message = get_wa_reply(input_message, input_room, input_sender)

    # Reply Message
    if reply_message is not None:
        reply_data["RESULT"]["RESULT_CODE"] = 0
        reply_data["RESULT"]["RESULT_MSG"] = "RESULT OK"
        reply_data["DATA"]["msg"] = reply_message
        reply_data["DATA"]["room"] = input_room
        reply_data["DATA"]["sender"] = input_sender
    else:
        reply_data["RESULT"]["RESULT_CODE"] = 100
        reply_data["RESULT"]["RESULT_MSG"] = "None WA Bot Message Found or Disabled Chatroom"

    return JSONResponse(content = reply_data)
 
if __name__ == "__main__":
    uvicorn.run("main:fastApiApp", host = "0.0.0.0", port = 80, workers = 4)