"""
The ShareableList does guarantee process safety. Use below code to make it process safe.
"""

from multiprocessing.shared_memory import ShareableList
from multiprocessing import Process
from multiprocessing import Lock


def task(sl, lock):
    # increment values in the shareable list
    for i in range(100):
        for j in range(len(sl)):
            # acquire the lock before the change
            with lock:
                # get the current value
                val = sl[j]
                # update the value
                val = val + 1
                # store the new value
                sl[j] = val


# protect the entry point
if __name__ == '__main__':
    # create a shared lock
    lock = Lock()
    # create a shared list
    sl = ShareableList([0, 0, 0, 0, 0])
    # create processes
    processes = [Process(target=task, args=(sl, lock)) for i in range(10)]
    # start processes
    for process in processes:
        process.start()
    # wait for processes to finish
    for process in processes:
        process.join()
    # report the shared list
    print(sl)
    # close the shared memory
    sl.shm.close()
    # release the shared memory
    sl.shm.unlink()
