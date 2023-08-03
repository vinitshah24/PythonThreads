## Thread Pool

A thread pool is a programming pattern for automatically managing a pool of worker threads.

The pool is responsible for a fixed number of threads.

* It controls when they are created, such as when they are needed.
* It also controls what they should do when they are not being used, such as making them wait without consuming computational resources.

The pool can provide a generic interface for executing ad hoc tasks with a variable number of arguments, much like the target property on the **threading.Thread** class, but does not require that we choose a thread to run the task, start the thread, or wait for the task to complete.

## ThreadPool Class

The [**multiprocessing.pool.ThreadPool** class](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.ThreadPool) provides a thread pool in Python.

It allows tasks to be submitted as functions to the thread pool to be executed concurrently.

> A thread pool object which controls a pool of worker threads to which jobs can be submitted.
>
> — [MULTIPROCESSING — PROCESS-BASED PARALLELISM](https://docs.python.org/3/library/multiprocessing.html)

The **ThreadPool** class is in the **multiprocessing** module, rather than the **threading** module because it provides a thread-based wrapper for the **multiprocessing.pool.Pool** class.

> A ThreadPool shares the same interface as Pool, which is designed around a pool of processes …
>
> — [MULTIPROCESSING — PROCESS-BASED PARALLELISM](https://docs.python.org/3/library/multiprocessing.html)

Because **ThreadPool** is a wrapper for  **Pool** , it does have some aspects that can be confusing initially, such as the number of workers are called “ **processes** “.


## **ThreadPool** Life Cycle:

There are four main steps in the life-cycle of using the **ThreadPool** class, they are: create, submit, wait, and shutdown.

* 1. **Create** : Create the thread pool by calling the constructor ThreadPool().
* 2. **Submit** : Submit tasks synchronously or asynchronously.

  * 2a. Submit Tasks Synchronously
  * 2b. Submit Tasks Asynchronously
* 3. **Wait** : Wait and get results as tasks complete (optional).

  * 3a. Wait on AsyncResult objects to Complete
  * 3b. Wait on AsyncResult objects for Result
* 4. **Shutdown** : Shutdown the thread pool by calling shutdown().

  * 4a. Shutdown Automatically with the Context Manager
