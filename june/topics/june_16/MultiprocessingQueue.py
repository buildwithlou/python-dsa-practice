import time
from multiprocessing import Process, Queue


# Pass data between processes in Queue
def producer(queue):
    for i in range(5):
        queue.put(i)  # sending data
        print(f"Produced: {i}")
        time.sleep(0.1)


def consumer(queue):
    while True:
        item = queue.get()  # receive data
        if item is None:  # None = stop signal
            break
        print(f"Consumed: {item}")


if __name__ == "__main__":
    queue = Queue()

    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    queue.put(None)  # signal consumer to stop
    p2.join()
