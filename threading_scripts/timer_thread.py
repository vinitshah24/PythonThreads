from threading import Timer


def task(message):
    print(message)

# It provides a useful way to execute a function after an interval of time.
timer = Timer(3, task, args=('Hello world',))
timer.start()
print('Waiting for the timer...')
