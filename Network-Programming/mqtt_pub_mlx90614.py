import paho.mqtt.client as mqtt
import time
import smbus

I2C = 0x5a
bus = smbus.SMBus(1)

def on_publish(client, userdata, mid):
    print("published mid:", mid)

client = mqtt.Client()
client.on_publish = on_publish
client.connect("localhost", 1883, 60)
client.loop_start()

print("Publisher start...")
try:
    while True:
        temp = bus.read_word_data(I2C, 0x06)
        temp_conv = round(temp * 0.02 - 273.15, 1)
        client.publish('sensor/temp/ambient', str(temp_conv), qos=0)
        print(f"Publish sensor/temp/ambient: {temp_conv}℃")

        temp = bus.read_word_data(I2C, 0x07)
        temp_conv = round(temp * 0.02 - 273.15, 1)
        client.publish('sensor/temp/object', str(temp_conv), qos=0)
        print(f"Publish sensor/temp/object: {temp_conv}℃")
        time.sleep(5)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()