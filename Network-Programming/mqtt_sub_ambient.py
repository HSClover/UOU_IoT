import paho.mqtt.client as mqtt

TOPIC = 'sensor/temp/ambient'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    if rc == 0:
        client.subscribe(TOPIC, qos=0)
    else:
        print("Connect failed, rc =", rc)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed:", mid, "granted_qos=", granted_qos)

def on_message(client, userdata, msg):
    print(f"Received: {msg.topic} -> {msg.payload.decode()}℃")

def on_log(client, userdata, level, buf):
    print("LOG:", level, buf)

client = mqtt.Client(client_id="sub_ambient")  # 명시적 client_id 권장
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_log = on_log

client.connect("localhost", 1883, 60)
client.loop_forever()