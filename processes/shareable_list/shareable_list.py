"""
A multiprocessing.shared_memory.ShareableList is a list that can be shared efficiently between multiple processes.

Shared between processes means that changes made to the list in one process will be visible and accessible in
another process.

It is backed by a shared memory block and can be used to store up to 10 megabytes of data as any of Python's primitive
types, e.g. integers, floats, and strings.

Provides a mutable list-like object where all values stored within are stored in a shared memory block.
This constrains storable values to only the int, float, bool, str (less than 10M bytes each), bytes
(less than 10M bytes each), and None built-in data types.

— MULTIPROCESSING.SHARED_MEMORY — SHARED MEMORY FOR DIRECT ACCESS ACROSS PROCESSES
Unlike the built-in list type, the size of the ShareableList cannot be changed after it is created.
Additionally, many of the operations that a regular list support are not supported on the ShareableList.

It also notably differs from the built-in list type in that these lists can not change their overall length
(i.e. no append, insert, etc.) and do not support the dynamic creation of new ShareableList instances via slicing.

— MULTIPROCESSING.SHARED_MEMORY — SHARED MEMORY FOR DIRECT ACCESS ACROSS PROCESSES
The ShareableList can be used as an alternative of a list hosted server process via a multiprocessing.Manager and
as an alternative to a shared ctype Array.
"""

from multiprocessing import Process
from multiprocessing.shared_memory import ShareableList


def task(sl):
    # report the shared list
    print(sl)
    # change the list
    for i in range(len(sl)):
        sl[i] = sl[i] * 10


# protect the entry point
if __name__ == '__main__':
    # create a shared list
    sl = ShareableList([1, 2, 3, 4, 5])
    # report the shared list
    print(sl)
    # create a child process
    process = Process(target=task, args=(sl,))
    # start the child process
    process.start()
    # wait for the child process to finish
    process.join()
    # report the shared list
    print(sl)
    # close the shared memory
    sl.shm.close()
    # release the shared memory
    sl.shm.unlink()
