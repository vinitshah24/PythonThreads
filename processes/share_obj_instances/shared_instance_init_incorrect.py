"""
Running the example first creates an instance of the custom class, then starts a child process that executes the run() method.

When an instance of the class is created, the attribute is initialized.
As before, the parent process blocks until the child process terminates.

The child process sets a value in the instance variable and terminates.
The parent process unblocks then reports the value of the instance variable.

In this case, the child process reports the correct value it stored then the parent value reports a
value of None in the instance variable.

This too is expected.

Waiting for the child process to finish
Child stored: 99
Parent got: None

The parent process can access the attribute.
This is because it was defined in the class constructor which was executed in the parent process.
Then the child process was started which executes a copy of the class instance and sets a value to the attribute
which is only accessible within the child process.

The parent process reports the attribute value which is still None because the change made by the child process was
not shared with the parent process.

"""

from time import sleep
from multiprocessing import Process


class CustomProcess(Process):
    # override the constructor
    def __init__(self):
        # execute the base constructor
        Process.__init__(self)
        # initialize attribute
        self.data = None

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
