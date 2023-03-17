# C Programming

## Lib Funcs

### `strsep()`: split line

```c
char * strsep(char **stringp, const char *delim);
```

```c
#include <stdio.h>
#include <string.h>

int main()
{
    char *string,*found;

    string = strdup("Hello there, peasants!");

    while( (found = strsep(&string, " ")) != NULL )
        printf("%s\n",found);

    return(0);
}
```

Output

```
Hello
there,
peasants!
```

## Kernal Funcs

### `open` & `close`: work with a file

```c
int fd;
fd = open("./data.txt", O_RDONLY);
if (fd != -1) {
    //
}
close(fd);
```

### `read`: read from a file

```c
int nBytesRead;
char buffer[256];
nBytesRead = read(fd, buffer, 10);
```

