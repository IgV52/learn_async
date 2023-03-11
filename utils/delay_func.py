import asyncio

async def delay(delay_sec: int) -> int:
    print(f"sleep {delay_sec}s")
    await asyncio.sleep(delay_sec)
    print(f"unsleep {delay_sec}s")
    return delay_sec