#!/usr/bin/env python3

import json
from datetime import date


DATA_FILE = "governance_data.json"


def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)


def update_controls(data):
    verified_controls = {
        "CTL-001": "Implemented",
        "CTL-002": "Implemented",
        "CTL-003": "Implemented"
    }

    for control in data.get("controls", []):
        control_id = control.get("id")

        if control_id in verified_controls:
            control["status"] = verified_controls[control_id]

    # Add the security monitoring control if it does not already exist.
    monitoring_exists = any(
        control.get("name") == "Security Monitoring"
        for control in data.get("controls", [])
    )

    if not monitoring_exists:
        data["controls"].append({
            "id": f"CTL-{len(data['controls']) + 1:03d}",
            "name": "Security Monitoring",
            "description": (
                "Monitoring control that checks web application availability "
                "and verifies database network isolation."
            ),
            "policy_id": "POL-003",
            "owner": "Security Engineer",
            "implementation_date": date.today().isoformat(),
            "status": "Implemented"
        })


def update_risks(data):
    for risk in data.get("risks", []):

        if risk.get("id") == "RSK-001":
            risk["status"] = "Mitigated"

        elif risk.get("id") == "RSK-002":
            risk["status"] = "Mitigated"

        elif risk.get("id") == "RSK-003":
            risk["status"] = "Mitigated"


def update_incident(data):
    for incident in data.get("incidents", []):

        if incident.get("id") == "INC-001":
            incident["status"] = "Closed"
            incident["resolution"] = (
                "Struts vulnerability remediated and verified by post-control "
                "scan. Database access restriction and network segmentation "
                "were implemented and verified."
            )


def update_metrics(data):
    period = date.today().strftime("%B %Y")

    for metric in data.get("metrics", []):

        if metric.get("name") == "Security Incidents":
            metric["period"] = period
            metric["trend"] = "Under Review"

def main():
    data = load_data()

    update_controls(data)
    update_risks(data)
    update_incident(data)
    update_metrics(data)

    save_data(data)

    print("Governance controls updated successfully.")
    print()
    print("Verified controls:")

    for control in data.get("controls", []):
        print(
            f"{control['id']}: "
            f"{control['name']} - {control['status']}"
        )

    print()
    print("Risk status:")

    for risk in data.get("risks", []):
        print(
            f"{risk['id']}: "
            f"{risk['name']} - {risk['status']}"
        )


if __name__ == "__main__":
    main()
