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


def task(job, condition, work_list):
    sleep_time = 2
    print(f"Running {job} for {sleep_time} seconds")
    sleep(sleep_time)
    work_list.append({"job": job, "task_time": sleep_time})
    print('Thread sending notification...')
    with condition:
        print(f"Wait for {job} condition to complete")
        sleep(sleep_time)
        # notify a waiting thread that the work is done
        condition.notify()


threads = []
work_list = []
print("Running jobs...")
condition = Condition()
with condition:
    for i in range(1, 5):
        t = Thread(target=task, args=(f"JOB-{i}", condition, work_list))
        t.start()
        threads.append(t)
    condition.wait()

for thread in threads:
    thread.join()
for task in work_list:
    print(task)

