from time import sleep
from multiprocessing import Process
from multiprocessing import active_children
from signal import signal
from signal import SIGTERM
import sys

# function executed in a child process
def task2():
    sleep(10)

# handle signal
def handler(sig, frame):
    # get all active child processes
    active = active_children()
    # terminate all active children
    for child in active:
        child.terminate()
    # terminate the process
    sys.exit(0)

# function executed in a child process
def task():
    # handle sigterm
    signal(SIGTERM, handler)
    # start another child process
    Process(target=task2).start()
    # block for a while
    sleep(10)

# protect the entry point
if __name__ == '__main__':
    # start many child processes
    children = [Process(target=task) for _ in range(10)]
    # start all child processes
    for child in children:
        child.start()
    # wait a moment
    print('Main waiting...')
    sleep(2)
    # get all active child processes
    active = active_children()
    print(f'Active Children: {len(active)}')
    # terminate all active children
    for child in active:
        child.terminate()
    # block until all children have closed
    for child in active:
        child.join()
    # report active children
    active = active_children()
    print(f'Active Children: {len(active)}')