


## What is the Global Interpreter Lock?

The internals of the Python interpreter are not thread-safe.

This means that there can be race conditions between multiple threads within a single Python process, potentially resulting in unexpected behavior and corrupt data.

As such, the Python interpreter makes use of a [Global Interpreter Lock](https://en.wikipedia.org/wiki/Global_interpreter_lock), or GIL for short, to make instructions executed by the Python interpreter (called Python bytecodes) thread-safe.

The GIL is a programming pattern in the reference Python interpreter called CPython, although similar locks exist in other interpreted languages, such as Ruby. It is a lock in the sense that it uses a synchronization primitive called a mutual exclusion or mutex lock to ensure that only one thread of execution can execute instructions at a time within a Python process.

> In CPython, the global interpreter lock, or GIL, is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. The GIL prevents race conditions and ensures thread safety.
>
> — [GLOBAL INTERPRETER LOCK, PYTHON WIKI](https://wiki.python.org/moin/GlobalInterpreterLock).

The effect of the GIL is that whenever a thread within a Python program wants to run, it must acquire the lock before executing. This is not a problem for most Python programs that have a single thread of execution, called the main thread.

It can become a problem in multi-threaded Python programs, such as programs that make use of the **threading.Thread** class or the **concurrent.futures.ThreadPoolExecutor** class.

The lock is explicitly released and re-acquired periodically by each Python thread, specifically after approximately every 100 bytecode instructions executed within the interpreter. This allows other threads within the Python process to run, if present.

The lock is also released in some circumstances, allowing other threads to run.

An important example is when a thread performs an I/O operation, such as reading or writing from an external resource like a file, socket, or device.

> Luckily, many potentially blocking or long-running operations, such as I/O, image processing, and NumPy number crunching, happen outside the GIL. Therefore it is only in multithreaded programs that spend a lot of time inside the GIL, interpreting CPython bytecode, that the GIL becomes a bottleneck.
>
> — [GLOBAL INTERPRETER LOCK, PYTHON WIKI](https://wiki.python.org/moin/GlobalInterpreterLock).

The lock is also explicitly released by some [third-party Python libraries](https://scipy-cookbook.readthedocs.io/items/ParallelProgramming.html) when performing computationally expensive operations in C-code, such as many array operations in NumPy.

> In CPython, due to the Global Interpreter Lock, only one thread can execute Python code at once (even though certain performance-oriented libraries might overcome this limitation).
>
> — [THREADING — THREAD-BASED PARALLELISM](https://docs.python.org/3/library/threading.html)

The GIL is a simple and effective solution to thread safety in the Python interpreter, but it has the major downside that full multithreading is not supported by Python.

An alternative solution might be to explicitly make the interpreter thread-safe by protecting each critical section. This has been [tried a number of times](https://docs.python.org/3/faq/library.html#can-t-we-get-rid-of-the-global-interpreter-lock) and typically results in worse performance of single-threaded Python programs by up to 30%.

> Unfortunately, both experiments exhibited a sharp drop in single-thread performance (at least 30% slower), due to the amount of fine-grained locking necessary to compensate for the removal of the GIL.
>
> — [PYTHON GLOBAL INTERPRETER LOCK, PYTHON WIKI](https://wiki.python.org/moin/GlobalInterpreterLock).

Now that we are familiar with the GIL, let's look at how multiprocessing is impacted.


## Multiprocessing and the Global Interpreter Lock

The **multiprocessing** module that provides process-based concurrency is not limited by the Global Interpreter Lock.

Both threads and processes can execute concurrently (out of order), but only python processes are able to execute in parallel (simultaneously), not Python threads (with some caveats).

This means that if we want out Python code to run on all CPU cores and make the best use of our system hardware, we should use process-based concurrency.

> The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows.
>
> — [MULTIPROCESSING — PROCESS-BASED PARALLELISM](https://docs.python.org/3.10/library/multiprocessing.html)

In fact, Jesse Noller and Richard Oudkerk proposed and developed the **multiprocessing** module (originally called “ **pyprocessing** “) in Python specifically to overcome the limitations and side-step the GIL.

> The pyprocessing package offers a method to side-step the GIL allowing applications within CPython to take advantage of multi-core architectures without asking users to completely change their programming paradigm (i.e.: dropping threaded programming for another “concurrent” approach – Twisted, Actors, etc).
>
> — [PEP 371 – ADDITION OF THE MULTIPROCESSING PACKAGE TO THE STANDARD LIBRARY](https://peps.python.org/pep-0371/)

**The multiprocessing module is not limited by the Global Interpreter Lock and can achieve full parallelism in Python.**

---



GIL stands for the Global Interpreter Lock. It is a mechanism used in some programming languages, including CPython (the most widely used implementation of Python), to ensure that only one thread executes Python bytecode at a time. This means that even in a multi-core processor, only one thread is allowed to execute Python code, while other threads are effectively paused.

The GIL has implications for multi-threaded Python programs. Although threads can be used for I/O-bound tasks (such as reading/writing files, making network requests, etc.), they are not well-suited for CPU-bound tasks (such as heavy computations) due to the GIL.

GIL prevents true parallel execution of Python bytecode. While the threads run concurrently, only one of them can be actively executing Python code at a given time. So, the threads compete for the GIL, and as a result, they end up being serialized rather than running in parallel. The GIL prevents them from making progress simultaneously, leading to contention and reduced performance.

As a result, Python threads are generally recommended for I/O-bound tasks, where they can be useful for handling multiple I/O operations concurrently (e.g., handling multiple network requests or file reads/writes). However, for CPU-bound tasks that require significant computation, using Python threads may not lead to a significant speedup. In such cases, developers often turn to multiprocessing, asyncio, or other approaches to achieve better parallelism and performance.
