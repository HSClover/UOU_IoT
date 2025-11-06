import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO = 24
print("Distance measurement starts ... \n")

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

try:
    while True:
        start, stop = 0, 0
        GPIO.output(GPIO_TRIGGER, False)
        time.sleep(2)

        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        while GPIO.input(GPIO_ECHO) == 0:
            start = time.time()
        while GPIO.input(GPIO_ECHO) == 1:
            stop = time.time()

        elapsed = stop - start
        distance = (elapsed * 34000.0) / 2
        print("Distance : %.1f cm" % distance)
except KeyboardInterrupt:
    print("Distance measurement ends\n")
    GPIO.cleanup()

GPIO.cleanup()