import RPi.GPIO as GPIO
import time

PIR = 23
LED = 25

GPIO.setmode(GPIO.BCM)
print("HC-SR501 sensor starts\n")

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        state = GPIO.input
        if(state == True):
            print("state: Mothion detected\n")
        else:
            print("state: No motion\n")
        GPIO.output(LED, state)
        time.sleep(5)
except KeyboardInterrupt:
    print("Motion detection ends\n")
    GPIO.cleanup()