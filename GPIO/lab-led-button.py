import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
switch = 0

def switch(channel):
	global switch
	if(switch==0):
		switch=1
		print ("switch on")
	else:
		switch=0
		print ("switch off")

GPIO.add_event_detect(18,GPIO.RISING, callback=switch)

try:
	state = 0
	while(True):
		if(switch == 1):
			if(state == 0):
				GPIO.output(23,0)
				GPIO.output(24,0)
				state = 1
			elif(state == 1):
				GPIO.output(24,1)
				state = 2
			elif(state == 2):
				GPIO.output(23,1)
				GPIO.output(24,0)
				state = 3
			else:
				GPIO.output(24,1)
				state = 0
			time.sleep(1)
		else:
			GPIO.output(23,0)
			GPIO.output(24,0)

except KeyboardInterrupt:
	print("Program end")
GPIO.cleanup()
