import smbus
import time

bus = smbus.SMBus(1)
addr = 0x5A

def read_temp(reg):
    data = bus.read_word_data(addr, reg)
    data_conv = (data & 0x00ff) + (data & 0xff00)
    temp = (data_conv * 0.02) - 273.15
    return temp

time.sleep(2)
print("Sensing start...")

try:
    while True:
        amb_temp = read_temp(0x06)
        obj_temp = read_temp(0x07)
        print(f"Ambient : {amb_temp:.2f} ℃ | Object : {obj_temp:.2f} ℃")
        time.sleep(2)
except KeyboardInterrupt:
    print("Program end...")