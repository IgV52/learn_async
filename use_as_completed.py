from aiohttp import ClientSession
from utils import async_timed, fetch_status

import asyncio

@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, "https://example.com", 1),
            fetch_status(session, "https://example.com", 1),
            fetch_status(session, "https://example.com", 5)
        ]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)

@async_timed()
async def main_timeout():
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, "https://example.com", 1),
            fetch_status(session, "https://example.com", 10),
            fetch_status(session, "https://example.com", 10)
        ]

        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print("TIMEOUT!!!")
        
        for task in asyncio.tasks.all_tasks():
            print(task)

asyncio.run(main_timeout())