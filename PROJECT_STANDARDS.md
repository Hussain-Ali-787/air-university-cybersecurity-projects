# Project Organization Standards

This repository is an academic cybersecurity portfolio. The goal is to keep every project easy to review, safe to publish, and consistent across semesters while preserving original coursework artifacts.

## Top-Level Structure

Use this structure for semester work:

```text
semester-XX-session-year/
  course-name/
    project-name/
      README.md
      src/
      docs/
      presentation/
      screenshots/
      data/
      configs/
      results/
      references/
      RUN_GUIDE.md
      PROJECT_NOTES.md
```

Not every project needs every folder. Include only folders that contain useful files.

## Naming Rules

- Use lowercase kebab-case for folders and files where possible.
- Use clear academic names, not temporary class names.
- Prefer `README.md`, `RUN_GUIDE.md`, and `PROJECT_NOTES.md` for standard documentation files.
- Keep original report and presentation filenames readable, but rename confusing or inconsistent names during cleanup when safe.
- Avoid spaces in new filenames. Existing screenshots may keep spaces if renaming would create too much churn.

## Required Project Files

Every complete project should have:

- `README.md`: public-facing overview and review guide.
- `PROJECT_NOTES.md`: maintainer-focused notes about cleanup decisions, source history, assumptions, and remaining tasks.
- `RUN_GUIDE.md`: required only when the project can be run, simulated, built, or tested.
- `.gitignore`: required only when the project has tool-specific generated files beyond the root ignore rules.

## Standard Project Folders

| Folder | Purpose |
|---|---|
| `src/` | Application, script, or program source code |
| `docs/` | Reports, PDFs, DOCX files, written submissions |
| `presentation/` | PPTX or slide decks |
| `screenshots/` | UI, report, tool, simulation, or verification screenshots |
| `data/` | Safe sample input data only |
| `configs/` | Sanitized configuration files, command notes, topology configs |
| `results/` | Benchmark outputs, generated reports, safe analysis outputs |
| `references/` | Source lists, tool references, bibliography notes |
| `rules/` | Detection rules such as YARA or Sigma |
| `iocs/` | Indicators of compromise, hashes, domains, IPs, and related notes |
| `original/` | Original coursework source kept for comparison |
| `reformed/` | Improved or cleaned version of an older project |
| `packet-tracer/` | Cisco Packet Tracer simulation files |
| `topology/` | Network or system topology diagrams |
| `benchmarks/` | Benchmark scripts or test harnesses |
| `scheduler-source/` | Kernel or scheduler source snapshots |
| `design/` | Circuit, spreadsheet, or design planning artifacts |
| `proteus/` | Proteus simulation projects and reconstruction notes |
| `media/` | Demo videos or hardware photos |
| `diagrams/` | Architecture, CPU, circuit, or design diagrams |
| `code/` | Source code for projects where `src/` would be misleading or less clear |
| `shared-data/` | Safe sample data shared by multiple project versions |
| `automated-analysis/` | Safe automated analysis reports and sandbox outputs |

## README Standard

Each project README should answer:

1. What is this project?
2. Which course and semester does it belong to?
3. What problem, topic, or scenario does it demonstrate?
4. What tools and technologies were used?
5. What files should a reviewer open first?
6. How can the project be run, tested, simulated, or reviewed?
7. What results or findings were produced?
8. What are the limitations?
9. What safety or ethics notes apply?

Use `PROJECT_README_TEMPLATE.md` as the starting point.

## Safety Standard

Before adding or committing a project, review `SAFE_UPLOAD_CHECKLIST.md`.

Do not commit:

- Real secrets, passwords, API keys, private keys, or tokens
- Live malware binaries or payloads
- Real packet captures, forensic images, memory dumps, or private logs
- Private university portal screenshots or personal data
- Compiled binaries, build output, virtual environments, or databases
- ZIP/RAR/7Z archives unless there is a clear reason and they have been reviewed

Use placeholders such as `<LAB_SECRET>`, `<REDACTED>`, and `<PRIVATE_DATA_REMOVED>` when documentation needs to refer to sensitive values.

## Cleanup Workflow

Clean one project at a time:

1. Inventory the current files.
2. Identify project type: code, presentation, report, simulation, lab, analysis, or mixed.
3. Remove or ignore unsafe/generated files.
4. Rename folders and files to match the naming rules.
5. Place files into standard folders.
6. Rewrite the project README using the standard sections.
7. Add or update `RUN_GUIDE.md` when runnable.
8. Add `PROJECT_NOTES.md` with cleanup decisions and remaining work.
9. Check links, screenshots, and relative paths.
10. Review `git status` before staging.

For report-only or presentation-only projects, `RUN_GUIDE.md` may be used as a `Review Guide` that explains how to inspect the artifacts safely.

## Project Status Labels

| Status | Meaning |
|---|---|
| `Planned` | Folder exists, but content has not been added yet |
| `Imported` | Original files are present but not cleaned |
| `Organized` | Files are in the standard structure |
| `Documented` | README and review instructions are complete |
| `Runnable` | Code can be built or run using documented steps |
| `Archived` | Kept for record only; no active cleanup planned |

## Recommended Migration Order

Start with projects that are already close to complete:

1. Projects with strong README files and safe artifacts.
2. Runnable code projects.
3. Simulation projects with screenshots and reports.
4. Presentation-only projects.
5. Empty semester/course placeholders.

This keeps the repository useful while cleanup is still in progress.
