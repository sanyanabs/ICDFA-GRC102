#!/usr/bin/env python3

import json
import datetime


def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)


def calculate_metrics():
    vulnerability_report = load_json("vulnerability_report.json")
    governance_data = load_json("governance_data.json")

    findings = {
        finding["name"]: finding
        for finding in vulnerability_report.get("findings", [])
    }

    metrics = []

    # Critical vulnerability status
    struts = findings.get("Apache Struts S2-045", {})
    struts_status = struts.get("status", "UNKNOWN")

    metrics.append({
        "metric": "Critical Vulnerability Status",
        "result": struts_status,
        "target": "NOT_DETECTED",
        "status": "PASS" if struts_status == "NOT_DETECTED" else "FAIL",
        "evidence": struts.get("evidence", "")
    })

    # Database access control
    db_access = findings.get(
        "Database application account host restriction", {}
    )

    db_access_status = db_access.get("status", "UNKNOWN")

    metrics.append({
        "metric": "Database Access Control",
        "result": db_access_status,
        "target": "RESTRICTED",
        "status": "PASS" if db_access_status == "RESTRICTED" else "FAIL",
        "evidence": db_access.get("evidence", "")
    })

    # Network segmentation
    network = findings.get(
        "Database network reachability", {}
    )

    network_status = network.get("status", "UNKNOWN")

    metrics.append({
        "metric": "Database Network Isolation",
        "result": network_status,
        "target": "NOT_REACHABLE",
        "status": "PASS" if network_status == "NOT_REACHABLE" else "FAIL",
        "evidence": network.get("evidence", "")
    })

    # Web exposure
    web = findings.get(
        "Web application host exposure", {}
    )

    web_status = web.get("status", "UNKNOWN")

    metrics.append({
        "metric": "Web Application Exposure",
        "result": web_status,
        "target": "LOCAL_ONLY",
        "status": "PASS" if web_status == "LOCAL_ONLY" else "FAIL",
        "evidence": web.get("evidence", "")
    })

    # Governance controls
    controls = governance_data.get("controls", [])

    implemented_controls = [
        control for control in controls
        if control.get("status") == "Implemented"
    ]

    metrics.append({
        "metric": "Governance Control Implementation",
        "result": len(implemented_controls),
        "target": len(controls),
        "status": (
            "PASS"
            if controls and len(implemented_controls) == len(controls)
            else "FAIL"
        ),
        "evidence": [
            control.get("id")
            for control in implemented_controls
        ]
    })

    # Risk treatment
    risks = governance_data.get("risks", [])

    mitigated_risks = [
        risk for risk in risks
        if risk.get("status") == "Mitigated"
    ]

    metrics.append({
        "metric": "Baseline Risk Treatment",
        "result": len(mitigated_risks),
        "target": len(risks),
        "status": (
            "PASS"
            if risks and len(mitigated_risks) == len(risks)
            else "FAIL"
        ),
        "evidence": [
            risk.get("id")
            for risk in mitigated_risks
        ]
    })

    report = {
        "report_timestamp": datetime.datetime.now().astimezone().isoformat(),
        "environment": "Local ICDFA GRC102 Security Governance Lab",
        "metrics": metrics
    }

    with open("metrics_report.json", "w") as file:
        json.dump(report, file, indent=2)

    print("==============================================")
    print("GRC102 SECURITY GOVERNANCE METRICS")
    print("==============================================")

    for metric in metrics:
        print(
            f"{metric['metric']}: "
            f"{metric['result']} | "
            f"Target: {metric['target']} | "
            f"{metric['status']}"
        )

    print()
    print("Metrics report saved to: metrics_report.json")


if __name__ == "__main__":
    calculate_metrics()
