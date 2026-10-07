#!/bin/bash

LOG_FILE="/monitoring/security_monitor.log"
TIMESTAMP=$(date -Iseconds)

echo "========================================" >> "$LOG_FILE"
echo "Security Monitoring Check: $TIMESTAMP" >> "$LOG_FILE"

# Check web application availability
if timeout 5 bash -c '</dev/tcp/web_server/8080' 2>/dev/null; then
    echo "[OK] Web application is reachable on TCP/8080" >> "$LOG_FILE"
else
    echo "[ALERT] Web application is not reachable on TCP/8080" >> "$LOG_FILE"
fi

# Verify database isolation
if timeout 3 bash -c '</dev/tcp/database_server/3306' 2>/dev/null; then
    echo "[ALERT] Database TCP/3306 is reachable from monitoring container" >> "$LOG_FILE"
else
    echo "[OK] Database TCP/3306 is not reachable from monitoring container" >> "$LOG_FILE"
fi

echo "Monitoring check completed." >> "$LOG_FILE"
