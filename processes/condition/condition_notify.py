"""
In concurrency, a condition (also called a monitor) allows multiple processes (or threads) to be notified about some
result.

It combines both a mutual exclusion lock (mutex) and a conditional variable.
A mutex can be used to protect a critical section, but it cannot be used to alert other processes that a condition has
changed or been met.

A condition can be acquired by a process (like a mutex) after which it can wait to be notified by another process that
something has changed. While waiting, the process is blocked and releases the lock for other processes to acquire.

Another process can then acquire the condition, make a change, and notify one, all, or a subset of processes waiting on
the condition that something has changed. The waiting process can then wake-up (be scheduled by the operating system),
re-acquire the condition (mutex), perform checks on any changed state and perform required actions.

This highlights that a condition makes use of a mutex internally (to acquire/release the condition),
but it also offers additional features such as allowing processes to wait on the condition and to allow processes to
notify other processes waiting on the condition.
"""

from time import sleep
from multiprocessing import Process
from multiprocessing import Condition

# target function to prepare some work
def task(condition):
    # block for a moment
    sleep(1)
    # notify a waiting process that the work is done
    print('Child process sending notification...', flush=True)
    with condition:
        condition.notify()
    # do something else...
    sleep(1)

# entry point
if __name__ == '__main__':
    # create a condition
    condition = Condition()
    # wait to be notified that the data is ready
    print('Main process waiting for data...')
    with condition:
        # start a new process to perform some work
        worker = Process(target=task, args=(condition,))
        worker.start()
        # wait to be notified
        condition.wait()
    # we know the data is ready
    print('Main process all done')