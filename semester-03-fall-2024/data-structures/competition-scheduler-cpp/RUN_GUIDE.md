# Run Guide

This project includes an original C++/CLI coursework version and a reformed hybrid version with a C++ backend DLL and C# WinForms frontend.

## Reformed Version

### Build Backend

From `reformed/backend-cpp-dll/`:

```powershell
.\build.bat
```

### Run Frontend

From `reformed/frontend-csharp-winforms/`:

```powershell
dotnet run
```

## Sample Data

Team input data is available in:

- `shared-data/Teams.txt`

## Original Version

The original coursework source is preserved under:

- `original/`

Open it with the appropriate Visual Studio tooling if you need to inspect or build the original C++/CLI version.

## Safety Notes

This is a tournament scheduling application for academic data-structures coursework. It does not process sensitive data.
