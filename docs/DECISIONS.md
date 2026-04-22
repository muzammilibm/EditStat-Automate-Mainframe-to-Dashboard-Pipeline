# Engineering Decisions Log

## Decision 1: Avoid Excel for Processing

**Why:**

* High memory usage
* Not scalable

**Alternative Chosen:**

* pandas + CSV pipeline

---

## Decision 2: Use CSV instead of Database (MVP)

**Why:**

* Simpler setup
* Faster iteration

**Future Plan:**

* Move to SQLite

---

## Decision 3: Incremental Append Model

**Why:**

* Avoid full reload of historical data
* Efficient for daily workflows

---

## Decision 4: Separate Layers (Ingest, Process, Output)

**Why:**

* Maintain modularity
* Easier debugging
* Scalable architecture
