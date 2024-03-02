from gpiozero import Motor

class Gate:

    def __init__(self, front_motor: Motor, back_motor: Motor) -> None:
        self.front_motor = front_motor
        self.back_motor = back_motor

    def open_front(self):
        pass

    def close_front(self):
        pass

    def open_back(self):
        pass

    def close_back(self):
        pass