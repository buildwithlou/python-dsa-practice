import os
import time
from multiprocessing import Process


def worker(name):
    print(f"Process {name} started - PID: {os.getpid()}")
    time.sleep(2)
    print(f"Process {name} finished")


if __name__ == "__main__":
    print(f"Main process PID: {os.getpid()}")

    # Creating two processes
    p1 = Process(target=worker, args=("A",))
    p2 = Process(target=worker, args=("B",))

    # Start them
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    print("All processes done!")
