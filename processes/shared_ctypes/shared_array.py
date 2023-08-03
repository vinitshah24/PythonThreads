from random import randint
from multiprocessing import Array
from multiprocessing import Process

# function to execute in a child process
def task(int_arr):
    # store new values in array
    for i in range(len(int_arr)):
        int_arr[i] = randint(0, 100)
    # read the items in the array into a list
    data = [item for item in int_arr]
    # report progress
    print(f'Wrote: {data}', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create shared array
    int_arr = Array('i', (1, 2, 3, 4, 5))
    # read the items in the array into a list
    data = [item for item in int_arr]
    print(f'Initialized: {data}')
    # create a child process process
    process = Process(target=task, args=(int_arr,))
    # start the process
    process.start()
    # wait for the process to finish
    process.join()
    # read the items in the array into a list
    data = [item for item in int_arr]
    # report the value
    print(f'Read: {data}')