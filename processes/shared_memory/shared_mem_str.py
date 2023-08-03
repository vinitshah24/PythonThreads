"""
The multiprocessing.shared_memory.SharedMemory class allows a block of memory to be used by multiple Python processes.

A SharedMemory object can be created and shared directly among multiple processes, or it can assigned a meaningful
name attached to a process using that name,

Creates a new shared memory block or attaches to an existing shared memory block.
Each shared memory block is assigned a unique name. In this way, one process can create a shared memory block
with a particular name and a different process can attach to that same shared memory block using that same name.
— MULTIPROCESSING.SHARED_MEMORY — SHARED MEMORY FOR DIRECT ACCESS ACROSS PROCESSES

A SharedMemory has a fixed size and stores byte data.

Python types can be converted to arrays of bytes and stored in a SharedMemory and read as arrays of bytes and
converted back into Python types.

It allows processes to read and write from the same memory, which is faster and more efficient than sharing data via
message passing, such as via a multiprocessing.Queue or multiprocessing.Pipe.

Processes are conventionally limited to only have access to their own process memory space but shared memory permits
the sharing of data between processes, avoiding the need to instead send messages between processes containing that data.
Sharing data directly via memory can provide significant performance benefits compared to sharing data via disk or
socket or other communications requiring the serialization/deserialization and copying of data.
— MULTIPROCESSING.SHARED_MEMORY — SHARED MEMORY FOR DIRECT ACCESS ACROSS PROCESSES

Shared Memory Life-Cycle:
1. Create shared memory.
    1a. Attach shared memory.
2. Read/Write shared memory.
3. Close shared memory.
4. Destroy shared memory
"""

from multiprocessing.shared_memory import SharedMemory
from multiprocessing import Process

# task executed in a child process
def task(shared_mem):
    # write some string data to the shared memory
    shared_mem.buf[:24] = b'Hello from child process'
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
    data = bytes(shared_mem.buf[:24]).decode()
    print(data)
    # close the shared memory
    shared_mem.close()
    # release the shared memory
    shared_mem.unlink()