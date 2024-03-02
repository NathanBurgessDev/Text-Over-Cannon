from gpiozero import Motor

def main():
    motor = Motor(17, 22)
    while True:
        motor.forward()
        print("forward :)")

if __name__ == "__main__":
    main()