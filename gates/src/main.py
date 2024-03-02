from gpiozero import Motor

def main():
    motor = Motor(17, 22)
    motor.stop()

if __name__ == "__main__":
    main()