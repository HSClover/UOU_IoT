import asyncio
from aiocoap import *
import time

async def main():
    context = await Context.create_client_context()

    req_list = Message(code=GET, uri='coap://localhost/.well-known/core')
    res_list = await context.request(req_list).response
    print("[resource list]", res_list.payload.decode())

    count = 1
    try:
        while True:
            print("count : ", count)
            req_at = Message(code=GET, uri='coap://localhost/at')
            res_at = await context.request(req_at).response
            print("[/at Response]", res_at.payload.decode())
            req_ot = Message(code=GET, uri='coap://localhost/ot')
            res_ot = await context.request(req_ot).response
            print("[/ot Response]", res_ot.payload.decode())
            await asyncio.sleep(2)
            count += 1
    except KeyboardInterrupt:
        print("Program end...")

if __name__ == "__main__":
    asyncio.run(main())