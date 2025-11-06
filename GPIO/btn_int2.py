import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0
def handler(channel):
    global count
    count += 1
    print("count = ", count)

GPIO.add_event_detect(24, GPIO.RISING, callback=handler)
try:
    GPIO.wait_for_edge(23, GPIO.FALLING)
    print("Falling edge detected")
except KeyboardInterrupt:
    print("Program end...")
GPIO.cleanup()