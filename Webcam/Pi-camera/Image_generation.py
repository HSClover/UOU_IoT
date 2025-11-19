import time
import picamera2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)  # 버튼 핀 설정

with picamera2.Picamera2() as cam:
    cam.start_preview()
    GPIO.wait_for_edge(18, GPIO.FALLING)  # 버튼이 눌릴 때까지 대기
    cam.capture('/home/pi/Documents/Webcam/Pi-camera/photo/image.jpg')
    cam.stop_preview()