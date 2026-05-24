@echo off
setlocal
if not exist build mkdir build
g++ -std=c++17 -O2 -shared ^
    -Iinclude ^
    src\CompetitionSchedulerBackend.cpp ^
    -o build\CompetitionSchedulerBackend.dll ^
    -Wl,--out-implib,build\libCompetitionSchedulerBackend.a
if errorlevel 1 (
    echo Build failed.
    exit /b 1
)
echo Backend DLL built successfully: build\CompetitionSchedulerBackend.dll
