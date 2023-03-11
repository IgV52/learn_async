from utils import delay

import asyncio

async def time_out_task():
    delay_task = asyncio.create_task(delay(2))

    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("TimeOut")
        print(f"Task cancell? {delay_task.cancelled()}")

async def shield_task():
    task = asyncio.create_task(delay(10))
    
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Task run >5sec, soon she done")
        result = await task
        print(result)


async def main():
    #await time_out_task()
    await shield_task()


asyncio.run(main())