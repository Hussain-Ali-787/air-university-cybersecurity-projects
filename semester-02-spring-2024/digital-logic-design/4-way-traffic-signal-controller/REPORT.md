# Report: 4-Way Traffic Signal Controller

## 1. Introduction

This project was completed as part of the Digital Logic Design course. The aim of the project was to design and implement a 4-way traffic signal controller using core digital logic concepts.

The project was based on a real-world traffic intersection where four roads are controlled using red, yellow, and green lights. The controller changes signal states automatically using a clock, counter, and combinational logic.

The project was implemented in both Proteus simulation and physical hardware form.

---

## 2. Project Objective

The main objective was to design a traffic signal controller that:

- Controls four roads
- Provides green signal to one road at a time
- Uses yellow transition states between roads
- Keeps other roads red during active movement
- Repeats the sequence continuously
- Demonstrates timer, counter, and logic gate concepts

---

## 3. Academic Requirement

The course instructor required the system to be built from base digital logic components. The purpose was not just to make a traffic signal work, but to understand how each internal module works.

Instead of using a modern IC or microcontroller that directly performs the task, the project was built using:

- NE555 timer
- Flip-flop based counter
- Logic gates
- LEDs and resistors

This approach helped demonstrate practical Digital Logic Design concepts.

---

## 4. System Architecture

The system architecture is:

```text
NE555 1Hz Timer
↓
4-Bit Counter
↓
Traffic Logic Circuit
↓
Traffic Light LEDs
```

### Timer Module

The timer module generates the clock pulse.

Implemented using:

```text
NE555 timer
Ra = 100kΩ
Rb = 22kΩ
C = 10µF
```

The output is approximately one pulse per second.

### Counter Module

The counter module generates 16 binary states.

In this project, the 4-bit counter was implemented using D flip-flops. Other possible implementations include JK flip-flops, T flip-flops, or a ready-made counter IC.

### Traffic Logic Module

The traffic logic module converts counter states into traffic signal outputs using Boolean logic.

### Traffic Lights Module

The traffic lights module displays the final outputs using LEDs and resistors.

---

## 5. Timing Sequence

The project follows this timing pattern:

- Green signal: 3 seconds
- Yellow transition: 1 second
- Full cycle: 16 seconds

| State | Road 1 | Road 2 | Road 3 | Road 4 |
|---:|---|---|---|---|
| 0 | Yellow | Red | Red | Yellow |
| 1 | Green | Red | Red | Red |
| 2 | Green | Red | Red | Red |
| 3 | Green | Red | Red | Red |
| 4 | Yellow | Yellow | Red | Red |
| 5 | Red | Green | Red | Red |
| 6 | Red | Green | Red | Red |
| 7 | Red | Green | Red | Red |
| 8 | Red | Yellow | Yellow | Red |
| 9 | Red | Red | Green | Red |
| 10 | Red | Red | Green | Red |
| 11 | Red | Red | Green | Red |
| 12 | Red | Red | Yellow | Yellow |
| 13 | Red | Red | Red | Green |
| 14 | Red | Red | Red | Green |
| 15 | Red | Red | Red | Green |

---

## 6. Components Used

| Component | Purpose |
|---|---|
| NE555 Timer | Generates 1Hz clock pulse |
| D Flip-Flops | Build 4-bit counter |
| NOT Gates | Generate complemented variables |
| AND Gates | Build product terms |
| OR Gates | Combine logic terms |
| LEDs | Display traffic signals |
| 330Ω Resistors | Limit LED current |
| Breadboard and jumper wires | Hardware implementation |
| Proteus | Simulation environment |

---

## 7. Implementation

The Proteus design was divided into subcircuits for clarity:

```text
1Hz Timer
4-Bit Counter
Traffic Logic
Traffic Lights
```

This modular structure made the simulation easier to understand, test, and debug.

The physical hardware implementation followed the same logical design and was built using breadboard components.

---

## 8. Results

The recreated Proteus simulation was tested and verified. The system correctly cycles through all traffic states.

The physical hardware implementation also demonstrated the working traffic light outputs using LEDs.

---

## 9. Limitations

- The design is for educational purposes only.
- It does not include real-world safety mechanisms.
- Timing depends on NE555 tolerance.
- It does not include pedestrian signals.
- It does not include vehicle sensors or adaptive timing.

---

## 10. Future Improvements

Possible improvements include:

- Adding reset button
- Adding pedestrian crossing signal
- Adding emergency override
- Adding sensor-based traffic control
- Comparing D flip-flop counter with JK flip-flop implementation
- Adding a seven-segment display for state number

---

## 11. Conclusion

The project successfully demonstrates how a real-world control system can be implemented using digital logic concepts. By building the system from an NE555 timer, flip-flop counter, logic gates, and LEDs, the project provides practical understanding of sequential and combinational logic.

The recreated Proteus simulation and hardware evidence show that the design works as intended.
