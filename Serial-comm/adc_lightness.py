import spidev, time
import RPi.GPIO as GPIO

led = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def analog_read(ch):
    r = spi.xfer2([1, (8+ch) << 4, 0])
    adc_out = ((r[1]&3)<<8) + r[2]
    return adc_out

try:
    while True:
        value = analog_read(1)
        light = value * 100.0 / 1024
        print("value: %d" % value, " lightness: %.1f" % light)
        time.sleep(1)
        if light < 30:
            GPIO.output(led, 1)
            print("LED ON")
        else:
            GPIO.output(led, 0)
            print("LED OFF")
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
