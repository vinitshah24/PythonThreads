"""
Running the example first creates the ThreadPool then issues the task to the ThreadPool.
The ThreadPool begins executing the task in a worker thread.
In this case, it does not get a chance to print the first message.

The main thread then terminates the ThreadPool while the task is running.
This prevents the pool from taking any further tasks, then closes all worker threads (almost) immediately.

The main threads then joins the ThreadPool, blocking until all worker threads are closed and released.
The task in the ThreadPool does not get a chance to start completely, let alone finish, and the worker threads in
the pool are terminated.

The main thread carries on and reports a final message.
"""

from time import sleep
from multiprocessing.pool import ThreadPool


def task():
    # report a message
    print(f"CHILD: Task executing...")
    # block for a moment
    sleep(20)
    # report a message
    print(f"CHILD: Task completed successfully!")


# protect the entry point
if __name__ == "__main__":
    # create and configure the thread pool
    pool = ThreadPool()
    # add a task to the thread pool
    print("MAIN: Adding task to thread pool...")
    pool.apply_async(task)
    # terminate the thread pool
    print("MAIN: Terminating thread pool...")
    pool.terminate()
    # wait a moment
    print("MAIN: Joining thread pool...")
    pool.join()
    # report a message
    print(f"MAIN: Thread completed successfully")
