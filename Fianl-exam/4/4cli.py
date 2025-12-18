import asyncio
import websockets
import json

SERV = 'ws://localhost:8888'

async def main():
    async with websockets.connect(SERV) as ws:
        try:
            async for message in ws:
                try:
                    data = json.loads(message)
                    print(f"Ambient: {data.get('Ambient_c')} °C, Object: {data.get('Object_c')} °C")
                except Exception:
                    print("Unknown received message: ", message)
        except websockets.ConnectionClosed:
            print("Connection closed.")

if __name__ == "__main__":
    asyncio.run(main())