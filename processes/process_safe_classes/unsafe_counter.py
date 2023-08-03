"""
Running the example first creates the shared UnsafeCounter object.

Then, 10 child processes are created and configured to execute our custom task() function and passed the
shared counter object.

The main process then starts all processes and waits for them to complete.

Each process executes the custom task() function and increments the shared counter 100,000 times.

All child processes executing their tasks share the same shared Value instance variable. Changes are propagated
among processes.

We would expect the final value of the counter to be 1,000,000, e.g. 10 processes multiplied by 100,000 increments.

The tasks are completed and the final value of the counter is reported.

In this case, the value is different every time the example is run and is not the expected value of one million.

165690
Running the program again produces a different final value of the count.
162723
The reason the program gives a count value that is different every time is because of a race condition.

The processes step on each other when updating the internal value of the counter.

Consider how the value of the counter is updated:

...
self._counter.value += 1
Unrolled, this is performing at least 3 operations, they are:

Read the current counter value into a copy.
Add one to the copy of the current counter value.
Replace the current counter value with the updated copy.
If these operations are interleaved among multiple processes, even just two processes,
then the value of the counter will be corrupted.

For example, an updated copy of the value may overwrite a stale version or an already updated version of the variable.

For example:
Process 1: Read the current counter value into a copy.
Process 1: Add one to the copy of the current counter value.
Process 2: Read the current counter value into a copy.
Process 2: Add one to the copy of the current counter value.
Process 2: Replace the current counter value with the updated copy.
Process 1: Replace the current counter value with the updated copy.

This is called a race condition.
"""

from multiprocessing import Process
from multiprocessing import Value

# define a counter
class UnsafeCounter():
    # constructor
    def __init__(self):
        # initialize counter
        self._counter = Value('i', 0)

    # increment the counter
    def increment(self):
        self._counter.value += 1

    # get the counter value
    def value(self):
        return self._counter.value

# task executed by processes
def task(counter):
    # increment the counter
    for _ in range(100000):
        counter.increment()

# protect the entry point
if __name__ == '__main__':
    # create the shared counter
    counter = UnsafeCounter()
    # create 10 processes to increment the counter
    processes = [Process(target=task, args=(counter,)) for _ in range(10)]
    # start all processes
    for process in processes:
        process.start()
    # wait for all processes to finish
    for process in processes:
        process.join()
    # report the value of the counter
    print(counter.value())