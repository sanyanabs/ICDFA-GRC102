# GRC102 Security Governance Controls Report

## 1. Purpose

This report documents the security governance controls implemented in the isolated ICDFA GRC102 Security Governance Lab.

The controls were implemented in response to weaknesses identified during the baseline assessment, including an unpatched Apache Struts condition, broad database account access, insufficient network segmentation, and limited security monitoring.

All testing was performed within the local Docker-based lab environment.

---

## 2. Control Implementation Summary

| Control ID | Control | Baseline State | Implementation | Post-Control Result |
|---|---|---|---|---|
| CTL-001 | Patch Management Process | Planned | Replaced the vulnerable Struts dependency with a local patched image using Struts 2.3.37 | Struts S2-045 condition no longer detected |
| CTL-002 | Vulnerability Scanning | Planned | Implemented a local vulnerability and control verification scanner | Post-control scan completed |
| CTL-003 | Incident Response Process | Planned | Added incident tracking and documented resolution of the simulated security incident | INC-001 closed |
| CTL-004 | Security Monitoring | Not implemented | Added security monitoring script to check web availability and database network reachability | Monitoring log generated |

---

## 3. Database Access Control

### Baseline Finding

The application database account was initially configured as:

```text
app_user@%
