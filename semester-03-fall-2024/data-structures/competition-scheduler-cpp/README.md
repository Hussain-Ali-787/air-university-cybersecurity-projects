# Competition Scheduler - Enhanced Hybrid DLL V3

![Course](https://img.shields.io/badge/Course-Data%20Structures-blue)
![Backend](https://img.shields.io/badge/Backend-C%2B%2B%20DLL-orange)
![Frontend](https://img.shields.io/badge/Frontend-C%23%20WinForms-purple)
![Style](https://img.shields.io/badge/Style-Original%20Dark%20GUI-black)
![Status](https://img.shields.io/badge/Status-Polished%20V3-brightgreen)

## Overview

This is the polished enhanced version of the original **Competition Scheduler** Data Structures project.

The original coursework project was a C++/CLI Windows Forms application for managing 16-team CTF/hackathon tournaments. V3 preserves the original GUI identity while improving the architecture:

```text
C# WinForms Frontend
        ↓ P/Invoke
C++ DLL Backend
        ↓
Data Structures Logic
```

## Improvements in V3

- Dark sidebar GUI inspired by the original project
- Original navigation workflow: Home, Load Teams, View Schedule, Simulate Matches, Tournament Rules
- Dashboard cards
- Original `Teams.txt` support
- Actual team logo resource folder included
- Team cards with logo badges
- Better schedule screen with logs
- Bracket-style simulation view with round columns
- Manual winner selection
- Full tournament simulation
- Report export
- Safer backend logic

## Build Backend

```powershell
cd backend-cpp-dll
.\build.bat
```

## Run Frontend

```powershell
cd frontend-csharp-winforms
dotnet run
```

## Team File Format

```text
Team Name, Member1;Member2;Member3, Rank
```

Example:

```text
Team Alpha, Ayan;Bilal;Hamza, 1
```

## Structure

```text
competition_scheduler_hybrid_dll_v3/
├── README.md
├── PROJECT_NOTES.md
├── .gitignore
├── backend-cpp-dll/
├── frontend-csharp-winforms/
├── shared-data/
├── output/
├── docs/
└── screenshots/
```

## Notes

The original C++/CLI project should still be preserved separately. This V3 version is a modern runnable enhancement that keeps the GUI-based identity and C++ data structures backend.
