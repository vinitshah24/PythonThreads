from random import random
from time import sleep
from multiprocessing import Value
from multiprocessing import Process

# function to execute in a child process


def task(float_var, int_var):
    # generate some data
    data = random()
    # block, to simulate computational effort
    print(f'Generated {data}', flush=True)
    sleep(data)
    # return data via value
    float_var.value = data
    int_var.value = 3


# protect the entry point
if __name__ == '__main__':
    # create shared float_var
    float_var = Value('f', 0.0)
    int_var = Value('i', 0)
    # create a child process process
    process = Process(target=task, args=(float_var, int_var,))
    # start the process
    process.start()
    # wait for the process to finish
    process.join()
    # report return value
    print(f'Returned: {float_var.value}')
    print(f'Returned: {int_var.value}')
