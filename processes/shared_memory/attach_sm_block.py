"""
Running the example first creates the shared memory.
The child process is then created and configured to run our custom function.
The child process does not pass the shared memory as an argument.
The main process starts the child process and waits for it to complete.
The child process runs and first attaches to the shared memory.
It then stores a string in the shared memory and terminates.

The main process resumes and retrieves the bytes data from the shared memory and decodes it into a string,
then reports it.

We can see that the reported string matches the string that was stored in the child process.
The shared memory is then closed and released.
This highlights how we can attach to shared memory from another process by name alone.
"""

from multiprocessing.shared_memory import SharedMemory
from multiprocessing import Process

def task():
    # attach another shared memory block
    sm = SharedMemory('MyMemory')
    # store data in the first shared memory block
    sm.buf[:11] = b'Hello world'
    # close as no longer needed
    sm.close()

# protect the entry point
if __name__ == '__main__':
    # create a shared memory
    shared_mem = SharedMemory(name='MyMemory', create=True, size=100)
    # create a child process
    process = Process(target=task)
    # start the child process
    process.start()
    # wait for the child process to finish
    process.join()
    # report the data in the shared memory
    print(bytes(shared_mem.buf[:11]).decode())
    # close the shared memory
    shared_mem.close()
    # release the shared memory
    shared_mem.unlink()