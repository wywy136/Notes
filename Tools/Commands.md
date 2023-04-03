# Commands for Shell

## Techniques

- `$_`: access the last argument of the previous command

- `sudo !!`: run the last command with sudo

- Use `{}` to expand the arguments:

  ```
  touch a{1,2}/b/c{1,2}
  -> touch a1/b/c1 a1/b/c2 a2/b/c1 a2/b/c2
  ```

- `shellckeck xxx.sh`: debug the shell script
- `history n`: show the history commands from n-th command to the end

## Filesystem

### /home

- contains all users' **home directories**

- On macOs, /home is replaced by /Users

### /bin

- contains programs that are installed by OS and are essential for running the OS
- e.x., `ls`, `pwd`

### /usr

- contains programs that are installed by OS
- not essential for OS, but very handy for users
- C compiler, Java VM, python interpreter

### /opt

- programs installed by third-parties (not OS)
- e.x., Google Chrome
- Contains alternate versions of apps in `/usr`

## Exploring filesystem

- `ls`: show contents under the current directory
- `pwd`: show the path to current directory

### `ls`

- `-l`: (long) show dates and size

- `-t`: (time) sort the contents by time

### Basic wildcards

- `*`: 0 or any amount of characters
- `?`: any single character

### `cd`

- `cd -` will return to the previous directory

### `less`

- opens files in read-only mode
- works only with plain text files
- How to navigate
  - PageUp and PageDown
  - **/someword** searches for a given word
  - **n** and **N** move to **next** and **previous** occurrence of the search
  - **q** closes the view and returns to shell

### `clear`

- clear output

### `man`

- `man` + any commands: get the help of the command

## Manipulating files and directories

### `mkdir`

- Use with `-p` to create nested directories

### `cp`

- `co sourcefile destfile`

- To copy one or more files to an existing directory: `cp file1 file2 destdir`

- use with `-r` to copy a whole directory
- use with `-u` to copy only sources that don't exist in destination or are newer than existing destination files

### `mv`

- Rename: `mv sourcename destname`

- Move: `mv sourcefile destdir`

### `rm`

- use with `-r` to remove a directory

- could bve used with wildcards

## File transfer

###  `scp`

- `scp SOURCE DEST`
  - SOURCE and DEST can be any combination of local and remote

### `curl`

- used to get files over HTTPS FTP etc
- `curl -0 url`: gets the URL and saves it to a file with the same name
- `curl url -o filename`: gets the URL and save it to the given filename

- Use `-L` to redirect the link to the actual file

### `zip` and `unzip`

- `unzip FILENAME [-d DEST]`:extracts to DEST dir
- use with `-l` to list the zip file's content without extracting it

- `zip ZIPFILE SOURCE1 [SOURCE2 ...]`
- use with `-r` to recurse the source directories (usually what is wanted)

## Permissions

### Intro

- A file or directory has a set of permissions for each of
  - The file's owner
  - The group
  - The world
- How permissions are represented
  - Bit 1-3: word permissions
  - bit 4-6: group permissions
  - bit 7-9: owner permissions
  - bit 10: file type
  - `r`: read, `w`: write, `x`: execute

### `chmod`

- `chmod MODE ... FILES ...`

- The mode can only be changed by the file's owner or a superuser
- sumbolic notation
  - `u, g, o/a` for user (owner), group, others (world) / all
  - `r, w, x` for read, write and exec
  - `+, -, =` to add, subtract or set
  - ![1](../../img/linux/1.png)

- Octal notation

  - ![2](../../img/linux/2.png)

  - 755 = rwxr-xr-x

## Environment

Environment is the term for information that controls the behavior of the shell and programs run by shell

### Shell variables

- can be used on the command line
- define and set arbitrary shell variables by using `=`
  - `bootcamp_dir="/home/bootcamp/"`

- When use the value of a variable, enclose its name with `${}`
  - `cd ${bootcamp_dir}`

- `echo` command simply shows a variable's value
  - `echo ${bootcamp_dir}`

- Unset a variable, assign it to `""`

### Spaces and quoting

- Quotes are not necessary
  - Only necessay if value contains spaces
  - `color=blue`
  - `color='light blue'`

### Environment variables

- They are available to subprocesses (programs run by the shell)

- `printenv` to show currently defined env var
- `export` to create an env var from a shell var
  - `export color`
- Can combine export and definitin in one statement
  - `export bird="kakapo"`
- Env var **do not persist when logout**

### $PATH

- $PATH specifies the directories that will be searched for commands
- Dirs are searched in order. The first matching executable will be used
- `which` to see where a command was found

### Adding to $PATH

