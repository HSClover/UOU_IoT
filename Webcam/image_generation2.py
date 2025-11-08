import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP) # button; pull-up register

with picamera.PiCamera() as cam:
    cam.start_preview()
    frame = 0
    while frame < 10:
        GPIO.wait_for_edge(18,GPIO.FALLING)
        cam.capture('/home/pi/photo/frame%d.jpg'% frame)
        frame += 1
    cam.stop_preview()