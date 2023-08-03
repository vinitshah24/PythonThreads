"""
A semaphore is a concurrency primitive that allows a limit on the number of processes (or threads)
that can acquire a lock protecting a critical section.

It is an extension of a mutual exclusion (mutex) lock that adds a count for the number of processes that
can acquire the lock before additional processes will block. Once full, new processes can only acquire access
on the semaphore once an existing process holding the semaphore releases access.

Internally, the semaphore maintains a counter protected by a mutex lock that is incremented each time the
semaphore is acquired and decremented each time it is released.

When a semaphore is created, the upper limit on the counter is set. If it is set to be 1,
then the semaphore will operate like a mutex lock.

A semaphore provides a useful concurrency tool for limiting the number of processes that can access a
resource concurrently. Some examples include:
* Limiting concurrent socket connections to a server.
* Limiting concurrent file operations on a hard drive.
* Limiting concurrent calculations.
"""

from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Semaphore


def task(semaphore, number):
    # attempt to acquire the semaphore
    with semaphore:
        # simulate computational effort
        value = random()
        sleep(value)
        # report result
        print(f'Process {number} got {value}')


if __name__ == '__main__':
    # create the shared semaphore
    semaphore = Semaphore(2)
    # create processes
    processes = [Process(target=task, args=(semaphore, i)) for i in range(10)]
    # start child processes
    for process in processes:
        process.start()
    # wait for child processes to finish
    for process in processes:
        process.join()
