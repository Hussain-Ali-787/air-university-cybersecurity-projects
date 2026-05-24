# Recompiling the Linux Kernel with a Custom Round-Robin CPU Scheduler

## Project Overview

This project modifies the Linux kernel CPU scheduler to compare the default Completely Fair Scheduler (CFS) with a custom Round-Robin (RR) style scheduler. The project includes the original and modified scheduler source files, benchmark scripts, benchmark outputs, a generated HTML comparison report, and a final academic report.

The goal is to understand how kernel-level scheduling decisions affect CPU throughput, scheduling latency, fairness, and I/O behavior.

## Course Information

| Field | Details |
|---|---|
| Course | Operating System Lab |
| Course Code | CS-325L |
| Instructor | Miss Iram Fatima |
| Class | BSCYSev-F-23-A |
| Date of Submission | 11 June 2025 |

## Team Members

| Name | Registration ID |
|---|---:|
| Hussain Ali | 232095 |
| Syed Jazib Ali Rizvi | 232145 |
| Sardar Ahmad Ali | 232147 |
| Sardar Shahbaz | 232089 |

## Repository Structure

```text
operating-system-round-robin-kernel-scheduler/
├── benchmarks/
│   ├── evaluate.c
│   ├── kernel_baseline_test.sh
│   └── kernelTest.py
├── docs/
│   ├── kernel-round-robin-scheduler-report.docx
│   └── kernel-round-robin-scheduler-report.pdf
├── results/
│   ├── kernel_comparison_report.html
│   ├── kernel_roundrobin/
│   └── kernel_vanilla/
├── scheduler-source/
│   ├── fair_modified.c
│   └── fair_original.c
├── screenshots/
│   ├── 01-report-cover.png
│   ├── 02-objective-and-scope.png
│   ├── 03-implementation-setup.png
│   ├── 04-scheduler-modification.png
│   ├── 05-benchmarking-results.png
│   ├── 06-result-highlights.png
│   ├── 07-limitations-and-conclusion.png
│   └── 08-attachments.png
├── .gitignore
├── PROJECT_NOTES.md
├── README.md
└── RUN_GUIDE.md
```

## Included Deliverables

| Path | Description |
|---|---|
| `docs/kernel-round-robin-scheduler-report.docx` | Final editable report |
| `docs/kernel-round-robin-scheduler-report.pdf` | Final PDF report |
| `scheduler-source/fair_original.c` | Original Linux scheduler source file used as baseline |
| `scheduler-source/fair_modified.c` | Modified scheduler file with Round-Robin style logic |
| `benchmarks/kernel_baseline_test.sh` | Shell script for running benchmark tests |
| `benchmarks/kernelTest.py` | Python script for orchestrating results and generating the HTML report |
| `benchmarks/evaluate.c` | C source for evaluation support |
| `results/kernel_vanilla/` | Collected benchmark output for vanilla kernel |
| `results/kernel_roundrobin/` | Collected benchmark output for modified kernel |
| `results/kernel_comparison_report.html` | Generated comparison report |
| `screenshots/` | Rendered report previews for GitHub |

## Benchmark Summary

| Test | Vanilla CFS | Round Robin | Winner |
|---|---:|---:|---|
| Sysbench CPU | 93.04 events/sec | 76.82 events/sec | Vanilla CFS |
| Stress-ng CPU | 127,435 bogo ops | 130,087 bogo ops | Mixed / close |
| Perf scheduling latency | 1119.708 ms | 896.388 ms | Round Robin |
| Sysbench File I/O read | 11.34 MiB/s | 15.37 MiB/s | Round Robin |
| Sysbench File I/O write | 7.56 MiB/s | 10.25 MiB/s | Round Robin |

## Key Findings

- The custom Round-Robin scheduler reduced scheduling latency in the collected `perf` result.
- The vanilla CFS scheduler performed better in single-threaded sysbench CPU throughput.
- Round-Robin showed better read/write throughput in the collected sysbench file I/O result.
- CFS remains more suitable for general-purpose systems because it is mature, adaptive, and optimized for mixed workloads.
- The RR implementation is useful for coursework, controlled experiments, and scheduler behavior study.

## Kernel Safety Warning

This project modifies kernel scheduler code. Test only inside a virtual machine or isolated lab environment. Do not install experimental kernels on a primary machine.

## Cleanup Notes

The final repository intentionally excludes:

- Nested duplicate ZIP archives
- Compiled binaries
- Kernel build output
- Temporary build/cache files

Only source files, reports, scripts, and benchmark results are preserved.

## Academic Note

This is an academic proof-of-concept created for Operating System Lab. It is not intended to replace the production Linux scheduler.
