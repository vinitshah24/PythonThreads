from time import sleep
from random import random
from threading import Thread
from threading import Condition


def task(condition, data):
    # block for a moment
    sleep(4)
    # wait for data
    with condition:
        print('Child thread waiting on condition')
        condition.wait()
    print(f'Thread received data: {data}')


condition = Condition()
data = list()
thread = Thread(target=task, args=(condition, data))
thread.start()
sleep(3)

# acquire the condition
with condition:
    # store data
    data.append('We did it!')
    # notify waiting threads
    print('Main is notifying')
    # Runtime error will be raised because the child thread has not acquired the lock before notify was called
    condition.notify()

# condition.acquire()
# data.append('We did it!')
# print('Main is notifying')
# condition.notify()
# condition.release()
