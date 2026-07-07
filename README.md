# Python Automation for Citrix Health Checks

A Python automation tool that simplifies routine Citrix health monitoring by automating VDA connectivity checks and log file analysis.

## Features

- Ping multiple VDAs to verify connectivity
- Scan log files for `ERROR` entries
- Count errors in each log file
- Identify the log file with the highest number of errors
- Generate a concise health report

## Project Structure

```
Python_automation/
│
├── health_monitor.py
└── logs/
    ├── broker.log
    ├── citrix.log
    └── vda.log
```

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

Log Error Report

broker.log      - 2 ERRORS
citrix.log      - 3 ERRORS
vda.log         - 1 ERROR

Worst file: citrix.log with 3 errors
```

## Technologies Used

- Python 3
- os
- subprocess

## How It Works

1. Reads the list of VDAs defined in the script.
2. Pings each VDA to verify connectivity.
3. Scans all `.log` files in the `logs` folder.
4. Counts the number of `ERROR` entries in each log file.
5. Displays a summarized health report.

## Getting Started

### Clone the repository

```bash
git clone https://github.com/Ritiknain/Python-Automation-for-Citrix-Health-Checks.git
```

### Navigate to the project

```bash
cd Python-Automation-for-Citrix-Health-Checks
```

### Run the script

```bash
python health_monitor.py
```

## Note

This project uses sample VDA names and sample log files for demonstration purposes. It can be extended to work with real Citrix environments using PowerShell or the Citrix SDK.

## Author

**Ritik Nain**

- GitHub: https://github.com/Ritiknain
- LinkedIn: https://linkedin.com/in/ritik-nain