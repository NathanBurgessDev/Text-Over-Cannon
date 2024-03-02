from gpiozero import Motor

def main():
    motor = Motor(17, 22)
    motor.forward()