# Run and Review Guide

## Primary Review Method Without Packet Tracer

If Cisco Packet Tracer is not installed, review the project through the included documentation:

1. Open `topology/logical_diagram.png` to understand the full network layout.
2. Open `docs/Avionics_Base_Network_Report.docx` for the complete written explanation.
3. Open `configs/Avionics_Base_Network_Configs.md` to review VLANs, point-to-point links, OSPF, DHCP exclusions, and security commands.
4. Open `presentation/Avionics_Base_Network_Presentation.pptx` for a summarized project walkthrough.

This is enough to understand the project structure and technical design without running the Packet Tracer file.

## Opening the Packet Tracer File

If Cisco Packet Tracer is available:

1. Launch Cisco Packet Tracer.
2. Open:

```text
packet-tracer/Avionics_Base_Network_Simulation.pkt
```

3. Wait for links and devices to initialize.
4. Review the logical topology.
5. Inspect router and switch CLI configurations.

## Suggested Verification Commands

Use these commands on routers and switches if Packet Tracer is available:

```cisco
show ip interface brief
show ip route
show ip ospf neighbor
show running-config
show vlan brief
show interfaces trunk
show logging
```

## Suggested Connectivity Tests

If Packet Tracer is available, test:

- PAC HQ device to factory device ping
- Factory device to PAC HQ server ping
- Inter-VLAN routing inside a factory
- DNS resolution
- FTP access
- Web server access
- Mail service availability

## Screenshots Policy

The current final repository relies on `topology/logical_diagram.png` as the main visual proof. The `screenshots/` folder is optional and currently reserved for future Packet Tracer verification screenshots.

Recommended future screenshots:

```text
01-full-logical-topology.png
02-pac-hq-core.png
03-factory-network-example.png
04-show-vlan-brief.png
05-show-ip-interface-brief.png
06-show-ip-ospf-neighbor.png
07-show-ip-route.png
08-successful-ping-test.png
09-service-verification.png
```

## Notes

The project can be reviewed academically without Packet Tracer because the report, configuration Markdown, presentation, and topology diagram explain the complete design.
