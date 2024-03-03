from time import sleep
from gate import Gate

class GateController:

    def __init__(self, blue_gate: Gate, green_gate: Gate):
        self.blue_gate = blue_gate
        self.green_gate = green_gate


    def send(self, message: str) -> None:
        # convert str to bytes
        b = message.encode()

        for byte in b:
            for i in range(8):
                # get each bit in byte
                match (byte >> i) & 1:
                    case 0:
                        self.release_green()
                    case 1:
                        self.release_blue()
                

    def release_blue(self):
        # Let ball out of turnstile :)
        self.blue_gate.open_front()
        sleep(1)
        self.blue_gate.close_front()

        # Let single ball into turnstile :)
        self.blue_gate.open_back()
        sleep(1)
        self.blue_gate.close_back()

    def release_green(self):
        # Let single ball into turnstile :)
        self.green_gate.open_back()
        sleep(1)
        self.green_gate.close_back()

        # Let ball out of turnstile :)
        self.green_gate.open_front()
        sleep(1)
        self.green_gate.close_front()