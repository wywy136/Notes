# Shell Scripting

Source: MPCS Unix Course & MIT Missing Semester

## Running a shell script

```
chmod u+x <file>.sh
./<file>.sh

bash <file>.sh

source <file>.sh
```

## Basic Syntax

### Interpreter

```shell
#!/path/to/bash
#!/path/to/path
```

For python recommended

```
#!/usr/bin/env python
```

### Shell variables

No space allowed for declaration

Once set, the variable is in scope until unset

```shell
AGE=64
echo "He is $AGE years old"
```

Using an undeclared variable meanas an empty value is used

When storing a multi-word string, must use quotes。

- Only double quotes will replace the `$` to its value. Not working for single quote.

### Capture command output

```shell
LS=$(ls *.txt)
echo $LS
```

### For loop

```shell
for file in *.txt; do
	mv $file ${file}2
done
```

### If-else

Must be spaced as shown:

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

## Function

- A sample function.

```shell
# mcd.sh

mcd() {
	mkdir -p "$1"
	cd "$1"
}
```

Run the function in shell

```shell
source mcd.sh
mcd test
```

- Access the i-th argument: `$i`

## Techniques

### Special $

- `$(date)`: show the current date
- `$0`: script name

- `$1, ..., \$9`: command-line arguments

- `$#`: number of arguments
- `$$`: process id
- `$@`: all the arguments
- `$?`: find the return value of the last executed command 
