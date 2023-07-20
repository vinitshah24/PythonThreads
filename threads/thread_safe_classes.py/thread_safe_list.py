from threading import Thread
from threading import Lock


class ThreadSafeList():

    def __init__(self):
        self._list = list()
        self._lock = Lock()

    def append(self, value):
        # acquire the lock
        with self._lock:
            # append the value
            self._list.append(value)

    # remove and return the last value from the list
    def pop(self):
        # acquire the lock
        with self._lock:
            # pop a value from the list
            return self._list.pop()

    def get(self, index):
        # acquire the lock
        with self._lock:
            # read a value at the index
            return self._list[index]

    def length(self):
        # acquire the lock
        with self._lock:
            return len(self._list)


def add_items(safe_list):
    for i in range(100000):
        safe_list.append(i)


safe_list = ThreadSafeList()
threads = [Thread(target=add_items, args=(safe_list,)) for i in range(10)]
for thread in threads:
    thread.start()
print('Main waiting for threads...')
for thread in threads:
    thread.join()

print(f'List size: {safe_list.length()}')
