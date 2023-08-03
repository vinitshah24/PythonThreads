"""
Running the example first creates an instance of the custom class.

A child process instance is created and configured to execute the task() function and is passed the instance of
our custom class.

The child process is started and the main process blocks and waits for the child process to terminate.

The task() function is executed, reports a message, updates the instance variable in the custom object,
then reports a second message showing that the instance variable was changed.

The child process terminates and the main process resumes and reports the value of the instance variable in the
custom object.

In this case, it shows that changes made to the instance variable in the “shared” object were propagated as we hoped.

Before update: 0
After update: 100
Main: 100
Although the object was shared with the child process, it was still copied as before.
In this case, the instance variable was not copied, and instead access to the same variable was shared among both
child and parent processes.

Changes made to the instance variable in the child process were propagated to the instance variable in the
parent process and we can see this when the main process reported the value at the end of the program.

This highlights how we can update instance variables in a custom object so that changes are propagated among processes.
"""

from multiprocessing import Process
from multiprocessing import Value

# custom class
class CustomClass():
    # constructor
    def __init__(self):
        # define instance variable
        self._var = Value('i', 0)

    # increment the variable
    def update(self, value):
        self._var.value = value

    # get the value
    def get(self):
        return self._var.value

# function executed in child process
def task(custom):
    # report the value
    print(f'Before update: {custom.get()}')
    # update the value
    custom.update(100)
    # report the value
    print(f'After update: {custom.get()}')

# protect the entry point
if __name__ == '__main__':
    # create the custom object
    custom = CustomClass()
    # configure a child process to run the task
    process = Process(target=task, args=(custom,))
    # start the process
    process.start()
    # wait for the process to terminate
    process.join()
    # report the value
    print(f'Main: {custom.get()}')