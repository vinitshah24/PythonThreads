"""
In multiprocessing, a pipe is a connection between two processes in Python.
It is used to send data from one process which is received by another process.

Under the covers, a pipe is implemented using a pair of connection objects, provided by the
multiprocessing.connection.Connection class.

Creating a pipe will create two connection objects, one for sending data and one for receiving data.
A pipe can also be configured to be duplex so that each connection object can both send and receive data.
"""

from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Pipe

# generate work
def sender(connection):
    print('Sender: Running', flush=True)
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block
        sleep(value)
        # send data
        connection.send(value)
    # all done
    connection.send(None)
    print('Sender: Done', flush=True)

# consume work
def receiver(connection):
    print('Receiver: Running', flush=True)
    # consume work
    while True:
        # get a unit of work
        item = connection.recv()
        # report
        print(f'>receiver got {item}', flush=True)
        # check for stop
        if item is None:
            break
    # all done
    print('Receiver: Done', flush=True)

# entry point
if __name__ == '__main__':
    # create the pipe
    conn1, conn2 = Pipe()
    # start the sender
    sender_process = Process(target=sender, args=(conn2,))
    sender_process.start()
    # start the receiver
    receiver_process = Process(target=receiver, args=(conn1,))
    receiver_process.start()
    # wait for all processes to finish
    sender_process.join()
    receiver_process.join()