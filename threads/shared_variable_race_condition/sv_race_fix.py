from threading import Thread
from threading import Lock


def incrementor(amount, repeats, lock):
    global GLOBAL_VAL
    for _ in range(repeats):
        with lock:
            GLOBAL_VAL += amount


def reducer(amount, repeats, lock):
    global GLOBAL_VAL
    for _ in range(repeats):
        with lock:
            GLOBAL_VAL -= amount


GLOBAL_VAL = 0
lock = Lock()

add_thread = Thread(target=incrementor, args=(100, 1000000, lock))
sub_thread = Thread(target=reducer, args=(100, 1000000, lock))

add_thread.start()
sub_thread.start()

print("Waiting for threads to finish...")
add_thread.join()
sub_thread.join()

print(f"GLOBAL_VAL: {GLOBAL_VAL}")
