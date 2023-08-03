
## What Is a Manager

A manager in the **multiprocessing** module provides a way to create Python objects that can be shared easily between processes.

> Managers provide a way to create data which can be shared between different processes, including sharing over a network between processes running on different machines. A manager object controls a server process which manages shared objects. Other processes can access the shared objects by using proxies.
>
> — [MULTIPROCESSING — PROCESS-BASED PARALLELISM](https://docs.python.org/3/library/multiprocessing.html)

A manager creates a server process that hosts a centralized version of objects that can be shared among multiple processes.

The objects are not shared directly. Instead, the manager creates a proxy object for each object that it manages and the proxy objects are shared among processes.

The proxy objects are used and operate just like the original objects, except that they serialize data, synchronize and coordinate with the centralized version of the object hosted in the manager server process.

> A proxy is an object which refers to a shared object which lives (presumably) in a different process. […] A proxy object has methods which invoke corresponding methods of its referent (although not every method of the referent will necessarily be available through the proxy).
>
> — [MULTIPROCESSING — PROCESS-BASED PARALLELISM](https://docs.python.org/3/library/multiprocessing.html)

This makes managers a process-safe and preferred way to share simple data structures like lists and dicts among processes.

They are also a preferred way to share concurrency primitives among processes, specifically among workers in a multiprocessing pool.

## What are the Benefits of a Manager

Managers provide three key capabilities for process-based concurrency, they are:

* **Centralized** : A single instance of a shared object is maintained in a separate server process.
* **Process-safety** : Proxy objects ensure that access to the centralized object is process-safe in order to avoid race conditions.
* **Pickability** : Proxy objects can be pickled and shared with child processes such as arguments in process pools and items in queues.

In addition to providing safe access to a shared object across processes on one system, managers allow the same object to be accessed safely across processes on other systems via network access.
