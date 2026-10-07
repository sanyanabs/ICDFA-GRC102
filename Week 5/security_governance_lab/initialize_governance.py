#!/usr/bin/env python3

import datetime
from governance_tracker import GovernanceTracker


def initialize_governance_data():

    tracker = GovernanceTracker()

    today = datetime.date.today()
    review_date = today + datetime.timedelta(days=365)

    # -----------------------------
    # Policies
    # -----------------------------

    patch_policy_id = tracker.add_policy(
        "Patch Management Policy",
        "Policy governing the timely identification, testing and application of security patches.",
        "IT Manager",
        today.isoformat(),
        review_date.isoformat()
    )

    vulnerability_policy_id = tracker.add_policy(
        "Vulnerability Management Policy",
        "Policy governing the identification, assessment and remediation of security vulnerabilities.",
        "Security Engineer",
        today.isoformat(),
        review_date.isoformat()
    )

    incident_policy_id = tracker.add_policy(
        "Incident Response Policy",
        "Policy governing the detection, escalation, response and recovery from security incidents.",
        "Security Director",
        today.isoformat(),
        review_date.isoformat()
    )

    # -----------------------------
    # Controls
    # -----------------------------

    tracker.add_control(
        "Patch Management Process",
        "Process for identifying, assessing, testing and applying security patches.",
        patch_policy_id,
        "IT Manager",
        today.isoformat()
    )

    tracker.add_control(
        "Vulnerability Scanning",
        "Regular scanning of systems for known security vulnerabilities.",
        vulnerability_policy_id,
        "Security Engineer",
        today.isoformat()
    )

    tracker.add_control(
        "Incident Response Process",
        "Defined process for detecting, escalating, investigating and resolving security incidents.",
        incident_policy_id,
        "Security Director",
        today.isoformat()
    )

    # -----------------------------
    # Risks
    # -----------------------------

    tracker.add_risk(
        "Unpatched Vulnerabilities",
        "Risk of exploitation due to known vulnerabilities remaining unpatched.",
        "High",
        "High",
        "Security Engineer",
        "Implement formal patch management and vulnerability remediation tracking."
    )

    tracker.add_risk(
        "Insufficient Network Segmentation",
        "Risk of lateral movement because systems share the same network segment.",
        "Medium",
        "High",
        "Network Engineer",
        "Implement network segmentation based on least privilege."
    )

    tracker.add_risk(
        "Weak Database Access Controls",
        "Risk of unauthorized database access due to broad application account host permissions.",
        "Medium",
        "High",
        "Database Administrator",
        "Restrict database account access and review database privileges."
    )

    # -----------------------------
    # Baseline Incident
    # -----------------------------

    tracker.add_incident(
        "Simulated Web Server Exposure",
        "Baseline security simulation identified a vulnerable Struts web application.",
        today.isoformat(),
        "High",
        "web_server",
        "Unpatched Apache Struts S2-045 vulnerability (CVE-2017-5638).",
        "Control implementation required; remediation will be verified in Part 3."
    )

    # -----------------------------
    # Baseline Metrics
    # -----------------------------

    period = today.strftime("%B %Y")

    tracker.add_metric(
        "Patch Compliance",
        "Percentage of systems with required security patches applied.",
        95.0,
        0.0,
        period,
        "Needs Improvement"
    )

    tracker.add_metric(
        "Critical Vulnerability Remediation Time",
        "Average time to remediate critical vulnerabilities in days.",
        7.0,
        0.0,
        period,
        "Baseline"
    )

    tracker.add_metric(
        "Security Incidents",
        "Number of security incidents recorded during the reporting period.",
        0.0,
        1.0,
        period,
        "Needs Improvement"
    )

    # -----------------------------
    # Baseline Audit
    # -----------------------------

    tracker.add_audit(
        "GRC102 Baseline Security Governance Assessment",
        "Baseline assessment of the simulated web application, database and network environment.",
        today.isoformat(),
        "GRC102 Lab Assessment",
        "Unpatched Struts vulnerability, broad database account host permission and insufficient network segmentation were identified.",
        "Implement patch management, strengthen database access controls and implement network segmentation."
    )

    print("Governance tracker initialized successfully.")


if __name__ == "__main__":
    initialize_governance_data()
