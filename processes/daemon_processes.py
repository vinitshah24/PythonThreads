"""
active_children():          Returns a list of all active child processes for the current process.
cpu_count():                Return the number of logical CPU cores in the system.
current_process():          Return the Process instance for the current process.
parent_process():           Return the Process instance for the parent of the current process.
------------------
freeze_support():           Add support for multiprocessing for a frozen Python executable on windows.
get_all_start_methods():    Return a list of process start methods supported on the system.
get_context():              Return a process context object.
get_start_method():         Return the currently configured process start method.
set_executable():           Set the path to the Python executable for child processes.
set_start_method():         Set the start method used for new processes.
"""

from time import sleep
from multiprocessing import active_children
from multiprocessing import Process
from multiprocessing import cpu_count
from multiprocessing import parent_process
from multiprocessing import current_process


def task():
    sleep(0.2)
    process = current_process()
    print(f"Child process: {process}")
    print(f'Child is Daemon process: {process.daemon}')
    parent_proc = parent_process()
    print(f"Parent Process: {parent_proc}")

if __name__ == '__main__':

    processes = [Process(target=task, daemon=True) for _ in range(5)]
    for process in processes:
        process.start()

    children = active_children()
    print(f'Active Children Count: {len(children)}')

    num_cores = cpu_count()
    print(f"# Cores: {num_cores}")

    process = current_process()
    print(f"Main process: {process}")
    # If the main process exists first, daemon threads will be terminated instantly
    sleep(1)
