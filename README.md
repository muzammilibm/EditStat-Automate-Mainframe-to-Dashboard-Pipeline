# 🚀 EdiStat-Automate: Mainframe-to-Dashboard Pipeline

### The Problem

The current process requires manual handling of Mainframe JCL outfiles, 45-minute Excel calculations, and extreme memory overhead ($70\%+$ RAM), leading to frequent system crashes and data loss.

### The Solution

A lightweight Micro SaaS that intercepts JCL reports, cleans data using Python, and runs multi-threaded calculations in the background, freeing up local resources and ensuring data persistence.

---

### 🛠 Tech Stack (2026 Modern Blend)

* **Frontend:** React.js (Vite) + Tailwind CSS (for the 12:00–21:00 monitoring dashboard).
* **Backend:** Node.js (Express) for API orchestration.
* **Processing Engine:** Python (Pandas + NumPy) for heavy-duty data cleaning and math.
* **Database:** MongoDB (to save state and prevent "accidental touch" crashes).
* **Automation:** Python `imaplib` (to listen for Outlook reports).

---

### 🏗 Architecture

---

### 📋 Phase-wise Implementation (Brick-by-Brick)

#### Phase 1: The "Sanitizer" (Python Script)

* Connect to Outlook via IMAP.
* Parse Fixed-Width Files (FWF) from JCL output.
* **Goal:** Convert `.txt` report to a cleaned `JSON/CSV` in $<5$ seconds.

#### Phase 2: The "Logic Engine" (Pandas/NumPy)

* Translate the "EdiStat" Excel formulas into Python functions.
* Use NumPy for vectorized calculations (replacing the 45-min Excel thread with a 30-second matrix operation).
* **Goal:** Achieve $100\%$ numerical parity with the original Excel sheet.

#### Phase 3: The "Persistence Layer" (MERN)

* Store every processed report in MongoDB.
* Build a React UI to view historical "EdiStat" trends.
* **Goal:** Eliminate "crash-and-restart" risks.

---

### 🚀 Getting Started (Under 30 Mins)

1. **Clone the Repo:**
```bash
git clone https://github.com/muzammil-13/edistat-automate.git

```


2. **Install Dependencies:**
* Python: `pip install pandas numpy`
* Node: `npm install express mongoose`


3. **Run the Parser:**
```bash
python src/parser.py --file report_from_mainframe.txt

```



---

### 📈 Future Vision (Micro SaaS Roadmap)

* **Multi-tenancy:** Allow other teams within IBM to create their own "Logic Blocks."
* **Export to PDF:** Automated weekly reports sent back to managers.
* **Alerting:** Slack/Teams notification if the calculation deviates from thresholds.

---

### 💡 Grit Mindset Note

*Don't build the dashboard first. Build the Python script that cleans the data today. That’s your first brick.*

---
