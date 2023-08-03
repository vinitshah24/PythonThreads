"""
Running the example first creates an instance of the custom class.

A child process instance is created and configured to execute the task() function and is passed the instance of our
custom class.

The child process is started and the main process blocks and waits for the child process to terminate.

The task() function is executed, reports a message, updates the instance variable in the custom object, then reports
a second message showing that the instance variable was changed.

The child process terminates and the main process resumes and reports the value of the instance variable in the custom
object.

In this case, it shows that the instance variable is still zero and that the change made by the child process had no
effect or was lost.

Before update: 0
After update: 100
Main: 0

The reason for this is that the child process received and operated upon a copy of the instance of the custom class.
The object was not shared as expected.
"""


from multiprocessing import Process


class CustomClass():
    # constructor
    def __init__(self):
        # define instance variable
        self._var = 0

    # increment the variable
    def update(self, value):
        self._var = value

    # get the value
    def get(self):
        return self._var


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
