import smbus
import time, asyncio
import websockets as ws
import json

I2C = 0x5a
HOST = '0.0.0.0'
PORT = 8888
PERIOD = 5

bus = smbus.SMBus(1)
time.sleep(2)

def read_temp():
    amb_raw = bus.read_word_data(I2C, 0x06)
    obj_raw = bus.read_word_data(I2C, 0x07)
    amb_temp = (amb_raw * 00.02) - 273.15
    obj_temp = (obj_raw * 0.02) - 273.15
    return {"Ambient_c" : round(amb_temp, 2), "Object_c" : round(obj_temp, 2)}

async def handler(ws):
    print(f"Connected from client")
    message = await ws.recv()
    if message == "new-period 10":
        global PERIOD
        PERIOD = 10
    elif message == "quit":
        await ws.close()
        print("Connection closed.")
    else:
        temps = read_temp()
        temp_str = json.dumps(temps)
        print(temp_str)
        await ws.send(temp_str)
        await asyncio.sleep(PERIOD)

async def main():
    async with ws.serve(handler, HOST, PORT):
        print(f"WebSocket server port number: {PORT}")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())