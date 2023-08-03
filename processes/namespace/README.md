A namespace is a Python object used to share primitive variables among multiple processes.

> A namespace object has no public methods, but does have writable attributes. Its representation shows the values of its attributes.
>
> — [MULTIPROCESSING — PROCESS-BASED PARALLELISM](https://docs.python.org/3/library/multiprocessing.html)

It may be used to share primitive variables such as:

* Integer values
* Floating point values.
* Strings
* Characters

It cannot be used to share simple Python data structures such as lists, tuples, and dicts.

A namespace must be created by a manager. This means it is hosted in a manager’s server process and shared via proxy objects.

The proxy objects can be shared with child processes and automatically handle serialization (pickling) of data to and from the manager process and provide process-safety.

* **Centralized** : A single copy of the namespace is hosted in the server process of a manager and interacted with via proxy objects, meaning all processes see the same data.
* **Pickability** : Namespace (proxy) objects can be pickled, allowing them to be put on queues or passed as arguments to the Pool class.
* **Safety** : Primitive variables on a namespace can be read and written concurrently in a process-safe manner.

This means that the proxy objects for the namespace can be shared via queues and as arguments to multiprocessing pools, where they must be pickled.

It also means that multiple child processes can read and write the variables on the namespace concurrently without fear of race conditions.
