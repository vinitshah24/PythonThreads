from time import sleep
from threading import Thread
from threading import Event


def task(event):
    while not event.is_set():
        sleep(2)
        print("Background performing task")
    print("Background done")


stop_event = Event()
thread = Thread(target=task, args=(stop_event,), daemon=True, name="Background")
thread.start()
print("Main thread running...")
sleep(10)
print("Main thread stopping")
# Request the background thread to stop
stop_event.set()
thread.join()
print("Main thread completed successfully!")
