"""
We can trigger an action once all parties reach the barrier.
This can be achieved by setting the “action” argument to a callable in the multiprocessing.Barrier constructor.
"""

from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Barrier



def report():
    # action once all processes reach the barrier
    # report once all processes are done
    print('All processes have their result', flush=True)


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
    barrier = Barrier(5, action=report)
    # create the worker processes
    processes = [Process(target=task, args=(barrier, i)) for i in range(5)]
    # start all process
    for process in processes:
        process.start()
    # wait for all processes to finish
    for process in processes:
        process.join()
