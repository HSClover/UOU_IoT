import RPi.GPIO as GPIO
import time

PIR = 23
TRI = 24
ECH = 25
LED = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(TRI, GPIO.OUT)
GPIO.setup(ECH, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED,0)

try:
	while(True):
		start, stop = 0,0
		GPIO.output(TRI,False)
		time.sleep(1)

		if GPIO.input(PIR):
			GPIO.output(TRI,True)
			time.sleep(0.00001)
			GPIO.output(TRI,False)

			while GPIO.input(ECH)==0:
				start = time.time()
			while GPIO.input(ECH)==1:
				stop = time.time()
			
			elapsed = stop-start
			distance = (elapsed * 34000.0) / 2
			
			if (distance < 10):
				GPIO.output(LED,1)
			else:
				GPIO.output(LED,0)

except KeyboardInterrupt:
	print("Program end...")
	GPIO.cleanup()