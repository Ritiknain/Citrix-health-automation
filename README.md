# Citrix Health Automation

A Python automation tool that simplifies routine Citrix health monitoring by automating VDA connectivity checks and log file analysis.

## Features

- Ping multiple VDAs to verify connectivity
- Scan log files for `ERROR` entries
- Count errors in each log file
- Identify the log file with the highest number of errors
- Generate a concise health report

---

## Project Structure

```text
Citrix-health-automation/
│
├── health_monitor.py
├── README.md
└── logs/
    ├── broker.log
    ├── citrix.log
    └── vda.log
```

---

## Sample Output

```text
========================================
      CITRIX HEALTH CHECK
========================================

Ping Status of VDAs:

google.com      - Online
VDA01           - Unreachable
VDA02           - Unreachable
VDA03           - Unreachable

=== Log Error Report ===

broker.log      - 2 ERRORS
citrix.log      - 3 ERRORS
vda.log         - 1 ERROR

Worst file: citrix.log with 3 errors
```

---

## Technologies Used

- Python 3
- os
- subprocess
- requests

---

## How It Works

1. Reads the list of VDAs defined in the script.
2. Pings each VDA to verify connectivity.
3. Scans all `.log` files in the `logs` folder.
4. Counts the number of `ERROR` entries in each log file.
5. Identifies the log file with the highest number of errors.
6. Displays a summarized health report.

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/Ritiknain/Citrix-health-automation.git
```

### Navigate to the project

```bash
cd Citrix-health-automation
```

### Run the script

```bash
python health_monitor.py
```

---

## Note

- This project uses **sample VDA names** and **sample log files** for demonstration purposes.
- The script is designed for **Windows** and uses the Windows `ping` command (`ping -n 1`).
- It can be extended to integrate with real Citrix environments using PowerShell or the Citrix SDK.

---

## Roadmap

- [ ] SQLite — store health check history and track trends
- [ ] Slack alerts — notify when VDAs go unreachable
- [ ] Windows Task Scheduler — run automatically every 15 minutes
- [ ] Claude AI — diagnose errors and suggest fixes

---

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## Author

**Ritik Nain**

- GitHub: https://github.com/Ritiknain
- LinkedIn: https://www.linkedin.com/in/ritik-nain/