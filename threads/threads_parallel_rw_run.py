import threading
import time
import datetime
import random
from queue import Queue
import time
import threading


def run_job(q, thread, runType, stop_threads):
    while not q.empty() and not stop_threads():
        try:
            value = q.get()
            runtime = random.randint(1, 3)
            print(f"Session {runType.upper()} Thread {thread} running {value} job")
            run_dict = {
                "id": value,
                "run": runType,
                "start_time": datetime.datetime.utcnow().isoformat(),
                "runtime": runtime,
                "end_time": None
            }
            time.sleep(runtime)
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


if __name__ == '__main__':
    """
    Runs the threads in parallel until the queue is empty or the timeout expires.
    Only the future threads are killed but the already running threads after the timeout are not killed
    rather allowed to complete.
    """
    try:
        readJobQueue = Queue()
        writeJobQueue = Queue()
        RESULT = []
        global_timeout = None
        read_threads_count = 5
        write_threads_count = 1
        job_count = 10
        stop_threads = False
        timeout_start = time.time()
        # READ JOB QUEUE
        for job in range(job_count):
            readJobQueue.put(f"READ-{job}")
        # WRITE JOB QUEUE
        for job in range(job_count):
            writeJobQueue.put(f"WRITE-{job}")
        threads = []
        # ADD READ THREADS
        for thread in range(read_threads_count):
            worker = threading.Thread(target=run_job,
                                      args=(readJobQueue, thread, "READ", lambda: stop_threads))
            threads.append(worker)
        # ADD WRITE THREADS
        for thread in range(write_threads_count):
            worker = threading.Thread(target=run_job,
                                      args=(writeJobQueue, thread, "WRITE", lambda: stop_threads))
            threads.append(worker)
        # START ALL THREADS
        for thread in threads:
            thread.start()
        print(f"Waiting for {readJobQueue.qsize()} read tasks to complete...")
        print(f"Waiting for {writeJobQueue.qsize()} write tasks to complete...")
        if global_timeout is not None:
            time.sleep(global_timeout)
            stop_threads = True
            readJobQueue.join()
            writeJobQueue.join()
        else:
            for thread in threads:
                thread.join()
    except KeyboardInterrupt:
        stop_threads = True
        readJobQueue.join()
        writeJobQueue.join()
    finally:
        print(f"Total Runtime: {time.time() - timeout_start}")
        for item in RESULT:
            if item.get("run") == "READ":
                print(item)
        print("-" * 100)
        for item in RESULT:
            if item.get("run") == "WRITE":
                print(item)
