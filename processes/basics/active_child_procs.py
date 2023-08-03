from time import sleep
from multiprocessing import active_children
from multiprocessing import Process

# function to execute in a new process
def task():
    # block for a moment
    sleep(1)

# protect the entry point
if __name__ == '__main__':
    # configure and start child processes
    for _ in range(10):
        # create and start child process
        Process(target=task).start()
    # wait a moment
    sleep(0.3)
    # get all active child processes
    children = active_children()
    # report details
    print(f'Active Children: {len(children)}')
    for child in children:
        print(child)
    # block until all children are finished
    for child in children:
        child.join()