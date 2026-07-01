from pydantic import BaseModel
from typing import Optional

class WaMessage(BaseModel):
    msg: str
    room: str
    sender: str
    image: Optional[str] = None
