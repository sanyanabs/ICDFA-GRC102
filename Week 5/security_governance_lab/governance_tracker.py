#!/usr/bin/env python3

import os
import json
import argparse


class GovernanceTracker:

    def __init__(self, data_file="governance_data.json"):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        """Load governance data from file."""

        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {
                "policies": [],
                "controls": [],
                "risks": [],
                "incidents": [],
                "metrics": [],
                "audits": []
            }

    def save_data(self):
        """Save governance data to file."""

        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=2)

    def add_policy(
        self,
        name,
        description,
        owner,
        approval_date,
        review_date
    ):
        policy = {
            "id": f"POL-{len(self.data['policies']) + 1:03d}",
            "name": name,
            "description": description,
            "owner": owner,
            "approval_date": approval_date,
            "review_date": review_date,
            "status": "Active"
        }

        self.data["policies"].append(policy)
        self.save_data()

        return policy["id"]

    def add_control(
        self,
        name,
        description,
        policy_id,
        owner,
        implementation_date
    ):
        control = {
            "id": f"CTL-{len(self.data['controls']) + 1:03d}",
            "name": name,
            "description": description,
            "policy_id": policy_id,
            "owner": owner,
            "implementation_date": implementation_date,
            "status": "Planned"
        }

        self.data["controls"].append(control)
        self.save_data()

        return control["id"]

    def add_risk(
        self,
        name,
        description,
        likelihood,
        impact,
        owner,
        mitigation_plan
    ):
        risk = {
            "id": f"RSK-{len(self.data['risks']) + 1:03d}",
            "name": name,
            "description": description,
            "likelihood": likelihood,
            "impact": impact,
            "owner": owner,
            "mitigation_plan": mitigation_plan,
            "status": "Open"
        }

        self.data["risks"].append(risk)
        self.save_data()

        return risk["id"]

    def add_incident(
        self,
        name,
        description,
        date,
        severity,
        affected_systems,
        root_cause,
        resolution
    ):
        incident = {
            "id": f"INC-{len(self.data['incidents']) + 1:03d}",
            "name": name,
            "description": description,
            "date": date,
            "severity": severity,
            "affected_systems": affected_systems,
            "root_cause": root_cause,
            "resolution": resolution,
            "status": "Closed"
        }

        self.data["incidents"].append(incident)
        self.save_data()

        return incident["id"]

    def add_metric(
        self,
        name,
        description,
        target,
        actual,
        period,
        trend
    ):
        metric = {
            "id": f"MET-{len(self.data['metrics']) + 1:03d}",
            "name": name,
            "description": description,
            "target": target,
            "actual": actual,
            "period": period,
            "trend": trend
        }

        self.data["metrics"].append(metric)
        self.save_data()

        return metric["id"]

    def add_audit(
        self,
        name,
        description,
        date,
        auditor,
        findings,
        recommendations
    ):
        audit = {
            "id": f"AUD-{len(self.data['audits']) + 1:03d}",
            "name": name,
            "description": description,
            "date": date,
            "auditor": auditor,
            "findings": findings,
            "recommendations": recommendations
        }

        self.data["audits"].append(audit)
        self.save_data()

        return audit["id"]

    def list_policies(self):
        return self.data["policies"]

    def list_controls(self):
        return self.data["controls"]

    def list_risks(self):
        return self.data["risks"]

    def list_incidents(self):
        return self.data["incidents"]

    def list_metrics(self):
        return self.data["metrics"]

    def list_audits(self):
        return self.data["audits"]

    def generate_dashboard(self):
        return {
            "policies": len(self.data["policies"]),
            "controls": len(self.data["controls"]),
            "risks": len(self.data["risks"]),
            "incidents": len(self.data["incidents"]),
            "metrics": len(self.data["metrics"]),
            "audits": len(self.data["audits"])
        }


def main():

    parser = argparse.ArgumentParser(
        description="GRC102 Security Governance Tracker"
    )

    parser.add_argument(
        "--list-policies",
        action="store_true"
    )

    parser.add_argument(
        "--list-controls",
        action="store_true"
    )

    parser.add_argument(
        "--list-risks",
        action="store_true"
    )

    parser.add_argument(
        "--list-incidents",
        action="store_true"
    )

    parser.add_argument(
        "--list-metrics",
        action="store_true"
    )

    parser.add_argument(
        "--list-audits",
        action="store_true"
    )

    parser.add_argument(
        "--dashboard",
        action="store_true"
    )

    args = parser.parse_args()

    tracker = GovernanceTracker()

    if args.list_policies:
        print(json.dumps(tracker.list_policies(), indent=2))

    elif args.list_controls:
        print(json.dumps(tracker.list_controls(), indent=2))

    elif args.list_risks:
        print(json.dumps(tracker.list_risks(), indent=2))

    elif args.list_incidents:
        print(json.dumps(tracker.list_incidents(), indent=2))

    elif args.list_metrics:
        print(json.dumps(tracker.list_metrics(), indent=2))

    elif args.list_audits:
        print(json.dumps(tracker.list_audits(), indent=2))

    elif args.dashboard:
        print(json.dumps(
            tracker.generate_dashboard(),
            indent=2
        ))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
