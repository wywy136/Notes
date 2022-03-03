# JAVA自学笔记与积累

## 积累

java.util.Arrays.toString：将整形数组转化为字符串

## B站java课程

### 基础速成

链接：https://www.bilibili.com/video/BV19X4y1M7RH?p=2

#### JDK JRE JVM

![1625215881719](C:\Users\Yu Wang\AppData\Roaming\Typora\typora-user-images\1625215881719.png)

JVM具有跨平台性

#### JAVA程序运行命令

javac：java源文件->class字节码文件(0, 1)

java：运行class文件

#### 基本语法

- 权限修饰符

|           | 类内部 | 本包 | 子类 | 外部包 |
| --------- | ------ | ---- | ---- | ------ |
| public    |        |      |      |        |
| protected |        |      |      | x      |
| default   |        |      | x    | x      |
| private   |        | x    | x    | x      |

- 每个.java文件里只能有一个公共类

#### 常量变量

基本数据类型；引用数据类型

强制数据类型转化：c = (int) b

#### 数组

- 数组初始化方法

- 动态

  ```java
  int [][] array = new int [3][];
  array[0] = new int [3];
  int [][] array = new int [3][2];
  array[0][0] = 2
  ```

- 静态

  ~~~java
  int array [][] = new int [][]{{1, 2, 3}, {2, 4}}
  ~~~

- 常见操作
  
  - 数组长度：array.length
  
  - 遍历
  
    ```java
    for (int m:a){
        System.out.println(m);
    }
    ```
  
  - 复制
  
    ```java
    int b [] = Arrays.copyOf(a, n)
    ```
  
  - 排序：Arrays.sort(a)

#### 输入输出

- 输入：Scanner(System.in)
- 格式化输出：printf("输出为 %d", i)

#### 继承

```java
class A [extends 父类名] [implements 接口名]
```

- object类是所有类的父类，新类的声明默认继承这个类，包含一系列方法
- 子类有父类非私有的方法
- 可重写父类的方法

#### 构造方法

- 有参构造函数
- 无参构造函数
- 构造时替换掉set函数

```java
public class Person {
    private String name;
    private int age;
    
    public Person(String name){
        this.name = name;
    }
    
    public Person(int age){
        this.age = age;
    }
    
    public Person(String name, int age){
        this.name = name;
        this.age = age;
    }
}

Person p = new Person(name: "", age: 0)
```

#### 重载和重写

- 重载
  - 必须同一个类中
  - 方法名相同
  - 方法的参数个数、顺序、类型不同
  - 与方法修饰符或返回值无关
- 重写
  - 一个子类一个父类
  - 重写的方法必须和父类一样（返回值类型、方法名、参数列表）
  - 子类的权限必须等于或宽松于父类的权限

#### this super

- this：对当前对象的代指，只能用在非静态方法中
- super：用在子类方法中，用于指向子类对象中的父类对象，可以访问父类的属性，函数以及构造函数

#### static final

- static：不需要实例化即可调用
- final：所修饰的方法不能被重写，但是子类可以用父类中final修饰的方法

#### 抽象类

```java
public abstract class Test {
    普通变量、方法；公共静态变量、抽象方法
    public abstract void myPrint();
}
```

子类必须实现父类的抽象方法

#### 接口

- 接口中所有的方法默认public abstract（可省略）

- 变量只能为public static final类型（不可被改变的共有静态常量，可省略）

  ```java
  public interface User {
      int age = 33;
      void myprint();
      void insert(A a);
  }
  
  public class UserTest implements User {
      public void myprint(){
          ...
      }
      public void insert(A a){
          ...
      }
  }
  ```

- 接口与抽象类

  - 接口被子类实现、抽象类被继承
  - 变量类型不同
  - 方法的声明 or 方法的声明、实现
  - 接口中不可有构造函数
  - 接口可实现多个，继承只能继承一个
  - 接口的方法都是抽象的，抽象类中也可以有非抽象方法

#### 多态

- 条件：继承、重写、父类引用指向子类对象

  ```java
  class Parent{
      void f(){
          111
      }
  }
  class Son extends Parent{
      void f(){
          222
      }
  }
  class Test{
      void main(){
          Parent p = new Son();
          p.f() -> 222
      }
  }
  ```

- 向上转型：子类赋给父类 Parent p = new Son()，不可调用子类独有的方法
- 向下转型：父类赋给子类 Son s = (Son) p，可以调用子类独有的方法，而且必须先得到向上转型的对象，再向下转型

#### 异常

- try - catch- finally
- 无论异常是否发生，都会执行finally里的逻辑
- throws放在方法后面，throw放在catch里

#### JAVA常用类库

- String：charAt, indexOf, equals, startsWith, toCharArray, trim, 
- StringBuffer：可变字符串
  - append, insert, delete, reverse
- Random
- Math

