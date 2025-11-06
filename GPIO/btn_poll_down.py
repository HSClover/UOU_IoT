# Button PULL_DOWN register
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN)

count = 0
try:
    while True:
        value = GPIO.input(24)
        if value == True:
            count += 500
            print(count, 'ms')
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Program end...")