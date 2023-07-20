from threading import Thread
from threading import Lock


class ThreadSafeCounter:
    # initialize mutex lock as a class variable
    lock = Lock()
    # initialize the counter as a class variable
    counter = 0

    # increment the counter
    @classmethod
    def increment(cls):
        # acquire the lock
        with cls.lock:
            # increment the counter
            cls.counter += 1

    # report the counter value
    @classmethod
    def report(cls):
        # acquire the lock
        with cls.lock:
            # report the counter value
            print(cls.counter)


def task():
    """ Task function to increment the counter in a new thread """
    for i in range(10000):
        ThreadSafeCounter.increment()


threads = [Thread(target=task) for _ in range(1000)]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

ThreadSafeCounter.report()
