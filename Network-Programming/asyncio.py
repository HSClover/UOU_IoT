import asyncio
import time

HOST = "127.0.0.1"
PORT = 8888

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    print("New client connected")
    while True:
        data = await reader.readline()  # ready 되면 읽기
        if not data:
            break
        msg = data.decode("utf-8").strip()  
        if msg == "time":
            now = time.ctime()
            writer.write((now + "\n").encode("utf-8"))
        elif msg == "quit":
            writer.write(b"Bye\n")
            await writer.drain()
            break
        else:
            writer.write(b"Invalid Command\n")
        await writer.drain()    # 쓰기 완료 대기
    
    print("client connection close\n")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    print("Time server start")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())