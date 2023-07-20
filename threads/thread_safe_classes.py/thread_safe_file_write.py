from random import random
from threading import Thread
from threading import Lock


def task(number, file, lock):
    # task loop
    for i in range(1000):
        # generate random number between 0 and 1
        value = random()
        # write to the file
        with lock:
            file.write(f'Thread {number} got {value}.\n')


# create the shared lock
lock = Lock()
# defile the shared file path
filepath = 'output.txt'
# open the file
file = open(filepath, 'a')
# configure many threads
threads = [Thread(target=task, args=(i, file, lock)) for i in range(1000)]
# start threads
for thread in threads:
    thread.start()
# wait for threads to finish
for thread in threads:
    thread.join()
# close the file
file.close()
