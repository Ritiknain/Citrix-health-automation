# Python Automation — Learning Journal

A hands-on Python automation project built while transitioning from Citrix L2 Admin to IT Automation / AI Engineer.

Each script is a real tool, not a tutorial exercise.

---

## Projects

### Citrix Health Check (`build_day2.py`)
Automated health monitor for Citrix environments.

**What it does:**
- Pings a list of VDA servers and reports Online / Unreachable status
- Scans a folder of log files and counts ERROR lines in each
- Identifies the worst offending log file
- Prints a unified health report

**What it replaces:**
- Manually opening CMD and pinging each VDA one by one
- Manually opening each log file and searching for errors

**Sample output:**
```
=== Citrix Health Check ===

Ping Status of VDAs:
VDA01           — Unreachable
VDA02           — Unreachable
google.com      — Online
VDA03           — Unreachable

=== Log Error Report ===
broker.log      — 2 ERRORS
citrix.log      — 3 ERRORS
vda.log         — 1 ERROR

Worst file: citrix.log with 3 errors
```

---

## Tech Stack
- Python 3.12
- `os` — folder scanning and file path handling
- `subprocess` — running system ping commands
- `requests` — calling REST APIs

---

## How to Run

**1. Clone the repo**
```bash
git clone https://github.com/Ritiknain/python-automation
cd python-automation
```

**2. Install dependencies**
```bash
pip install requests
```

**3. Add your log files**

Create a `logs/` folder and add `.log` files with INFO/ERROR lines.

**4. Update the VDA list**

Open `build_day2.py` and edit this line with your actual VDA hostnames or IPs:
```python
vdas = ["VDA01", "VDA02", "VDA03"]
```

**5. Run**
```bash
python build_day2.py
```

---

## Roadmap
- [ ] SQLite — store every health check run, track trends over time
- [ ] CSV export — generate reports for stakeholders
- [ ] Slack alerts — send notifications when VDAs go down
- [ ] Windows Task Scheduler — run automatically every 15 minutes
- [ ] Claude AI — diagnose errors and suggest fixes automatically

---

## Author
**Ritik Nain** — Citrix L2 Admin transitioning to IT Automation / AI Engineer

[GitHub](https://github.com/Ritiknain) · [LinkedIn](https://linkedin.com/in/ritiknain)
