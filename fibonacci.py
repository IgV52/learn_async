import threading
import time

def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    
    print(f"fib({number}) = {fib(number)}")

# def fibs_no_threading():
#     print_fib(40)
#     print_fib(41)

# start = time.time()

# fibs_no_threading()

# end = time.time()

# print(f"Время работы {end - start:.4f}c.")

def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))

    fortieth_thread.start()
    forty_first_thread.start()

    fortieth_thread.join()
    forty_first_thread.join()

strart_threads = time.time()

fibs_with_threads()

end_threads = time.time()

print(f"Многопоточное вычисление заняло {end_threads - strart_threads:.4f}c")