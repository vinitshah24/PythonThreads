import concurrent.futures
import threading
from concurrent.futures import ThreadPoolExecutor
from threading import Event
from threading import current_thread
import time
import datetime
import queue
import random
import signal


def run_job(event, q):
    id = q
    sleep_time = random.randint(3, 8)
    run_dict = {
        "id": id,
        "thread": None,
        "sleep_time": sleep_time,
        "start_time": None,
        "end_time": None,
        "run_time": None,
    }
    while not event.is_set():
        start_time = datetime.datetime.utcnow()
        time.sleep(sleep_time)
        end_time = datetime.datetime.utcnow()
        run_time = float((end_time - start_time).total_seconds())
        run_dict["thread"] = current_thread().name
        run_dict["start_time"] = str(start_time)
        run_dict["end_time"] = str(end_time)
        run_dict["run_time"] = run_time
        return run_dict
    else:
        return run_dict


def exit_threads(executor):
    """
    The shutdown() method is used to initiate a graceful shutdown of an executor, allowing the
    currently running tasks to complete but preventing any new tasks from being submitted.
    The wait=False parameter indicates that the shutdown should not wait for the active tasks to complete.

    The _work_queue is an internal attribute of the executor object that represents the queue of pending
    work items. The get_nowait() method is used to retrieve an item from the queue without blocking.
    If the queue is empty at the time of the call, a queue.Empty exception is raised.

    If work_item is not None, it means there is a pending work item that hasn't started executing yet.
    In this case, the code calls work_item.future.cancel(). The cancel() method is used to attempt canceling
    the associated future object, which represents the result of the work item.
    """
    executor.shutdown(wait=False)
    while True:
        try:
            work_item = executor._work_queue.get_nowait()
        except queue.Empty:
            break
        if work_item is not None:
            work_item.future.cancel()


def signal_handler(event, signum, frame):
    event.set()


def run_processes(jobs, max_threads=5, timeout=2):
    try:
        event = Event()
        signal.signal(signal.SIGTERM, signal_handler)
        pool = ThreadPoolExecutor(max_workers=max_threads)
        threads = []
        while jobs:
            job = jobs.pop()
            threads.append((job, pool.submit(run_job, event, job)))
        print(f"Waiting for {timeout} seconds...")
        time.sleep(timeout)
        exit_threads(pool)
        event.set()
        event.clear()
        for t in threads:
            t.join()
    except KeyboardInterrupt as ke:
        print(f"Keyboard Interrupt occurred: {ke}")
        exit_threads(pool)
        event.set()
        for t in threads:
            t.join()
    finally:
        result = []
        cancelled_jobs = []
        for t in threads:
            print(t)
            # If the thread completed successfully, capture the results
            if not t[1].cancelled():
                result.append(t[1].result())
            # Capture the future threads that were cancelled
            else:
                cancelled_jobs.append(t[0])
        return result, cancelled_jobs


if __name__ == "__main__":
    """
    Runs the jobs using thread pool. Waits for all threads to finish and only kills future threads after timeout.
    """
    parallel_start_time = time.time()
    jobs = [f"JOB-{i}" for i in range(1, 16)]
    result, cancelled_jobs = run_processes(jobs, max_threads=5, timeout=3)
    parallel_end_time = time.time()
    parallel_run_time = parallel_end_time - parallel_start_time
    print(f"Total Execution time: {parallel_run_time}")
    print("Completed jobs:")
    for item in result:
        print(item)
    print("Cancelled jobs:")
    for job in cancelled_jobs:
        print(job)
