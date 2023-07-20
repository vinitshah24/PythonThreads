from time import sleep
from random import random
from threading import Thread
from queue import SimpleQueue
from queue import Empty

# generate work
def producer(queue):
    print("Producer: Running")
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block
        sleep(value)
        # add to the queue
        queue.put(value)
    # all done
    queue.put(None)
    print("Producer: Done")

# consume work
def consumer(queue):
    print("Consumer: Running")
    # consume work
    while True:
        # get a unit of work
        try:
            item = queue.get(timeout=0.5)
        except Empty:
            print("Consumer: gave up waiting...")
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f">got {item}")
    # all done
    print("Consumer: Done")

# create the shared queue
queue = SimpleQueue()
# start the consumer
consumer = Thread(target=consumer, args=(queue,))
consumer.start()
# start the producer
producer = Thread(target=producer, args=(queue,))
producer.start()
# wait for all threads to finish
producer.join()
consumer.join()