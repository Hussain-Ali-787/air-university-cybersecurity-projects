# Project Notes

## Project Name

Avionics Base Network Project

## Purpose

The purpose of this project is to design and simulate a secure and scalable network for a military aviation base inspired by PAC Kamra / PAF Base Minhas. The project demonstrates practical Computer Networks Lab concepts using Cisco Packet Tracer and supporting documentation.

## Review Note

Cisco Packet Tracer is not required to understand the final repository. The main topology screenshot is provided in:

```text
topology/logical_diagram.png
```

This diagram should be treated as the primary visual reference for GitHub review and portfolio presentation.

The `screenshots/` folder is intentionally kept only as a placeholder. Additional screenshots such as ping tests, OSPF verification, or service checks can be added later if Packet Tracer is available.

## Main Concepts Demonstrated

- Hierarchical network design
- VLAN-based segmentation
- Inter-VLAN routing
- Point-to-point WAN links
- OSPF dynamic routing
- Centralized DNS, FTP, Web, and Mail services
- Firewall and ACL concepts
- Basic device hardening
- Syslog logging concept
- Secure access concept using SSH

## Network Areas

### PAC HQ

PAC HQ represents the core site. It contains the firewall, main router, distribution switch, SOC, control center, and centralized service servers.

### AMF

Aircraft Manufacturing Factory. It includes design, prototyping, quality control, and support service departments.

### APF

Avionics Production Factory. It uses VLAN 80-110 in the final corrected mapping.

### ARF

Aircraft Rebuild Factory. It uses VLAN 120-150 in the final corrected mapping.

### MRF

Mirage Rebuild Factory. It uses VLAN 160-190.

## Final VLAN Mapping

| VLAN Range | Site |
|---|---|
| 10-30 | PAC HQ |
| 40-70 | AMF |
| 80-110 | APF |
| 120-150 | ARF |
| 160-190 | MRF |
| 200 | PAC-WAP |

## Addressing Design

The project uses:

- `/24` subnets for VLANs.
- `/30` subnets for point-to-point router links.
- Private addressing for internal networks.
- Example public addressing for the ISP-to-firewall segment.

## Routing Design

OSPF is used for dynamic routing between PAC HQ, factory routers, and routed distribution links. OSPF area 0 is used in the provided configuration notes.

## Security Design

Security concepts included in the project:

- Firewall placement at the PAC HQ edge
- VLAN segmentation
- ACL-based restriction concept
- Console and VTY password protection
- SSH remote access concept
- Password encryption
- MOTD warning banner
- Syslog host configuration
- Recommendations for IPS, WPA3, RBAC, VPNs, audits, and redundancy

## Files Included

| Folder | Purpose |
|---|---|
| `packet-tracer/` | Packet Tracer simulation file |
| `configs/` | Markdown configuration documentation |
| `docs/` | Final report |
| `presentation/` | Final presentation |
| `topology/` | Main logical topology diagram |
| `screenshots/` | Optional placeholder for future verification screenshots |

## Limitations

- The project is a Packet Tracer simulation, not a real deployed network.
- Live verification screenshots are not included because Packet Tracer is not currently available.
- Security controls are implemented at an academic simulation level.
- Some advanced enterprise features such as AAA, HSRP/VRRP, EtherChannel, VPN tunnels, and IPS are suggested as future improvements.

## Future Improvements

- Add Packet Tracer verification screenshots when Packet Tracer is available.
- Add ping test screenshots between HQ and factory VLANs.
- Add OSPF neighbor and routing table screenshots.
- Add DNS, FTP, Web, and Mail service verification screenshots.
- Add HSRP or VRRP gateway redundancy.
- Add EtherChannel between distribution and access switches.
- Add centralized AAA using RADIUS or TACACS+.
- Add a formal ACL policy matrix.
- Add a separate IP addressing spreadsheet.
