"""
The multiprocessing.JoinableQueue class extends the multiprocessing.Queue class.
This means it provides the same functionality, such as adding items to the queue via put() and getting items from the queue via get().

The multiprocessing.JoinableQueue class offers two additional methods for joining a queue and marking items on the
queue as done.

An object added to a queue by representing a task or a unit of work.
When a consumer process calls get() to retrieve the item from the queue,
it may need to do additional work to it before the task is considered complete.

Once complete, the process may then call the task_done() method on the queue to indicate that the item that was just
retrieved has been completely processed.
"""

from time import sleep
from random import random
from multiprocessing import JoinableQueue
from multiprocessing import Process


def producer(queue):
    print('Producer starting', flush=True)
    # add tasks to the queue
    for i in range(10):
        # generate a task
        task = (i, random())
        print(f'.producer added {task}', flush=True)
        # add it to the queue
        queue.put(task)
    # send a signal that no further tasks are coming
    queue.put(None)
    print('Producer finished', flush=True)


def consumer(queue):
    print('Consumer starting', flush=True)
    # process items from the queue
    while True:
        # get a task from the queue
        task = queue.get()
        # check for signal that we are done
        if task is None:
            break
        # process the item
        sleep(task[1])
        print(f'.consumer got {task}', flush=True)
        # mark the unit of work as processed
        queue.task_done()
    # mark the signal as processed
    queue.task_done()
    print('Consumer finished', flush=True)


if __name__ == '__main__':
    # create the shared queue
    queue = JoinableQueue()
    # create and start the producer process
    producer_process = Process(target=producer, args=(queue,))
    producer_process.start()
    # create and start the consumer process
    consumer_process = Process(target=consumer, args=(queue,))
    consumer_process.start()
    # wait for the producer to finish
    producer_process.join()
    print('Main found that the producer has finished', flush=True)
    # wait for the queue to empty
    queue.join()
    print('Main found that all tasks are processed', flush=True)
