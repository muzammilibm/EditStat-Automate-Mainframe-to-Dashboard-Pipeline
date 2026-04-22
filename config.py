from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Data Paths ---
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MASTER_DATA_DIR = DATA_DIR / "master"

# --- Output Paths ---
OUTPUT_DIR = BASE_DIR / "outputs"
REPORTS_DIR = OUTPUT_DIR / "reports"

# --- File Names ---
MASTER_CSV_PATH = MASTER_DATA_DIR / "master_dataset.csv"
EDITSTAT_REPORT_PATH = REPORTS_DIR / "EditStat_Report.xlsx"
QUEUESTAT_REPORT_PATH = REPORTS_DIR / "QueueStat_Report.xlsx"