"""
We might want to abort the coordination of processes on the barrier for some reason.
This might be because one of the processes is unable to perform its required task.
We can abort the barrier by calling the abort() function, this will cause all processes waiting on the barrier to
raise a BrokenBarrierError and all new callers to wait() to raise the same error.
This means that all calls to wait() should be protected by a try-except structure.
"""

from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Barrier
from threading import BrokenBarrierError

# target function to prepare some work


def task(barrier, number):
    # generate a unique value
    value = random() * 10
    # block for a moment
    sleep(value)
    # report result
    print(f'Process {number} done, got: {value}', flush=True)
    # check if the result was "bad"
    if value > 8:
        print(f'Process {number} aborting...', flush=True)
        barrier.abort()
    else:
        # wait on all other processes to complete
        try:
            barrier.wait()
        except BrokenBarrierError:
            pass


# entry point
if __name__ == '__main__':
    # create a barrier
    barrier = Barrier(5 + 1)
    # create the worker processes
    for i in range(5):
        # start a new process to perform some work
        worker = Process(target=task, args=(barrier, i))
        worker.start()
    # wait for all processes to finish
    print('Main process waiting on all results...')
    try:
        barrier.wait()
        print('All processes have their result')
    except BrokenBarrierError:
        print('At least one process aborted due to bad results.')
