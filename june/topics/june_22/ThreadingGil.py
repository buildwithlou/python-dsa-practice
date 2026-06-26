import threading
import time


def io_task():
    print("Waiting for I/O...")
    time.sleep(2)
    print("Done!")


start = time.time()
t1 = threading.Thread(target=io_task)
t2 = threading.Thread(target=io_task)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Time: {time.time() - start:.2f}s")
