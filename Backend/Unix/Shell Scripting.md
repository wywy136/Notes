# Shell Scripting

## Basic syntax

### Interpreter

```shell
#!/bin/bash
```

### Running a shell script

```
chmod u+x <file>.sh
./<file>.sh

bash <file>.sh

source <file>.sh
```

### Shell variables

No space allowed for declaration

Once set, the variable is in scope until unset

```shell
AGE=64
echo "He is $AGE years old"
```

Using an undeclared variable meanas an empty value is used

When storing a multi-word string, must use quotes

### Capture command output

```shell
LS=$(ls *.txt)
echo $LS
```

### Command-line arguments

$0: script name

$1, ..., \$9: arguments

$#: number of arguments

### For loop

```shell
for file in *.txt; do
	mv $file ${file}2
done
```

### If-else

Must be spaces as show

```shell
if [ <test> ]; then
	<commands>
elif [ <test> ]; then
	<commands>
else
	<commands>
fi
```

### Test operators

![截屏2022-10-02 下午7.51.33](/Users/yuwang/Library/Application Support/typora-user-images/截屏2022-10-02 下午7.51.33.png)

![截屏2022-10-02 下午7.53.17](/Users/yuwang/Library/Application Support/typora-user-images/截屏2022-10-02 下午7.53.17.png)

### Command line I/O

#### `read`

```shell
read -p "What's your name?" name
```

