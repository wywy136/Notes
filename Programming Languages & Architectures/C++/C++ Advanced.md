# C++ Advanced

## C++ Best Practice

- Rule of 3: If you define any of “copy constructor,” “copy assignment operator” or “destructor,” then define them all

- Rule of 5: if use the rule of 3, think hard about whether should define move constructors and move assignment

- Use preprocessor to prevent multiple inclusion
  ```c++
  #ifndef XXX
  #define XXX
  ...
  #endif
  ```

- Always put headers in a namespace

- Never use a namespace in a header

  - use `std::xxx` instead

- Prefer C++ versions of standard to C headers

- Prefer C++ style casts to C style casts
  ```c++
  A *a = (A *)&b; // bad
  A *a = dynamic_cast<A*>(&b); // better
  ```

- Prefer putting `const` at **right**

  - what left to `const` is const

- Define symmetric binary operators as global functions

- Think about types inferred by templates

- Watch out for method hiding

- Use `override` and `final` to indicate intent

- Throw exceptions by value and catch then by `const &`
  ```c++
  void f() { try {
         throw MyException("foo");
       } catch (exception e) { // Bad!
     //} catch (exception const &e) { // Better
  cout << e.what(); // May crash due to slicing }
  ```

- Never have a destructor throw an exception

- Use virtual destructors when inheriting

- Prefer templates to macros

- Don’t make tricky assumptions about order of evaluation - use parenthesis

- Don’t return a reference/pointer to a local variable

- Prefer range member functions to their single-element counterparts

  - The best way to copy the second half of v2 to v1
    ```c++
    v1.assign(v2.begin() + v2.size()/2, v2.end());
    ```

- Always use a smart pointer to manage lifetime of an object

- Make mutex members mutable

  - So const method can lock

- Prefer `using` to `typedef`

- Use C++20 Concepts to constrain templates

  - ```c++
    template<integral T>
    ```

- Functions that take in text should use` string_view const`

- Use uniform initialization `{}`

- Use namespace for versioning

## STL

### queue

```c++
#include <queue>          // std::queue

std::queue<int> q;
q.push(0);
int s = q.size()
int f = q.front();
q.pop();
```



## Classes

### Inheriance

#### Reference

A subclass could be refered as its father class

```c++
class Animal;
class Gorilla:public Animal;
unique_ptr<Gorilla> g = make_unqiue<Gorilla>;
Animal &a = *g;
```

#### Virtual method

A virtual function is called based on the runtime type of the object even if it is accessed through a base class pointer

Virtual method uses dynamic type, while non-virtual method uses static type

### Static

Initialize the static data members with class types in a separate `.cpp` file.

函数内的静态变量只被初始化一次，即使函数被多次调用；如果函数没有被调用，则不会被初始化

## rvalue, std::move, universal reference, std::forward

http://thbecker.net/articles/rvalue_references/section_01.html

### rvalue

- **左值（lvalue）**：表达式结束后依然存在的持久对象。
- **右值（rvalue）**：表达式结束后就不再存在的临时对象。

字面量（字符字面量除外）、临时的表达式值、临时的函数返还值这些短暂存在的值都是右值。

右值引用类型&&负责匹配右值，左值引用则负责匹配左值。

```c++
//拷贝构造函数：这意味着深拷贝
Vector::Vector(Vector& v){
    this.num = v.num;
    this.a = new int[num];
    for(int i=0;i<num;++i){a[i]=v.a[i]}
}
//移动构造函数：这意味着浅拷贝
Vector::Vector(Vector&& temp){
    this.num = temp.num;
    this.a = temp.a;
    temp.a = nullptr;    //实际上Vector一般都会在析构函数来释放指向的内存，所以需赋值空地址避免释放
}
```

移动构造函数/赋值函数的参数类型都应该是rvalue

### std::move

将原本的左值转成右值

```c++
void func(){
    Vector result;  // result is a lvalue
    //...DoSomehing with result
    if(xxx){ans = std::move(result);}   // 移动构造函数
    return;
}
```

**右值引用类型只是用于匹配右值，而并非表示一个右值。因此，尽量不要声明右值引用类型的变量，而只在函数形参使用它以匹配右值。**

```c++
Vector&& b = Vector();  // 尽管b是&&类型，但是b有变量名，可永久存在，所以b是左值
```

