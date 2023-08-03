## Comparison of Thread vs Process

Now that we are familiar with the Thread and Process classes, let’s review their similarities and differences.

### Similarities Between Thread and Process

The Thread and Process classes are very similar, let’s review some of the most important similarities.

#### 1. Both Classes Used For Concurrency

Both the **threading.Thread** class and the **multiprocessing.Process** classes are intended for concurrency.

There are whole classes of problems that require the use of concurrency, that is running code or performing tasks out of order.

Problems of these types can generally be addressed in Python using threads or processes, at least at a high-level.

#### 2. Both Have The Same API

Both the **threading.Thread** class and the **multiprocessing.Process** classes have the same API.

Specifically when:

* Running a function in a new thread or process, e.g. the “ **target** ” argument on the class constructor.
* Extending the class and overriding the **run()** function.
* Starting a new thread or process via the **start()** function.

This was the intention by the module designers and this similarity carries over to other parts of the threading and multiprocessing modules.

#### 3. Both Support The Same Concurrency Primitives

Both the **threading.Thread** class and the **multiprocessing.Process** classes support the same concurrency primitives.

Concurrency primitives are mechanisms for synchronizing and coordinating threads and processes.

Concurrency primitives with the same classes and same API are provided for use with both threads and processes, for example:

* Locks (mutex) with **threading.Lock** and  **multiprocessing.Lock** .
* Recurrent Locks with **threading.RLock** and  **multiprocessing.RLock** .
* Condition Variables with **threading.Condition** and  **multiprocessing.Condition** .
* Semaphores with **threading.Semaphore** and  **multiprocessing.Semaphore** .
* Event Objects with **threading.Event** and  **multiprocessing.Event** .
* Barriers with **threading.Barrier** and  **multiprocessing.Barrier** .

This allows the same concurrency design patterns to be used with either thread-based concurrency or process-based concurrency.

### Differences Between Thread and Process

The Thread and Process are also quite different, let’s review some of the most important differences.

#### 1. Native Threads vs. Native Processes

Perhaps the most important difference is the functionality that underlies each.

The **threading.Thread** class represents a naive thread managed by the operating system. The **multiprocessing.Process** class represents a native process managed by the underlying operating system.

A process is a high-level of abstraction than a thread.

* A process has a main thread.
* A process may have additional threads.
* A process may have child processes.

Whereas a thread belongs to a process.

#### 2. Shared Memory vs. Inter-Process Communication

The classes have important differences in the way they access shared state.

Threads can share memory within a process.

This means that functions executed in new threads can access the same data and state. These might be global variables or data shared via function arguments. As such, sharing state between threads is straightforward.

Processes do not have shared memory like threads.

Instead, state must be serialized and transmitted between processes, called inter-process communication. Although it occurs under the covers, it does impose limitations on what data and state can be shared and adds overhead to sharing data.

Typically sharing data between processes requires explicit mechanisms, such as the use of a **multiprocessing.Pipe** or a  **multiprocessing.Queue** .

As such, sharing state between threads is easy and lightweight, and sharing state between processes is harder and heavyweight.

#### 3. GIL vs. no GIL

Multiple threads are subject to the global interpreter lock (GIL), whereas multiple child processes are not subject to the GIL.

The GIL is a programming pattern in the reference Python interpreter (e.g. CPython, the version of Python you download from python.org).

It is a lock in the sense that it uses synchronization to ensure that only one thread of execution can execute instructions at a time within a Python process.

This means that although we may have multiple threads in our program, only one thread can execute at a time.

The GIL is used within each Python process, but not across processes. This means that multiple child processes can execute at the same time and are not subject to the GIL.

This has implications for the types of tasks best suited to each class.

### Summary of Differences

It may help to summarize the differences between Thread and Process.

#### Thread

* Uses native threads, not a native process.
* Thread belongs to a process.
* Shared memory, not inter-process communication.
* Subject to the GIL, not true parallel execution.
* Suited to IO-bound tasks, not CPU bound tasks.
* Create 10s to 1,000s of threads, not really constrained.

#### Process

* Uses native processes, not native threads.
* Process has threads, and has child processes.
* Heavyweight and slower to start, not lightweight and fast to start.
* Inter-process communication, not shared memory.
* Suited to CPU-bound tasks, probably not IO-bound tasks.
* Create 10s of processes, not 100s or 1,000s of tasks.
