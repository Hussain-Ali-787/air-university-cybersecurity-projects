# Information Assurance Semester Project

## Project Title

**A Robust Contingency Framework for Habib Bank Limited (HBL)**

## Course

Information Assurance / Intro to Management Project  
Department of Cyber Security  
Air University, Islamabad

## Project Overview

This project presents a contingency framework for **Habib Bank Limited (HBL)**, a banking-sector organization that requires operational resilience, regulatory compliance, and recovery capability. The framework focuses on maintaining critical banking services during disruptions such as cyber incidents, IT failures, network downtime, data center issues, and natural disasters.

The project covers:

- Compliance framework analysis
- Risk assessment and management
- Compliance monitoring and auditing
- Employee training and awareness
- Contingency planning
- Incident Response Plan (IRP)
- Business Continuity Plan (BCP)
- Disaster Recovery Plan (DRP)

## Selected Organization

**Organization:** Habib Bank Limited (HBL)  
**Sector:** Banking

HBL was selected because banking organizations operate under strict regulatory, operational, and cybersecurity requirements. Their services, including core banking, online banking, payment processing, and customer support, must remain available and recoverable during disruptions.

## Team Members

| Name | Registration ID |
|---|---:|
| Muhammad Abdullah | 232992 |
| Hussain Ali | 232095 |
| Jazib Ali Rizvi | 232145 |
| Shehroze Sameer | 232091 |
| Sardar Ahmad Ali | 232147 |

## Key Framework Components

### Compliance Framework Analysis

The project analyzes HBL against major standards and frameworks:

- State Bank of Pakistan (SBP) regulatory requirements
- ISO/IEC 27001
- PCI DSS
- NIST Cybersecurity Framework

### Risk Assessment and Management

The risk assessment prioritizes operational and cybersecurity risks based on impact, likelihood, and priority.

Key risks include:

- Cybersecurity breach
- Hardware or data center failure
- Natural disasters
- Network downtime

### Contingency Plan

The contingency plan defines recovery and continuity strategies for critical banking functions.

| Business Function | RTO | RPO | Backup Solution |
|---|---:|---:|---|
| Core banking systems | 2 hours | 30 minutes | Cloud-based data replication |
| Online banking | 1 hour | 15 minutes | Redundant servers |
| Payment processing | 2 hours | 30 minutes | Off-site and cloud backups |
| Customer service helplines | 4 hours | 2 hours | Call forwarding and backup sites |

### Incident Response Plan

The IRP defines a structured response process:

1. Detection
2. Containment
3. Eradication
4. Recovery
5. Post-incident review

### Business Continuity Plan

The BCP focuses on keeping essential banking services available during disruptions through alternate work locations, redundant IT infrastructure, customer communication channels, and regular testing.

### Disaster Recovery Plan

The DRP focuses on restoring critical IT systems after a disaster using cloud failover, secondary data centers, redundant backups, and structured restoration steps.

## Repository Structure

```text
hbl-contingency-framework/
|-- docs/
|   `-- hbl-contingency-framework-report.docx
|-- presentation/
|   `-- hbl-contingency-framework-presentation.pptx
|-- .gitignore
|-- PROJECT_NOTES.md
|-- RUN_GUIDE.md
`-- README.md
```

## Deliverables

| Deliverable | Description |
|---|---|
| `docs/hbl-contingency-framework-report.docx` | Detailed written project report covering compliance, risk, contingency, IRP, BCP, and DRP |
| `presentation/hbl-contingency-framework-presentation.pptx` | Slide deck summarizing the framework and key findings |
| `PROJECT_NOTES.md` | Short explanation of project scope, limitations, and future improvements |

## Recommendations

The project recommends:

- Regular BCP and DRP drills
- AI-driven monitoring and detection
- Stronger compliance automation
- Improved employee awareness training
- Legacy system upgrades
- Quarterly compliance reviews
- Integration of threat intelligence platforms

## Academic Note

This is an academic project prepared for learning and demonstration purposes. It does not claim to represent HBL's actual internal security architecture, confidential processes, or non-public compliance status.
