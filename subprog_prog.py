from utils import delay

import asyncio

async def add_one(number: int) -> int:
    return number+1

async def hello_world() -> str:
    await delay(1)
    return "hello world"

async def main() -> None:
    message = await hello_world()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)

asyncio.run(main())


