Instructor: Tue, 4:30-6:30 JCL

TA: times TBD, remote

### Midterm

#### Topics

- **binary algebra and truth tables**
- **binary arithmetic**
- **negative numbering systems (sign-magnitude, ones complement, twos complement)**
- **logic circuit design**
- **Karnaugh maps**
- **combinatorical chips**
- **sequential chips**
- **hardware description language (HDL)**
- **how the ALU, CPU, and memory work in the Hack computer**
- **fetch/execute cycle**
- **Von Neumann machines**
- **the correlation between machine language and assembly language**
- **Hack assembly language**
- **the Hack assembler**

#### Negative numbering systems

Sign-magnitude

- 4-bit: 15 numbers, 2 zeros

1's complement

- flip the bits for negative numbers
  - -1: 1110
  - -2: 1101
- 15 numbers for 4-bit, 2 zeros

2's complement

- flip the bits, then + 1
  - -1: 0001 -> 1110 -> 1111
  - -2: 0010 -> 1101 -> 1110
- 4-bit: -8 ~ 7

#### ALU

- x, y, zx, nx, zy, ny, f, zo -> out, zr, ng

#### Combinatorical chips & sequential chips

#### Hack Language

Instructions

![截屏2022-02-07 下午10.28.40](/Users/yuwang/Library/Application Support/typora-user-images/截屏2022-02-07 下午10.28.40.png)

C-instruction:

1 x x (0-A|1-M) zx nx zy ny f zo A D M j j j 

#### Von Neumann machines

![截屏2022-02-08 下午2.31.41](/Users/yuwang/Library/Application Support/typora-user-images/截屏2022-02-08 下午2.31.41.png)

#### CPU

Each instruction tells the CPU which computation to perform, which registers to access, and which instruction to fetch and execute next. 

The CPU executes these tasks using three main elements: An Arithmetic Logic Unit (ALU), a set of registers, and a control unit.

- ALU
- D Register: only for storing data values
- A Register
  - storing a data value (like D)
  - selecting address in instruction memory
  - selecting address in data memory

![截屏2022-02-08 下午3.14.31](/Users/yuwang/Library/Application Support/typora-user-images/截屏2022-02-08 下午3.14.31.png)

If one of the destination registers is M, the CPU’s outM output is set to the ALU output, and the CPU’s writeM output is set to 1.

![截屏2022-02-08 下午3.27.12](/Users/yuwang/Library/Application Support/typora-user-images/截屏2022-02-08 下午3.27.12.png)

- Mux16-1: instruction[15]
- ARegister: not instruction[15] (is a A-instruction) | instruction[5] (dest includes A)
- Mux16-2: instruction[12] (0 for ARegOut, 1 for inM)
- DRegister: instruction[15] (is a C-instruction) & instruction[4] (dest includes D)
- writeM: instruction[15] (is C-instruction) & instruction[3] (dest includes M)
- ALU: instruction[11..6] (comp)
- PC
  - inc: always true
  - load
    - Instruction[2] (JLT;JNE;JLE;JMP) & ng & instruction[15]
    - Instruction[1] (JEQ;JGElJLE;JMP) & not zr & instruction[15]
    - Instruction[0] (JGT;JGE;JNE;JMP) & not zr & not ng & instruction[15]

## Final

- compilers
- data types
- data life cycles
- mapping variables to memory segments in Jack
- expressing high-level Jack commands in VM
- writing programs in Jack
- expressing VM code in assembly language

### Ch7

- RAM

![截屏2022-03-13 下午5.13.09](/Users/yuwang/Library/Application Support/typora-user-images/截屏2022-03-13 下午5.13.09.png)

![截屏2022-03-13 下午5.13.20](/Users/yuwang/Library/Application Support/typora-user-images/截屏2022-03-13 下午5.13.20.png)

#### Mapping variables to memory segments in Jack

- Pointer
  - Pointer 0 = THIS
  - Pointer 1 = THAT

- Temp
  - Any access to temp i, should translated into assembly code to RAM[5 + i]
- Static
  - static variables that appear in a VM program to be mapped on addresses 16 and onward, *in the order in which they appear in the VM code*

#### Data Types

Single 16-bit data type could be used as

- Integer: -32768 - 32767
- Boolean: 0 or -1
- Pointer: 0 to 24k

### VM -> Assembly

