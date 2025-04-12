from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse

import json
import os
import uvicorn

from message import get_wa_reply

fastApiApp = FastAPI()
 
@fastApiApp.get("/")
def main_page():
    return RedirectResponse(url = "https://github.com/yymin1022/Wa_API")

@fastApiApp.post("/getMessage")
async def get_message(request: Request):
    err_code = 0
    err_message = "RESULT OK"

    try:
        input_data = await request.json()
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
        return JSONResponse(content = reply_data)

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
    return JSONResponse(content = reply_data)
 
if __name__ == "__main__":
    uvicorn.run("main:fastApiApp", host = "0.0.0.0", port = 80)