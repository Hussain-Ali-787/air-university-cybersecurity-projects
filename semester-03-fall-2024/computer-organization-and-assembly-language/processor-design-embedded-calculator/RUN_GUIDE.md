# Run Guide

## Environment
This project uses MASM assembly with the Irvine32 library.

## Requirements
- Windows
- Visual Studio with C++ desktop development workload
- MASM enabled
- Irvine32 library configured
- x86 target

## Steps
1. Open Visual Studio.
2. Create or open a MASM/Irvine32 project.
3. Add `code/main.asm`.
4. Configure Irvine32 include and library directories.
5. Build in x86 mode.
6. Run the program.

## Program Flow
1. Menu is displayed.
2. User enters first number.
3. User enters second number.
4. User enters operation code.
5. Result or error is displayed.
6. Program loops until opcode `99`.

## Opcodes
| Opcode | Operation |
|---:|---|
| 1 | ADD |
| 2 | SUB |
| 3 | MUL |
| 4 | DIV |
| 5 | AND |
| 6 | OR |
| 99 | EXIT |
