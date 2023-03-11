from typing import Callable, Any

import functools
import time

def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"processing {func} args {args}, kwargs {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"{func} done at time: {total:.4f}s")
        return wrapped
    return wrapper

