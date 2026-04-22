# MVP Execution Checklist (7 Days)

## 🎯 Goal

Ship a working pipeline that replaces Excel-heavy workflow.

---

## Day 1: Problem Lock + Data Understanding

* [ ] Identify exact input file format
* [ ] List required columns
* [ ] Identify transformations (Excel logic → Python)
* [ ] Define output structure

---

## Day 2: Ingestion Layer

* [ ] Read raw file using pandas
* [ ] Handle encoding issues
* [ ] Select required columns only
* [ ] Save cleaned raw snapshot

---

## Day 3: Processing Layer

* [ ] Apply transformations
* [ ] Handle missing values
* [ ] Create required metrics
* [ ] Validate outputs

---

## Day 4: Append System

* [ ] Create master.csv
* [ ] Append daily data
* [ ] Avoid duplicates
* [ ] Test incremental updates

---

## Day 5: Excel Output

* [ ] Generate EditStat sheet
* [ ] Generate QueueStat sheet
* [ ] Format basic output
* [ ] Ensure no manual Excel steps needed

---

## Day 6: Optimization

* [ ] Add chunk processing
* [ ] Reduce memory usage
* [ ] Add logging
* [ ] Test with larger data

---

## Day 7: Finalization

* [ ] Clean repo
* [ ] Update README
* [ ] Add sample data
* [ ] Record demo video (optional)

---

## 🚫 Rules

* No Excel in processing
* No overengineering
* Focus on working pipeline, not perfection
