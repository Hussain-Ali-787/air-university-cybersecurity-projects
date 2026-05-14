# Gaussian Elimination Solver in C++

![Course](https://img.shields.io/badge/Course-Linear%20Algebra-blue)
![Language](https://img.shields.io/badge/Language-C%2B%2B-orange)
![Topic](https://img.shields.io/badge/Topic-Gaussian%20Elimination-purple)
![Type](https://img.shields.io/badge/Type-Console%20Application-lightgrey)
![Status](https://img.shields.io/badge/Status-Enhanced-brightgreen)

## Overview

This project was completed for the **Linear Algebra** course. The project implements a C++ program to solve systems of linear equations using the **Gaussian Elimination** method.

The program accepts a coefficient matrix `A` and constants vector `b`, forms the augmented matrix `[A | b]`, performs Gaussian Elimination, and determines whether the system has:

- A unique solution
- Infinite solutions
- No solution

The enhanced version improves the original coursework implementation with cleaner structure, safer pivot handling, better solution status detection, and clearer console output.

---

## Project Information

| Field | Details |
|---|---|
| Course | Linear Algebra |
| Project Topic | Solving Linear Equations using Gaussian Elimination |
| Language | C++ |
| Application Type | Console Application |
| Method | Gaussian Elimination with Partial Pivoting |
| Status | Completed and Enhanced |

---

## Problem Statement

Write a C++ program to solve a system of linear equations using the Gaussian Elimination method. The program should input the number of unknowns, the coefficient matrix `A`, and the constants vector `b` for the system `Ax = b`.

The program should form the augmented matrix `[A | b]`, perform Gaussian Elimination, display the augmented matrix before and after elimination, and output whether the system has a unique solution, infinite solutions, or no solution.

---

## Mathematical Background

A system of linear equations can be written in matrix form as:

```text
Ax = b
```

Where:

| Symbol | Meaning |
|---|---|
| `A` | Coefficient matrix |
| `x` | Unknown variable vector |
| `b` | Constants vector |

Gaussian Elimination transforms the augmented matrix `[A | b]` into row echelon form using elementary row operations.

---

## Features

- Accepts any `n x n` system
- Forms augmented matrix `[A | b]`
- Uses partial pivoting for better numerical stability
- Prints matrix before elimination
- Prints matrix after elimination
- Detects unique solution
- Detects infinite solutions
- Detects no solution
- Uses EPSILON-based floating point comparison
- Provides clearer code structure and output formatting

---

## Algorithm Flow

```mermaid
flowchart TD
    A[Input number of unknowns] --> B[Input coefficient matrix A]
    B --> C[Input constants vector b]
    C --> D[Form augmented matrix A|b]
    D --> E[Select pivot using partial pivoting]
    E --> F[Perform row elimination]
    F --> G[Check consistency and rank]
    G --> H{Solution Type}
    H -->|Unique| I[Back substitution]
    H -->|Infinite| J[Report infinite solutions]
    H -->|No solution| K[Report inconsistent system]
```

---

## Repository Structure

```text
gaussian-elimination-solver-cpp/
│
├── README.md
├── PROJECT_NOTES.md
│
├── src/
│   └── gaussian_elimination_solver.cpp
│
├── original/
│   ├── 232095_Project.cpp
│   └── linear_project.cpp
│
├── sample-data/
│   ├── unique-solution-input.txt
│   ├── infinite-solutions-input.txt
│   └── no-solution-input.txt
│
├── output/
│   ├── unique-solution-output.txt
│   ├── infinite-solutions-output.txt
│   └── no-solution-output.txt
│
└── screenshots/
```

---

## How to Compile

```bash
g++ src/gaussian_elimination_solver.cpp -o gaussian_solver
```

On Windows PowerShell, this creates:

```text
gaussian_solver.exe
```

---

## How to Run

### Windows PowerShell

```powershell
.\gaussian_solver.exe
```

### Linux/macOS

```bash
./gaussian_solver
```

You can also redirect sample input:

```bash
./gaussian_solver < sample-data/unique-solution-input.txt
```

On Windows PowerShell:

```powershell
Get-Content sample-data\unique-solution-input.txt | .\gaussian_solver.exe
```

---

## Sample Input: Unique Solution

```text
3
2 1 -1
-3 -1 2
-2 1 2
8
-11
-3
```

This represents:

```text
2x + y - z = 8
-3x - y + 2z = -11
-2x + y + 2z = -3
```

Expected solution:

```text
x1 = 2
x2 = 3
x3 = -1
```

---

## Screenshots

Add screenshots using these names:

```text
screenshots/
├── unique-solution.png
├── infinite-solutions.png
└── no-solution.png
```

---

## Original Files

The `original/` folder contains the original coursework source files:

```text
original/232095_Project.cpp
original/linear_project.cpp
```

The enhanced implementation is kept separately in:

```text
src/gaussian_elimination_solver.cpp
```

---

## Learning Outcomes

Through this project, I learned how to:

- Represent systems of equations using matrices
- Form augmented matrices
- Apply Gaussian Elimination
- Use row operations
- Understand rank and consistency
- Detect unique, infinite, and no-solution cases
- Improve numerical stability using partial pivoting
- Implement mathematical algorithms in C++

---

## Limitations

- Console-based only
- Does not show symbolic parametric form for infinite solutions
- Uses floating point arithmetic, so very ill-conditioned systems may still have numerical error
- Does not support reading matrix input from a file directly inside the program

---

## Future Enhancements

- Add file input/output support
- Add Gauss-Jordan elimination
- Show parametric solutions for infinite-solution systems
- Add determinant calculation
- Add inverse matrix calculation
- Add step-by-step row operation display
- Add a GUI version

---

## Academic Notice

This project was created and enhanced for academic learning and portfolio documentation.

---

## Disclaimer

This is an educational Linear Algebra project intended to demonstrate Gaussian Elimination in C++.
