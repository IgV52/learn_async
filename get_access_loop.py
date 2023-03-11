from utils import delay

import asyncio

def call_later():
    print("Call me little soon")

async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)

asyncio.run(main())