"""
The ThreadPool begins executing the task in a worker thread.

The main thread then closes the ThreadPool while the task is running.

This prevents the pool from taking any further tasks, then closes all worker threads once all tasks are completed.
The main thread blocks waiting for all worker threads to be released.

The task in the ThreadPool finishes and the worker threads in the pool are closed.
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
    # close the thread pool
    pool.close()
    # wait a moment
    pool.join()
    # report a message
    print('Main all done.')
    # report the number of worker threads that are still active
    active_threads = active_count()
    print(f'Active threads: {active_threads}')
