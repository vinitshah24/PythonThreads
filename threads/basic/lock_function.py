from time import sleep
from threading import Thread
from threading import Lock


def task():
    # declare scope of global lock variable
    global lock
    # acquire the lock
    with lock:
        # block for a moment
        sleep(1)


lock = Lock()
thread = Thread(target=task)
thread.start()
thread.join()
