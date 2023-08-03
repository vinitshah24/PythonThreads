"""
Running the example first creates the ThreadPool then issues the task to the ThreadPool.
The ThreadPool begins executing the task in a worker thread.
The main thread blocks for a moment.
It then reports the number of active threads, which is 12 in this case.
On my system, there are 8 worker threads, 1 main thread, and 3 helper threads internal to the ThreadPool class.

Note, the number of active threads will differ depending on your system and the default number of worker threads
that were created.

The daemon status of all worker threads is then reported.
We can see that all worker threads with the name “DummyProcess” are daemon threads, as expected.
This means they will not prevent the main thread from exiting. We can also see the three helper threads are also
daemon threads, as we would expect, and the main thread is not a daemon thread.

The main thread exits. The Python garbage collector triggers the multiprocessing.pool.ThreadPool object to be
deleted and indirectly results in the terminate() function on the pool being called.

This prevents the pool from taking any further tasks, then closes all worker threads.
The task in the thread pool does not get a chance to finish. The worker threads in the pool are forcefully stopped.
"""

from time import sleep
from multiprocessing.pool import ThreadPool
import threading


def task():
    # report a message
    print(f'Task executing')
    # block for a moment
    sleep(1)
    # report a message
    print(f'Task done')


# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    pool = ThreadPool()
    # issue tasks to the thread pool
    result = pool.apply_async(task)
    # wait a moment
    sleep(0.5)
    # report a message
    print('Main all done.')
    # report the number of thread that are still active
    active_threads = [t for t in threading.enumerate()]
    print(f'Active children: {len(active_threads)}')
    # report the daemon status of the child
    for thread in active_threads:
        print(thread)

