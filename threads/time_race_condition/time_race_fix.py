from time import sleep
from threading import Thread
from threading import Condition
from threading import Event


def task(condition, event):
    sleep(0.5)
    with condition:
        print("Child Thread: Ready to get notified!")
        event.set()
        print("Child Thread: Waiting to be notified...")
        condition.wait()
    print("Child Thread: Notified")


condition = Condition()
event = Event()

thread = Thread(target=task, args=(condition, event))
thread.start()

print("Main Thread: Waiting for child threads to get ready...")
while not event.is_set():
    sleep(0.1)

with condition:
    print("Main Thread: Notifying child threads...")
    condition.notify()
print("Main thread completed successfully!")
