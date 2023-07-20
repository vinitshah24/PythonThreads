from time import sleep
from threading import Thread


def incrementor(amount, repeats):
    global GLOBAL_VAL
    for _ in range(repeats):
        tmp = GLOBAL_VAL
        sleep(0)
        tmp = tmp + amount
        sleep(0)
        GLOBAL_VAL = tmp


def reducer(amount, repeats):
    global GLOBAL_VAL
    for _ in range(repeats):
        tmp = GLOBAL_VAL
        sleep(0)
        tmp = tmp - amount
        sleep(0)
        GLOBAL_VAL = tmp


GLOBAL_VAL = 0

add_thread = Thread(target=incrementor, args=(100, 1000000))
sub_thread = Thread(target=reducer, args=(100, 1000000))

add_thread.start()
sub_thread.start()

print("Waiting for threads to finish...")
add_thread.join()
sub_thread.join()

print(f"GLOBAL_VAL: {GLOBAL_VAL}")
