from pydantic import BaseModel


class MessageStatus(BaseModel):
    balls_sent: int = 0
    balls_remaining: int = 8
