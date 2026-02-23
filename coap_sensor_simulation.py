import asyncio
import random
from aiocoap import Context, Message, POST

async def simulate_sensor_data():
    protocol = await Context.create_client_context()

    while True:
        temperature = random.uniform(20.0, 25.0)
        humidity = random.uniform(30.0, 50.0)

        payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'.encode("utf-8")

        request = Message(code=POST, payload=payload)
   request.set_request_uri("coap://127.0.0.1:5683/sensor/data")

        try:
            response = await protocol.request(request).response
            print("Result:", response.code, response.payload)
        except Exception as e:
            print("Failed to send request:", e)

        await asyncio.sleep(1)

asyncio.run(simulate_sensor_data())