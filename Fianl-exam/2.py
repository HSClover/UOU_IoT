import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 50)
bright = 0
pwm.start(bright)

def btn1(channel):
     bright += 20
def btn2(channel):
     bright -= 20

GPIO.add_event_detect(23,GPIO.RISING,callback=btn1)
GPIO.add_event_detect(24,GPIO.RISING,callback=btn2)


try:
    while True:
            pwm.ChangeDutyCycle(bright)
            time.sleep(0.01)
except KeyboardInterrupt:
    print("Program end...")