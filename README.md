# EditStat Automate: Mainframe to Dashboard Pipeline

## 🚀 Overview

EditStat Automate is a lightweight data pipeline that transforms raw mainframe outputs into structured datasets and dashboard-ready insights.

This project replaces manual Excel-heavy workflows with a scalable, memory-efficient pipeline using Python.

---

## 🎯 Problem

Current workflow:

* Mainframe outputs → Excel processing → manual cleanup → reporting
* High memory usage (VDI constraints)
* Repetitive manual effort
* No structured historical tracking

---

## 💡 Solution

A 3-layer pipeline:

1. **Data Ingestion**
   * Read raw mainframe output (CSV/TXT)
2. **Processing**
   * Clean, validate, transform data using Python
   * Append daily records incrementally
3. **Output**
   * Generate Excel reports (only as final output)
   * Optional dashboard (Streamlit)

---

## 🏗️ Architecture

Mainframe Output
↓
Raw Files (CSV/TXT)
↓
Python Processing Layer
↓
Master Dataset (CSV / SQLite)
↓
Excel Output / Dashboard

---

## 📁 Project Structure

```
EdiStat-Automate/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── master/
│
├── scripts/
│   ├── ingest.py
│   ├── process.py
│   ├── append.py
│   └── export_excel.py
│
├── outputs/
│   └── reports/
│
├── docs/
│   ├── checklist.md
│   ├── ai_instructions.md
│
├── main.py
└── README.md
```

---

## ⚙️ Key Features

* No dependency on Excel for processing
* Incremental data appending (daily basis)
* Memory-efficient (chunk processing)
* Modular pipeline design
* Dashboard-ready output

---

## 🧠 Core Concepts

* Excel = Output layer only
* CSV/DB = Source of truth
* Python = Processing engine

---

## 🚧 MVP Scope (7 Days)

* [ ] Read raw mainframe file
* [ ] Clean and validate data
* [ ] Append to master dataset
* [ ] Generate Excel report (EditStat + QueueStat)
* [ ] Basic logging
* [ ] Optional: simple dashboard

---

## 🧪 How to Run

```bash
python main.py
```

---

## 🔥 Future Enhancements

* Streamlit dashboard
* SQLite integration
* Automated scheduling
* Data validation rules engine
* Email automation

---

## 📌 Goal

Transform manual reporting into a reproducible, scalable data pipeline aligned with real-world enterprise workflows.
