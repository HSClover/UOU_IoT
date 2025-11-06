import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
btn_cnt, sleep_cnt = 0, 0
def handler(channel):
    global btn_cnt
    btn_cnt += 1
    print("btn_cnt = ", btn_cnt)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(12, GPIO.RISING, callback=handler)

try:
    while True:
        time.sleep(1)
        sleep_cnt += 1
        print("sleep_cnt = ", sleep_cnt)
except KeyboardInterrupt:
    print("Program end...")