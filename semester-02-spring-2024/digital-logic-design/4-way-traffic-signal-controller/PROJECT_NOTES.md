# Project Notes: 4-Way Traffic Signal Controller

## Purpose

These notes summarize the 4-way traffic signal controller project completed for Digital Logic Design.

---

## Final Architecture

```text
NE555 1Hz Timer
↓
4-Bit Counter
↓
Traffic Logic Circuit
↓
Traffic Light LEDs
```

The implemented counter was built using D flip-flops.

---

## Why the Project Was Built from Base Components

The instructor required the project to be implemented using basic digital logic modules instead of using a single modern IC or microcontroller. This was important because the course objective was to understand the internal working of digital circuits.

Using a ready-made IC or microcontroller could complete the task quickly, but it would not demonstrate:

- Sequential logic design
- Flip-flop behavior
- Counter construction
- Boolean equation implementation
- Gate-level traffic logic
- Practical digital logic application

Therefore, the project was built from core modules.

---

## Module Details

### Timer Module

Implemented using:

```text
NE555 timer
Ra = 100kΩ
Rb = 22kΩ
C = 10µF
```

Purpose:

```text
Generate approximately 1-second clock pulses.
```

### Counter Module

Implemented as:

```text
4-bit counter using D flip-flops
```

Purpose:

```text
Generate 16 states from 0000 to 1111.
```

Alternative possible designs:

```text
JK flip-flop counter
T flip-flop counter
Dedicated 4-bit counter IC
Microcontroller timer/counter
```

### Traffic Logic Module

Implemented using:

```text
NOT gates
AND gates
OR gates
```

Purpose:

```text
Convert 4-bit counter states into traffic signal outputs.
```

### Traffic Lights Module

Implemented using:

```text
LEDs
330Ω resistors
```

Purpose:

```text
Display red, yellow, and green outputs for each road.
```

---

## Timing

```text
Green interval: 3 seconds
Yellow transition: 1 second
Full cycle: 16 seconds
```

---

## Screenshot Set

Final screenshot files:

```text
screenshots/
├── hardware-running-state.jpg
├── proteus-dff-counter-module.png
├── proteus-main-circuit.png
├── proteus-ne555-timer-module.png
├── proteus-running-state-1.png
├── proteus-running-state-2.png
├── proteus-running-state-overview.png
├── proteus-traffic-lights-module.png
└── proteus-traffic-logic-module.png
```

---

## Media Files

Hardware evidence:

```text
media/
├── led-output-state-green.jpg
├── led-output-state-red-yellow.jpg
└── traffic-signal-demo.mp4
```

---

## Project Evidence

This project includes:

- Recreated Proteus simulation
- Proteus module screenshots
- Hardware implementation screenshots
- Demo video
- Excel truth table
- Reconstruction guide
- Academic report in Markdown format

---

## Key Takeaways

- NE555 timers can generate clock signals for sequential circuits.
- Flip-flops can be used to build counters.
- A counter can drive a state-based control system.
- Boolean equations can convert states into output signals.
- Subcircuits make large Proteus projects easier to understand.
- Building from base components improves understanding of Digital Logic Design.
