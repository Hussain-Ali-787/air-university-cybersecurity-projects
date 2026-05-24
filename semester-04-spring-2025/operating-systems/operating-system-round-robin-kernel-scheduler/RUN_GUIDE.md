# Run Guide

## Warning

This project modifies Linux kernel scheduler code. Do not run kernel build/install commands on a primary machine. Use a virtual machine or isolated lab system.

## Review Without Building the Kernel

For GitHub review, start with:

```text
docs/kernel-round-robin-scheduler-report.pdf
scheduler-source/fair_original.c
scheduler-source/fair_modified.c
results/kernel_comparison_report.html
```

## Inspect Source Differences

Use any diff tool:

```bash
diff -u scheduler-source/fair_original.c scheduler-source/fair_modified.c
```

or:

```bash
git diff --no-index scheduler-source/fair_original.c scheduler-source/fair_modified.c
```

## Benchmark Files

The benchmark scripts are stored in:

```text
benchmarks/kernel_baseline_test.sh
benchmarks/kernelTest.py
benchmarks/evaluate.c
```

The collected benchmark outputs are stored in:

```text
results/kernel_vanilla/
results/kernel_roundrobin/
```

## Open HTML Report

Open this file in a browser:

```text
results/kernel_comparison_report.html
```

It compares the collected benchmark outputs and includes visual plots.

## Do Not Commit Build Artifacts

Do not commit compiled kernel trees, object files, temporary build folders, or compiled binaries. Keep only source, scripts, reports, and result text files.
