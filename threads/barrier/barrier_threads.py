"""
A barrier is a synchronization primitive.
It allows multiple threads to wait on the same barrier object instance (e.g. at the same point in code)
until a predefined fixed thread_num of threads arrive (e.g. the barrier is full),
after which all threads are then notified and released to continue their execution.

Internally, a barrier maintains a count of the thread_num of threads waiting on the barrier and a configured maximum
thread_num of parties (threads) that are expected. Once the expected thread_num of parties reaches the pre-defined maximum,
all waiting threads are notified. This provides a useful mechanism to coordinate actions between multiple threads.
"""
from time import sleep
import random
from threading import Thread
from threading import Barrier


def task(barrier, thread_num):
    value = random.randint(1, 4)
    sleep(value)
    print(f"Thread-{thread_num} completed after {value} seconds")
    # wait on all other threads to complete
    barrier.wait()

# We need one party for each thread we intend to create, five in this place,
# as well as an additional party for the main thread that will also wait for all threads to reach the barrier.
barrier = Barrier(5 + 1)

for i in range(5):
    thread = Thread(target=task, args=(barrier, i))
    thread.start()

# wait for all threads to finish
print("Main thread waiting on all results...")
barrier.wait()
print("All threads completed execution!")