- To extend the search path, append or prepend to $PATH
  - `export PATH="${PATH}:/some/other/dir"`
  - `export PATH="$/some/other/dir:${PATH}"`

### Startup files

- If want to define env vars for every shell session, can set them in one of the shell's startup files
- `~/.bash_profile`: User-specific startup file for login sessions
  - Example: logging into an ssh session
- `~/.bashrc`: User-specific startup file for non-login sessions
  - Example: running shell scripts
  - If `.bash_profile` isn’t present, `.bashrc` is the fallback
  - Many `.bash_profile` files are setup to read `.bashrc`

## I/O and Pipeline

### `n>file`

- `1>file` redirect stdout 

  - ```
    cat /proc/cpuinfo > cat.stdout
    ```

- `2>file` redirect stderr

- Ignore the output: write to a special device

  ```
  cat xxx > /dev/null 2> /dev/null
  ```

### `n>>file`

- appending stdout and stderr

  - ```
    cat /proc/cpuinfo >> cat.stdout
    cat /proc/meminfo >> cat.stdout
    ```

### `|`

- Pipelining allows to redirect the stdout form one command into the stdin of another command
- E.x., `ls /usr/bin | less`

### `sort`

- can be used to sort stdin
  - `printenv | sort | less`

### `uniq`

- By default, will show only unique lines
  - `ls /usr/bin/ /opt/conda/bin/ | sort | uniq`

- With the -d flag, uniq will show duplicate lines

  - ```
    ls /usr/bin/ /opt/conda/bin/ | sort | uniq -d
    ```

### `/dev/stdin`

- Some commands are not written to take stdin and only work on files

- Use /dev/stdin to replace the file

- e.x., diff compares to or more files

  - ```
    printenv | sort | diff /dev/stdin some_file.txt
    ```

## Text Processing

### `sort`

sort the file by line

```
sort <file>
```

sort the file by line with a column and delimiter

```shell
sort -k 2 <file> # by space
sort -k 2 -t "," <file> # by ","
```

sort in numerical order

```shell
sort -n <file>
sort -n -r <file>
```

### `uniq`

show uniqe lines in a range of consecutive lines

```shell
uniq <file>
uniq -c <file>  # show repeat num
```

### File Redirection

#### Pipeline

Overwriting

```shell
sort <file0> > <file1>
```

Appending

```shell
sort <file0> >> <file1>
```

#### `tee`

```shell
sort <file0> | tee <file1>
```

### `head, tail, cat`

```shell
head -n 10 <file>
tail <file>
tail -n +2 <file> # show the rest of the file starting from line 2 (1-indexing)
```

`cat` could be used to concatenate multiple files.

### `wc`

Word count

```shell
wc -l <file>  # conut the line
```

### `paste`

Paste all the lines from multiple files into a single file with column values

```shell
paste <file0> <file1> ...  # by default, space as delimiter
paste -d "," <file0> <file1> ...
```

### `cut`

get out a column

```
cut -f1,3 -d, --output-delimiter=":" <file> # get out the first and third column from a file with column values seperated by "," to a new file delimited by ":"
```

### `grep`

Find all lines in a file matching the pattern (a regular expression)

```sh
grep "<a pattern>" <file>
grep --color "<a pattern>" <file>
grep -P "<Peral pattern>" <file>
```

"." matches any character in an RE

Any characters between [] could be matched: `[a-zA-A]@[a-zA-Z]`

Repetition qualifiers

- "*" matches 0 or more occurences of the preceding char
- "+" matches 1 or more occurrences
- "?" matches 0 or 1 occurences
- "{m,n}" match m to n occurences

If "-" is included, make sure it is placed at the last position of a set

`(?:<some pattern>)+`: 1 or more repetition of `<some pattern>`

Filter out valid email addressed

```shell
grep -P --color "[\w.-]+@[\w-]+(?:\.[\w-]+)+" <file>
```

Use `|` to join two patterns

### `sed`

Substituting text

```shell
sed 's/old_string/new_string/' <file>  # Only the first occurences
sed 's/Linux/Unix/g' <file>  # Add flag g to replace all occurrences of string
sed 's/Linux/Unix/ig' <file>  # Add flag i to ignore case
```

Deleting text

```shell
sed 's/Linux//ig' <file>
```

Deleting lines

```sh
sed 3d <file>  # Remove the 3rd line of the file
sed '1,4d' <file>  # Remove lines 1-4 from the file
```

## Searching

### `locate`

Look for paths in the system that contains a substring

## Conda Commands

- Export an environment to a yml file

```
conda env export | grep -v "^prefix: " > environment.yml
```

- Create an environment from a yml file

```
conda env create -f environment.yml
```

- Update an environment from a yml file

```
conda activate myenv
conda env update --file local.yml --prune
```

