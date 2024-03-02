from gpiozero import Motor

def main():
    motor = Motor(17, 22)
    motor.forward()

if __name__ == "__main__":
    main()