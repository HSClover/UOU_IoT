import spidev, time

spi = spidev.SpiDev()
spi.open(0, 0) 
spi.max_speed_hz = 1000000 #안줘도 될듯

def analog_read(channel):
    r = spi.xfer2([1, (0x08 + channel) << 4, 0])
    adc_out = ((r[1] & 0x03) << 8) + r[2]
    return adc_out

while True:
    value = analog_read(0)  #channel 0 = 0 to 1023
    voltage = value * 3.3 / 1023    # 3.3V * (0~1) [1024해상도]
    print("Input Value : {}, Voltage : {:.1f} V \n".format(value, voltage))
    time.sleep(2)