import threading
import time
import datetime
import random
from queue import Queue
import time
import threading


def run_job(q, stop_threads):
    while not q.empty() and not stop_threads():
        try:
            value = q.get()
            runtime = random.randint(6, 8)
            run_dict = {
                "id": value,
                "start_time": datetime.datetime.utcnow().isoformat(),
                "runtime": runtime,
                "end_time": None
            }
            time.sleep(runtime)
            print(f"Completed task {value} after {runtime} seconds")
        except:
            print("Caught Exception")
            run_dict["end_time"] = datetime.datetime.utcnow().isoformat()
        finally:
            if run_dict["end_time"] is None:
                run_dict["end_time"] = datetime.datetime.utcnow().isoformat()
            RESULT.append(run_dict)
            q.task_done()
    if stop_threads():
        print("Timed Out. Exiting")
        # Clears the queue
        while not q.empty():
            val = q.get()
            print(f"Killing future threads {val}")
            q.task_done()
        return True


try:
    jobQueue = Queue()
    RESULT = []
    global_timeout = 6
    threads_count = 5
    job_count = 10
    stop_threads = False
    timeout_start = time.time()
    for job in range(job_count):
        jobQueue.put(job)
    threads = []
    for _ in range(threads_count):
        worker = threading.Thread(target=run_job,
                                  args=(jobQueue, lambda: stop_threads))
        threads.append(worker)
    for worker in threads:
        worker.start()
    print(f"Waiting for {jobQueue.qsize()} tasks to complete...")
    time.sleep(global_timeout)
    print(f"Timeout occurred after {global_timeout} secs")
    stop_threads = True
    jobQueue.join()
    for thread in threads:
        thread.join()
except KeyboardInterrupt:
    stop_threads = True
    jobQueue.join()
finally:
    print(f"Total Runtime: {time.time() - timeout_start}")
    for item in RESULT:
        print(item)
