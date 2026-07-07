# Project Notes

## Alignment Status

Status: Runnable

This project contains the Competition Scheduler coursework and a reformed hybrid C++ DLL plus C# WinForms version.

## Standardization Notes

- Existing `original/` and `reformed/` folders are accepted because they preserve source history and the improved version separately.
- `shared-data/` is retained for common sample team data.
- `docs/PROJECT_NOTES.md` existed historically, but this root-level `PROJECT_NOTES.md` is now the standard project note location.

## Remaining Work

- Full WinForms build/run still needs a machine with the .NET 8 SDK installed.
- Review whether `Classes/` belongs to the original implementation or should be documented more clearly.

## Technical Review - 2026-07-07

- Reviewed the reformed C++ DLL backend, C# WinForms wrapper, sample team data, build script, and run guide.
- Fixed a WinForms constructor typo that prevented `_rootDir` from being initialized.
- Hardened backend team loading so invalid numeric fields are skipped instead of relying on uncaught `stoi` parsing.
- Added explicit empty-path validation for exports and report generation.
- Cleaned broken UI/report characters to plain ASCII text.
- Made the backend build script portable to its own folder and enabled compiler warning flags.
- Verified the backend DLL builds with MinGW-w64 `g++`.
- Verified backend API flow with the sample `Teams.txt`: load teams, generate schedule, simulate full tournament, export report, and reject an empty team path.
- Attempted the WinForms build, but this machine has no .NET SDK installed.
