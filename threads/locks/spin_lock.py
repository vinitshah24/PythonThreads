"""
A spinlock is a busy wait for a mutual exclusion (mutex) lock.
Busy waiting, also called spinning, refers to a thread that repeatedly checks a condition.
It is referred to as “busy” or “spinning” because the thread continues to execute the same code,
such as an if-statement within a while-loop, achieving a wait by executing code (e.g. keeping busy).

Busy Wait: When a thread “waits” for a condition by repeatedly checking for the condition in a loop.
Busy waiting is typically undesirable in concurrent programming as the tight loop of checking a condition consumes
CPU cycles unnecessarily, occupying a CPU core. As such, it is sometimes referred to as an anti-pattern of concurrent
programming, a pattern to be avoided.


"""

from time import sleep
from threading import Thread
from threading import Lock

# target function
def task(lock, job):
    sleep(1)
    while True:
        print(f'{job} trying to acquire the lock...')
        # acquired = lock.acquire(blocking=False)
        acquired = lock.acquire(blocking=True, timeout=0.5)
        if acquired:
            print(f"{job} acquired the lock!")
            lock.release()
            break

# Create the mutex lock
lock = Lock()
thread = Thread(target=task, args=(lock, "Job-1"))
thread.start()

print('Main thread acquiring lock...')
with lock:
    sleep(5)
    print('Main thread completed successfully!')
