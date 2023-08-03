"""
A manager in the multiprocessing module provides a way to create Python objects that can be shared easily
between processes.

A manager creates a server process that hosts a centralized version of objects that can be shared among multiple
processes.

The objects are not shared directly. Instead, the manager creates a proxy object for each object that it manages and
 the proxy objects are shared among processes.

The proxy objects are used and operate just like the original objects, except that they serialize data, synchronize
and coordinate with the centralized version of the object hosted in the manager server process.

This makes managers a process-safe and preferred way to share Python objects among processes.
----------------------------------------------------------------

Running the example first creates the manager which starts the manager's server process.
Next, the shared list is created via the manager. The main process then defines a new dict with three initial values
set to zero and adds the dict to the shared list. It reports the contents of the dict, matching what was initialized.

Next, the main process configures and starts a new child process and passes the shared list to it. It then blocks
until the child process terminates.

The child process runs, first retrieving the dict from the shared list. It reports the content of the dict,
which matches the content stored by the main process.

This highlights that a dict was added to the list and was stored in the manager's process.
Next, the child process changes the content of the dict and reports the new values, confirming that the change was
made, at least to the local copy of the dict.

The child process terminates and the main process continues on and reports the content of the dict within the shared
list. Here, we see an unexpected result. The changes made to the dict within the shared list by the child process are
not reflected in the main process.

This suggests that the child process got a local copy of the list and the changes were not propagated to the manager
and therefore remain unavailable to other processes.

Main Before: {'a': 0, 'b': 0, 'c': 0}
Task Before: {'a': 0, 'b': 0, 'c': 0}
Task After: {'a': 1, 'b': 2, 'c': 3}
Main After: {'a': 0, 'b': 0, 'c': 0}

"""

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
        dict_item = {'a':0, 'b':0, 'c':0}
        # add the dict to the list
        list_proxy.append(dict_item)
        print(f'Main Before: {list_proxy[0]}', flush=True)
        # start a child process
        process = Process(target=task, args=(list_proxy,))
        process.start()
        process.join()
        # report the list of dicts
        print(f'Main After: {list_proxy[0]}', flush=True)
