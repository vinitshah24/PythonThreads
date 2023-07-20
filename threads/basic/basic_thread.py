from threading import Thread
import threading
import random
import time


def run_job(job):
    print(f"Starting job {job}")
    wait_time = random.randint(1, 3)
    time.sleep(wait_time)
    print(f"Completed {job} after {wait_time} seconds")


main_thread = threading.main_thread()
print(f"MAIN THREAD: name={main_thread.name}, daemon={main_thread.daemon}, id={main_thread.ident}")

threads = []
for i in range(1, 3):
    thread = Thread(target=run_job, args=(f"Job-{i}",))
    threads.append(thread)

# This is asynchronous so it will not block until the job finishes
# MAIN thread will not exit until the child threads complete
for t in threads:
    t.start()

print("Waiting for child threads to finish...")

for t in threads:
    t.join()

# Completed Job-2 after 1 seconds
# Completed Job-1 after 1 seconds
# Completed running jobs!

print("Completed running jobs!")
