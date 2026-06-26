import threading
import time


def cpu_heavy_task():
    count = 0
    for i in range(50_000_000):
        count += 1


# Single thread
start = time.time()
cpu_heavy_task()
cpu_heavy_task()
print(f"Sequential: {time.time() - start:.2f}s")

# Two threads - Should be faster on multi-core, but isn't
start = time.time()
t1 = threading.Thread(target=cpu_heavy_task)
t2 = threading.Thread(target=cpu_heavy_task)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Threaded: {time.time() - start:.2f}s")
