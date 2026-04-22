# Data Flow Documentation

## 📥 Input

Mainframe Output:

* EditStat raw data
* QueueStat raw data

---

## 🔄 Transformation Steps

1. Select required columns
2. Clean missing values
3. Apply business rules
4. Calculate metrics
5. Standardize format

---

## 📊 Output

### EditStat

* Pending claims
* Daily updates

### QueueStat

* Queue distribution
* Status tracking

---

## 📦 Storage

* master.csv → full history
* daily.csv → current day snapshot

---

## 🧠 Key Logic

* Daily append only (no overwrite)
* Avoid duplicates
* Maintain consistency across days
