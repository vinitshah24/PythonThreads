from multiprocessing import Process
from multiprocessing import Value

# define a counter
class SafeCounter():
    # constructor
    def __init__(self):
        # initialize counter
        self._counter = Value('i', 0)

    # increment the counter
    def increment(self):
        # get the lock
        with self._counter.get_lock():
            self._counter.value += 1

    # get the counter value
    def value(self):
        # get the lock
        with self._counter.get_lock():
            return self._counter.value

# task executed by processes
def task(counter):
    # increment the counter
    for _ in range(100000):
        counter.increment()

# protect the entry point
if __name__ == '__main__':
    # create the shared counter
    counter = SafeCounter()
    # create 10 processes to increment the counter
    processes = [Process(target=task, args=(counter,)) for _ in range(10)]
    # start all processes
    for process in processes:
        process.start()
    # wait for all processes to finish
    for process in processes:
        process.join()
    # report the value of the counter
    print(counter.value())