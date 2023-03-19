# Parallel Programming

## Knowledge

### Threads vs Processes

The advantages of using threads are as follows:

- The speed of communication of the threads in the same process, data location, and shared information is fast
- The creation of threads is less costly than the creation of a process, as it is not necessary to copy all the information contained in the context of the main process
- Making the best use of data locality by optimizing memory access through the processor cache memory

The disadvantages of using threads are as follows:

- Data sharing allows swift communication. However, it also allows the

  introduction of difficult-to-solve errors by inexperienced developers.

- Data sharing limits the flexibility of the solution. Migrating to a distributed architecture, for instance, may cause a real headache. In general, they limit the scalability of algorithms.

