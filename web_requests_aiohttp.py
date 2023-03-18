from aiohttp import ClientSession, ClientTimeout
from utils import async_timed

import asyncio

@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = ClientTimeout(total=2)
    async with session.get(timeout=ten_millis, url=url) as res:
        return res.status
    
@async_timed()
async def main():
    session_timeout = ClientTimeout(total=1, connect=.1)
    async with ClientSession(timeout=session_timeout) as session:
        url = "https://example.com"
        status = await fetch_status(session, url)
        print(f"Состояние для {url} было равно {status}")

asyncio.run(main())