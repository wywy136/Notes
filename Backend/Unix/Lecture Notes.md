# Lecture Notes

## Unix Architectures

### Layers

- **Hardware** - includes computer resources (the CPU, RAM, and input/output devices) connected to the Unix system
- **Kernel** - The central program of the operating system that manages the hardware and acts as an *interface between users and hardware*. The Kernel performs tasks like process scheduling, memory and file management, etc.
- **Shells** - Acts as an *interface between user and the kernel*. Interprets and executes commands entered by the user and provides an answer. Unix includes various kinds of shells such as C shell, Bourne again shell and Korn shell and more.
- **User**: An entity that logins into a Unix system and communicates with the system through a shell and/or utilities and applications.
- **Commands**: Small programs provided by the operating system to perform file, text, and system tasks needed by the user. Unix provides more are more than 200 commands along with 3rd party commands.
- **User Applications** - Third-party programs installed by the user.

### Kernel

- Process scheduling - a program executing on system is known as a process.
- Main memory management
- Managing devices (keyboard, mouse, hard drives)
- Networking
- Filesystem
- Switching between kernel space and user space

### Users

- A unique login name (username) and a numeric user ID (UID)
- Group ID
- Home directory
- Login shell

## Programs, Process & Memory Management

### Programs

Parts of a Program File

- Binary format Identification: format about the program file, usually use Executable and Linking Format (ELF)
- Machine-language instructions
- Program entry-point address (ELF header)
- Data: values used to initialize variabels and also literal constants used by the program
- Symbol and relocation tables: Tables that describe information about the locations of functions and variables in the program
- Shared-library and dynamic-linking information

```sh
readelf -h <program_file>
readelf -x .rodata <program_file>
```

### Process

#### Init Process

- It’s program file is located in /sbin/init.
- It’s PID is always 1
- All processes on the system are created by init or a descendants of it.
- The init process cannot be killed (not even by the superuser) and is only terminated when the system shut downs.

#### Daemon Process

- A long running process that typically is started at system boot up and remains active and running until the system shuts down.
- Runs in the background and has no interaction with a user or the terminal via retrieving input and producing output.

- Example Daemon Processes
  - Init process
  - syslogd - records messages in system log
  - httpd - servers web pages via HTTP

### Memory Management

Each process runs in its own memory sandbox, known as a virtual address space

- OS Kernel Space: 1GB
- User Mode Space: 3GB, deducted from the space needed by the operating system

#### **Process Virtual Address Space**

- Stack: function calls, args, return values
- Heap
- BSS: global/static variables that are not explicitly initialized
- Data: global/static variables that are initialized by the programmer
- Text: executable instructions of a program

#### Virtual Memory Management

Virtual memory management splits a program’s memory space into small fixed-size units called pages

The operating system maintains a page table for each process, which maps pages to physical page frames in RAM.

#### VM and Swap Space

Simply put, virtual memory is a combination of RAM and disk space that running processes can use.

Swap space is the portion of virtual memory that is on the hard disk, used when RAM is full.

At any time, only a few pages of a program resides in RAM. These pages are known as the resident set. When a process references a page not in the resident set then a page fault occurs, which makes the kernel go grab that page from the swap area and load it into RAM.

## Exceptional Control Flow

### Exceptions

An exception is a transfer of control to the OS *kernel* in response to some event (i.e., change in processor state).

Asynchronous Exceptions: Caused by events external to the processor

- Timer interrupt
- I/O interrupt from external device

Synchronous Exceptions: Caused by events that occur as a result of executing an instruction

- **system calls**, breakpoint traps, special instructions
- pagefaults (recoverable) , protection faults (unrecoverable), floating point exceptions
- illegal instruction, parity error, machine check

### System Calls

#### Error Messages

```c
#include <stdio.h> 
#include <stdlib.h> 
#include <errno.h> 
#include <string.h> 
int main() {
    FILE * fd;
    fd = fopen("file_does_not_exist.txt", "r"); 
    if (fd == NULL) {
        char * str = strerror(errno);
        printf("Error Number=%d, Error String=%s\n",errno, str); 
        perror(str);
        exit(EXIT_FAILURE);
    }
    return 0; 
}
```

### Process Control

Process provides each program with two key abstractions

- Logical control flow
- Private address space

#### Context Switching for Multiprocess

All the processed share the same kernal memory

Process A in user code -> **kernel code** -> Process B in user code -> **kernal code** -> Process A in user code

#### Concurrent Processes

Two processes run concurrently (are concurrent) if their flows overlap in time

#### Obtaining Process IDs

```c
# include <sys/types.h> 
pid_t getpid(void)
```

#### Creating and Terminating Processes

One of three states

- Running
  - Process is executing or waiting to be executed
  - Forground job - connects to the terminal, communicate with a user via the screen and keyboard
  - Background job - disconnects from the terminal and cannot communicate with the user 
  - `ps ux`: check all processes running under the current user
  - `ps PID`:  check the process status of a single process
  - `pidof Process_name`: find the PID of a process

- Stopped
  - Suspended, will not be scheduled
    - Stopped by `^Z`
  - `fg jobname`: continue a program which was stopped and bring it to the foreground
  - `bg jobname`
- Terminated
  - Stopped permanetly

#### Terminating Processes

- Receiving a signal whose default action is to terminate
- Returning from the `main` routine
- Calling the `exit` function

#### Creating a process

Code under `folk` are executed by multiple processes

Called once but returns twice, runs concurrently, duplicate but seperate address space, shard open files

Returns 0 for child process, and child process id for parent process

```c
int main() {
    pid_t pid;
    int x = 1;
    pid = Fork();
    if (pid == 0) {  /* Child */
        printf("child : x=%d\n", ++x);
       exit(0);
}
/* Parent */
    printf("parent: x=%d\n", --x);
    exit(0);
}
```

#### Reaping Child Processes

Exited child process with parent process still running

Zombie process is annotated with `<defunct>`

#### `wait`: synchronizing with Children

Suspends current process until one of its children terminates

If `child_status != NULL`, then the integer it points to will be set to a value that indicates reason the child terminated and the exit status

```c
void fork9() {
    int child_status;
    if (fork() == 0) {
        printf("HC: hello from child\n");
       exit(0);
    } else {
        printf("HP: hello from parent\n");
        wait(&child_status);
        printf("CT: child has terminated\n");
    }
    printf("Bye\n");
}
```

`waitpid`: wait for a specific process

#### `execve`: Loading and Running Programs

All command-line arguments have be ended with NULL

Take over and create a brand new process

## File System

### I-nodes

The i-node table contains an i-node for each file in the file system

- Contains information about a single file in the file system

### Virtual File System (VFS)

A kernel feature that resolves the problem of different implementations of file systems by creating an abstraction layer for file-system operations.

- The VFS defines a generic interface for file-system operations.

### Mount and Umont File systems

