from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from models import MessageStatus


app = FastAPI()
app.message_status = None


@app.get("/")
async def read_root():
    return "hiii!!! :33"


@app.post("/send")
async def read_item(message: str):
    if app.message_status is not None:
        raise HTTPException(status_code=503, detail="Message currently being sent")

    app.message_status = MessageStatus()

    return message


@app.get("/status")
async def get_status() -> MessageStatus:
    if app.message_status is None:
        raise HTTPException(status_code=404, detail="No current status")

    return app.message_status
