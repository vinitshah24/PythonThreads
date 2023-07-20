"""
A latch or countdown latch is a synchronization primitives used in concurrent programming.
It is created in the closed position and requires a count to be decremented until zero before opening.
The count is decremented by threads that pass through the latch, calling a count_down() function.
This is a non-blocking call, allowing the caller to proceed immediately.
Other threads register interest in the latch by calling wait() to block on the latch until it is opened.
A latch is used to coordinate more threads with the full opening of the latch. It just so happens that the latch is
designed to be opened incrementally each time other threads pass through, e.g. counting down from specified number to 0.
A latch is a one-use structure and is not reset after use. Once open, additional threads that may wait on the latch
will not block but will instead return immediately.
Internally, the latch may count up or count down, but typically decrements with each arrival, hence the common name
“countdown latch“. Internally, the latch may or may not raise an exception if more than the specified number of
arrivals (countdowns) are performed.
"""

from time import sleep
from random import random
from threading import Thread
from threading import Condition


class CountDownLatch():

    def __init__(self, count):
        self.count = count
        # control access to the count and notify when latch is open
        self.condition = Condition()

    def count_down(self):
        """ Count down the latch by one increment """
        # acquire the lock on the condition
        with self.condition:
            # check if the latch is already open
            if self.count == 0:
                return
            # decrement the counter
            self.count -= 1
            # check if the latch is now open
            if self.count == 0:
                # notify all waiting threads that the latch is open
                self.condition.notify_all()

    def wait(self):
        """ Wait for the latch to open """
        # acquire the lock on the condition
        with self.condition:
            # check if the latch is already open
            if self.count == 0:
                return
            # wait to be notified when the latch is open
            self.condition.wait()


def task(latch, i):
    """ Task that counts down the latch """
    # block for a moment
    sleep(random() * 10)
    # count down the latch
    print(f"Thread {i} counting down the latch...")
    latch.count_down()
    # report done
    print(f"Thread {i} done.")


latch = CountDownLatch(5)
for i in range(5):
    thread = Thread(target=task, args=(latch, i))
    thread.start()

print("Main Thread: Waiting for latch to be closed...")
latch.wait()
print("Main Thread: Latch is closed.")
