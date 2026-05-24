# Processor Design for Embedded Calculator

## Project Title
**Designing a Processor for a Small Embedded System**

## Course
Computer Organization and Assembly Language  
Course Code: CS-226  
Department of Cyber Security, Air University, Islamabad

## Overview
This project presents the design and simulation of a simplified processor architecture for a small embedded calculator system. The design demonstrates core Computer Organization and Assembly Language concepts, including CPU components, bus architecture, datapath design, instruction set design, and MASM assembly implementation.

## Group Members
| Name | Registration ID |
|---|---:|
| Hussain Ali | 232095 |
| Sardar Ahmad Ali | 232147 |

## Main Components
| Component | Purpose |
|---|---|
| Control Unit (CU) | Coordinates instruction execution and control signals |
| Arithmetic Logic Unit (ALU) | Performs arithmetic and logical operations |
| Register Array | Stores operands, intermediate values, and results |
| Memory Unit | Uses RAM/ROM concepts for data and instruction storage |
| Input Unit | Accepts numbers and operation codes |
| Output Unit | Displays results and error messages |

## Supported Operations
| Opcode | Operation | Description |
|---:|---|---|
| 1 | ADD | Adds two numbers |
| 2 | SUB | Subtracts the second number from the first |
| 3 | MUL | Multiplies two numbers |
| 4 | DIV | Divides the first number by the second |
| 5 | AND | Performs bitwise AND |
| 6 | OR | Performs bitwise OR |
| 99 | EXIT | Terminates the simulation |

## Repository Structure
```text
processor-design-embedded-calculator/
├── code/
│   └── main.asm
├── docs/
│   └── COAL_Final_Report.docx
├── presentation/
│   └── COAL_Presentation.pptx
├── diagrams/
│   ├── CPU_BlockDiagram.png
│   ├── BusArchitecture.png
│   └── DataPathDiagram.png
├── screenshots/
│   └── .gitkeep
├── exports/
│   └── .gitkeep
├── README.md
├── PROJECT_NOTES.md
├── RUN_GUIDE.md
└── .gitignore
```

## How to Run
The assembly implementation uses MASM with the Irvine32 library.

Recommended setup:
- Windows
- Visual Studio
- MASM enabled
- Irvine32 library configured
- x86 build target

Basic steps:
1. Create or open a MASM/Irvine32 project.
2. Add `code/main.asm`.
3. Configure Irvine32 include and library paths.
4. Build using x86 mode.
5. Run and enter two numbers plus an opcode.

## Deliverables
| Deliverable | Description |
|---|---|
| Assembly Code | MASM/Irvine32 calculator processor simulation |
| Final Report | Processor design, implementation, testing, and conclusion |
| Presentation | Summary of architecture and code implementation |
| Diagrams | CPU block diagram, bus architecture, and datapath diagram |

## Academic Note
This is an academic simulation of a simplified embedded calculator processor. It demonstrates processor organization and assembly-level behavior, but it is not a hardware-level processor implementation.
