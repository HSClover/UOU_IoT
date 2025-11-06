import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 18

temperature = sensor.temperature
humidity = sensor.humidity
print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))