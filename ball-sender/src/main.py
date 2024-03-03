from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from models import MessageStatus


app = FastAPI()
app.message_status = None


@app.get("/")
async def read_root():
    return "hiii!!! :33"


@app.post("/send")
async def send(
    message: str = Query(
        ...,
        description="The message to be sent.",
        title="Message",
    )
):
    """
    Sends a message. Returns 503 if a message is in progress.
    """
    if app.message_status is not None:
        raise HTTPException(status_code=503, detail="Message currently being sent")

    app.message_status = MessageStatus()

    return message


@app.get("/status")
async def status() -> MessageStatus:
    """
    Gets the message status. Returns 404 if no message is being sent.
    """
    if app.message_status is None:
        raise HTTPException(status_code=404, detail="No current status")

    return app.message_status
