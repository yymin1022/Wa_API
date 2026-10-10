from pydantic import BaseModel, Field
from typing import List, Optional


class ReplyMessage(BaseModel):
    msg: str
    sender: str
    images: List[str] = Field(default_factory=list)


class WaMessage(BaseModel):
    msg: str
    room: str
    sender: str
    images: List[str] = Field(default_factory=list)
    replyMessage: Optional[ReplyMessage] = None
