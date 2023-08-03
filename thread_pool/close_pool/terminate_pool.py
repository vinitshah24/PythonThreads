"""
The ThreadPool begins executing the task in a worker thread.

The main thread blocks for a moment, then terminates the ThreadPool.

This prevents the pool from taking any further tasks, then immediately closes all worker threads.
The main thread blocks waiting for all worker threads to be closed.

Note, the running tasks are not terminated, but are instead allowed to finish. This because threading.Thread
instances cannot be terminated mid-task, e.g. they do not have a terminate() method.

The task in the ThreadPool does not get a chance to finish. The worker threads in the pool are closed.
"""

from time import sleep
from multiprocessing.pool import ThreadPool
from threading import active_count


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
    # terminate the thread pool
    pool.terminate()
    # wait a moment
    pool.join()
    # report a message
    print('Main all done.')
    # report the number of worker threads that are still active
    active_threads = active_count()
    print(f'Active threads: {active_threads}')
