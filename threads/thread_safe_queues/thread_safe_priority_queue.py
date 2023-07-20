from time import sleep
from random import random
from random import randint
from threading import Thread
from queue import PriorityQueue

# generate work


def producer(queue):
    print("Producer: Running")
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # generate a priority
        priority = randint(0, 10)
        # create an item
        item = (priority, value)
        # add to the queue
        queue.put(item)
    # wait for all items to be processed
    queue.join()
    # send sentinel value
    queue.put(None)
    print("Producer: Done")

# consume work


def consumer(queue):
    print("Consumer: Running")
    # consume work
    while True:
        # get a unit of work
        item = queue.get()
        # check for stop
        if item is None:
            break
        # block
        sleep(item[1])
        # report
        print(f">got {item}")
        # mark it as processed
        queue.task_done()
    # all done
    print("Consumer: Done")


# create the shared queue
queue = PriorityQueue()
# start the producer
producer = Thread(target=producer, args=(queue,))
producer.start()
# start the consumer
consumer = Thread(target=consumer, args=(queue,))
consumer.start()
# wait for threads to finish
producer.join()
consumer.join()
