# Project Notes

## Purpose
The purpose of this COAL project is to design a simplified processor for an embedded calculator and simulate its behavior using assembly language.

## Learning Goals
- Understand processor organization
- Design a small instruction set
- Understand CU, ALU, registers, memory, and I/O roles
- Explain bus and datapath communication
- Implement arithmetic and logical operations in assembly
- Test execution behavior and edge cases

## Important Design Decisions
The design uses a simple calculator-oriented instruction set with arithmetic, logical, and exit operations. The processor architecture includes a Control Unit, ALU, register array, memory unit, input, and output.

## Testing Summary
The code was tested for ADD, SUB, MUL, DIV, AND, OR, invalid opcode, and division by zero. Expected and actual outputs matched for the main test cases.

## Limitations
- Simulated in MASM rather than implemented in hardware
- Limited instruction set
- Irvine32 dependency
- No pipelining, interrupt handling, or FPGA implementation

## Future Enhancements
- Add MOD, XOR, NOT, and shift operations
- Improve input validation
- Implement in Verilog/VHDL
- Test on FPGA
- Add pipeline stages
- Add a richer output interface
