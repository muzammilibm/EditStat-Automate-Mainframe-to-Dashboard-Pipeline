"""
ingest.py
---------
Responsibility: Read raw mainframe TXT files into DataFrames.
Validates that files exist, load without errors, and have expected columns.

Returns: Two DataFrames (editstat_df, queuestat_df) for the next pipeline stage.
"""

import pandas as pd
import os
import logging

# --- Config ---
RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
EDITSTAT_FILE = os.path.join(RAW_DIR, "editstat_raw.txt")
QUEUESTAT_FILE = os.path.join(RAW_DIR, "queuestat_raw.txt")
SEPARATOR = "|"

EDITSTAT_EXPECTED_COLS = [
    "DATE", "JOB_ID", "JOB_NAME", "STATUS",
    "RECORDS_PROCESSED", "ERROR_COUNT", "RUNTIME_SECS"
]
QUEUESTAT_EXPECTED_COLS = [
    "DATE", "QUEUE_NAME", "AGENT_ID", "ITEMS_IN",
    "ITEMS_OUT", "PENDING", "AVG_HANDLE_TIME"
]

logger = logging.getLogger(__name__)


def load_file(filepath: str, expected_cols: list, label: str) -> pd.DataFrame:
    """
    Load a pipe-separated TXT file into a DataFrame.
    Raises clear errors if file is missing or columns don't match.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"[{label}] File not found: {filepath}")

    df = pd.read_csv(filepath, sep=SEPARATOR, engine="python")

    # Strip whitespace from column names (mainframe outputs often pad them)
    df.columns = df.columns.str.strip()

    # Validate expected columns are present
    missing_cols = set(expected_cols) - set(df.columns)
    if missing_cols:
        raise ValueError(f"[{label}] Missing columns: {missing_cols}")

    logger.info(f"[{label}] Loaded {len(df)} rows, {len(df.columns)} columns.")
    return df


def run() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Entry point for ingest stage.
    Returns (editstat_df, queuestat_df).
    """
    logger.info("Starting ingestion...")

    editstat_df = load_file(EDITSTAT_FILE, EDITSTAT_EXPECTED_COLS, "EditStat")
    queuestat_df = load_file(QUEUESTAT_FILE, QUEUESTAT_EXPECTED_COLS, "QueueStat")

    logger.info("Ingestion complete.")
    return editstat_df, queuestat_df


# Quick smoke test when run directly
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
    es, qs = run()
    print("\n--- EditStat Sample ---")
    print(es.head())
    print("\n--- QueueStat Sample ---")
    print(qs.head())