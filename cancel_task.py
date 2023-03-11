from utils import delay

import asyncio

async def main():
    long_task = asyncio.create_task(delay(10))

    seconds_elasped = 0

    while not long_task.done():
        print(f"Задача не закончилась следующая проверка через секунду")
        await asyncio.sleep(1)
        seconds_elasped = seconds_elasped + 1
        if seconds_elasped == 5:
            long_task.cancel()

    try:
        await long_task
    except asyncio.CancelledError:
        print("Task cancel")

asyncio.run(main())