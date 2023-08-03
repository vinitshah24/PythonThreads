"""
Running the example first creates the ThreadPool then issues the task to the ThreadPool.
The ThreadPool begins executing the task in a worker thread.
The main thread then does not join the ThreadPool, instead, it reports a message and exits.
The Python garbage collector finalizes the ThreadPool which ultimately results in the terminate()
function being called automatically on the pool.

This terminates all threads immediately, preventing the issued task from finishing.
This example highlights an important case of why we might need to join the ThreadPool,
specifically to allow issued tasks to finish before exiting the application.
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
    # issue a task to the thread pool
    print("MAIN: Adding task to thread pool...")
    pool.apply_async(task)
    print("MAIN: Closing thread pool...")
    pool.close()
    # report a message
    print(f"MAIN: Thread completed successfully")