# Python Parallel Programming

## Multithreading

### Threading

- Create a thread

  ```python
  import threading
  threading.Thread(
      group=None,
      target=None,
      name=None,
      args=(),
      kwargs={}
  )
  ```

- Get thread name

  ```python
  threading.currentThread().getName()
  ```

- Using thread in a subclass
  - Define a new subclass of the `Thread` class
  - Override the `_init__(self [,args])` method to add additional arguments
  - Override the `run(self [,args])` method to implement what the thread should do when it is started
  - call `start()` function to execute the `run()`

### Lock

- Use a lock

  ```python
  lock = threading.Lock()
  lock.acquire()
  ...
  lock.release()
  ```

- Use a RLock

  ```python
  lock = threading.RLock()
  ```

- An RLock could be acquired multiple times by the same thread. It should also be released multiple times.

### Semaphore

- Create a semaphore (value defaults to 1)

  ```python
  semaphore = threading.Semaphore(value)
  ```

- Use the semaphore

  ```python
  semaphore.acquire()  # reduce 1 if value-1 > 0 else block
  semaphore.release(value=1)  # add value and wake up n of waiting threads
  ```

### Conditional Variable

- Create a condition

  ```python
  import threading
  condition = threading.Condition()
  ```

- Use a condition

  ```python
  condition.acquire()
  if <time to wait>:
      condition.wait()
  // Get notified
  ...
  condition.release()
  ===================
  condition.acquire()
  // Notify waiting threads
  condition.notify()/notifyAll()
  condition.release()
  ```

### Event

- Create an event

  ```python
  event = threading.Event()
  ```

- Use an event

  - Wait for an event

    ```python
    event.wait()
    ```

  - Set an event

    ```python
    event.set()
    event.clear()
    ```

### Using with Python With Statement

The following objects can be used as context managers for a `with` statement

- Lock
- RLock
- Condition
- Semaphore

### Queue in Python

It is considered a best practice to instead concentrate on using the module queue.

- `put()`: This puts an item in the queue
- `get()`: This removes and returns an item from the queue
- `task_done()`: This needs to be called each time an item has been processed
- `join()`: This blocks until all items have been processed

```python
from queue import Queue
q = Queue()
```

### GIL

The main thread acquires the GIL first. When a new thread is acquired, it tries to acquire the GIL. It waits for a fixed time interval called the **switch interval** (5 ms by default), and if the GIL is not released during that time, it sets the `eval_breaker` and `gil_drop_request` flags. The `eval_breaker` flag tells the GIL-holding thread to suspend bytecode execution, and `gil_drop_request` explains why. The GIL-holding thread sees the flags when it starts the next iteration of the evaluation loop and releases the GIL. It notifies the GIL-awaiting threads, and one of them acquires the GIL. It's up to the OS to decide which thread to wake up, so it may or may not be the thread that set the flags.

The first effect of the GIL is well-known: multiple Python threads cannot run in parallel. Thus, a multi-threaded program is not faster than its single-threaded equivalent even on a multi-core machine (for CUP-bound tasks). In fact, multi-threaded programs may run slower because of the overhead associated with [context switching](https://en.wikipedia.org/wiki/Context_switch).

Although Python threads cannot help us speed up CPU-intensive code, they are useful when we want to perform multiple I/O-bound tasks simultaneously. Consider a server that listens for incoming connections and, when it receives a connection, runs a handler function in a separate thread. The handler function talks to the client by reading from and writing to the client's socket. When reading from the socket, the thread just hangs until the client sends something. This is where multithreading helps: another thread can run in the meantime.

To allow other threads run while the GIL-holding thread is waiting for I/O, CPython implements all I/O operations using the following pattern:

1. release the GIL;
2. perform the operation, e.g. [`write()`](https://man7.org/linux/man-pages/man2/write.2.html), [`recv()`](https://man7.org/linux/man-pages/man2/recv.2.html), [`accept()`](https://man7.org/linux/man-pages/man2/accept.2.html);
3. acquire the GIL.

Thus, a thread may release the GIL voluntarily before another thread sets `eval_breaker` and `gil_drop_request`. In general, a thread needs to hold the GIL only while it works with Python objects. So CPython applies the release-perform-acquire pattern not just to I/O operations but also to other blocking calls into the OS like [select()](https://man7.org/linux/man-pages/man2/select.2.html) and [pthread_mutex_lock()](https://linux.die.net/man/3/pthread_mutex_lock), and to heavy computations in pure C. For example, hash functions in the [`hashlib`](https://docs.python.org/3/library/hashlib.html) standard module release the GIL. This allows us to actually speed up Python code that calls such functions using multithreading. The conclusion here is that it's possible to speed up CPU-intensive Python code using multithreading if the code calls C functions that release the GIL. 

## Multiprocessing

### Process

- Create a process

```python
import multiprocessing
p = multiprocessing.Process()
```

- Name a process

  ```python
  process_with_name = multiprocessing.Process(
      name='foo_process',
      target=foo
  )
  
  def foo():
      name = multiprocessing.current_process().name
  ```

- Run a process in background

  ```python
  process.daemon = True
  ```

- Using a process in a subclass
  - Define a new subclass of the Process class
  - Override the `_init__(self [,args])` method to add additional arguments
  - Override the `run(self [,args])` method to implement what Process should when it is started

### `multiprocessing.Queue`

- Using a queue to exchange objects between processes

  Unlike the queue in python, this queue does not require calling `task_done()`

  ```python
  import multiprocessing
  
  queue = multiprocessing.Queue()
  queue.put(item)
  item = queue.get()
  ```

### Pipe

https://www.educative.io/answers/pipes-queues-and-lock-in-multiprocessing-in-python

### Process pool

- `map()`: This is the parallel equivalent of the map() built-in function. It blocks until the result is ready, this method chops the iterable data in a number of chunks that submits to the process pool as separate tasks.

  ```python
  inputs = list(range(100))
  pool = multiprocessing.Pool(processes=4)
  pool_outputs = pool.map(function_square, inputs)
  pool.close()
  pool.join()
  ```


## Asynchronous Programming

### Futures

- `concurrent.futures.Executor`: This is an abstract class that provides methods to execute calls asynchronously.
- `submit (function, argument)`: This schedules the execution of a function (called callable) on the arguments.
- `map (function, argument)`: This executes the function on arguments in an asynchronous mode.
- `shutdown(Wait = True)`: This signals the executor to free any resource.
- `concurrent.futures.Future`: This encapsulates the asynchronous execution of a callable function. Future objects are instantiated by submitting tasks (functions with optional parameters) to executors.

### Pool

```python
import concurrent.futures

with concurrent.futures.ThreadPoolExecuter(max_workers=n) as e:
    for _ in list:
        e.submit(callable, args)
        
with concurrent.futures.ProcessPoolExecuter(max_workers=n) as e:
    ...
```

