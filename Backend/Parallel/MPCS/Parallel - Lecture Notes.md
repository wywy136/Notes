# Lecture Notes

## Projects

https://github.com/mpcs52060-aut22/proj1-wywy136

https://github.com/mpcs52060-aut22/project-2-wywy136

https://github.com/mpcs52060-aut22/proj3-wywy136

## Shared memory Architectures

### Instruction Parallelism

Simultaneous execution of a sequence of instructions

Various techniques to exploit ILP

- Instruction Pipelining - different pipeline stages can oprerate in parallel
- Out-of-order execution
- Speculative execution & Branch prediction

### Improving Data Access Performance

#### Caches

Alleviate the problem of wasting hundreds of CPU cycles waiting to access main memory

Cache line: fixed-size block of data containng metadata, normally 64 or 128 bytes

Caches are effecitve because most programs display a high degree of locality

LRU: least recently used strategy

Cache coherence

#### MESI

- Modified
- Exlusive
- Shared
- Invalid

Write-through Caches

Write-back Caches

## **Principles of Mutual Exclusion**

### Theoretical principles of parallel computing

- Mutual Exclusion Property: Critical sections of different threads do not overlap. Only one

  thread is executing a critical section at a time.

- Deadlock-freedom Property: If multiple threads simultaneously request to enter a critical

  section, then it must allow one to proceed

- Starvation-freedom property: Every thread that attempts to acquire the lock eventually succeeds.

- Fairness Principle: A thread who just left the critical section cannot immediately re-enter the critical section if other threads have already requested to enter the critical section.

### Parallel Performance

Amdahl's law: 
$$
speedup = \frac{1}{1-p+\frac{p}{n}}
$$


## Councurrent Data Structures

### Introduction

#### Performance issue of lock based system

- Sequential bottleneck
- Memory contention: Overheadintrafficasaresultofmultiplethreadsconcurrently attempting to access the same memory location.

- Blocking

  - Ifthreadthatcurrentlyholdsthelockisdelayed,thenallother threads attempting to access are also delayed.

  - Implementationoflocksisknownasablockingalgorithm
  - Considernon-blocking(lock-free)algorithm

#### Nonblocking algorithms

- Implemented by a hardware operation
  - atomicallycombinesaloadandastore
- lock-free
- wait-free

### Concurrent Linked List

#### Coarse Grain Sync

Lock the entire linked list and perform the operations.

#### Fine Grain Sync

Hand-to-hand lock

Always aquire two locks:

- If a node is locked, no one can delete node’s successor
- If a thread locks the node to be deleted and its predecessor – Then it works

#### Lazy List

### Concurrent Hash Tables

