# Python Internal

## Inner Functions/Data Structures

### `repr()`

Use `repr()` to get a nice string representing each argument. `[repr(a) for a in args]`.

### `ord()`

Get ascii value of a char.

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

### `map`

Apply a function for each entries in an iterable

```python
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
```

### `sorted`

#### using sorted with user-defined function

using `cmp_to_key()`

```python
def compare(x, y): return int(y+x) - int(x+y)
nums = sorted(map(str, nums), key=cmp_to_key(compare))
```



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

### `ast`

#### Converting a list represented in string format back to list 

Using `ast.literal_eval() `

```python
import ast
ini_list = "[1, 2, 3, 4, 5]"
res = ast.literal_eval(ini_list)
```

### `bisect`

- `bisect.bisect_left()`: Locate the insertion point for *x* in *a* to maintain sorted order. The returned insertion point *i* partitions the array *a* into two halves so that `all(val < x for val in a[lo : i])` for the left side and `all(val >= x for val in a[i : hi])` for the right side.
- `bisect.bisect_right()`
- `bisect.insort_left()`: Insert *x* in *a* in sorted order. This function first runs [`bisect_left()`](https://docs.python.org/3/library/bisect.html#bisect.bisect_left) to locate an insertion point. Next, it runs the `insert()` method on *a* to insert *x* at the appropriate position to maintain sort order. Keep in mind that the `O(log n)` search is dominated by the slow `O(n)` insertion step.

### `collections`

#### `deque`

```python
from collections import deque
```

Operations:

- `append()`
- `appendleft()`
- `pop()`
- `popleft()`

#### `defaultdict`

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

#### `namedtuple`

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

#### `counter`

Return a dict with element frequencies.

### `itertools`

#### Permutations and Combinations

https://www.geeksforgeeks.org/permutation-and-combination-in-python/

### `random`

#### `choice `

The `random.choice()` method returns a randomly selected element from the specified sequence.

```python
import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))
```

### `string`

#### `ascii_lowercase`

In Python3, **`ascii_lowercase `** is a pre-initialized string used as string constant. In Python, string `ascii_lowercase ` will give the lowercase letters ‘abcdefghijklmnopqrstuvwxyz’.

### `queue`

A synchronized class of queue supporting parallel programming.

#### `PriorityQueue`

```python
from queue import PriorityQueue
customers = PriorityQueue()
customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))
while customers:
     print(customers.get())
# Riya Harry Charles Stacy
```

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

https://realpython.com/primer-on-python-decorators/

Decorators let you execute code before and after a function.

### Basic

#### Simple decorator

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
```

#### Using the Syntactic Sugar

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
```

#### With parameters

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")
```

#### Returning values

Make sure the wrapper function returns the return value of the decorated function.

```python
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Adam")
```

#### Identifying

Decorators should use the [`@functools.wraps`](https://docs.python.org/library/functools.html#functools.wraps) decorator, which will preserve information about the original function.

```python
import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

>>> say_whee.__name__
'say_whee'
```

### Simple Boilerplate

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```

### Real World Examples

#### Timing Functions

```python
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
```

#### Debugging Code

```python
import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
```

#### Applying a decorator to a function that has already been defined

```python
import math
from decorators import debug

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)
```

#### Slow Down Code

Why would you want to slow down your Python code? Probably the most common use case is that you want to rate-limit a function that continuously checks whether a resource—like a web page—has changed. The `@slow_down` decorator will sleep one second before it calls the decorated function:

```python
import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)
```

#### With Flask

```python
from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...
```

While this gives an idea about how to add authentication to your web framework, you should usually not write these types of decorators yourself. For Flask, you can use [the Flask-Login extension](https://flask-login.readthedocs.io/en/latest/#flask_login.login_required) instead, which adds more security and functionality. 

### Decorating Class

#### Decorating class methods

The first way to decorate a class is to decorate the methods of a class. Some commonly used built-in decorators are:

- `@classmethod`
- `@staticmethod`
- `@property`

The `@classmethod` and `@staticmethod` decorators are used to define methods inside a class [namespace](https://realpython.com/python-namespaces-scope/) that are not connected to a particular instance of that class. The `@property` decorator is used to customize [getters and setters](hhttps://realpython.com/python-getter-setter/) for class attributes.

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

#### Decorating the whole class

For example,

```python
from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str
```

Decorating a class does not decorate its methods. 

### Decorators With Arguments

Add another layer of inner function. The outermost function returns a reference to the decorator function.

```python
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
```

- Defining `decorator_repeat()` as an inner function means that `repeat()` will refer to a function object—`decorator_repeat`. Earlier, we used `repeat` without parentheses to refer to the function object. The added parentheses are necessary when defining decorators that take arguments.
- The `num_times` argument is seemingly not used in `repeat()` itself. But by passing `num_times` a [closure](https://realpython.com/inner-functions-what-are-they-good-for/) is created where the value of `num_times` is stored until it will be used later by `wrapper_repeat()`.

### Cache decorator

`cache` is a decorator that helps in reducing function execution for the same inputs using the memoization technique. The function returns the same value as `lru_cache(maxsize=None)`, where the cache grows indefinitely without evicting old values. The decorator creates a thin wrapper around a dictionary lookup for the function arguments.

```python
from functools import cache
import time

@cache
def factorial_with_cache(num):
    return num * factorial_with_cache(num-1) if num else 1
```

## Class

### Magic Methods

Implementing `__getitem__` in a class allows its instances to use the [] (indexer) operator. 

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

Context manager. **`with`** statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. 

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

### User defined objects supporting "`with`

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

### Using `with` Parallel Programming

Refer to "Python Parallel Programming".

## Miscellaneous

### Copy

By assignment: not a copy but a reference. Changes to the original list will result into changes in the new list.

Shallow copy: new list, but inner lists are bound the original list.

Deep copy: totally new list without any dependency

### Argument passing

DIfference between immutable arguments and mutable arguments.

### Bit Operation

`n >> m`: Left move m bits of binary number n: 0b01001 >> 3 = 0b01

`1 << m`: Get a binary number with m-th digit 1: 1 << 3 = 0b100

`bin(n)`: Get a binary number string equal to n: bin(5) = '0b101'

