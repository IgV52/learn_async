from utils import async_timed, delay

import asyncio

@async_timed()
async def main1() -> None:
    delay_times = [3,3,3]
    [await asyncio.create_task(delay(seconds))
    for seconds in delay_times]

@async_timed()
async def main2() -> None:
    delay_times = [3,3,3]
    tasks = [asyncio.create_task(delay(seconds))
    for seconds in delay_times]
    [await task for task in tasks]

asyncio.run(main2())