"""
A daemon thread is a thread that will not keep running if the rest of the script has stopped and
there are no more non-daemon threads left. We can tell the main thread is non-daemon as it is not abruptly
stopped when it's the only thread running.
This means setting a threads daemon value to True will mean that it will not keep running after the main thread has
finished (or other non-daemon threads); we can set daemon to False to make sure the thread keeps running even
when the main thread finishes.

Best example of a daemon thread is Garbage Collector because assume that the main thread
is executing or running, at that time any memory problem occurs then immediately python virtual machine (PVM) is
going to execute Garbage Collector. The Garbage Collector is going to execute in the background and destroy all
the useless objects and then free memory by default will be provided, once there is free memory will available
then the main thread is going to be executed without any problem.
"""

from threading import Thread
import random
import time


def run_job():
    for i in range(1, 5):
        print(f"Running job {i}")
        time.sleep(3)

# Without daemon, the script will wait for the entire job iterations to complete
# With daemon, the script will not wait for job to complete and will end as soon as main thread finishes (script end)

# thread = Thread(target=run_job)
thread = Thread(target=run_job, daemon=True)
thread.start()
time.sleep(5)
print("Run completed!")
