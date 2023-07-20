"""
A mutual exclusion lock or mutex lock is a synchronization primitive intended to prevent a race condition.

A race condition is a concurrency failure case when two threads run the same code and access or update the same
resource (e.g. data variables, stream, etc.) leaving the resource in an unknown and inconsistent state.
Race conditions often result in unexpected behavior of a program and/or corrupt data.

These sensitive parts of code that can be executed by multiple threads concurrently and may result in race conditions
are called critical sections. A critical section may refer to a single block of code,
but it also refers to multiple accesses to the same data variable or resource from multiple functions.

A mutex lock can be used to ensure that only one thread at a time executes a critical section of code at a time,
while all other threads trying to execute the same code must wait until the currently executing thread is finished
with the critical section.

Each thread must attempt to acquire the lock at the beginning of the critical section.
If the lock has not been obtained, then a thread will acquire it and other threads must wait until the thread
that acquired the lock releases it.
"""

import time
import random
from threading import Thread, current_thread
from threading import Lock


def run_job(lock, job):
    print(f"Starting {job}...")
    # Check if a lock is currently acquired
    if lock.locked():
        print(f"Lock is already acquired. {job} waiting for execution...")
    # Acquires the lock and release after end of the block | lock.acquire() & lock.release()
    with lock:
        sleep_time = random.randint(1, 5)
        print(f'{current_thread().name}: {job} acquired the lock. Sleeping for {sleep_time} seconds.')
        time.sleep(sleep_time)
        print(f"{job} completed the execution.")

threads = []
# Create a shared lock
lock = Lock()
for i in range(1, 6):
    t = Thread(target=run_job, args=(lock, f"Job-{i}"))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
