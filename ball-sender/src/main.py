from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from gate import Gate
from gate_controller import GateController
from gpiozero import Motor
from models import MessageStatus


app = FastAPI()
app.message_status = None

motor1 = Motor(17, 27)
motor2 = Motor(5, 6)

motor3 = Motor(23, 24)
motor4 = Motor(14, 15)

gate1 = Gate(motor1, motor2)
gate2 = Gate(motor3, motor4)

app.gate_controller = GateController(gate1, gate2)


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

    # app.message_status = MessageStatus()

    app.gate_controller.send(message)

    return message


@app.get("/status")
async def status() -> MessageStatus:
    """
    Gets the message status. Returns 404 if no message is being sent.
    """
    if app.message_status is None:
        raise HTTPException(status_code=404, detail="No current status")

    return app.message_status
