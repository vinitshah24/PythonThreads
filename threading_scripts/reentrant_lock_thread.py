"""
A reentrant mutual exclusion lock, reentrant mutex or reentrant lock for short, is like a mutex lock except
it allows a thread to acquire the lock more than once.

A thread may need to acquire the same lock more than once for many reasons.

We can imagine critical sections spread across a number of functions, each protected by the same lock.
A thread may call across these functions in the course of normal execution and may call into one critical section
from another critical section.

A limitation of a (non-reentrant) mutex lock is that if a thread has acquired the lock that it cannot acquire it again.
In fact, this situation will result in a deadlock as it will wait forever for the lock to be released so that
it can be acquired, but it holds the lock and will not release it.

A reentrant lock will allow a thread to acquire the same lock again if it has already acquired it.
This allows the thread to execute critical sections from within critical sections, as long as they are protected
by the same reentrant lock.

Each time a thread acquires the lock it must also release it, meaning that there are recursive levels of acquire and
release for the owning thread. As such, this type of lock is sometimes called a recursive mutex lock.

*** DIFFERENCES ***

A threading.Lock can only be acquired once, and once acquired it cannot be acquired again by the same thread or
any other thread until it has been released.

A threading.RLock can be acquired more than once by the same thread, although once acquired by a thread it
cannot be acquired by a different thread until it is been released.

Importantly, each time the threading.RLock is acquired by the same thread it must be released the same number of
times until it is available to be acquired again by a different thread.
his means that the number of calls to acquire() must have the same number of calls to release() for the RLock to
return to the unlocked state.
"""

import time
import random
from threading import Thread
from threading import RLock


def run_subtask(lock, job_name):
    # acquire the lock
    with lock:
        print(f"{job_name} subtask completed!")


def task(lock, job_name):
    # acquire the lock
    with lock:
        sleep_time = random.randint(1, 3)
        print(f"{job_name} running for {sleep_time} seconds...")
        time.sleep(sleep_time)
        run_subtask(lock, job_name)


lock = RLock()
for i in range(10):
    t = Thread(target=task, args=(lock, f"JOB-{i}"))
    t.start()
