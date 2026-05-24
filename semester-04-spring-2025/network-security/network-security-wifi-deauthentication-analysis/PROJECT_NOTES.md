# Project Notes

## Project Name

De-authentication Attack on Wi-Fi Networks

## Purpose

The purpose of this project is to understand how Wi-Fi deauthentication attacks work, how they appear in packet analysis tools, and how defenders can mitigate them. The project was prepared for Network Security Lab and focuses on controlled lab testing and defensive learning.

## Final Deliverables

```text
docs/network-security-deauthentication-report.docx
docs/network-security-deauthentication-report.pdf
screenshots/*.png
references/references.md
README.md
PROJECT_NOTES.md
.gitignore
```

## Key Concepts

### Deauthentication Frames

Deauthentication frames are IEEE 802.11 management frames used to disconnect a wireless client from an access point. If management frame protection is not enabled, attackers can spoof these frames and disrupt connectivity.

### Wireshark Analysis

Wireshark can identify deauthentication frames using WLAN frame filters. Repeated deauthentication frames, spoofed source addresses, and sudden bursts of management traffic can indicate suspicious activity.

### Defensive Mechanisms

Important mitigations include:

- Protected Management Frames
- WPA3 where supported
- Wireless Intrusion Detection Systems
- Router and client firmware updates
- Monitoring for repeated disconnect events
- VPN use for data confidentiality on untrusted networks

## Safety Decisions

The repository intentionally excludes:

```text
packet captures
WPA/WPA2 handshake files
real client MAC addresses
raw wireless traffic logs
attack automation scripts
```

The report and screenshots are sufficient for academic review while keeping the repository safe for GitHub.

## Screenshots

The screenshots folder contains rendered pages from the final report:

```text
01-report-cover.png
02-introduction-objectives-scope.png
03-technical-background-environment-setup.png
04-network-scanning-packet-capture.png
05-deauth-and-wireshark-analysis.png
06-results-and-defensive-mechanisms.png
07-defense-comparison-limitations-conclusion.png
```

## Limitations

This project was performed in a small controlled environment, so results may differ in enterprise wireless networks. Some routers and clients reconnect quickly, which can reduce visible disruption. The project does not include raw packet captures to avoid exposing sensitive wireless data.

## Future Improvements

- Add a separate diagram comparing normal association and deauthentication flow.
- Add a defensive checklist for Wi-Fi administrators.
- Add WIDS detection examples.
- Add comparison of WPA2, WPA3, and 802.11w protections.
- Add a short presentation version for quick viva/demo use.
