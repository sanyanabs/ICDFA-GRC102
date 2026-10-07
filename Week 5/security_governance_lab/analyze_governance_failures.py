#!/usr/bin/env python3

import json
import datetime


def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)


def analyze_governance_failures():
    vulnerability_report = load_json("vulnerability_report.json")
    governance_data = load_json("governance_data.json")

    failures = []

    findings = {
        finding["name"]: finding
        for finding in vulnerability_report.get("findings", [])
    }

    # 1. Patch / Vulnerability Management
    struts = findings.get("Apache Struts S2-045")

    if struts and struts.get("status") == "VULNERABLE":
        failures.append({
            "area": "Patch and Vulnerability Management",
            "severity": "High",
            "finding": "Known Apache Struts S2-045 vulnerability remains present.",
            "evidence": struts.get("evidence"),
            "impact": (
                "A known critical vulnerability remains in the environment, "
                "indicating that vulnerability identification has not yet "
                "resulted in effective remediation."
            )
        })

    # 2. Database Access Control
    database_account = findings.get(
        "Database application account host restriction"
    )

    if database_account and database_account.get("status") == "WEAK":
        failures.append({
            "area": "Authentication and Access Control",
            "severity": "High",
            "finding": "Database application account has a wildcard host restriction.",
            "evidence": database_account.get("evidence"),
            "impact": (
                "The application database account is permitted from a broad "
                "host scope rather than being restricted to an approved source."
            )
        })

    # 3. Network Segmentation
    database_network = findings.get("Database network reachability")

    if database_network and database_network.get("status") == "REACHABLE":
        failures.append({
            "area": "Network Segmentation",
            "severity": "High",
            "finding": (
                "Database TCP/3306 is reachable from the monitoring container "
                "on the shared lab network."
            ),
            "evidence": database_network.get("evidence"),
            "impact": (
                "The baseline environment does not yet enforce network "
                "segmentation that restricts database connectivity."
            )
        })

    # 4. Policy Implementation
    controls = governance_data.get("controls", [])

    planned_controls = [
        control for control in controls
        if control.get("status") != "Implemented"
    ]

    if planned_controls:
        failures.append({
            "area": "Policy Implementation and Governance",
            "severity": "Medium",
            "finding": "Governance policies exist but baseline controls are not implemented.",
            "evidence": [
                {
                    "id": control.get("id"),
                    "name": control.get("name"),
                    "status": control.get("status")
                }
                for control in planned_controls
            ],
            "impact": (
                "Policies alone do not provide assurance that security "
                "requirements are operating effectively."
            )
        })

    # 5. Security Monitoring
    monitoring_control_exists = any(
        "monitor" in control.get("name", "").lower()
        for control in controls
    )

    if not monitoring_control_exists:
        failures.append({
            "area": "Security Monitoring",
            "severity": "Medium",
            "finding": "No dedicated security monitoring control is recorded in the baseline tracker.",
            "evidence": "No monitoring control found in governance_data.json",
            "impact": (
                "Security events may not be consistently detected, recorded "
                "and escalated."
            )
        })

    # 6. Governance Metrics
    metrics = governance_data.get("metrics", [])

    metric_gaps = []

    for metric in metrics:
        target = metric.get("target")
        actual = metric.get("actual")
        name = metric.get("name")

        if name == "Patch Compliance" and actual < target:
            metric_gaps.append({
                "metric": name,
                "target": target,
                "actual": actual
            })

        elif name == "Security Incidents" and actual > target:
            metric_gaps.append({
                "metric": name,
                "target": target,
                "actual": actual
            })

    if metric_gaps:
        failures.append({
            "area": "Governance Metrics and Measurement",
            "severity": "Medium",
            "finding": "Baseline security metrics show performance gaps.",
            "evidence": metric_gaps,
            "impact": (
                "Management metrics identify security performance issues "
                "that require remediation and follow-up."
            )
        })

    report = {
        "report_timestamp": datetime.datetime.now().astimezone().isoformat(),
        "environment": "Local ICDFA GRC102 Security Governance Lab",
        "scope": "Authorized local Docker simulation only",
        "failure_count": len(failures),
        "failures": failures
    }

    filename = "governance_failure_report.json"

    with open(filename, "w") as file:
        json.dump(report, file, indent=2)

    print("==============================================")
    print("GRC102 GOVERNANCE FAILURE ANALYSIS")
    print("==============================================")
    print(f"Failures identified: {len(failures)}")
    print()

    for number, failure in enumerate(failures, start=1):
        print(f"{number}. {failure['area']}")
        print(f"   Severity: {failure['severity']}")
        print(f"   Finding: {failure['finding']}")
        print()

    print(f"Report saved to: {filename}")


if __name__ == "__main__":
    analyze_governance_failures()
