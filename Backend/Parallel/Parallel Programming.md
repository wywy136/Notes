# Parallel Programming

### Threads vs Processes

In computing, a thread is a single sequence of execution within a process. A process, on the other hand, is an instance of a computer program that is being executed and consists of one or more threads of execution.

A process is essentially an isolated instance of a program that has its own memory space, system resources, and execution environment. It can contain multiple threads, each of which is capable of executing independently and simultaneously with other threads in the same process.

A thread, on the other hand, is a lightweight process that shares the same memory space and system resources as other threads in the same process. Threads within the same process can communicate with each other and share data more efficiently than processes that need to use inter-process communication mechanisms.

In summary, processes are isolated instances of programs, while threads are sequences of instructions within a process that can execute independently and share the same memory space and system resources.

The advantages of using threads are as follows:

- The speed of communication of the threads in the same process, data location, and shared information is fast
- The creation of threads is less costly than the creation of a process, as it is not necessary to copy all the information contained in the context of the main process
- Making the best use of data locality by optimizing memory access through the processor cache memory

The disadvantages of using threads are as follows:

- Data sharing allows swift communication. However, it also allows the

  introduction of difficult-to-solve errors by inexperienced developers.

- Data sharing limits the flexibility of the solution. Migrating to a distributed architecture, for instance, may cause a real headache. In general, they limit the scalability of algorithms.

### Parallel Programming Models

#### Shared memory model

In this model the tasks share a single shared memory area, where the access (reading and writing data) to shared resources is asynchronous. There are mechanisms that allow the programmer to control the access to the shared memory, for example, locks or semaphores. This model offers the advantage that the programmer does not have to clarify the communication between tasks. An important disadvantage in terms of performance is that
 it becomes more difficult to understand and manage data locality.

#### The multithread model

In this model, a process can have multiple flows of execution, for example, a sequential
 part is created and subsequently, a series of tasks are created that can be executed parallelly. Usually, this type of model is used on shared memory architectures. So, it will be very important for us to manage the synchronization between threads, as they operate on shared memory, and the programmer must prevent multiple threads from updating the same locations at the same time. 

#### The message passing model

The message passing model is usually applied in the case where each processor has its own memory (distributed memory systems). More tasks can reside on the same physical machine or on an arbitrary number of machines. The programmer is responsible for determining the parallelism and data exchange that occurs through the messages. 

#### The data parallel model

In this model, we have more tasks that operate on the same data structure, but each task operates on a different portion of data.

