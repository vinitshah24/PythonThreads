import datetime
import json
import multiprocessing
import random
import time


def run_job(q, curr_thread, stop_processes, result_list, running_processes):
    while not q.empty() and not stop_processes.value:
        try:
            job = q.get()
            start_time = datetime.datetime.utcnow().isoformat()
            runtime = random.randint(2, 3)
            running_processes[job] = {
                "id": job,
                "thread": curr_thread,
                "start_time": start_time,
                "runtime": runtime
            }
            print(f"Starting the task {job} on {curr_thread}")
            run_dict = {
                "id": job,
                "thread": curr_thread,
                "start_time": start_time,
                "runtime": runtime,
                "end_time": None
            }
            time.sleep(runtime)
            print(f"Completed task {job} after {runtime} seconds")
        except:
            print("Caught Exception")
            run_dict["end_time"] = datetime.datetime.utcnow().isoformat()
        finally:
            if run_dict["end_time"] is None:
                run_dict["end_time"] = datetime.datetime.utcnow().isoformat()
            del running_processes[job]
            result_list.append(run_dict)


if __name__ == '__main__':
    try:
        jobQueue = multiprocessing.Queue()
        global_timeout = 6
        processes_count = 5
        job_count = 100
        stop_processes = multiprocessing.Value('b', False)
        result_list = multiprocessing.Manager().list()
        running_processes = multiprocessing.Manager().dict()
        processes = []
        timeout_start = time.time()
        print(f"START: {datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')}")
        for job in range(job_count):
            jobQueue.put(f"JOB-{job + 1}")
        for _ in range(processes_count):
            curr_thread = f"Thread-{_+1}"
            process = multiprocessing.Process(name=curr_thread,
                                              target=run_job,
                                              args=(jobQueue, curr_thread, stop_processes,
                                                    result_list, running_processes))
            processes.append(process)
        for process in processes:
            process.start()
        print(f"Waiting for {jobQueue.qsize()} tasks to complete...")
        time.sleep(global_timeout)
        print(f"Timeout occurred after {global_timeout} secs")
        stop_processes.value = True
        # Empty the queue to avoid OError: [Errno 32] Broken pipe
        while not jobQueue.empty():
            jobQueue.get()
        jobQueue.close()
        for process in processes:
            if process.is_alive():
                process.kill()
                print(f"Process {process.name} is killed!")
                process.join(timeout=1)
    except KeyboardInterrupt:
        stop_processes.value = True
    finally:
        if timeout_start is not None:
            print(f"END: {datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')}")
            print(f"Total Runtime: {time.time() - timeout_start}")
        for item in result_list:
            print(item)
        if running_processes:
            print("Running processes that was killed:")
            # print(json.dumps(dict(running_processes), indent=4))
            for key, item in dict(running_processes).items():
                print(item)
