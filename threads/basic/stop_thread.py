from time import sleep
from threading import Thread
from threading import Event


class CustomThread(Thread):
    # constructor
    def __init__(self, event):
        # call the parent constructor
        super(CustomThread, self).__init__()
        # store the event
        self.event = event

    # execute task
    def run(self):
        # execute a task in a loop
        for i in range(5):
            # block for a moment
            sleep(1)
            # check for stop
            if self.event.is_set():
                break
            # report a message
            print('Worker thread running...')
        print('Worker closing down')


# create the event
event = Event()
# create a new thread
thread = CustomThread(event)
# start the new thread
thread.start()
# block for a while
sleep(3)
# stop the worker thread
print('Main stopping thread')
event.set()
# wait for the new thread to finish
thread.join()
