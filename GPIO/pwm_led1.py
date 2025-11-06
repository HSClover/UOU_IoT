import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
pwm = GPIO.PWM(12, 50)

pwm.start(0)
try:
    while True:
        for dc in range(0, 100, 5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.2)
        for dc in range(100, 0, -5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.2)
except KeyboardInterrupt:
    print("Program end...")