`x = move(y)`, we don't care about the value of y after moving

### lvalue, xvalue, prvalue in c++11

C++11使用下面两种独立的性质来区别类别：

1. 拥有身份：指代某个非临时对象
2. 可被移动：可被右值引用类型匹配

- 拥有身份且不可被移动的表达式被称作 **左值 (lvalue)** 表达式，指**持久存在的对象**或类型为**左值引用类型**的返还值。
- 拥有身份且可被移动的表达式被称作 **将亡值 (xvalue)** 表达式，一般是指类型为**右值引用类型**的返还值。
- 不拥有身份且可被移动的表达式被称作 **纯右值 (prvalue)** 表达式，也就是指纯粹的**临时值**（即使指代的对象是持久存在的）。
- 不拥有身份且不可被移动的表达式无法使用.

```c++
Vector& func1();
Vector&& func2();
Vector func3();

int main(){
    Vector a;
    a;              //左值表达式
    func1();        //左值表达式，返还值是临时的，返还类型是左值引用，因此被认为不可移动。
    func2();        //将亡值表达式，返还值是临时的，返还类型是右值引用，因此指代的对象即使非临时也会被认为可移动。
    func3();        //纯右值表达式，返还值为临时值。
    std::move(a)；  //将亡值表达式，std::move本质也是个函数，同上。
    Vector();       //纯右值表达式
}
```

`std::move()`返回的是将亡值

总结：

- **左值（lvalue）** 指持久存在（有变量名）的对象或返还值类型为左值引用的返还值，是不可移动的。
- **右值（rvalue）** 包含了 **将亡值、纯右值**，是可移动（可被右值引用类型匹配）的值。
- **形参：若参数有支持移动构造（或移动赋值）的类型，应提供左值引用和右值引用的重载版本。**
- **返还值：不要且没必要编写返还右值引用类型的函数，除非有特殊用途。**

```c++
void func1(Vector&& v){return;}
Vector func2(
  Vector a;
  return std::move(a)
)
int main(){
  Vector a;
  func1(std::move(a));
  Vector b = func2();
}
```

### Universal Reference

发生类型推导（例如模板、auto）的时候，使用T&&类型表示为万能引用，否则表示右值引用。

```c++
template<class T>
void func(T&& t){
    return;
}

int main() {
    Vector a,b;
    func(a);                //OK
    func(std::move(b));     //OK
}
```

### std::forward

当我们使用了万能引用时，即使可以同时匹配左值、右值，但需要转发参数给其他函数时，会丢失引用性质（形参是个左值，从而无法判断到底匹配的是个左值还是右值）

```c++
template<class T>
void func(T&& object){
    doSomething(std::forward<T>(object));
}
```

object可能被匹配为左值或右值，如果不借助std::forward，object一律被视为左值引用类型

## Multi-thread & Concurrency

### Thread

#### mutex

将mutex声明为mutable，可以在const函数中修改mutex

#### join()

线程对象调用次方法，知道线程完成了它的函数的任务时，才返回

线程对象所在的调用线程被阻塞，直到join()返回后才继续执行

#### detach()

与join相反，调用线程不用等待子线程结束才继续运行，而是直接运行，所以可能调用线程已经结束但子线程还没有结束

#### std::ref()

线程函数模版不知道f通过reference的方式获得参数，所以如果要给线程里的函数传引用参数，必须通过ref()

### Lock

#### std::scoped_lock

https://en.cppreference.com/w/cpp/thread/scoped_lock

**The scoped_lock is a strictly superior version of lock_guard** that locks an arbitrary number of mutexes all at once

声明`std::scoped_lock`自动加锁，作用域`{}`结束自动解锁

Used for locking multiple mutexes.

Not copyable

#### std::unique_lock

https://en.cppreference.com/w/cpp/thread/unique_lock

Movable, not copyable

Used for locking one mutex.

Compared to `scoped_lock`, has a series of features, and is copyable.

相比于`std::lock_guard`，可以手动加锁解锁从而控制锁控制的区域，不需要用作用域来限定

#### std::shared_lock

Motivating use case

- Multiple threads can read from a data structure at the same time as long as no thread is modifying it - shared_lock

