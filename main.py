import util.cipher_util
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.concurrency import run_in_threadpool

import uvicorn

from message import get_wa_reply
from models import ReplyMessage, WaMessage


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

from message_util.message_gemini import evict_expired_histories


@fastApiApp.post("/getMessage")
async def get_message(request: Request, background_tasks: BackgroundTasks):
    reply_data = dict([("RESULT",
                        dict([("RESULT_CODE", 0),
                                ("RESULT_MSG", "RESULT OK")])),
                        ("DATA",
                         dict([("msg", ""),
                               ("room", ""),
                               ("sender", "")]))])

    # Message Input Parse
    try:
        input_data = await request.json()
        input_message = input_data["msg"]
        input_room = input_data["room"]
        input_sender = input_data["sender"]

        input_images = input_data.get("images", [])
        if not input_images and "image" in input_data and input_data["image"]:
            input_images = [input_data["image"]]
        elif isinstance(input_images, str):
            input_images = [input_images]

        reply_message_data = input_data.get("replyMessage", None)
        reply_message = None
        if reply_message_data:
            reply_images = reply_message_data.get("images", [])
            if not reply_images and "image" in reply_message_data and reply_message_data["image"]:
                reply_images = [reply_message_data["image"]]
            elif isinstance(reply_images, str):
                reply_images = [reply_images]

            reply_message = ReplyMessage(
                msg = reply_message_data.get("msg", ""),
                sender = reply_message_data.get("sender", ""),
                images = reply_images
            )

        wa_message = WaMessage(
            msg = input_message,
            room = input_room,
            sender = input_sender,
            images = input_images,
            replyMessage = reply_message
        )
    except Exception as err_data:
        reply_data["RESULT"]["RESULT_CODE"] = 200
        reply_data["RESULT"]["RESULT_MSG"] = repr(err_data)
        return JSONResponse(content = reply_data)

    # Get Message
    reply_message = await run_in_threadpool(get_wa_reply, wa_message)

    # Reply Message
    if reply_message is not None:
        reply_data["RESULT"]["RESULT_CODE"] = 0
        reply_data["RESULT"]["RESULT_MSG"] = "RESULT OK"
        reply_data["DATA"]["msg"] = reply_message
        reply_data["DATA"]["room"] = wa_message.room
        reply_data["DATA"]["sender"] = wa_message.sender
    else:
        reply_data["RESULT"]["RESULT_CODE"] = 100
        reply_data["RESULT"]["RESULT_MSG"] = "None WA Bot Message Found or Disabled Chatroom"

    background_tasks.add_task(evict_expired_histories)
    return JSONResponse(content = reply_data)
 
if __name__ == "__main__":
    uvicorn.run("main:fastApiApp", host = "0.0.0.0", port = 80)