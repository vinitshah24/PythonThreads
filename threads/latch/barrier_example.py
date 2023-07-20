"""
Barrier:
A barrier is another synchronization primitive that allows a set of threads to wait for each other at a specific point
in their execution before continuing. It's often used to ensure that multiple threads reach a certain stage of their
execution simultaneously before proceeding.
"""

import threading

barrier = threading.Barrier(3)  # Set the number of threads required to pass the barrier.


def worker():
    print("Worker is waiting at the barrier.")
    barrier.wait()
    print("Worker passed the barrier and continues its task.")


# Main thread
print("Main thread is initializing...")

# Start three worker threads.
threads = [threading.Thread(target=worker) for _ in range(3)]
for thread in threads:
    thread.start()

# Wait for all worker threads to reach the barrier before continuing.
for thread in threads:
    thread.join()

print("Main thread continues.")
