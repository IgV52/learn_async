from utils import async_timed

import asyncio
import requests

@async_timed()
async def get_example_status() -> int:
    return requests.get("https://www.example.com").status_code

@async_timed()
async def main():
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())

    await task_1
    await task_2
    await task_3

asyncio.run(main())