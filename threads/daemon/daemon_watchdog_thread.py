"""
A watchdog thread is a thread that monitors another resource and takes action if a change or failure is detected.

Generally, a watchdog may monitor any resource, although when we are describing watchdog threads,
the resource is typically directly relevant to the parent application.

A watchdog may monitor a resource within the application, such as:
- Another thread, such as a worker thread.
- Data, such as data structures in memory.
- Program state, such as global or instance variables.

A watchdog may also monitor an external resource, perhaps on which the application is dependent, such as:
- A server, e.g. webserver, fileserver, etc.
- A file or directory, e.g. for change.
- A database, e.g. for accessibility.
- A watchdog thread will typically monitor the resource using polling.
  This means checking the status of the resource repeatedly in a loop after an interval of time.

If a fault or problem with the monitored resource is detected, then the watchdog thread will take action,
depending on the nature of the resource, such as:
- Reporting the fault, e.g. logging.
- Restarting or resuming a task or service.
- Changing the server address, e.g. fail-over.
"""

from time import sleep
from random import random
from threading import Thread


def worker_task():
    """ Task for a worker thread """
    # work forever
    counter = 0
    while True:
        counter += 1
        print(f"Worker: {counter}")
        # conditionally fail
        if random() < 0.3:
            print("Worker: Task Failed")
            break
        sleep(1)


def boot_worker():
    """ Create and start a worker thread, returns instance of thread """
    worker = Thread(target=worker_task, name="Worker")
    worker.start()
    return worker


def watchdog(target, action):
    """ Task for a watchdog thread """
    print("Watchdog running forever...")
    while True:
        # check the status of the target thread
        if not target.is_alive():
            # report fault
            print("Watchdog: target thread is not running, restarting...")
            # restart the target thread
            target = action()
        # block for a moment
        sleep(0.5)


worker = boot_worker()
watchdog = Thread(target=watchdog, args=(worker, boot_worker), daemon=True, name="Watchdog")
# start the watchdog
watchdog.start()
# do other things...
watchdog.join()