- If a thread is modifying the data structure, it should acquire sole ownership of the object so no thread sees the data structure in a partially modified state - unique_lock

```c++
std::list<int> some_list; 
std::shared_mutex some_mutex;
void add_to_list(int new_value) {
  std::unique_lock guard(some_mutex); // Unique writer access
  some_list.push_back(new_value);
}
bool list_contains(int value_to_find) {
	std::shared_lock guard(some_mutex); // Shared reader access return
}
```

### Conditional Variable

用来同步线程：线程1阻塞，等待线程2调用`notify_one()`

Producer-Consumer

```c++
std::mutex m;
std::conditional_variable cv;
void data_preparation_thread(){
  lock_guard lk(m);
  data_queue.push(data);
  cv.nofify_one();
}
void data_processing_thread(){
  std::unique_lock<mutex> lk(m);
  cv.wait(lk, []{return !data_queue.empty()});
  data = data_queue.pop();
  lk.unlock();
  process(data);
}
```

### Async

#### Future & Promise

刚实例化的future是没有储存值的，但在调用std::future对象的get()成员函数时，主线程会被阻塞直到异步线程执行结束，并把返回结果传递给std::future.

使用时，从 [std::promise](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.cppreference.com%2Fw%2Fcpp%2Fthread%2Fpromise) 的`get_future()`得到 [std::future](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.cppreference.com%2Fw%2Fcpp%2Fthread%2Ffuture)，再从 [std::future](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.cppreference.com%2Fw%2Fcpp%2Fthread%2Ffuture) 中得到在 [std::promise](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.cppreference.com%2Fw%2Fcpp%2Fthread%2Fpromise) 端通过`set_value()`写入的值。如果在从 [std::future](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.cppreference.com%2Fw%2Fcpp%2Fthread%2Ffuture) 获取值时，[std::promise](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.cppreference.com%2Fw%2Fcpp%2Fthread%2Fpromise) 并未写入，那么 [std::future](https://links.jianshu.com/go?to=https%3A%2F%2Fzh.cppreference.com%2Fw%2Fcpp%2Fthread%2Ffuture) 所在的线程将阻塞。

#### packaged_task

将一个**普通的可调用函数对象转换为异步执行的任务**

Moveable, not copyable

```c++
std::packaged_task<int(int,int)> task(sum);
std::future<int> future = task.get_future();
std::thread t(std::move(task), 1, 2);
cout << future.get();
t.join();
```

### Cache-conscious programming

## Generic Programming

### Type Erasure

https://fuzhe1989.github.io/2017/10/29/cpp-type-erasure/

首先定义内部基类（Concept）

```c++
class CounterBase {
public:
    virtual ~CounterBase {}  // This class is meant to be inherited
    virtual void Increase(int v) = 0;
    virtual void Decrease(int v) = 0;
}
```

使用类模版实现子类（Model），存储实际对象

```c++
template <typename T>
class CounterImpl:public CounterBase{
private:
    T mImpl;
public:
    explicit CounterImpl(T t): mImpl(std::move(t)) {}
    void Increase(int v) override {
        mImpl.Increase(v);
    }
    void Decrease(int v) override {
        mImpl.Decrease(v);
    }
}
```

使用一个单独的类（非模版化的类）表示所有满足条件的类型，声明一个虚基类指针，并在构造函数指向实际的类（通过模版参数和CTAD）。在所有的方法中通过虚基类指针进行调用实际类的方法。

```c++
class Counter {
private:
    std::unique_ptr<CounterBase> mPtr;  // 指向concept的pointer
public:
    // 模版化的构造函数，pointer赋值为model<T>
    template <typename T>
    Counter(T&& t): mPtr(new CounterImpl(std::forward<T>(t))) {}
    void Increase(int v) {
        mPtr->Increase(v);
    }
    void Decrease(int v) {
        mPtr->Decrease(v);
    }
};
```

### Template

https://github.com/wuye9036/CppTemplateTutorial#1-template%e7%9a%84%e5%9f%ba%e6%9c%ac%e8%af%ad%e6%b3%95

#### CTAD

部分参数推导：先写需要制定的模版参数，再把能推导出来的模版参数放在后面

```c++
template <typename DstT, typename SrcT> DstT c_style_cast(SrcT v)	// 模板参数 DstT 需要人肉指定，放前面
{
    return (DstT)(v);
}

int v = 0;
float i = c_style_cast<float>(v);  //可以推导SrcT，DstT读取float
```

#### Specialization, Partial Specialization

任何specialization必须有一个primary template，其中参数数量是specialization具有的参数数量

对内容不同，但是模版参数形式相同的类进行区分

```c++
// 模板的基本形式
template <typename T> class AddFloatOrMulInt;
// 这个类给T是int的时候用
template <> class AddFloatOrMulInt<int>;
```

```c++
template <typename T> class TypeToID
{
public:
    static int const ID = -1;
};

template <> class TypeToID<uint8_t>
{
public:
    static int const ID = 0;
};

TypeToID<uint8_t>::ID = 0;
TypeToID<double>::ID = -1;  // 类模版的“原型”形式
```

特化之间、特化和它原型的类模板之间，是分别独立实现的，不一定需要具备同样的内容

对指针类型进行特化：

```c++
template <typename T> // 需要一个T
class TypeToID<T*> // 要对所有的指针类型特化，所以这里就写T*
{
public:
    static int const ID = 0x80000000;
};
```

创建新类的时候回去匹最合适的模版类特化

偏特化

```c++
template <class T2>
class A<int, T2>{
    ...
};
```

### Concept - only for c++20

用于确定一个类具有某些行为/属性，类似于基类，但是不需要定义基类

```c++
template<typename T>
concept Animal = requires(T a) {
    { a.eats() } -> convertible_to<string>;
    { a.name() } -> convertible_to<string>;
};

struct Cat {
    string eats() { return "delicious mice"; }
    string name() { return "cat";}
};

int main() {
    Animal auto a = Cat();
    cout << "A " << a.name() << " eats " << a.eats();
}
```

Cat类一定具有Animal的concept

#### Contraining templates using concept

使用concept限制模版参数的类别：只接受整数类型

```c++
template <integral T>
T gcd(T a, T b){...}
```

只接受可随机访问的迭代器类型

```c++
template<random_access_iterator it>
```

## Others

### Lambda

#### return values

If your lambda does not contain return statements that return different types, the compiler can usually figure out the return type without your saying anything

If needed, you can explicitly specify the return type with the following notation

```c++
[](int x, int y) -> int {
  int z = x + y; return z + x; 
}
```

#### capture

可以在lambda内部访问外部的变量

- `=` 按值捕获
- `&` 按引用捕获

### Keywords

#### explicit

在类的构造函数前加上explicit关键字，可以防止形参隐式转换为该类类型的转换

#### if constexpr

Saying `if constexpr` rather than just `if` tells the compiler not to compile the branch not run if the condition is known at compile-time

`constexpr` means the value is known at compile- time

`constexpr` functions run at complie time

#### decltype & invoke_result_t

`decltype(x)` gives you the type of x

```c++
template<typename Func, typename ... Args>
(Func f, Args ... args)
using RetType = decltype(f(args...));
packaged_task<RetType(Args...)> pt(f);
```

Advanced: `std::invoke_result_t<>` and `std::decay_t<>`

```c++
template<typename Func, typename ... Args>
(Func&& f, Args&& ... args)
using RetType = std::invoke_result_t<std::decay_t<Func>, std::decay_t<Args>...>
```

Note: prefer `using` to `typedef`

### Features

#### tuple & structured bindings

used for funtions returning multiple values

`auto[page, err] = getPage()`

#### string_view

对字符串一种只读取不修改的类型，比const string类型速度更快

### range - only for c++20

https://www.jianshu.com/p/75316eed8566

```c++
int main()
{
    auto const ints = {0,1,2,3,4,5};
    auto even = [](int i) { return 0 == i % 2; };
    auto square = [](int i) { return i * i; };
 
    // "pipe" syntax of composing the views:
    for (int i : ints | std::views::filter(even) | std::views::transform(square)) {
        std::cout << i << ' ';
    }
 
    std::cout << '\n';
 
    // a traditional "functional" composing syntax:
    for (int i : std::views::transform(std::views::filter(ints, even), square)) {
        std::cout << i << ' ';
    }
}
```

### std

#### std::function

使用`std::function<R(Args...)> `表示一个通用的可调用对象

```c++
std::function<R(Args...)> callable;
```

