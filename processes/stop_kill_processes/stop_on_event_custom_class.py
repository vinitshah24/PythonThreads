from time import sleep
from multiprocessing import Process
from multiprocessing import Event


class CustomProcess(Process):
    # constructor
    def __init__(self):
        # call the parent constructor
        Process.__init__(self)
        # create and store an event
        self.event = Event()

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
            print('Worker process running...', flush=True)
        print('Worker closing down', flush=True)


# entry point
if __name__ == '__main__':
    # create a new process
    process = CustomProcess()
    # start the new process
    process.start()
    # block for a while
    sleep(3)
    # stop the worker process
    print('Main stopping process')
    process.event.set()
    # wait for the new process to finish
    process.join()
