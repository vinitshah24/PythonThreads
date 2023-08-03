from multiprocessing.shared_memory import SharedMemory
from multiprocessing import Process


def task(shared_mem):
    # write some integer data to the shared memory
    shared_mem.buf[:5] = bytearray([1, 2, 3, 4, 5])
    # close as no longer needed
    shared_mem.close()


# protect the entry point
if __name__ == '__main__':
    # create a shared memory
    shared_mem = SharedMemory(create=True, size=100)
    # create a child process
    process = Process(target=task, args=(shared_mem,))
    # start the child process
    process.start()
    # wait for the child process to finish
    process.join()
    # report the shared memory
    data = [int(shared_mem.buf[i]) for i in range(5)]
    print(data)
    # close the shared memory
    shared_mem.close()
    # release the shared memory
    shared_mem.unlink()
