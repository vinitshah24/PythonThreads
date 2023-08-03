"""
A barrier is a synchronization primitive.
It allows multiple processes (or threads) to wait on the same barrier object instance (e.g. at the same point in code)
until a predefined fixed number of processes arrive (e.g. the barrier is full), after which all processes are then
notified and released to continue their execution.

Internally, a barrier maintains a count of the number of processes waiting on the barrier and a configured maximum
number of parties (processes) that are expected. Once the expected number of parties reaches the pre-defined maximum,
all waiting processes are notified.


Running the example first creates the barrier then creates and starts the worker processes.
Each worker process performs its calculation and then waits on the barrier for all other processes to finish.
Finally, the processes finish and are all released, including the main process, reporting a final message.
"""

from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Barrier

# target function to prepare some work
def task(barrier, number):
    # generate a unique value
    value = random() * 10
    # block for a moment
    sleep(value)
    # report result
    print(f'Process {number} done, got: {value}', flush=True)
    # wait on all other processes to complete
    barrier.wait()

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
    barrier.wait()
    # report once all processes are done
    print('All processes have their result')