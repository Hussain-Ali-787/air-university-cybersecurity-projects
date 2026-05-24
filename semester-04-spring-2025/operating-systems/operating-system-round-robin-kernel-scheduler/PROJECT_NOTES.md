# Project Notes

## Project Name

Recompiling the Linux Kernel with a Custom Round-Robin CPU Scheduler

## Purpose

The purpose of this project is to study the Linux kernel scheduling mechanism by modifying scheduler source code and comparing the behavior of the default Completely Fair Scheduler with a simplified Round-Robin style scheduler.

## What Was Preserved

The final repository keeps the important academic and technical artifacts:

```text
docs/
scheduler-source/
benchmarks/
results/
screenshots/
```

The duplicate nested archive and compiled binary were removed.

## Main Technical Work

- Inspected the Linux kernel scheduler source.
- Preserved the original `fair.c` file.
- Modified scheduler behavior in `fair_modified.c`.
- Compiled and tested the modified kernel in a lab environment.
- Ran benchmarks on vanilla and modified kernels.
- Compared CPU, I/O, scheduling latency, and runtime behavior.

## Important Limitation

The modified scheduler is an academic prototype. It does not fully implement a production-grade scheduler and does not preserve all CFS features such as vruntime balancing, group scheduling behavior, energy-aware scheduling, and mature I/O responsiveness.

## Kernel Version Labeling Note

The benchmark result folders show the same base kernel release string. A recommended future improvement is to set:

```text
CONFIG_LOCALVERSION="-rr-scheduler"
```

before compilation so `uname -r` clearly differentiates the custom kernel from the vanilla kernel.

## Result Correction

The final report and README treat sysbench file I/O as a Round-Robin win because the collected output shows higher read/write throughput for the modified kernel:

```text
Vanilla read throughput: 11.34 MiB/s
Round Robin read throughput: 15.37 MiB/s
Vanilla write throughput: 7.56 MiB/s
Round Robin write throughput: 10.25 MiB/s
```

## Safety Note

Kernel development should be done inside a VM or isolated test system. Experimental kernels can break boot behavior, drivers, package compatibility, or system stability.

## Future Improvements

- Add a clear custom kernel local version string.
- Add a controlled multi-run benchmark average instead of a single run.
- Add graphs in a separate `figures/` folder.
- Compare additional schedulers or workloads.
- Document exact kernel configuration differences.
- Add boot logs and GRUB entry screenshots if needed.
