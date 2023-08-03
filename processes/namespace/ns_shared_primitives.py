"""
Running the example first creates the manager and starts the manager's server process.

The manager is then used to create a namespace. The namespace is created in the Manager's server process and a proxy
object is returned that may be shared and used to access the namespace in a process-safe manner.

The main process then defines a variable on the namespace and assigns it an integer value.

A child process is configured and started to execute our custom task1() function. The main process blocks until the
process terminates.

The first child process generates a random number, blocks, defines a new variable on the shared namespace, then
reports the value defined by the main process as well as the random number that was generated.

The child process terminates and the main process continues on.

The main process configures and starts a second child process, this time to execute our task2() function.
It blocks until the process terminates.

The second child process generates a random number, blocks for a fraction of a second then reports the value on the
namespace defined by the first child process, as well as the random number that was generated.
It then defines a new variable on the namespace with the generated floating point value.

The second process terminates and the main process continues on and reports the content of the shared namespace.

We can see the integer value defined by the main process, the floating point value defined by the first child
process and the floating point value defined by the second child process.

This highlights that variables can be defined and accessed on the shared namespace arbitrarily by different processes.

Note: output will vary each time the program is run given the use of random numbers.
Task1 sees 55 got 0.19925402509706536
Task2 sees 0.19925402509706536 got 0.9487094130571998
Main sees: Namespace(main=55, task1=0.19925402509706536, task2=0.9487094130571998)
"""

from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Manager

# task executed in a new process
def task1(shared_ns):
    # generate a number between 0 and 1
    value = random()
    # block for a fraction of a second
    sleep(value)
    # update the namespace variables
    shared_ns.task1 = value
    # report the data
    print(f'Task1 sees {shared_ns.main} got {value}', flush=True)

# task executed in a new process
def task2(shared_ns):
    # generate a number between 0 and 1
    value = random()
    # block for a fraction of a second
    sleep(value)
    # report the data
    print(f'Task2 sees {shared_ns.task1} got {value}', flush=True)
    # update the namespace variables
    shared_ns.task2 = value

# protect the entry point
if __name__ == '__main__':
    # create the manager
    with Manager() as manager:
        # create the shared namespace
        namespace = manager.Namespace()
        # initialize the attribute
        namespace.main = 55
        # start and run a process for task 1
        process = Process(target=task1, args=(namespace,))
        process.start()
        process.join()
        # start and run a process for task 2
        process = Process(target=task2, args=(namespace,))
        process.start()
        process.join()
        # report everything
        print(f'Main sees: {namespace}')