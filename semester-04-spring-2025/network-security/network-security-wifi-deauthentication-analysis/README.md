# De-authentication Attack on Wi-Fi Networks

## Project Overview

This project is a **Network Security Lab** report on Wi-Fi deauthentication attacks. It explains the security weakness in unprotected IEEE 802.11 management frames, demonstrates the behavior in an authorized lab setup, analyzes the traffic using Wireshark, and discusses practical defensive mechanisms.

The final repository is prepared as a safe academic/portfolio version. It does not include packet captures, handshakes, raw wireless traffic, or sensitive client identifiers.

## Course Information

| Field | Details |
|---|---|
| Course | Network Security Lab |
| Course Code | CY-223L |
| Instructor | Miss Iram Fatima |
| Class | BSCYSev-F-23-A |
| Date of Submission | 24 May 2026 |

## Group Members

| Name | Registration ID |
|---|---:|
| Hussain Ali | 232095 |
| Syed Jazib Ali Rizvi | 232145 |
| Shehroze Sameer | 232091 |

## Repository Structure

```text
network-security-wifi-deauthentication-analysis/
├── docs/
│   ├── network-security-deauthentication-report.docx
│   └── network-security-deauthentication-report.pdf
├── screenshots/
│   ├── 01-report-cover.png
│   ├── 02-introduction-objectives-scope.png
│   ├── 03-technical-background-environment-setup.png
│   ├── 04-network-scanning-packet-capture.png
│   ├── 05-deauth-and-wireshark-analysis.png
│   ├── 06-results-and-defensive-mechanisms.png
│   ├── 07-defense-comparison-limitations-conclusion.png
│   └── README.md
├── references/
│   └── references.md
├── README.md
├── PROJECT_NOTES.md
└── .gitignore
```

## Deliverables

| Path | Description |
|---|---|
| `docs/network-security-deauthentication-report.docx` | Final editable report |
| `docs/network-security-deauthentication-report.pdf` | PDF version of the final report for quick review |
| `screenshots/` | Rendered report screenshots for GitHub preview |
| `references/references.md` | Reference list used in the project |
| `PROJECT_NOTES.md` | Short explanation of project scope, safety decisions, and future improvements |

## Main Topics Covered

- Wireless deauthentication attack concept
- IEEE 802.11 management frames
- Lab environment setup
- Network scanning and packet capture
- Wireshark analysis of deauthentication frames
- Results and observations
- Attack indicators
- Defensive mechanisms
- Ethical and legal scope
- Limitations and conclusion

## Defensive Focus

The project emphasizes security analysis and mitigation. Key defenses include:

- WPA3 or WPA2 with 802.11w Protected Management Frames
- Wireless Intrusion Detection Systems
- Router and client firmware updates
- Monitoring for repeated deauthentication frames
- VPN use for protecting traffic during reconnection events

## Safety Notice

This project was conducted only in a controlled lab environment using an owned/authorized router. It is intended for educational and defensive cybersecurity learning only.

Do not use this material to disrupt networks or test wireless systems without explicit permission.

## How to Review

1. Open the PDF report in `docs/` for the easiest review.
2. Open the DOCX report if editing is required.
3. View the screenshots in `screenshots/` for a quick visual overview.
4. Check `references/references.md` for supporting references.
