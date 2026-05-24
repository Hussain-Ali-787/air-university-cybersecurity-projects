# Avionics Base Network Configuration

## Overview

This file documents the configuration notes for the **Avionics Base Network Project**.

The original configuration was provided in `Config.txt` and has been converted into a cleaner Markdown format for GitHub documentation.

The configuration includes:

- VLAN gateway addressing
- Point-to-point link addressing
- VLAN creation commands
- Layer-3 switch interface configuration
- OSPF routing configuration
- DHCP excluded-address ranges
- Basic switch/router security configuration
- Logging and MOTD banner configuration

> Note: The original configuration is preserved separately as `Config.txt`. This Markdown version improves readability and fixes obvious documentation typos in notes.

---

## 1. VLAN Gateway Addressing

| VLAN | Gateway IP Address | Name / Department |
|---:|---|---|
| 10 | 192.168.10.1 | HQ-DataCenter |
| 20 | 192.168.20.1 | HQ-ControlCenter |
| 30 | 192.168.30.1 | HQ-SOC |
| 40 | 192.168.40.1 | AMF-Design & Development |
| 50 | 192.168.50.1 | AMF-Prototyping & Testing |
| 60 | 192.168.60.1 | AMF-Quality Control |
| 70 | 192.168.70.1 | AMF-Support Services |
| 80 | 192.168.80.1 | APF-Avionics Design |
| 90 | 192.168.90.1 | APF-Production |
| 100 | 192.168.100.1 | APF-Testing & Calibration |
| 110 | 192.168.110.1 | APF-Support Services |
| 120 | 192.168.120.1 | ARF-Overhaul Division |
| 130 | 192.168.130.1 | ARF-Repair Division |
| 140 | 192.168.140.1 | ARF-Testing & Certification |
| 150 | 192.168.150.1 | ARF-Support Services |
| 160 | 192.168.160.1 | MRF-Overhaul Division |
| 170 | 192.168.170.1 | MRF-Repair Division |
| 180 | 192.168.180.1 | MRF-Testing Division |
| 190 | 192.168.190.1 | MRF-Support Services |
| 200 | 192.168.200.1 | PAC-WAP |

---

## 2. Point-to-Point Link Addressing

| Link | Subnet ID | Usable IPs | Broadcast Address |
|---|---|---|---|
| ISP → FW | 203.0.113.0/30 | 203.0.113.1, 203.0.113.2 | 203.0.113.3 |
| FW → MR | 10.0.0.0/30 | 10.0.0.1, 10.0.0.2 | 10.0.0.3 |
| MR → AMF | 10.0.0.4/30 | 10.0.0.5, 10.0.0.6 | 10.0.0.7 |
| MR → APF | 10.0.0.8/30 | 10.0.0.9, 10.0.0.10 | 10.0.0.11 |
| MR → ARF | 10.0.0.12/30 | 10.0.0.13, 10.0.0.14 | 10.0.0.15 |
| MR → MRF | 10.0.0.16/30 | 10.0.0.17, 10.0.0.18 | 10.0.0.19 |
| MR → DS | 192.168.1.0/30 | 192.168.1.1, 192.168.1.2 | 192.168.1.3 |
| AMF → DS | 192.168.1.4/30 | 192.168.1.5, 192.168.1.6 | 192.168.1.7 |
| APF → DS | 192.168.1.8/30 | 192.168.1.9, 192.168.1.10 | 192.168.1.11 |
| ARF → DS | 192.168.1.12/30 | 192.168.1.13, 192.168.1.14 | 192.168.1.15 |
| MRF → DS | 192.168.1.16/30 | 192.168.1.17, 192.168.1.18 | 192.168.1.19 |

---

## 3. MRF VLAN Configuration

```cisco
enable
configure terminal

vlan 160
vlan 170
vlan 180
vlan 190

exit

interface vlan 160
 ip address 192.168.160.1 255.255.255.0

interface vlan 170
 ip address 192.168.170.1 255.255.255.0

interface vlan 180
 ip address 192.168.180.1 255.255.255.0

interface vlan 190
 ip address 192.168.190.1 255.255.255.0

exit

ip default-gateway 192.168.1.17
ip routing
```

---

## 4. MRF OSPF Configuration

```cisco
router ospf 1
 network 192.168.1.16 0.0.0.3 area 0
 network 192.168.160.0 0.0.0.255 area 0
 network 192.168.170.0 0.0.0.255 area 0
 network 192.168.180.0 0.0.0.255 area 0
 network 192.168.190.0 0.0.0.255 area 0
end
```

> Correction note: the original text contained `192.168.19y0.0`, which has been corrected to `192.168.190.0`.

---

## 5. MRF Router OSPF Configuration

```cisco
enable
configure terminal

ip routing

router ospf 1
 network 10.0.0.16 0.0.0.3 area 0
 network 192.168.1.16 0.0.0.3 area 0

end
```

---

## 6. DHCP Excluded Addresses

```cisco
enable
configure terminal

ip default-gateway 192.168.1.17

ip dhcp excluded-address 192.168.160.1 192.168.160.20
ip dhcp excluded-address 192.168.170.1 192.168.170.20
ip dhcp excluded-address 192.168.180.1 192.168.180.20
ip dhcp excluded-address 192.168.190.1 192.168.190.20
```

