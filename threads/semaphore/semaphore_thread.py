"""
A semaphore is a concurrency primitive that allows a limit on the number of threads that can acquire a
lock protecting a critical section.
It is an extension of a mutual exclusion (mutex) lock that adds a count for the number of threads that can
acquire the lock before additional threads will block.
Once full, new threads can only acquire a position on the semaphore once an existing thread holding the semaphore
releases a position.
Internally, the semaphore maintains a counter protected by a mutex lock that is incremented each time the semaphore
is acquired and decremented each time it is released.
When a semaphore is created, the upper limit on the counter is set. If it is set to be 1, then the semaphore will
operate like a mutex lock.

A semaphore provides a useful concurrency tool for limiting the number of threads that can access a resource
concurrently. Some examples include:
* Limiting concurrent socket connections to a server.
* Limiting concurrent file operations on a hard drive.
* Limiting concurrent calculations.
"""

from time import sleep
import random
from threading import Thread
from threading import Semaphore


def task(semaphore, number):
    with semaphore:
        sleep_time = 2 #random.randint(1, 2)
        print(f"Thread {number} running for {sleep_time} secs")
        sleep(sleep_time)
        print(f"Thread {number} completed...")

# At a time, only 2 threads can run the critical section of the code
semaphore = Semaphore(2)
for i in range(8):
    worker = Thread(target=task, args=(semaphore, i))
    worker.start()
