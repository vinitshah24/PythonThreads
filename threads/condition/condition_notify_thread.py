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
    sleep_time = random.randint(1, 4)
    print(f"Running {job} for {sleep_time} seconds")
    sleep(sleep_time)
    work_list.append({"job": job, "task_time": sleep_time})
    with condition:
        print(f"Condition acquired by {job} for {sleep_time} seconds")
        sleep(sleep_time)
        # notify a waiting thread that the work is done
        condition.notify()
        print(f"Thread {job} notified of completed job!")


threads = []
work_list = []
print("Running jobs...")
condition = Condition()
with condition:
    for i in range(1, 5):
        t = Thread(target=task, args=(f"JOB-{i}", condition, work_list))
        t.start()
        threads.append(t)
    print("Main thread waiting for condition")
    # Even if the main thread acquires the condition before child, it is not notifying so nothing will change
    # on how the threads execute (which is each child thread will run one by one as it gets chance to
    # acquire the condition and notify so other thread can work and notify)
    condition.wait()
    print("Main thread acquired the lock for condition")

for thread in threads:
    print(f"Joining thread {thread.name}...")
    thread.join()
for task in work_list:
    print(task)

"""
You cannot call join() on a thread that has already completed in the Python threading module.
If you attempt to do so, nothing will happen because the join() method is used to block the calling thread until the
target thread has finished executing.
When a thread completes its execution, it enters the "dead" state, and it cannot be restarted or joined again.
Once a thread is finished, calling join() on it will have no effect. The join() method is typically used to wait
for a thread to finish its execution before continuing with the rest of the code in the calling thread.
If you try to call join() on a completed thread, the method will return immediately, and the program will continue
without any further delay or synchronization with the completed thread.
"""
