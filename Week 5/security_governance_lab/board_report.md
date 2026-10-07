# GRC102 Security Governance Board Report

## Security Governance Simulation – Executive Summary

**Reporting Date:** 7 October 2026  
**Environment:** Isolated GRC102 Security Governance Laboratory

---

## 1. Executive Summary

The baseline security governance assessment identified weaknesses in
vulnerability management, database access control, network segmentation,
security monitoring and governance control implementation.

The assessment used an isolated Docker environment containing a
simulated web application, database and monitoring environment.

Following the baseline assessment, security controls were implemented
and independently verified.

The post-control assessment demonstrates that the identified baseline
technical weaknesses were addressed within the scope of the laboratory
environment.

---

## 2. Baseline Security Position

The baseline assessment identified the following key weaknesses:

- Apache Struts S2-045 (CVE-2017-5638) was detected as vulnerable.
- The application database account used a wildcard host permission:
  `app_user@%`.
- The monitoring container could reach the database on TCP/3306.
- Security governance controls were recorded as Planned.
- No dedicated security monitoring control was recorded.
- Three security risks were identified as Open.

These findings demonstrated a gap between security governance
requirements and implemented technical controls.

---

## 3. Control Actions Implemented

The following controls were implemented:

### Patch and Vulnerability Management

The vulnerable Struts dependency was replaced with a remediated local
image using Struts 2.3.37.

Post-control scanning no longer detected the Struts S2-045 vulnerability.

### Database Access Control

The database application account was changed from:

`app_user@%`

to:

`app_user@localhost`

This restricts the account host scope.

### Network Segmentation

The Docker architecture was changed from a shared network to separate
frontend and backend networks.

The database is attached only to the backend network.

The monitoring container is attached only to the frontend network.

Post-control verification confirmed that TCP/3306 was not reachable from
the monitoring container.

### Security Monitoring

A monitoring control was implemented to verify:

- Web application availability.
- Database network isolation.

Monitoring results are recorded in a security monitoring log.

### Governance Oversight

The governance tracker was updated to reflect implemented controls,
mitigated risks and closure of the simulated security incident.

---

## 4. Post-Control Results

| Indicator | Result | Status |
|---|---|---|
| Critical vulnerability status | NOT_DETECTED | PASS |
| Database access control | RESTRICTED | PASS |
| Database network isolation | NOT_REACHABLE | PASS |
| Web application exposure | LOCAL_ONLY | PASS |
| Governance controls | 4 Implemented | PASS |
| Baseline risks | 3 Mitigated | PASS |

---

## 5. Governance Impact

The exercise demonstrates that effective security governance requires
more than documented policies.

The baseline assessment contained policies and governance records, but
the associated controls were initially marked Planned.

Following implementation and verification, the governance tracker
records the controls as Implemented and the baseline risks as Mitigated.

This provides a traceable relationship between:

**Risk → Control → Evidence → Measurement → Management Review**

---

## 6. Key Governance Lessons

### Vulnerability Management

Known vulnerabilities must have accountable owners, remediation
deadlines and verification evidence.

### Least Privilege

Database access should be restricted to approved sources and unnecessary
wildcard permissions should be removed.

### Network Segmentation

Critical systems should have controlled communication paths to reduce
the potential for lateral movement.

### Security Monitoring

Security controls require monitoring and evidence to demonstrate that
they continue to operate effectively.

### Management Oversight

Security metrics should be linked to ownership, risk treatment and
management review.

---

## 7. Recommendations

### 1. Maintain Vulnerability Management

Continue regular vulnerability scanning and track remediation through
assigned owners and defined deadlines.

### 2. Maintain Access Reviews

Periodically review database accounts and host restrictions to identify
unnecessary access.

### 3. Maintain Network Segmentation

Review network paths whenever infrastructure or application architecture
changes.

### 4. Continue Security Monitoring

Maintain monitoring logs and incorporate monitoring results into regular
security governance reviews.

### 5. Maintain Governance Evidence

Retain control verification evidence and use governance metrics to
support management decision-making.

---

## 8. Management Conclusion

The GRC102 simulation demonstrates measurable improvement between the
baseline and post-control states.

The critical vulnerability identified during the baseline assessment is
no longer detected, database access has been restricted, prohibited
database connectivity has been blocked, monitoring has been implemented
and the identified baseline risks have been treated.

These results demonstrate effective control implementation within the
scope of the isolated laboratory environment.

The controls should continue to be monitored and periodically
reassessed to ensure that the improvements are sustained.
