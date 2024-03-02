from gpiozero import Motor
from gate import Gate
from gate_controller import GateController

def main():
    motor1 = Motor(17, 22)
    motor2 = Motor(5,6)

    gate = Gate(motor1, motor2)
    while True:
        # gate.open_front()
        motor2.forward()
    # gate_con = GateController(gate, None)
    # gate_con.blue_gate.close_front()

if __name__ == "__main__":
    main()