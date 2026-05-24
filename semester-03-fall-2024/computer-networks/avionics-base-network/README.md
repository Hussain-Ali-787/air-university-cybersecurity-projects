# Avionics Base Network Project

## Project Title

**Avionics Base Network**

## Course Information

**Course:** Computer Networks Lab  
**Course Code:** CS260L  
**Department:** Cyber Security  
**University:** Air University, Islamabad  
**Instructor:** Sir Mohsin Sarfraz

## Project Overview

This project presents a simulated network architecture for an aviation/military base inspired by PAC Kamra and PAF Base Minhas. The design models a secure, scalable, and segmented network that connects PAC HQ with multiple factory locations using VLANs, point-to-point links, OSPF routing, centralized services, and basic security controls.

The project was developed as a Cisco Packet Tracer based design. Since the final repository may be reviewed without Packet Tracer installed, the main visual reference is included as:

```text
topology/logical_diagram.png
```

This topology image should be used as the primary visual overview of the network.

## Team Members

| Name | Registration ID |
|---|---:|
| Hussain Ali | 232095 |
| Ahmad Ali | 232147 |

## Main Network Sites

| Site | Purpose |
|---|---|
| PAC HQ | Core infrastructure, firewall, main router, distribution switch, servers, SOC, and control center |
| AMF | Aircraft Manufacturing Factory |
| APF | Avionics Production Factory |
| ARF | Aircraft Rebuild Factory |
| MRF | Mirage Rebuild Factory |

## Design Objectives

- Design a scalable aviation-base network.
- Segment departments using VLANs.
- Provide inter-department and inter-site communication.
- Use point-to-point links for factory-to-HQ connectivity.
- Configure OSPF for dynamic routing.
- Provide centralized services such as DNS, FTP, Web, and Mail.
- Apply basic security features such as firewall placement, ACL concepts, password encryption, SSH access concept, and logging.

## Network Design Summary

The network follows a hierarchical design:

1. **PAC HQ Core Layer**  
   Contains the firewall, main router, distribution switch, SOC, control center, and centralized servers.

2. **Factory Networks**  
   AMF, APF, ARF, and MRF are connected to PAC HQ using point-to-point links.

3. **VLAN Segmentation**  
   Each department is placed in a separate VLAN to improve organization, isolation, and manageability.

4. **Routing**  
   OSPF is used for route advertisement between HQ and factory networks.

5. **Centralized Services**  
   DNS, FTP, Web, and Mail services are hosted for network-wide access.

## VLAN Allocation Summary

| VLAN Range | Site / Department Group |
|---|---|
| VLAN 10 | HQ Data Center |
| VLAN 20 | HQ Control Center |
| VLAN 30 | HQ SOC |
| VLAN 40-70 | AMF departments |
| VLAN 80-110 | APF departments |
| VLAN 120-150 | ARF departments |
| VLAN 160-190 | MRF departments |
| VLAN 200 | PAC Wireless Access Point |

## Important Files

| Path | Description |
|---|---|
| `packet-tracer/Avionics_Base_Network_Simulation.pkt` | Cisco Packet Tracer simulation file |
| `topology/logical_diagram.png` | Main logical topology diagram for review without Packet Tracer |
| `configs/Avionics_Base_Network_Configs.md` | Clean Markdown configuration documentation |
| `docs/Avionics_Base_Network_Report.docx` | Final project report |
| `presentation/Avionics_Base_Network_Presentation.pptx` | Final presentation |
| `PROJECT_NOTES.md` | Project explanation, assumptions, and future improvements |
| `RUN_GUIDE.md` | Review and run guide |

## Repository Structure

```text
avionics-base-network/
├── configs/
│   └── Avionics_Base_Network_Configs.md
├── docs/
│   └── Avionics_Base_Network_Report.docx
├── packet-tracer/
│   └── Avionics_Base_Network_Simulation.pkt
├── presentation/
│   └── Avionics_Base_Network_Presentation.pptx
├── screenshots/
│   └── .gitkeep
├── topology/
│   └── logical_diagram.png
├── .gitignore
├── PROJECT_NOTES.md
├── README.md
└── RUN_GUIDE.md
```

## Reviewing Without Cisco Packet Tracer

If Cisco Packet Tracer is not installed, review the project using:

1. `topology/logical_diagram.png` for the complete network topology.
2. `docs/Avionics_Base_Network_Report.docx` for technical explanation.
3. `configs/Avionics_Base_Network_Configs.md` for VLAN, IP addressing, OSPF, DHCP, and security commands.
4. `presentation/Avionics_Base_Network_Presentation.pptx` for summarized project flow.

The `screenshots/` directory is kept as a placeholder for optional future Packet Tracer verification screenshots. It is not required for the current final version.

## How to Open the Simulation

If Cisco Packet Tracer is available:

1. Open Cisco Packet Tracer.
2. Load `packet-tracer/Avionics_Base_Network_Simulation.pkt`.
3. Review the logical topology.
4. Inspect device configurations through CLI.
5. Test connectivity and services using ping, DNS, FTP, Web, and Mail tools.

## Academic Note

This project is an academic simulation created for Computer Networks Lab. It demonstrates network design, VLAN segmentation, routing, services, and security concepts in a Packet Tracer environment. It is not a real deployment of PAC Kamra or any military aviation base network.
