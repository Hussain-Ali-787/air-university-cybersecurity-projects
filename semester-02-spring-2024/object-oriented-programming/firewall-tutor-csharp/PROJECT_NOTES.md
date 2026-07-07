# Project Notes

## Alignment Status

Status: Runnable

This project is a C# WinForms educational firewall simulator for OOP coursework.

## Standardization Notes

- Existing `src/`, `data/`, `docs/`, `output/`, and `screenshots/` folders are accepted.
- Sample rules and packets are lab examples only.
- The project is a teaching simulator and does not interact with live network traffic.

## Technical Review

- Reviewed the WinForms entry point, main form, models, firewall engine, and CSV storage service.
- Attempted `dotnet build`, but this machine has .NET runtimes only and no .NET SDK installed.
- Confirmed sample `data/` and `output/` CSV artifacts are consistent with the built-in sample rules and packets.
- Tightened packet IP validation to IPv4 only, matching the simulator's IPv4 rule logic.
- Tightened port rule matching so invalid ports and reversed ranges do not match accidentally.
- Tightened last-octet IP range matching so reversed ranges are rejected.
- Cleaned the README repository tree to use ASCII-safe formatting.
- Updated `RUN_GUIDE.md` to explain the .NET SDK requirement.

## Remaining Work

- Confirm `dotnet build` and `dotnet run` on a machine with the .NET SDK installed.
- Review whether `output/` should remain tracked after final validation.
- Consider adding unit tests for `FirewallRule.Matches`, CIDR matching, port ranges, and default policy behavior.
