from typing import Set
from utils import delay

import asyncio, signal

async def await_all_tasks():
    tasks = asyncio.all_tasks()
    [await task for task in tasks]

def cancel_tasks():
    print("Request signal SIGINT")
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f"Removed {len(tasks)} task")
    [task.cancel() for task in tasks]

async def main():
    loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()

    loop.add_signal_handler(signal.SIGINT, 
                            lambda: asyncio.create_task(await_all_tasks()))

    await delay(10)