---

## 7. AMF Distribution Switch Security Configuration

```cisco
enable
configure terminal

hostname AMF-Dist-SW
no ip domain-lookup

enable secret packamra

line console 0
 password packamra
 login

line vty 0 4
 password packamra
 login
 transport input ssh

service password-encryption
no service dhcp

logging on
logging host 192.168.30.10
logging trap debugging
logging console
logging userinfo

banner motd #
 Unauthorized access is prohibited.
#
```

---

## 8. Security Notes

| Security Control | Purpose |
|---|---|
| `enable secret` | Protects privileged EXEC mode |
| Console password | Restricts local console access |
| VTY password | Restricts remote terminal access |
| `transport input ssh` | Allows SSH-based remote access concept |
| `service password-encryption` | Encrypts plaintext passwords in configuration |
| MOTD banner | Displays an unauthorized access warning |
| Syslog host | Sends logs to the SOC logging server |
| `no ip domain-lookup` | Prevents mistyped commands from triggering DNS lookup delays |

---

## 9. Verification Commands

```cisco
show vlan brief
show interfaces trunk
show ip interface brief
show ip route
show ip ospf neighbor
show running-config
show logging
```

---

## 10. Original Raw Configuration

The raw configuration from `Config.txt` is included below for preservation.

```text
VLAN	IP Address	Name
 10	192.168.10.1	HQ-DataCenter
 20	192.168.20.1	HQ-ControlCenter
 30	192.168.30.1	HQ-SOC
 40	192.168.40.1	AMF-Design & Development
 50	192.168.50.1	AMF-Prototyping & Testing
 60	192.168.60.1	AMF-Quality Control
 70	192.168.70.1	AMF-Support Services
 80	192.168.80.1	APF- Avionics Design
 90	192.168.90.1	APF- Production
100	192.168.100.1	APF-Testing & Calibration
110	192.168.110.1	APF-Support Services
120	192.168.120.1	ARF-Overhaul Division
130	192.168.130.1	ARF-Repair Division
140	192.168.140.1	ARF-Testing & Certification
150	192.168.150.1	ARF-Support Services
160	192.168.160.1	MRF-Overhaul Division
170	192.168.170.1	MRF-Repair Division
180	192.168.180.1	MRF-Testing Division
190	192.168.190.1	MRF-Support Services
200	192.168.200.1	PAC-WAP

Point-to-Point Links
Devices	Subnet ID	Usable IPs			Broadcast Address
ISP->FW	203.0.113.0/24	203.0.113.1,203.0.113.255	203.0.113.255

FW->MR	10.0.0.0/30	10.0.0.1, 10.0.0.2		10.0.0.3
MR->AMF	10.0.0.4/30	10.0.0.5, 10.0.0.6		10.0.0.7
MR->APF	10.0.0.8/30	10.0.0.9, 10.0.0.10		10.0.0.11
MR->ARF	10.0.0.12/30	10.0.0.13, 10.0.0.14		10.0.0.15
MR->MRF	10.0.0.16/30	10.0.0.17, 10.0.0.18		10.0.0.19

MR->DS	192.168.1.0/30	192.168.1.1, 192.168.1.2	192.168.1.3
AMF->DS	192.168.1.4/30	192.168.1.5, 192.168.1.6	192.168.1.7
APF->DS	192.168.1.8/30	192.168.1.9, 192.168.1.10	192.168.1.11
ARF->DS	192.168.1.12/30	192.168.1.13, 192.168.1.14	192.168.1.15
MRF->DS	192.168.1.16/30	192.168.1.17, 192.168.1.18	192.168.1.19


en
conf t 
vlan 160
vlan 170
vlan 180
vlan 190
exit
int vlan 160
ip address 192.168.160.1 255.255.255.0
int vlan 170
ip address 192.168.170.1 255.255.255.0
int vlan 180
ip address 192.168.180.1 255.255.255.0
int vlan 190
ip address 192.168.190.1 255.255.255.0
exit
ip default-gateway 192.168.1.17
ip routing
router ospf 1
network 192.168.1.16 0.0.0.3 area 0
network 192.168.160.0 0.0.0.255 area 0
network 192.168.170.0 0.0.0.255 area 0
network 192.168.180.0 0.0.0.255 area 0
network 192.168.19y0.0 0.0.0.255 area 0
end 

en
conf t
ip routing
router ospf 1
network 10.0.0.16 0.0.0.3 area 0
network 192.168.1.16 0.0.0.3 area 0
end

enable
configure terminal
ip default-gateway 192.168.1.17
ip dhcp excluded-address 192.168.160.1 192.168.160.20
ip dhcp excluded-address 192.168.170.1 192.168.170.20
ip dhcp excluded-address 192.168.180.1 192.168.180.20
ip dhcp excluded-address 192.168.190.1 192.168.190.20

enable
config t
hostname AMF-Dist-SW
no ip domain-lookup
enable secret packamra
line console 0
 password packamra
 login
line vty 0 4
 password packamra
 login
 transport input ssh
service password-encryption
no service dhcp
logging on
logging host 192.168.30.10
logging trap debugging
logging console
logging userinfo
banner motd #
 Unauthorized access is prohibited.
# End of Banner

```
