import threading
import time
from multiprocessing import Process


def cpu_task(n):
    total = 0
    for i in range(n):
        total += i**2
    return total


if __name__ == "__main__":
    # Sequential
    start = time.time()
    cpu_task(20_000_000)
    cpu_task(20_000_000)
    sequential_time = time.time() - start
    print(f"Sequential: {sequential_time:.2f}s")

    # Threading
    start = time.time()
    t1 = threading.Thread(target=cpu_task, args=(20_000_000,))
    t2 = threading.Thread(target=cpu_task, args=(20_000_000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    thread_time = time.time() - start
    print(f"Threading: {thread_time:.2f}s")

    # Multiprocessing
    start = time.time()
    p1 = Process(target=cpu_task, args=(20_000_000,))
    p2 = Process(target=cpu_task, args=(20_000_000,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    mp_time = time.time() - start
    print(f"Multiprocessing: {mp_time:.2f}s")

    # Comparison
    print(f"\nThreading speedup:    {sequential_time / thread_time:.2f}x")
    print(f"Multiprocessing speedup:    {sequential_time / mp_time:.2f}x")
