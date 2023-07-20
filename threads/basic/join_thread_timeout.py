from time import sleep
from threading import Thread


def task(runtime=5):
    sleep(runtime)
    print(f"Child: Task completed after {runtime} seconds")


thread = Thread(target=task)
thread.start()
print("Main: Waiting for child thread to terminate...")
thread.join(timeout=2)
print("Timeout occurred for join")

"""
The new thread continues to execute and then reports its messages before terminating itself.
Note, the Python interpreter will only terminate when there are no non-daemon threads running,
not when the main thread exits. The new thread we created is a non-daemon thread, as is the main thread.
"""

if thread.is_alive():
    print("Main: The target thread is still running")
else:
    print("Main: The target thread has terminated")
