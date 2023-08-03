from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing.managers import BaseManager

# custom class
class MyCustomClass():
    # constructor
    def __init__(self, data):
        # store the data in the instance
        self.data = data
        self.storage = list()

    # do something with the data
    def task(self):
        # generate a random number
        value = random()
        # block for a moment
        sleep(value)
        # calculate a new value
        new_value = self.data * value
        # store everything
        self.storage.append((self.data, value, new_value))
        # return the new value
        return new_value

    # get all stored values
    def get_storage(self):
        return self.storage

# custom manager to support custom classes
class CustomManager(BaseManager):
    # nothing
    pass

# custom function to be executed in a child process
def work(shared_custom):
    # call the function on the shared custom instance
    value = shared_custom.task()
    # report the value
    print(f'>child got {value}')

# protect the entry point
if __name__ == '__main__':
    # register the custom class on the custom manager
    CustomManager.register('MyCustomClass', MyCustomClass)
    # create a new manager instance
    with CustomManager() as manager:
        # create a shared custom class instance
        shared_custom = manager.MyCustomClass(10)
        # call the function on the shared custom instance
        value = shared_custom.task()
        # report the value
        print(f'>main got {value}')
        # start some child processes
        processes = [Process(target=work, args=(shared_custom,)) for i in range(4)]
        # start processes
        for process in processes:
            process.start()
        # wait for processes to finish
        for process in processes:
            process.join()
        # all done
        print('Done')
        # report all values stored in the central object
        for t in shared_custom.get_storage():
            print(t)