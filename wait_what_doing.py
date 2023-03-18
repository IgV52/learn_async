from aiohttp import ClientSession
from utils import fetch_status

import asyncio
import logging

async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, "https://example.com", 1)),
            asyncio.create_task(fetch_status(session, "https://example.com", 1))
        ]
        done, peding = await asyncio.wait(fetchers)

        print(f"Число завершенных задач: {len(done)}")
        print(f"Число ожидающих задач: {len(peding)}")

        for done_task in done:
            result = await done_task
            print(result)

async def main_expt():
    async with ClientSession() as session:
        good_request = fetch_status(session, "https://example.com", 1)
        bad_request = fetch_status(session, "bad.Bad", 1)

        fetchers = [asyncio.create_task(good_request),
                    asyncio.create_task(bad_request)]
        
        done, peding = await asyncio.wait(fetchers)

        print(f"Число завершенных задач: {len(done)}")
        print(f"Число ожидающих задач: {len(peding)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение",
                            exc_info=done_task.exception())
                
async def main_stop_task():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, "bad.bad")),
            asyncio.create_task(fetch_status(session, "https://example.com", 3)),
            asyncio.create_task(fetch_status(session, "https://example.com", 3)),
                ]
        
        done, peding = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f"Число завершенных задач: {len(done)}")
        print(f"Число ожидающих задач: {len(peding)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение",
                            exc_info=done_task.exception())
            
        for peding_task in peding:
            peding_task.cancel()

async def main_first_done():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, "https://example.com")),
            asyncio.create_task(fetch_status(session, "https://example.com", 10)),
            asyncio.create_task(fetch_status(session, "https://example.com", 10)),
        ]
        
        done, peding = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

        print(f"Число завершенных задач: {len(done)}")
        print(f"Число ожидающих задач: {len(peding)}")

        for done_task in done:
            print(await done_task)

async def main_custom_all_done():
    async with ClientSession() as session:
        url = "https://example.com"
        peding = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url, 10)),
            asyncio.create_task(fetch_status(session, url, 10)),
        ]

        while peding:
            done, peding = await asyncio.wait(peding, return_when=asyncio.FIRST_COMPLETED)

            print(f"Число завершенных задач: {len(done)}")
            print(f"Число ожидающих задач: {len(peding)}")

            for done_task in done:
                print(await done_task)

async def main_timeout():
    async with ClientSession() as session:
        url = "https://example.com"
        fetchers = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url, 10)),
            asyncio.create_task(fetch_status(session, url, 10)),
        ]

        done, peding = await asyncio.wait(fetchers, timeout=2)

        print(f"Число завершенных задач: {len(done)}")
        print(f"Число ожидающих задач: {len(peding)}")

        for done_task in done:
            print(await done_task)

async def main_who_err():
    async with ClientSession() as session:
        url = "https://example.com"
        api_a = fetch_status(session, url)
        api_b = fetch_status(session, url, 5)

        done, peding = await asyncio.wait([api_a, api_b], timeout=2)

        for task in peding:
            if task is api_b:
                print("API B slow, cancel")
                task.cancel()

async def main_who():
    async with ClientSession() as session:
        url = "https://example.com"
        api_a = asyncio.create_task(fetch_status(session, url))
        api_b = asyncio.create_task(fetch_status(session, url, 5))

        done, peding = await asyncio.wait([api_a, api_b], timeout=2)

        for task in peding:
            if task is api_b:
                print("API B slow, cancel")
                task.cancel()

asyncio.run(main_who())