from concurrent.futures import ThreadPoolExecutor
from threading import Event
import time
import datetime
import queue
import random
import signal

def query_data(event, q, sleep_time=None):
    id = q
    if not sleep_time:
        sleep_time = random.randint(1,2)
    run_dict = {
        "id": id,
        "sleep_time": sleep_time,
        "start_time": None,
        "end_time": None,
        "run_time": None
    }
    while not event.is_set():
        start_time = datetime.datetime.utcnow()
        time.sleep(sleep_time)
        end_time = datetime.datetime.utcnow()
        run_time = float((end_time - start_time).total_seconds())
        run_dict["start_time"] = str(start_time)
        run_dict["end_time"] = str(end_time)
        run_dict["run_time"] = run_time
        return run_dict
    else:
        return run_dict


def exit_threads(executor):
    executor.shutdown(wait=False)
    while True:
        try:
            work_item = executor._work_queue.get_nowait()
        except queue.Empty:
            break
        if work_item is not None:
            work_item.future.cancel()


def run_processes(queries, max_threads=5, timeout=2):
    result = []
    try:
        start_time = time.time()
        event = Event()
        def signal_handler(event, signum, frame):
            event.set()
        signal.signal(signal.SIGTERM, signal_handler)
        pool = ThreadPoolExecutor(max_workers=max_threads)
        threads = []
        i = 1
        while queries:
            q = queries.pop()
            threads.append((q, pool.submit(query_data, event, q, i)))
            i += 1
        time_to_wait = timeout - (time.time() - start_time)
        print(f"Waiting for {time_to_wait} seconds...")
        time.sleep(time_to_wait)
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
        for t in threads:
            print(t)
            if not t[1].cancelled():
                # If the timeout occurs, the future threads get killed automatically
                result.append(t[1].result())
            else:
                result.append((t[0], "Failed"))
        return result

parallel_start_time = time.time()
result = run_processes(list(range(15)), max_threads=5, timeout=10)
for item in result:
    print(item)
parallel_end_time = time.time()
parallel_run_time = parallel_end_time - parallel_start_time
print(f"TOTAL EXECUTION TIME: {parallel_run_time}")