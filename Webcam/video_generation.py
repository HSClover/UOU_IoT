import time
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN, GPIO.PUD_UP) #button; pull-up register

with picamera.PiCamera() as cam:
    cam.start_preview()
    GPIO.wait_for_edge(18, GPIO.FALLING)
    cam.start_recording('/home/pi/photo/video.h264')
    time.sleep(5)
    cam.stop_recording()
    cam.stop_preview()