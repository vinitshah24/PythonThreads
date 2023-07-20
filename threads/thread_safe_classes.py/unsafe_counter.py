from threading import Thread


class ThreadUnsafeCounter():
    """ Thread unsafe counter class """

    def __init__(self):
        # initialize counter
        self._counter = 0

    def increment(self):
        self._counter += 1

    def get_count(self):
        return self._counter


def task(counter):
    """ Task executed by threads """
    # increment the counter
    for _ in range(100000):
        counter.increment()


# create the counter
counter = ThreadUnsafeCounter()
# create 10 threads to increment the counter
threads = [Thread(target=task, args=(counter,)) for _ in range(10)]
# start all threads
for thread in threads:
    thread.start()
# wait for all threads to finish
for thread in threads:
    thread.join()
# report the counter
print(counter.get_count())
