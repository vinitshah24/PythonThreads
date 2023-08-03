from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Pipe


def generate_send(connection, user, value):
    # generate value
    new_value = random()
    # block
    sleep(new_value)
    # update value
    value = value + new_value
    # report
    print(f'{user} sending {value}', flush=True)
    # send value
    connection.send(value)



def ping_pong(connection, user, send_first):
    # ping pong between processes
    print(f'{user} Process Running', flush=True)
    # check if this process should seed the process
    if send_first:
        generate_send(connection, user, 0)
    # run until limit reached
    while True:
        # read a value
        value = connection.recv()
        # report
        print(f'{user} received {value}', flush=True)
        # send the value back
        generate_send(connection, user, value)
        # check for stop
        if value > 10:
            break
    print('Process Done', flush=True)


# entry point
if __name__ == '__main__':
    # create the pipe
    conn1, conn2 = Pipe(duplex=True)
    # create players
    player1 = Process(target=ping_pong, args=(conn1, "User1", True))
    player2 = Process(target=ping_pong, args=(conn2, "User2", False))
    # start players
    player1.start()
    player2.start()
    # wait for players to finish
    player1.join()
    player2.join()
