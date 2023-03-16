from aiohttp import ClientSession
from utils import async_timed

import asyncio

@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as res:
        return res.status
    
@async_timed()
async def main():
    async with ClientSession() as session:
        url = "https://example.com"
        status = await fetch_status(session, url)
        print(f"Состояние для {url} было равно {status}")

asyncio.run(main())