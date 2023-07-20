"""
In concurrency, a condition (also called a monitor) allows multiple threads to be notified about some result.
It combines both a mutual exclusion lock (mutex) and a conditional variable.
A mutex can be used to protect a critical section, but it cannot be used to alert other threads that a condition
has changed or been met.
A condition can be acquired by a thread (like a mutex) after which it can wait to be notified by another thread
that something has changed. While waiting, the thread is blocked and releases the lock for other threads to acquire.
Another thread can then acquire the condition, make a change, and notify one, all, or a subset of threads waiting on
the condition that something has changed. The waiting thread can then wake-up (be scheduled by the operating system),
re-acquire the condition (mutex), perform checks on any changed state and perform required actions.
This highlights that a condition makes use of a mutex internally (to acquire/release the condition),
but it also offers additional features such as allowing threads to wait on the condition and to allow threads to
notify other threads waiting on the condition.
"""

import random
from time import sleep
from threading import Thread, Condition


def task(condition, thread_num):
    # wait to be notified
    with condition:
        print(f"Thread-{thread_num} waiting for condition to be notified")
        condition.wait()
    sleep_interval = random.randint(1, 4)
    print(f"Thread-{thread_num} running for {sleep_interval} seconds")
    sleep(sleep_interval)
    print(f"Thread-{thread_num} completed after running for {sleep_interval} seconds")


condition = Condition()

# Start threads that will wait to be notified
for i in range(5):
    t = Thread(target=task, args=(condition, i))
    t.start()

# Block for a moment
sleep(1)

print("MAIN Thread notifying child threads to run...")
# Notify all waiting threads that they can run
with condition:
    # wait to be notified
    condition.notify_all()
# Block until all non-daemon threads finish.
