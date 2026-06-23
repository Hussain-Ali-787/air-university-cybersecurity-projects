# Project Migration Tracker

Use this file to align projects with `PROJECT_STANDARDS.md` one by one.

## Legend

| Status | Meaning |
|---|---|
| `Planned` | Folder exists, but content has not been added yet |
| `Imported` | Original files are present but not fully cleaned |
| `Organized` | Files are in a standard, reviewable structure |
| `Documented` | README and project notes are present |
| `Runnable` | Build, run, simulation, or review guide is present |
| `Needs review` | Likely safe, but requires manual review before commit |
| `Blocked` | Missing files, unsafe content, or unclear source state |

## Current Repository Notes

- Repo-wide standards are defined in `PROJECT_STANDARDS.md`.
- Root, semester, course, and project entry-point READMEs are now present for the visible folder structure.
- All listed project folders now have `README.md`.
- All listed project folders now have `PROJECT_NOTES.md`.
- Runnable, simulation, and security-analysis projects now have `RUN_GUIDE.md` or a review guide.
- Some older semester README files still contain mojibake from box-drawing characters and can be polished in a later documentation pass.
- Four local ZIP archives were found under `semester-03-fall-2024/`; review before committing.
- The root `.gitignore` blocks common secrets, binaries, archives, packet captures, databases, and malware sample paths.

## Migration Checklist

| Semester | Course | Project | Type | Status |
|---|---|---|---|---|
| Final Year Project | Privacy / FYP | spot-smart-privacy-oversharing-tracker | Product / research | Planned |
| Semester 1 | Applications of ICT | crowdstrike-website-development | Presentation / web concept | Documented |
| Semester 1 | Applications of ICT | telecom-cybersecurity-presentation | Presentation | Documented |
| Semester 1 | Discrete Structures | relations-and-their-properties | Presentation | Documented |
| Semester 1 | Functional English | cybersecurity-in-pakistan-presentation | Presentation | Documented |
| Semester 1 | Introduction to Cyber Security | hash-cracking-john-the-ripper | Presentation / security tools | Documented |
| Semester 1 | Programming Fundamentals | firewall-rule-engine-cpp | C++ code | Runnable |
| Semester 2 | Digital Logic Design | 4-way-traffic-signal-controller | Circuit / report | Runnable |
| Semester 2 | Introduction to Software Engineering | software-testing-with-selenium | Report / testing | Documented |
| Semester 2 | Linear Algebra | gaussian-elimination-solver | C++ code | Runnable |
| Semester 2 | Object-Oriented Programming | firewall-tutor-csharp | C# WinForms code | Runnable |
| Semester 3 | Computer Networks | avionics-base-network | Packet Tracer simulation | Runnable |
| Semester 3 | Computer Organization and Assembly Language | processor-design-embedded-calculator | Assembly / diagrams | Runnable |
| Semester 3 | Data Structures | competition-scheduler-cpp | C++ DLL / C# WinForms | Runnable |
| Semester 3 | Information Assurance | hbl-contingency-framework | Report / presentation | Documented |
| Semester 3 | Introduction to Management | business-intelligence-management-apple | Report / presentation | Documented |
| Semester 4 | Malware Analysis | malware-analysis-netsupport-rat | Malware analysis report | Runnable |
| Semester 4 | Multivariable Calculus | multivariable-calculus-vector-derivatives | Presentation | Documented |
| Semester 4 | Network Security | network-security-wifi-deauthentication-analysis | Security analysis report | Runnable |
| Semester 4 | Operating Systems | operating-system-round-robin-kernel-scheduler | Kernel experiment | Runnable |
| Semester 4 | Secure Software Design and Development | secure-student-management-system | Flask app | Runnable |
| Semester 5 | Internship | internship | Internship materials | Imported |
| Semester 6 | Artificial Intelligence | TBD | Placeholder | Planned |
| Semester 6 | Civics and Community Engagement | TBD | Placeholder | Planned |
| Semester 6 | Digital Forensics | TBD | Placeholder | Planned |
| Semester 6 | Ethical Hacking and Defense | TBD | Placeholder | Planned |
| Semester 6 | Expository Writing | TBD | Placeholder | Planned |
| Semester 6 | Parallel and Distributed Computing | TBD | Placeholder | Planned |
| Semester 7 | TBD | TBD | Placeholder | Planned |

## Remaining Repo-Wide Cleanup

1. Review the four local ZIP archives under `semester-03-fall-2024/`.
2. Polish older semester README files that still contain box-drawing mojibake.
3. Verify run guides on a clean machine.
4. Review DOCX/PPTX files for private information before staging.
5. Decide whether generated outputs such as `output/` folders should remain tracked.
