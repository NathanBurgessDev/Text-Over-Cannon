from gpiozero import Motor
from time import sleep

class Gate:

    def __init__(self, front_motor: Motor, back_motor: Motor) -> None:
        self.front_motor = front_motor
        self.back_motor = back_motor

    def open_front(self):            
        self.front_motor.forward(0.7)
        sleep(0.5)
        self.front_motor.stop()

    def close_front(self):
        self.front_motor.backward(0.7)
        sleep(0.5)
        self.front_motor.stop()

    def open_back(self):
        self.back_motor.backward(0.7)
        sleep(0.5)
        self.back_motor.stop()

    def close_back(self):
        self.back_motor.forward(0.7)
        sleep(0.5)
        self.back_motor.stop()