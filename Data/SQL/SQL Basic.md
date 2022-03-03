# SQL 学习笔记

## 基本语句

sql的基本语句顺序不可改变：SELECT FROM WHERE ORDER BY

SELECT 对于数字对象可以进行数学运算后取数 使用AS可以改名字，添加引号可以增加空格 DISTINCT可以去除重复项

WHERE+AND OR NOT进行筛选，使用括号

IN用于组合多个筛选条件，使用小括号

BETWEEN+AND用来比较范围

L IKE匹配字符串；%表示任意多任何字符；_表示一个任何字符，可以重复添加

REGEXP: ^+s表示以s开头的字符串，s+$表示以s结尾的字符串，｜表示多个搜寻模式，[-]表示多个字符的匹配

ORBER BY可以组合多个排序条件；可以加上DESC；用于排序的内容不一定要被选出，也不一定是表格中的一列，可以是一个表达式，还可以是SELECT时赋予的alias

**LIMIT a OFFSET b：a是选取的数量，b是忽略的数量（常用于第n大问题）**

## JOIN

INNER JOIN连接多个表，使用ON指定条件

SELF JOIN时需要指定不同的别名

JOIN可以进行多表连接，使用AND进行复合条件连接

OUTER JOIN返回所有记录，无论某一表中的记录是否满足条件

- LEFT JOIN返回左表所有的记录，不管条件正确还是错误
- RIGHT同上

使用USING代替ON，当join的两个表有相同的列名称时

- USING (column name，)

CROSS JOIN组合所有的item

UNION结合多个查询结果的行，但是必须保证列数一样；

## 插入删除

列属性

- PK：主键（唯一标识一行）
- NN：非空的值
- AI：自动增加
- Default：默认值

INSERT INFO () + VALUES () 插入一行或多行，可以在VALUES部分指定哪些赋值哪些用默认值，但必须按照列顺序；也可以在INFO后面制定，还可以改变列的顺序

使用LAST_INSERT_ID()内置函数来获取新插入行的id，用于在另一个表中插入数据

使用CREATE_TABLE AS来从一个表复制得到另一个表，但是mysql不会复制主键和自动增加属性

UPDATE SET更新一行或多行数据，通过WHERE制定条件

DELECT FROM用于删除

## 聚合函数

MAX MIN AVG SUM 

COUNT包含重复值，可以用COUNT(DISTINCE)去重

聚合函数只运行非空值，括号里可以写表达式

GROUP BY分组求和，永远出现在FROM和WHERE子句之后，在ORDER BY子句之前

HAVING子句在分组之后对数据进行筛选，WHERE在分组之前

- Having常用于去除分组后的重复：Having count(*)

当选择语句中有聚合函数，而且正在对数据进行分组，可以直接根据select子句里的所有列来进行分组（GROUP BY）

WITH ROLLUP用于聚合的列，计算每组的总和（多列分组时）和所有组的总和

分组排序并在组内赋予序号

```sql
dense_rank() OVER (partition by DepartmentId Order By Salary Desc)
```

- dense_rank()在排序内容相同时赋予相同的序号
- 几个常见的窗口函数
  - row_number:返回连续的排序，无论值是否相等 - 1，2，3，4
  - rank：具有相等值得行排序相同，序数值随后跳跃 - 1，2，2，4
  - dense_rank:具有相等值得行排序相同，序号是连续 - 1，2，2，3

## 复杂查询

IN运算符用于筛选，返回一列数据

![SQL学习笔记](../img/sql/SQL学习笔记.png)

自查询会返回一个数、一列数或一张表，对于一列数，可以ALL来整合

ANY：同ALL，返回大于任意返回值的行

相关子查询：内查询需要借助外查询

EXISTS可以替代在WHERE中使用IN，避免返回大量数据后的比较，而是一条一条添加，在大量数据的时候更高效

SELECT字句中也可以用子查询，不可以使用别名但是可以用SELECT + 别名

## 内置函数

数值函数

- ROUND：四舍五入，可以选择保留几位小数

- TRUNCATE：保留小数位数

- CEILNG：向上取整
- FLOOR：向下取整
- ABS：绝对值
- RAND：生成0-1之间的随机数 

字符函数（sql中从1计数而不是0）

- LENGTH：返回字符串长度
- UPPER/LOWER：大写/小写
- LTRIM：去掉字符串开始的空格
- RTRIM：去掉字符串结尾的空格
- TRIM：删除所有前置后置空格
- LEFT/RIGHT：选择左侧、右侧的n个字符
- SUBSTRING：选择起始、结束位置的字符串
- LOCATE：返回制定字符串第一次出现在字符串中的位置
- REPLACE：替换字符串一部分
- CONCAT：拼接两个字符串

日期时间

- NOW/CURDATE/CURTIME
- YEAR/MONTH/DAY/HOUR/MINUTE/SECOND/DAYNAME/MONTHNAME(NOW())
- EXTRACT：所有sql通用
  - EXTRACT(YEAR FROM NOW())
- DATE_FORMAT：从yyyy-mm-dd得到更合适的日期表达方式
- 增加/删减日期：DATE_ADD(NOW(), INTERVAL n DAY)
- TIME_TO_SEC：得到从午夜开始的秒数

COALESE()：返回一堆值中的非空值

IF(experssion, first, second)：e？f：s

CASE WHEN THEN结合多个判断条件

## 视图

CREATE VIEW name AS

视图可以当作普通的表格一样使用，但是视图不存储数据

DROP VIEW name删除视图

CREATE OR REPLACE更新视图

可更新视图：可以插入（INSERT）、删除（DROP FROM）、修改（UPDATE SET）数据的视图，其中不能包含

在创建视图的最后加上WITH CHECK OPTION可以防止DELETE、UPDATE操作导致某一行消失

## 存储过程

存储过程是一个包含一堆SQL代码的数据库对象，在应用代码里调用这些过程来获取或保存数据

- 存储、组织SQL代码
- 更快的执行
- 数据安全

CREATE_PROCEDURE name() BEGIN END

使用DELIMITER指定分隔符，一般用$$

CALL调用存储的过程

存储过程里的每一条语句都要用分号结尾

DROP PROCEDURE IF EXISTS删除存储过程

带默认值的参数：IF p IS NULL THEN SET p = v END IF

IFNULL用于判断传入的第一个参数是否为NULL，如果是NULL，返回第二个参数![ifnull](../img/sql/ifnull.png)

验证参数范围，IF THEN SIGNAL SLQSTATE；SET_MESSAGE_TEXT

输出参数：参数列表里加上OUT，SELECT之后添加INTO

SET @定义全局变量![output](../img/sql/output.png)

DECLARE声明存储过程内的本地变量，存储过程结束变量消失 可用DEFAULT指定默认值

CREATE FUNCTION创建函数 RETURNS + 变量类型

函数必须具有一些属性

### 触发器

CREATE TRIGGER 

命名规则：表名-之前/之后-操作![Trigger](/Users/yuwang/Desktop/学习笔记/Study-scripts/img/sql/Trigger.png)

SHOW TRIGGERS显示已经创建好的触发器

DROP TRIGGER IF EXISTS删除触发器

CREATE EVENT创建事件，ON SCHEDULE指定频率，DO BEGIN END

### 事务

事务包含的一系列操作应该都被完成，否则所有的操作退回重做

使用事务使数据库处于一致状态

每个事务都互相隔离，一个事务执行完另一个事务才可以执行

