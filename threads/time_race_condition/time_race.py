"""
Running the example first creates and starts the new thread.
The new thread starts running and then sleeps for a fraction of a second.
Meanwhile, the main thread acquires the condition and calls notify().
The new thread wakes up, acquires the condition and waits to be notified.
Because the notification has already occurred, it is missed and the new thread waits forever.
"""

from time import sleep
from threading import Thread
from threading import Condition


def task(condition):
    sleep(0.5)
    print("Thread: Waiting to be notified...")
    with condition:
        condition.wait()
    print("Thread: Notified")


condition = Condition()
thread = Thread(target=task, args=(condition,))
thread.start()

with condition:
    print("Main thread notifying child threads...")
    condition.notify()

print("Main thread completed successfully!")
