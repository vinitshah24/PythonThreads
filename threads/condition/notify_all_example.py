"""
notify_all(): This method wakes up all threads that are waiting on the condition.
All waiting threads will be awakened and can proceed concurrently.
Like notify(), the awakened threads do not automatically acquire the lock associated with the Condition object.

In this example, there are two consumer threads waiting for the shared_variable to reach a value of 5.
The producer thread updates the shared_variable and calls condition.notify_all() to wake up all waiting consumer threads.
By using notify() or notify_all(), you can control which threads are awakened and resume their execution
based on the conditions you define in your program.
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
            # Wait until SHARED_VARIABLE is updated
            condition.wait()
        print(f"Consumer {job}: SHARED_VARIABLE =", SHARED_VARIABLE)


def producer():
    global SHARED_VARIABLE
    with condition:
        SHARED_VARIABLE = 5
        # Wake up all waiting threads
        condition.notify_all()


# Create and start the threads
consumer_thread1 = threading.Thread(target=consumer, args=(f"JOB1",))
consumer_thread2 = threading.Thread(target=consumer, args=(f"JOB2",))
producer_thread = threading.Thread(target=producer)
consumer_thread1.start()
consumer_thread2.start()
producer_thread.start()
