import threading
import time
import multiprocessing
import os

# print(f"Исполняется Python-process id: {os.getpid()}")

# total_threads = threading.active_count()
# thread_name = threading.current_thread().name

# print(f"В данный момент Python use {total_threads} streams")
# print(f"Имя  текущего потока {thread_name}")

def hello_from_threading():
    time.sleep(1)
    print(f"Привет от потока {threading.current_thread()}!")

hello_thread = threading.Thread(target=hello_from_threading)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"В данный момент Python выполняет: {total_threads} streams")
print(f"Имя текущего потока {thread_name}")
hello_thread.join()

def hello_from_process():
    print(f"Привет от дочернего процесса {os.getpid()}!")


if __name__ == "__main__":
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()

    print(f"Привет от родительского процесса {os.getpid()}")

    hello_process.join()