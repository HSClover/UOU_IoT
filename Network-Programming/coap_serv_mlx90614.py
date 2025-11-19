import smbus
import asyncio
from aiocoap import resource, Context, Message

I2C = 0x5a
bus = smbus.SMBus(1)

class Ambient_temp(resource.Resource):
    async def render_get(self, request):
        temp = bus.read_word_data(I2C, 0x06)
        temp_conv = (temp * 0.02) - 273.15
        msg_str = "Ambient Temperature:" + str(round(temp_conv, 1))
        msg = msg_str.encode()
        return Message(payload=msg)
    
class Object_temp(resource.Resource):
    async def render_get(self, request):
        temp = bus.read_word_data(I2C, 0x07)
        temp_conv = (temp * 0.02) - 273.15
        msg_str = "Object Temperature:" + str(round(temp_conv, 1))
        msg = msg_str.encode()
        return Message(payload=msg)

async def main():
    root = resource.Site()
    root.add_resource(['at'], Ambient_temp())
    root.add_resource(['ot'], Object_temp())
    root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader))
    await Context.create_server_context(root)
    print("Start CoAP Server...")
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())