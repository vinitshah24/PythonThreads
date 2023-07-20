from time import sleep
from threading import Thread, Condition


def task(condition, data):
    sleep(4)
    # Wait for data to arrive from main thread
    while True:
        with condition:
            # Here even though the condition was missed out by child thread, it will end if condition was met
            print('Child thread waiting on condition')
            if len(data) > 0:
                print(f"Data: {data}")
                break
        print("Sleeping for 2 seconds while waiting for condition")
        sleep(2)


condition = Condition()
data = list()

thread = Thread(target=task, args=(condition, data))
thread.start()
sleep(2)
with condition:
    data.append('Processing completed')
    print('Main thread notifying waiting threads...')
    # condition.notify()
    condition.notify_all()

