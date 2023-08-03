from multiprocessing import Process
rom time import sleep


def task():
    # execute a task in a loop
    while True:
        # block for a moment
        sleep(1)
        # report a message
        print('Worker process running...', flush=True)


if __name__ == '__main__':
    # create a process
    process = Process(target=task)
    # run the process
    process.start()
    # wait for a moment
    sleep(5)
    # terminate the process
    process.terminate()
    # continue on...
    print('Parent is continuing on...')
