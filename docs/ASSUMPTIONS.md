# Assumptions

* Input files are generated daily
* File format remains consistent
* Required columns are always present
* Data size grows incrementally
* Excel is required only for final output

---

## Risks

* Format changes in mainframe output
* Missing or corrupt data
* Large file size growth

---

## Mitigation

* Add validation layer
* Log errors
* Handle missing values gracefully
