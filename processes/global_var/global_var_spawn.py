"""
Running the example first sets the process start method to "spawn".

A global variable named "data" is then defined, assigned, and reported as per normal.

A new child process is then created using the spawn start method to execute our custom function.
The process starts and declares a global variable named data.
It then attempts to report the value of the global variable.

This results in a NameError, and the child process terminates. This is expected.
The main parent process blocks while the child process is running, then continues on once the child process terminates.

The main process then reports the value of the global variable again, reporting no change as expected.

This highlights that child processes created using the spawn method will not inherit global variables from the
parent process.

main process: Hello there
Process Process-1:
Traceback (most recent call last):
  ...
NameError: name 'data' is not defined
main process: Hello there
"""

from time import sleep
from multiprocessing import Process
from multiprocessing import set_start_method

# function to be executed in a new process
def task():
    # declare global state
    global data
    # report global state
    print(f'child process: {data}')
    # change global state
    data = 'hello hello!'
    # report global state
    print(f'child process: {data}')

# protect entry point
if __name__ == '__main__':
    # set the start method to spawn
    set_start_method('spawn')
    # define global state
    data = 'Hello there'
    # report global state
    print(f'main process: {data}')
    # start a child process
    process = Process(target=task)
    process.start()
    # wait for the child to terminate
    process.join()
    # report global state
    print(f'main process: {data}')
