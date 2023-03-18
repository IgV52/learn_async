from aiohttp import ClientSession
from utils import async_timed, fetch_status

import asyncio

@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ["https://example.com" for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_code = await asyncio.gather(*requests)

        print(status_code)

@async_timed()
async def main_fake_url():
    async with ClientSession() as session:
        urls = ["https://example.com", "fake://example.com"]
        tasks = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        exceptions = [res for res in results if isinstance(res, Exception)]
        successful_results = [res for res in results if not isinstance(res, Exception)]

        print(f"Все результаты: {results}")
        print(f"Завершились успешно: {successful_results}")
        print(f"Завершились с ошибкой: {exceptions}")

asyncio.run(main_fake_url())