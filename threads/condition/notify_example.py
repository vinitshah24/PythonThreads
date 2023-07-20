"""
notify(): This method wakes up a single thread that is waiting on the condition.
If multiple threads are waiting, only one of them will be awakened.
The choice of which thread to wake is arbitrary and may vary between different runs of the program.
It is important to note that the awakened thread does not automatically acquire the lock associated with Condition object.

The thread will need to re-acquire the lock before it can proceed.
In this example, the consumer thread waits until the SHARED_VARIABLE reaches a value of 5.
The producer thread updates the SHARED_VARIABLE and calls condition.notify() to wake up the consumer thread.
"""

import threading

# Create a Condition object
condition = threading.Condition()

# Shared variable
SHARED_VARIABLE = 0


def consumer(job):
    global SHARED_VARIABLE
    with condition:
        while SHARED_VARIABLE < 5:
            condition.wait()  # Wait until SHARED_VARIABLE is updated
        print(f"Consumer {job}: SHARED_VARIABLE = {SHARED_VARIABLE}")


def producer():
    global SHARED_VARIABLE
    with condition:
        SHARED_VARIABLE = 5
        # Wake up one waiting thread
        print(f"Producer: Notifying...")
        condition.notify()


# Create and start the threads
consumer_thread = threading.Thread(target=consumer, args=(f"JOB1",))
consumer_thread.start()

producer_thread = threading.Thread(target=producer)
producer_thread.start()
