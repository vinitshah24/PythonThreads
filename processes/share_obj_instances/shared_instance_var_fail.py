"""
Running the example first creates an instance of the custom class, then starts the child process.
The parent process then blocks until the child process terminates.
The child process executes the run() method, blocks, sets an integer value in the instance variable,
reports the stored value then exits.

The parent process continues on, then attempts to report the value of the instance variable set by the child process.
This fails with an error that no such instance variable attribute exists.

This was expected.

Waiting for the child process to finish
Child stored: 99
Traceback (most recent call last):
  ...
AttributeError: 'CustomProcess' object has no attribute 'data'

This error occurred because the child process operates on a copy of the CustomProcess instance that is different
from the copy of the CustomProcess instance used in the parent process.
When the child process adds an attribute to the class instance, it only exists in the child process and not the
parent process.
"""

from time import sleep
from multiprocessing import Process


class CustomProcess(Process):
    # override the constructor
    def __init__(self):
        # execute the base constructor
        Process.__init__(self)

    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        # store the data variable
        self.data = 99
        # report stored value
        print(f'Child stored: {self.data}')


# entry point
if __name__ == '__main__':
    # create the process
    process = CustomProcess()
    # start the process
    process.start()
    # wait for the process to finish
    print('Waiting for the child process to finish')
    # block until child process is terminated
    process.join()
    # report the process attribute
    print(f'Parent got: {process.data}')
