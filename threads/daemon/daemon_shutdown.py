from time import sleep
from threading import Thread
from threading import Event
import atexit


def task(event):
    while not event.is_set():
        sleep(2)
        print("Daemon Thread: Running task...")
    print("Daemon Thread: Task completed successfully!")


def stop_background(stop_event, thread):
    print("Stopping background threads")
    stop_event.set()
    thread.join()
    print("Background threads stopped successfully!")


stop_event = Event()
thread = Thread(target=task, args=(stop_event,), daemon=True, name="Background")
thread.start()
atexit.register(stop_background, stop_event, thread)
sleep(10)
print("Main thread completed successfully!")
