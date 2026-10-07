# GRC102 Security Governance Metrics Framework

## 1. Purpose

This framework defines the security governance metrics used to measure
the effectiveness of the controls implemented during the GRC102
security governance simulation.

The metrics are intended to support management oversight, identify
control weaknesses and provide evidence for security governance
decision-making.

---

## 2. Metrics

### 2.1 Critical Vulnerability Status

**Purpose:**  
Measure whether identified critical vulnerabilities have been
remediated and verified.

**Measurement:**

Number of critical vulnerabilities detected during the latest verified
security scan.

**Baseline:**

Apache Struts S2-045 was detected as vulnerable.

**Post-control result:**

Apache Struts S2-045 was not detected after remediation.

**Target:**

No unresolved critical vulnerabilities.

**Reporting frequency:**

Monthly and after significant remediation activity.

**Owner:**

Security Engineer.

---

### 2.2 Database Access Control Compliance

**Purpose:**  
Measure whether database application accounts are restricted to approved
hosts.

**Measurement:**

Number of application database accounts using approved host restrictions.

**Baseline:**

`app_user@%`

**Post-control result:**

`app_user@localhost`

**Target:**

No unnecessary wildcard host permissions.

**Reporting frequency:**

Monthly and after database access-control changes.

**Owner:**

Database Administrator.

---

### 2.3 Network Segmentation Status

**Purpose:**  
Measure whether restricted systems can communicate only through approved
network paths.

**Measurement:**

Verification of prohibited network connectivity between monitoring and
database systems.

**Baseline:**

Monitoring container could reach database TCP/3306.

**Post-control result:**

Monitoring container cannot reach database TCP/3306.

**Target:**

Prohibited database connectivity blocked.

**Reporting frequency:**

Monthly and after network architecture changes.

**Owner:**

Network Engineer.

---

### 2.4 Security Monitoring Coverage

**Purpose:**  
Measure whether the defined security monitoring control is operating.

**Measurement:**

Successful execution of the monitoring check and availability of
monitoring logs.

**Baseline:**

No dedicated security monitoring control recorded.

**Post-control result:**

Security monitoring script implemented and producing monitoring logs.

**Target:**

Monitoring control operational with evidence available for review.

**Reporting frequency:**

Continuous operation with monthly management review.

**Owner:**

Security Engineer.

---

### 2.5 Governance Control Implementation

**Purpose:**  
Measure whether security governance controls are implemented and
operating.

**Measurement:**

Number of defined security controls with verified implementation status.

**Baseline:**

3 controls were recorded as Planned.

**Post-control result:**

4 controls are recorded as Implemented.

**Target:**

All required controls implemented and supported by evidence.

**Reporting frequency:**

Monthly.

**Owner:**

Security Governance Owner.

---

### 2.6 Open Security Risks

**Purpose:**  
Measure whether identified security risks have been addressed.

**Measurement:**

Number of open risks in the governance tracker.

**Baseline:**

3 security risks were open.

**Post-control result:**

The three baseline risks are recorded as Mitigated.

**Target:**

No unaddressed high-priority risks without an approved treatment plan.

**Reporting frequency:**

Monthly.

**Owner:**

Security Governance Owner.

---

## 3. Management Reporting Principles

Metrics should:

1. Have a clearly defined measurement method.
2. Have an accountable owner.
3. Have a defined target.
4. Be supported by evidence.
5. Be reviewed regularly.
6. Trigger remediation when targets are not achieved.

Metrics should not be presented as evidence of control effectiveness unless
the underlying measurement method and evidence are available.

---

## 4. Baseline-to-Post-Control Reporting

| Metric | Baseline | Post-Control | Target |
|---|---|---|---|
| Critical vulnerability status | S2-045 detected | S2-045 not detected | No unresolved critical vulnerabilities |
| Database access restriction | `app_user@%` | `app_user@localhost` | No unnecessary wildcard access |
| Database network isolation | TCP/3306 reachable | TCP/3306 blocked | Prohibited access blocked |
| Security monitoring | No dedicated control | Control operational | Monitoring evidence available |
| Governance controls | 3 Planned | 4 Implemented | Required controls implemented |
| Open baseline risks | 3 Open | 3 Mitigated | Risks treated or formally accepted |

---

## 5. Executive Interpretation

The post-control results demonstrate improvement in the specific security
weaknesses identified during the baseline assessment.

The results should be interpreted as evidence of control effectiveness
within the isolated GRC102 laboratory environment and should not be
represented as evidence of security posture across a real production
environment.
