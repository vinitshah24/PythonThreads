import multiprocessing
import time
import datetime
import random


def run_job(q, stop_processes, result_list):
    while not q.empty() and not stop_processes.value:
        try:
            job = q.get()
            print(f"Starting the task {job}")
            runtime = random.randint(2, 3)
            run_dict = {
                "id": job,
                "start_time": datetime.datetime.utcnow().isoformat(),
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
            result_list.append(run_dict)


if __name__ == '__main__':
    global RESULT
    try:
        jobQueue = multiprocessing.Queue()
        global_timeout = 6
        processes_count = 5
        job_count = 100
        stop_processes = multiprocessing.Value('b', False)
        result_list = multiprocessing.Manager().list()
        processes = []
        timeout_start = time.time()
        for job in range(job_count):
            jobQueue.put(f"JOB-{job + 1}")
        for _ in range(processes_count):
            process = multiprocessing.Process(name=f"Thread-{_+1}",
                                              target=run_job,
                                              args=(jobQueue, stop_processes, result_list))
            processes.append(process)
        for process in processes:
            process.start()
        print(f"Waiting for {jobQueue.qsize()} tasks to complete...")
        time.sleep(global_timeout)
        print(f"Timeout occurred after {global_timeout} secs")
        stop_processes.value = True
        for process in processes:
            if process.is_alive():
                process.kill()
                print(f"Process {process} is killed!")
                process.join(timeout=1)
    except KeyboardInterrupt:
        stop_processes.value = True
        jobQueue.join()
    finally:
        print(f"Total Runtime: {time.time() - timeout_start}")
        for item in result_list:
            print(item)
