# Project Notes - Hybrid DLL V3

## Purpose

V3 improves the working prototype into a more polished, original-style application.

## Original Features Preserved

- Dark WinForms GUI identity
- Sidebar navigation
- Load Teams page
- View Schedule page
- Simulate Matches bracket page
- Tournament Rules page
- 16-team CTF/hackathon scheduler concept

## Technical Improvements

- C++ DLL backend
- C# WinForms frontend
- P/Invoke integration
- Safer round progression
- Manual and simulated winners
- CSV output for tables
- Report generation

## Data Structures

- `vector<Team>` for teams
- `vector<Match>` for match history
- `queue<Team>` for pairing teams
- sorting for rank-based scheduling
