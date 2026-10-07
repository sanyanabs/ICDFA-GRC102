# GRC102 Governance Failure Analysis

## 1. Purpose

This analysis documents the governance weaknesses identified during the
baseline assessment of the isolated GRC102 security governance simulation.

The findings are based on the vulnerability scan, governance tracker,
database configuration and authorized attack simulation.

No real-world systems, customer data or external infrastructure were tested.

---

## 2. Governance Failures Identified

### 2.1 Patch and Vulnerability Management

**Severity:** High

The baseline environment contains Apache Struts S2-045
(CVE-2017-5638), which was identified as vulnerable during the baseline
security scan.

**Evidence:**

- Finding: Apache Struts S2-045
- Status: VULNERABLE
- Evidence: `X-Vulnerable=true`

**Governance weakness:**

The vulnerability has been identified but has not yet been remediated.
This demonstrates a gap between vulnerability identification and
effective remediation.

**Potential impact:**

A known critical vulnerability could remain available for exploitation
if remediation is not tracked, assigned and completed within the required
timeframe.

---

### 2.2 Authentication and Access Control

**Severity:** High

The database application account was found with a wildcard host
restriction:

`app_user    %`

**Governance weakness:**

The database account is permitted from a broad host scope rather than
being restricted to an approved source.

**Potential impact:**

A broader account scope increases the potential attack surface and is
inconsistent with the principle of least privilege.

---

### 2.3 Network Segmentation

**Severity:** High

The baseline Docker environment uses a shared network and the monitoring
container was able to establish TCP connectivity to the database on
port 3306.

**Evidence:**

`TCP/3306 reachable from monitoring container`

**Governance weakness:**

Network segmentation controls have not yet been implemented to restrict
which systems can communicate with the database.

**Potential impact:**

If an attacker compromised another system on the same network, the lack
of network-level restrictions could increase opportunities for lateral
movement.

**Scope clarification:**

The test confirms monitoring-container-to-database connectivity. It does
not establish that the web server directly accessed the database.

---

### 2.4 Policy Implementation and Governance

**Severity:** Medium

The governance tracker contains security policies and associated
controls, but the controls are still recorded as `Planned`.

The baseline controls include:

| Control | Status |
|---|---|
| Patch Management Process | Planned |
| Vulnerability Scanning | Planned |
| Incident Response Process | Planned |

**Governance weakness:**

Policies have been defined, but the associated controls have not yet been
implemented and verified.

**Potential impact:**

Having documented policies without operating controls does not provide
assurance that security requirements are being followed.

---

### 2.5 Security Monitoring

**Severity:** Medium

No dedicated security monitoring control is recorded in the baseline
governance tracker.

**Governance weakness:**

There is no baseline control demonstrating that security events are
consistently monitored, detected, recorded and escalated.

**Potential impact:**

Security events may remain undetected or may not be escalated in a
consistent and timely manner.

---

### 2.6 Governance Metrics and Measurement

**Severity:** Medium

The baseline governance metrics show performance gaps.

| Metric | Target | Actual |
|---|---:|---:|
| Patch Compliance | 95% | 0% |
| Security Incidents | 0 | 1 |

**Governance weakness:**

The metrics show that security performance is below the defined targets.

**Potential impact:**

If metrics are not linked to ownership, remediation actions and
management review, identified security weaknesses may remain unresolved.

---

## 3. Root Governance Themes

The six findings can be grouped into four broader governance themes.

### 3.1 Preventive Control Weakness

The vulnerable Struts component, broad database account scope and lack of
network segmentation demonstrate weaknesses in preventive security
controls.

### 3.2 Control Implementation Gap

Security policies exist, but their associated controls remain planned.
This demonstrates a gap between policy definition and operational
implementation.

### 3.3 Detection and Monitoring Gap

The baseline does not contain a dedicated security monitoring control.
This creates a weakness in the ability to detect and escalate security
events.

### 3.4 Measurement and Accountability Gap

The governance metrics show that patch compliance and security incident
performance are outside their targets. These results require ownership,
remediation and management follow-up.

---

## 4. Authorized Attack Simulation

An authorized attack simulation was performed against the vulnerable
local web application.

The simulation identified the Struts S2-045 vulnerability and recorded
a simulated database access and data-exfiltration scenario.

The simulation was explicitly configured as a safe simulation.

No command execution or actual data exfiltration was performed.

The database contained only synthetic laboratory records.

Therefore, the simulation demonstrates the potential impact of the
identified weakness rather than documenting a real compromise.

---

## 5. Overall Assessment

The baseline assessment demonstrates that security governance weaknesses
can exist even when policies and governance records have been created.

The primary issue is the gap between identifying security requirements
and demonstrating that controls are implemented, operating effectively
and producing measurable results.

The next stage of the laboratory will therefore focus on implementing
the required controls and performing post-control verification.
