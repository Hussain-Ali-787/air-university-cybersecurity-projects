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

## Project Preview

### Unique Solution

![Unique Solution](screenshots/unique-solution.png)

### Infinite Solutions

![Infinite Solutions](screenshots/infinite-solutions.png)

### No Solution

![No Solution](screenshots/no-solution.png)

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
| Main Output | Unique solution, infinite solutions, or no solution |

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
linear_algebra_gaussian_elimination_project/
│
├── README.md
├── PROJECT_NOTES.md
│
├── src/
│   └── gaussian_elimination_solver.cpp
│
├── original/
│   ├── general_gaussian_elimination_solver.cpp
│   └── fixed_6x6_consistency_checker.cpp
│
├── sample-data/
│   ├── unique-solution-input.txt
│   ├── infinite-solutions-input.txt
│   └── no-solution-input.txt
│
└── screenshots/
    ├── unique-solution.png
    ├── infinite-solutions.png
    └── no-solution.png
```

---

## Original Files

The `original/` folder preserves the original coursework files.

| File | Purpose |
|---|---|
| `general_gaussian_elimination_solver.cpp` | Original general Gaussian Elimination solver for an `n x n` system |
| `fixed_6x6_consistency_checker.cpp` | Instructor-specific 6x6 consistency checker with fixed system size |

The fixed `6 x 6` version was intentionally hardcoded because the instructor specifically required checking the consistency of a 6-equation system. The enhanced version generalizes the same idea and supports any `n x n` system, including `6 x 6`.

---

## Enhanced Implementation

The enhanced implementation is located in:

```text
src/gaussian_elimination_solver.cpp
```

It combines the main ideas from both original files:

- General Gaussian Elimination from the first original file
- Consistency checking from the fixed 6x6 requirement
- Improved rank and inconsistency detection
- Cleaner output and structure

---

## How to Compile

```bash
g++ src/gaussian_elimination_solver.cpp -o gaussian_solver
```

On Windows, this creates:

```text
gaussian_solver.exe
```

> Do not commit the generated `.exe` file to GitHub.

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

## Sample Cases Included

| Case | Input File | Screenshot |
|---|---|---|
| Unique solution | `sample-data/unique-solution-input.txt` | `screenshots/unique-solution.png` |
| Infinite solutions | `sample-data/infinite-solutions-input.txt` | `screenshots/infinite-solutions.png` |
| No solution | `sample-data/no-solution-input.txt` | `screenshots/no-solution.png` |

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

- Add file input/output support inside the program
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
