from gpiozero import Motor
from gate import Gate
from gate_controller import GateController

def main():
    motor2 = Motor(17, 22)
    motor1 = Motor(5,6)

    motor3 = Motor(23,24)
    motor4 = Motor(14,15)

    gate1 = Gate(motor1, motor2)
    gate2 = Gate(motor3, motor4)

    gate_con = GateController(gate1, gate2)
    while True:
        gate_con.release_blue()

if __name__ == "__main__":
    main()