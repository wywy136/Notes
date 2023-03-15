# Python Internal

## Sorted Containers

### SortedList

```python
from sortedcontainers import SortedList
```

Sorted list is a sorted mutable sequence in which the values are maintained in sorted order. $O(\lg n)$ for insert and delete

- `add(value)` - value could a simple value or a tuple where the first element is used for sorting
- `discard(value)`

`pop()` returns the last element in O(1), same as traditional lists

## Built-in Features

### Collections

#### deque

```python
from collections import deque
```

Operations:

- `append()`
- `appendleft()`
- `pop()`
- `popleft()`

#### defaultdict

**Defaultdict** is a container like [dictionaries](https://www.geeksforgeeks.org/python-dictionary/) present in the module **collections**. Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

```python
from collections import defaultdict
  
# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"
      
# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])
print(d["c"])
```

`default_factory` could be a function returning the default value for missing key, or any data structure that you hope the dictionary to initiate for every new key.

```python
from collections import defaultdict
  
  
# Defining a dict
d = defaultdict(list)
  
for i in range(5):
    d[i].append(i)
      
print("Dictionary with values as list:")
print(d)
"""
defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})
"""
```

#### Named Tuple

Well, so now what are `namedtuples`? They turn **tuple**s into convenient containers for simple tasks. With **named**tuples you don’t have to use integer indexes for accessing members of a tuple. You can think of namedtuples like dictionaries but unlike dictionaries they are immutable.

```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)
# Output: Animal(name='perry', age=31, type='cat')

print(perry.name)
# Output: 'perry'
```

Moreover, as `namedtuple` instances do not have per-instance dictionaries, they are lightweight and require no more memory than regular tuples. This makes them faster than dictionaries. 

Last but not the least, you can convert a **named****tuple** to a dictionary. Like this:

```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type="cat")
print(perry._asdict())
# Output: OrderedDict([('name', 'Perry'), ('age', 31), ...
```

#### Counter

Return a dict with element frequencies.

### Itertools

#### Permutations and Combinations

https://www.geeksforgeeks.org/permutation-and-combination-in-python/

### Random

#### Choice 

The `random.choice()` method returns a randomly selected element from the specified sequence.

```python
import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))
```

### Dict

The key-value pairs are maintained **in order** in python dict. This makes a dict like a stack.

#### Pop the last key-value pair

```python
key, value = dictionary.popitem()
```

#### Delete a key

```scss
dictionary.pop(key_to_remove, not_found)
```

The pop() method can accept either one or two parameters:

- The name of the key you want to remove (mandatory).
- The value that should be returned if a key cannot be found (optional).

### map

Apply a function for each entries in an iterable

```python
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
```

### sorted

#### using sorted with user-defined function

using `cmp_to_key()`

```python
def compare(x, y): return int(y+x) - int(x+y)
        nums = sorted(map(str, nums), key=cmp_to_key(compare))
```

### string

#### ascii_lowercase

In Python3, **`ascii_lowercase `** is a pre-initialized string used as string constant. In Python, string `ascii_lowercase ` will give the lowercase letters ‘abcdefghijklmnopqrstuvwxyz’.

## Garbage Collector

### Generational garbage collector

The garbage collector is keeping track of all objects in memory. A new object starts its life in the first generation of the garbage collector. If Python executes a garbage collection process on a generation and an object survives, it moves up into a second, older generation. The Python garbage collector has three generations in total, and an object moves into an older generation whenever it survives a garbage collection process on its current generation.

For each generation, the garbage collector module has a threshold number of objects. If the number of objects exceeds that threshold, the garbage collector will trigger a collection process. For any objects that survive that process, they’re moved into an older generation.

```python
>>> import gc
>>> gc.get_threshold()
(700, 10, 10)
```

```python
>>> import gc
>>> gc.get_count()
(596, 2, 1)
```

```python
>>> gc.get_count()
(595, 2, 1)
>>> gc.collect()
577
>>> gc.get_count()
(18, 0, 0)
```

```python
>>> import gc
>>> gc.get_threshold()
(700, 10, 10)
>>> gc.set_threshold(1000, 15, 15)
>>> gc.get_threshold()
(1000, 15, 15)
```

## Decorator

Decorators let you execute code before and after a function.

Function as a decorator:

```python
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run
```

Class as a decorator:

```python
class logit(object):

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        with open(self._logfile, 'a') as opened_file:
            # Now we log to the specified logfile
            opened_file.write(log_string + '\n')
        # Now, send a notification
        self.notify()

        # return base func
        return self.func(*args)



    def notify(self):
        # logit only logs, no more
        pass
  

logit._logfile = 'out2.log' # if change log file
@logit
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called
```

With class as decorator, you can implement more decorators by just inheritance. For the example above,

```python
class email_logit(logit):
    '''
    A logit implementation for sending emails to admins
    when the function is called.
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # Send an email to self.email
        # Will not be implemented here
        pass
```

## Class

### Magic Methods

Implementing **getitem** in a class allows its instances to use the [] (indexer) operator. 

## Generator

### Iterator

An **iterator** is any object in Python which has a `__next__` method defined.

### Generators

Generators are **iterator**s, but you can only iterate over them once. It’s because they do not store all the values in memory, they generate the values on the fly.

Generators are best for calculating large sets of results (particularly calculations involving loops themselves) where you don’t want to allocate the memory for all results at the same time. 

```python
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
```

To access the next element of an iterator, use python's built-in `next()` method.

Str is an interable but not an iterator. To change it into an iterator, use python's built-in `iter()` method.

## With

**`with`** statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. 

```python
# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()
  
# 2) without using with statement
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()
 

# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')
```

Using with statement, no need to call `file.close()`. The `with` statement itself ensures proper acquisition and release of resources, even there is an exception running `file.write()`.

### User defined objects supporting "with"

To use `with` statement in user defined objects you only need to add the methods `__enter__()` and `__exit__()` in the object methods. 

```python
class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name
      
    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file
  
    def __exit__(self):
        self.file.close()
  
# using with statement with MessageWriter
  
with MessageWriter('my_file.txt') as xfile:
    xfile.write('hello world')
```

## Copy

By assignment: not a copy but a reference. Changes to the original list will result into changes in the new list.

Shallow copy: new list, but inner lists are bound the original list.

Deep copy: totally new list without any dependency

## Argument passing

DIfference between immutable arguments and mutable arguments.

## Multithreading, Multiprocessing

### Multithreading

Threading is game-changing because many scripts related to network/data I/O spend the majority of their time waiting for data from a remote source. Because downloads might not be linked (i.e., scraping separate websites), the processor can download from different data sources in parallel and combine the result at the end. For CPU intensive processes, there is little benefit to using the threading module.

```python
def testThread(num):
    print(num)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=testThread, arg=(i,))
        t.start()
```

#### Thread-safe queue

```python
from threading import Thread
from queue import Queue
 
# add items to the list
def add_items(safe_list):
    for i in range(100000):
        safe_list.put(i)
 
# create the thread safe list (queue)
safe_list = Queue()
# configure threads to add to the list
threads = [Thread(target=add_items, args=(safe_list,)) for i in range(10)]
# start threads
for thread in threads:
    thread.start()
# wait for all threads to terminate
print('Main waiting for threads...')
for thread in threads:
    thread.join()
# report the number of items in the list
print(f'List size: {safe_list.qsize()}')
```

### GIL

GIL is necessary because Python is not thread-safe and there is a globally enforced lock when accessing a Python object. Though not perfect, it's a pretty effective mechanism for memory management. 

GIL 会使得多线程在执行时只有IO操作时多线程并发的，计算时还是单线程依次执行

GIL会在IO 时释放，计算时上锁

### Multiprocessing

Since the processes don't share memory, they can't modify the same memory concurrently.

```python
import multiprocessing
def spawn():
    print('test!')

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn)
        p.start()
        p.join()
```

