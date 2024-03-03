from gpiozero import Motor
from time import sleep

class Gate:

    def __init__(self, front_motor: Motor, back_motor: Motor) -> None:
        self.front_motor = front_motor
        self.back_motor = back_motor

    def open_front(self):            
        self.front_motor.backward()
        sleep(1)
        self.front_motor.stop()

    def close_front(self):
        self.front_motor.forward()
        sleep(1)
        self.front_motor.stop()

    def open_back(self):
        self.back_motor.backward()
        sleep(1)
        self.back_motor.stop()

    def close_back(self):
        self.back_motor.forward()
        sleep(1)
        self.back_motor.stop()