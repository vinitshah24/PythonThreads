## ThreadPool Does Not Support Terminate

Because threads do not support the **terminate()** method, the **ThreadPool** **terminate()** method does not work as expected.

At the latest at the time of writing in Python version 3.10 and lower.

As mentioned, the terminate method exists and can be called.

Therefore, when we call **terminate()** in a **ThreadPool** object, it does not terminate the threads.

Instead, it closes the threads that are not running, and waits for the executing threads to complete.

Calling **terminate()** on the **ThreadPool** has the same effect as calling the **close()** method.

> close(): Prevents any more tasks from being submitted to the pool. Once all the tasks have been completed the worker processes will exit.
>
> — [MULTIPROCESSING — PROCESS-BASED PARALLELISM](https://docs.python.org/3/library/multiprocessing.html)
