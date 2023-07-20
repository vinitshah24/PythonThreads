"""
Latch:
A latch, often referred to as a "CountDownLatch," is a synchronization primitive that allows one or more threads to
wait until a certain number of operations or events have occurred before proceeding. It's like a countdown mechanism.
The latch is initialized with a count, and each time an event occurs, the count is decremented.
Threads can wait for the latch to reach zero, at which point they will be released and can proceed with their tasks.

In summary, latches and barriers are both useful for thread synchronization, but they have different use cases.
Latches are designed to wait for a certain number of events to occur before allowing threads to proceed,
while barriers wait for a specific number of threads to reach a certain point in their execution before letting
them continue.
"""

import threading

latch = threading.Event()


def worker():
    print("Worker is waiting.")
    latch.wait()
    print("Worker is released and can proceed with its task.")


# Main thread
print("Main thread is initializing...")
# Set the latch count to 1 (one event needs to happen).
latch.set()

# Start the worker thread.
thread = threading.Thread(target=worker)
thread.start()

# Simulate an event happening.
# Decrease the latch count by 1.
latch.clear()

# Wait for the worker thread to complete its task.
thread.join()

print("Main thread continues.")
