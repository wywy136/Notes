### 字符串

C风格字符串，使用cin.getline()读取一整行

### 指针

指针+1后，其增加的值=指向的类型占用的字节数

### 运算符重载

```c++
operator op(argument list)
```

#### 友元

重载运算符有友元和非友元两种方式

### 类和动态内存分配

C++提供的特殊成员函数

- 默认构造函数
- 默认析构函数
- 复制构造函数
  - 最好定义显示复制构造函数
  - 深复制指针
- 赋值运算符
- 地址运算符

![1631114102833](C:\Users\Yu Wang\AppData\Roaming\Typora\typora-user-images\1631114102833.png)

### 继承

#### 静态成员变量、函数

静态成员变量

- 所有对象共享同一份数据
- 编译阶段就分配内存
- 类内声明类外初始化

静态成员函数

- 只能访问静态成员变量

继承同名静态成员

- 通过对象访问 s.Base::A
- 通过类名访问 Son::Base::A

### 多态

静态多态的函数地址早绑定 - 编译阶段确定函数地址

动态多态的函数地址晚绑定 - 运行阶段确定函数地址

动态多态满足条件

- 有继承关系
- 子类重写父类的虚函数（区别于重载，重写要求返回值类型、名称、参数列表要完全相同）

使用：父类的指针或引用指向子类对象
