# Run Guide

This project is a C# WinForms educational firewall simulator.

## Requirements

- Windows
- .NET 8 SDK or newer SDK that can build `net8.0-windows`

Check SDK availability:

```powershell
dotnet --list-sdks
```

If this command prints no SDK versions, install the .NET SDK before building. The .NET runtime alone is not enough for `dotnet build` or `dotnet run`.

## Build

From this project folder:

```powershell
dotnet build src/FirewallTutor.csproj
```

## Run

From this project folder:

```powershell
dotnet run --project src/FirewallTutor.csproj
```

## Review Sample Data

The project includes safe sample files:

- `data/rules.csv`
- `data/packets.csv`

## Review Screenshots

Use `screenshots/` to preview the main app screens without running the program.

## Safety Notes

This is a classroom simulator. It does not inspect or control real network traffic.
