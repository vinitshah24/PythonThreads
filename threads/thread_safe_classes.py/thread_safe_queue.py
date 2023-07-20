from threading import Thread
from queue import Queue


def add_items(queue):
    for i in range(100000):
        queue.put(i)


queue = Queue()
threads = [Thread(target=add_items, args=(queue,)) for i in range(10)]
for thread in threads:
    thread.start()
print("Main waiting for threads...")
for thread in threads:
    thread.join()
print(f"List size: {queue.qsize()}")
