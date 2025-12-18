import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)

state = 0
trigger = 0

def switch(channel):
		if trigger == 0:
			trigger = 1
		if(state == 3):
			GPIO.output(23,0)
			GPIO.output(24,0)
			state = 0
			print('(off, off)')
		elif(state == 0):
			GPIO.output(24,1)
			state = 1
			print('(off, on)')
		elif(state == 1):
			GPIO.output(23,1)
			GPIO.output(24,0)
			state = 2
			print('(on, off)')
		else:
			GPIO.output(24,1)
			state = 3
			print('(on, on)')
		time.sleep(0.001)	


GPIO.add_event_detect(18,GPIO.RISING, callback=switch)

try:
	state = 0
	while(True):
		if(trigger==0):
			GPIO.output(23,0)
			GPIO.output(24,0)

except KeyboardInterrupt:
	print("Program end")
GPIO.cleanup()