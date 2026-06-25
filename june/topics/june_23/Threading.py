import threading 
import time

def worker(name, delay):
    print(f"Thread {name} started")
    time.sleep(delay)
    print(f"Thread {name} fnished")

#Without threading - sequential
start = time.time()
worker("A", 2)
worker("B", 2)
print(f"Sequential: {time.time() - start:.2f}s")

#With threading - concurrent
start = time.time()
t1 = threading.Thread(target=worker, args=("A",2))
t2 = threading.Thread(target=worker, args=("B",2))

t1.start()
t2.start()

t1.join()
t2.join()
print(f"Threaded: {time.time() - start:.2f}s")
