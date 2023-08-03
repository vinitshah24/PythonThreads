from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Condition


def task(condition, number):
    # wait to be notified
    print(f'Process {number} waiting...', flush=True)
    with condition:
        condition.wait()
    # block for a moment
    value = random()
    sleep(value)
    # report a result
    print(f'Process {number} got {value}', flush=True)


if __name__ == '__main__':
    # create a condition
    condition = Condition()
    # create all child processes
    processes = [Process(target=task, args=(condition, i)) for i in range(5)]
    # start all child processes
    for process in processes:
        process.start()
    # block for a moment
    sleep(1)
    # notify all waiting processes that they can run
    with condition:
        # wait to be notified
        condition.notify_all()
    # wait for all child processes to terminate
    for process in processes:
        process.join()
