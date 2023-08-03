from multiprocessing import Process
from multiprocessing import Manager

# task executed in child process
def task(shared_list):
    # get the first item from the list
    item = shared_list[0]
    # report the list of dicts
    print(f'Task Before: {item}', flush=True)
    # update the dict in the shared list
    item['a'] = 1
    item['b'] = 2
    item['c'] = 3
    # report the list of dicts
    print(f'Task After: {item}', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create the manager
    with Manager() as manager:
        # create the shared list
        list_proxy = manager.list()
        # create a dict
        dict_item = manager.dict({'a':0, 'b':0, 'c':0})
        # add the dict to the list
        list_proxy.append(dict_item)
        print(f'Main Before: {list_proxy[0]}', flush=True)
        # start a child process
        process = Process(target=task, args=(list_proxy,))
        process.start()
        process.join()
        # report the list of dicts
        print(f'Main After: {list_proxy[0]}', flush=True)