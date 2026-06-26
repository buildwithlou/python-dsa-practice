import time
from multiprocessing import Process


def cpu_heavy_task():
    count = 0
    for i in range(50_000_000):
        count += 1


if __name__ == "__main__":
    # Multiprocessing - each process has its OWN GIL
    start = time.time()
    p1 = Process(target=cpu_heavy_task)
    p2 = Process(target=cpu_heavy_task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Multiprocessing: {time.time() - start:.2f}s")
