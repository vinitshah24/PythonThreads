from threading import Thread
import threading
import time
import random


class CustomThread(Thread):

    def __init__(self, job_name):
        super(CustomThread, self).__init__()
        self.job_name = job_name

    def run(self):
        print(f"Starting {self.job_name}")
        wait_time = random.randint(1, 5)
        time.sleep(wait_time)
        print(f"Completed {self.job_name} after {wait_time} seconds")


threads = []
for i in range(1, 3):
    thread = CustomThread(f"Job-{i}")
    thread.name = f"CustomThread-{i}"
    thread.start()
    threads.append(thread)

for thread in threading.enumerate():
    print(f"{thread.name} is alive {thread.is_alive()}")

for t in threads:
    t.join()

for thread in threading.enumerate():
    print(f"{thread.name} is alive {thread.is_alive()}")

print("Completed running jobs!")
