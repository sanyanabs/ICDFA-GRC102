# GRC102 Security Governance Simulation

## Practical Lab 8 — Monitoring, Auditing Controls and Executive Reporting

This repository contains the implementation and evidence for the ICDFA GRC102 Security Governance Simulation.

The lab demonstrates how security governance weaknesses can be identified, documented, treated through security controls, and verified using measurable evidence.

All testing was performed in an isolated local Docker environment using synthetic data.

---

## 1. Lab Scope

The simulation models a fictitious organisation with:

- A customer-facing web application
- A customer data database
- A security monitoring component
- Security governance policies, controls, risks, incidents and metrics

The lab focuses on governance weaknesses involving:

- Vulnerability and patch management
- Database access control
- Network segmentation
- Security monitoring
- Incident response
- Governance accountability and measurement

No public systems, third-party infrastructure, real customer data or production credentials were used.

---

## 2. Environment

### Host

- macOS on Apple Silicon
- Docker Desktop
- Docker Compose
- Docker containers using `linux/amd64` where required

### Main Services

| Service | Container | Purpose |
|---|---|---|
| Web application | `web_server` | Simulated customer-facing application |
| Database | `database_server` | Synthetic customer data |
| Monitoring | `monitoring_server` | Security monitoring checks |

### Network Architecture

The environment uses two isolated Docker networks:

```text
                    frontend_network
                           |
              +------------+------------+
              |                         |
       monitoring_server           web_server
                                        |
                                 backend_network
                                        |
                                database_server
