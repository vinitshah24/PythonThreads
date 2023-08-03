
"""
Running the example first sets the start method to "fork".

It then defines a global variable and assigns it the value "Hello there" and reports the variable to
confirm that this is the current value.

A child process is then started using the "fork" start method and executes our custom function.
The main process then blocks until the child process terminates.

The child process declares the "data" variable as being global.

It then reports the "data" global variable. This works as expected, as the variable was inherited from the parent
process. The value is the same as that assigned in the parent value, specifically "Hello there".

The child process then changes the value of the global variable, then reports the value again.
This shows that the value was changed to "hello hello!".

The child process terminates and the parent process wakes up. It then reports the value of the global variable again,
which is unchanged with the value "Hello there".

This highlights that indeed a forked child process will inherit global variables, but changes to the global variable
are not propagated from the child back to the parent.
"""

from time import sleep
from multiprocessing import Process
from multiprocessing import set_start_method


def task():
    # declare global state
    global data
    # report global state
    print(f'child process before: {data}')
    # change global state
    data = 'hello hello!'
    # report global state
    print(f'child process after: {data}')


# protect entry point
if __name__ == '__main__':
    # set the start method to fork
    set_start_method('fork')
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
