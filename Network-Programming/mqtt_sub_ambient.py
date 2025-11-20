import paho.mqtt.client as mqtt

TOPIC = 'sensor/temp/ambient'

def handler_message(client, userdata, msg):
    print(f"Received: {msg.topic} -> {msg.payload.decode()}℃")

client = mqtt.Client()

client.on_message = handler_message
client.connect("localhost", 1883, 60)
client.subscribe(TOPIC, qos=0)

try:
    print("Subscriber start... Press Ctrl+C to stop.")
    client.loop_forever()
except KeyboardInterrupt:
    print("Subscriber end...")
    client.disconnect()