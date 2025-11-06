import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR = 18
GPIO.setup(PIR, GPIO.IN)

try:
    while True:
        if GPIO.input(PIR) == GPIO.HIGH:
            print("Motion detected!\n")
        else:
            print("No motion\n")
        time.sleep(5)
except KeyboardInterrupt:
    print("Motion detection ends...\n")
    GPIO.cleanup()

GPIO.cleanup()