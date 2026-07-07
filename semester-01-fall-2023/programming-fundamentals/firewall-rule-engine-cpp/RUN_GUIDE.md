# Run Guide

This project is a small C++ firewall rule engine simulation.

## Requirements

- A C++17-compatible compiler
- PowerShell, Command Prompt, or a terminal

## Build

From this project folder:

```powershell
g++ src/main.cpp src/firewall.cpp -std=c++17 -Wall -Wextra -pedantic -o firewall
```

## Run with Default Files

```powershell
.\firewall
```

The default run uses:

- `data/rules.txt`
- `data/packets.txt`
- `output/result.txt`

## Run with Custom Files

```powershell
.\firewall data/rules.txt data/packets.txt output/result.txt
```

## Review Output

Open `output/result.txt` and compare it with the screenshots in `screenshots/`.

## Safety Notes

This project is a file-based simulation. It does not capture, inspect, filter, or modify real network traffic.
