# Architecture Overview

## 🎯 Goal

Design a lightweight pipeline to process mainframe outputs into structured datasets and reports.

---

## 🧱 System Layers

### 1. Ingestion Layer

* Input: Mainframe output (CSV/TXT)
* Tool: pandas
* Output: Clean raw snapshot

---

### 2. Processing Layer

* Data cleaning
* Transformation logic
* Validation rules

---

### 3. Storage Layer

* master.csv (historical data)
* summary.csv (aggregated metrics)

---

### 4. Output Layer

* Excel report (EditStat, QueueStat)
* Optional: Streamlit dashboard

---

## 🔄 Data Flow

Raw File → Ingest → Process → Append → Export

---

## ⚡ Design Decisions

* No Excel in processing layer
* Incremental updates (daily append)
* Memory-efficient (chunk processing)

---

## 🚨 Constraints

* Low memory VDI
* Large Excel files
* Manual workflow dependency

---

## 📌 Future Improvements

* SQLite DB
* Scheduling (cron)
* API layer
