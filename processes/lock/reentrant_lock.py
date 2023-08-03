"""
A reentrant mutual exclusion lock, “reentrant mutex” or “reentrant lock” for short, is like a mutex lock except it
allows a process (or thread) to acquire the lock more than once.

A process may need to acquire the same lock more than once for many reasons.

We can imagine critical sections spread across a number of functions, each protected by the same lock.
A process may call across these functions in the course of normal execution and may call into one critical section
from another critical section.

A limitation of a (non-reentrant) mutex lock is that if a process has acquired the lock that it cannot acquire it again. In fact, this situation will result in a deadlock as it will wait forever for the lock to be released so that it can be acquired, but it holds the lock and will not release it.

A reentrant lock will allow a process to acquire the same lock again if it has already acquired it.
This allows the process to execute critical sections from within critical sections, as long as they are
protected by the same reentrant lock.

Each time a process acquires the lock it must also release it, meaning that there are recursive levels of acquire and
release for the owning process. As such, this type of lock is sometimes called a “recursive mutex lock”.
"""

from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import RLock

def report(lock, identifier):
    with lock:
        print(f'>process {identifier} done')

def task(lock, identifier, value):
    with lock:
        print(f'>process {identifier} sleeping for {value}')
        sleep(value)
        report(lock, identifier)

if __name__ == '__main__':
    # create a shared reentrant lock
    lock = RLock()
    processes = [Process(target=task, args=(lock, i, random())) for i in range(10)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
