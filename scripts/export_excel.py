"""
export_excel.py
---------------
Responsibility: Read master CSVs and write a formatted Excel report.

Output: outputs/reports/editstat_report_YYYYMMDD.xlsx
- Sheet 1: EditStat data
- Sheet 2: QueueStat data
- Sheet 3: Summary (aggregated metrics)

Excel is ONLY the output layer — no processing logic lives here.
"""

import pandas as pd
import logging
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path to allow importing config.py
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import MASTER_DATA_DIR, REPORTS_DIR

EDITSTAT_MASTER = MASTER_DATA_DIR / "editstat_master.csv"
QUEUESTAT_MASTER = MASTER_DATA_DIR / "queuestat_master.csv"

logger = logging.getLogger(__name__)


def build_summary(editstat_df: pd.DataFrame, queuestat_df: pd.DataFrame) -> pd.DataFrame:
    """
    Build a simple summary sheet with key metrics.
    Extend this as reporting requirements grow.
    """
    editstat_summary = editstat_df.groupby("JOB_NAME").agg(
        TOTAL_RUNS=("JOB_ID", "count"),
        SUCCESS_RUNS=("STATUS", lambda x: (x == "SUCCESS").sum()),
        FAILED_RUNS=("STATUS", lambda x: (x == "FAILED").sum()),
        AVG_RECORDS=("RECORDS_PROCESSED", "mean"),
        TOTAL_ERRORS=("ERROR_COUNT", "sum"),
    ).reset_index()

    queuestat_summary = queuestat_df.groupby("QUEUE_NAME").agg(
        TOTAL_ITEMS_IN=("ITEMS_IN", "sum"),
        TOTAL_ITEMS_OUT=("ITEMS_OUT", "sum"),
        AVG_PENDING=("PENDING", "mean"),
        AVG_HANDLE_TIME=("AVG_HANDLE_TIME", "mean"),
    ).reset_index()

    # Return as a dict of named DataFrames for separate sections
    return editstat_summary, queuestat_summary


def run() -> str:
    """
    Entry point for export stage.
    Reads master CSVs, writes Excel report.
    Returns path to generated file.
    """
    logger.info("Starting Excel export...")

    # Guard: master files must exist before exporting
    if not EDITSTAT_MASTER.exists() or not QUEUESTAT_MASTER.exists():
        raise FileNotFoundError("Master CSV files not found. Run append stage first.")

    editstat_df = pd.read_csv(EDITSTAT_MASTER)
    queuestat_df = pd.read_csv(QUEUESTAT_MASTER)

    editstat_summary, queuestat_summary = build_summary(editstat_df, queuestat_df)

    # Output filename includes today's date for versioning
    today = datetime.now().strftime("%Y%m%d")
    output_path = REPORTS_DIR / f"editstat_report_{today}.xlsx"
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        editstat_df.to_excel(writer, sheet_name="EditStat", index=False)
        queuestat_df.to_excel(writer, sheet_name="QueueStat", index=False)
        editstat_summary.to_excel(writer, sheet_name="EditStat Summary", index=False)
        queuestat_summary.to_excel(writer, sheet_name="QueueStat Summary", index=False)

    logger.info(f"Report written to: {output_path}")
    return output_path


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
    path = run()
    print(f"\nReport saved: {path}")