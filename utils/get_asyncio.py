from aiohttp import ClientSession

import asyncio

async def fetch_status(session: ClientSession, url: str, delay: int = 1) -> int:
    await asyncio.sleep(delay)
    async with session.get(url=url) as res:
        return res.status