""""
The task_done() function is used in Python"s queue module, specifically in the Queue and PriorityQueue classes,
to indicate that a task has been completed. It is typically used in scenarios where multiple threads or processes
are working on a shared queue of tasks, and it helps in coordinating the work and ensuring that all tasks are
processed before the program exits.

When a thread or process completes a task that it has taken from the queue, it calls the task_done() method to notify
the queue that the task has been processed. This is crucial for the join() method of the queue, which can be used by
the main thread or process to wait until all tasks are completed before proceeding further.

Here"s how the task_done() method works:
    1. Before starting to process the tasks, you need to call the queue.join() method.
        This method will block until all tasks in the queue have been processed and marked as done.
    2. When you add a task to the queue using the put() method, the queue"s internal counter for the number of tasks
        in the queue is increased.
    3. After a thread or process retrieves a task from the queue using the get() method and processes it,
        it should call task_done() to signal that the task has been completed.
    4. When task_done() is called, the queue"s internal counter is decreased to reflect the completion of a task.
    5. The queue.join() method waits until the internal counter becomes zero, indicating that all tasks have been
        processed.

Using the task_done() method in combination with queue.join() ensures that your program does not exit prematurely before all tasks in the queue have been processed, which is particularly important in multithreaded or multiprocessing scenarios.
"""

from time import sleep
from random import random
from threading import Thread
from queue import Queue


def producer(id, queue):
    print("Producer: Running")
    for i in range(10):
        sleep(random())
        queue.put(f"Producer-{id}: {i}")
    print(f"Producer-{id}: Done")


def consumer(queue):
    print("Consumer: Running")
    while True:
        item = queue.get()
        print(f"Consumer: Processing {item}")
        queue.task_done()


# create the shared queue
queue = Queue(2)
# start the consumer
consumer = Thread(target=consumer, args=(queue,), daemon=True)
consumer.start()
# start 5 producers
producers = [Thread(target=producer, args=(_, queue,)) for _ in range(5)]
for producer in producers:
    producer.start()
# wait for all producers to finish
for producer in producers:
    producer.join()
# wait for all work to be processed
queue.join()
