"""
append.py
---------
Responsibility: Append cleaned DataFrames to master CSV files incrementally.

Dedup logic:
- EditStat: unique key = (DATE, JOB_ID)         — one job per day is unique
- QueueStat: unique key = (DATE, QUEUE_NAME, AGENT_ID) — one agent+queue per day

If master CSV doesn't exist yet, it creates it.
If it does exist, it appends only rows not already present (by dedup key).
"""

import pandas as pd
import os
import logging

MASTER_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "master")
EDITSTAT_MASTER = os.path.join(MASTER_DIR, "editstat_master.csv")
QUEUESTAT_MASTER = os.path.join(MASTER_DIR, "queuestat_master.csv")

EDITSTAT_DEDUP_KEY = ["DATE", "JOB_ID"]
QUEUESTAT_DEDUP_KEY = ["DATE", "QUEUE_NAME", "AGENT_ID"]

logger = logging.getLogger(__name__)


def append_to_master(new_df: pd.DataFrame, master_path: str, dedup_key: list, label: str) -> int:
    """
    Append new rows to master CSV, skipping duplicates by dedup_key.
    Returns count of rows actually appended.
    """
    if os.path.exists(master_path):
        master_df = pd.read_csv(master_path)

        # Normalize dedup key columns to string for safe comparison
        # (avoids datetime format mismatches between CSV read and new data)
        for col in dedup_key:
            master_df[col] = master_df[col].astype(str)
            new_df[col] = new_df[col].astype(str)

        # Find rows in new_df whose dedup key combo doesn't exist in master
        merged = new_df.merge(master_df[dedup_key], on=dedup_key, how="left", indicator=True)
        rows_to_add = new_df[merged["_merge"] == "left_only"]

        if rows_to_add.empty:
            logger.info(f"[{label}] No new rows to append — all duplicates.")
            return 0

        rows_to_add.to_csv(master_path, mode="a", header=False, index=False)
        logger.info(f"[{label}] Appended {len(rows_to_add)} new rows to master.")
        return len(rows_to_add)

    else:
        # First run — create the master file (ensure directory exists)
        os.makedirs(os.path.dirname(master_path), exist_ok=True)
        new_df.to_csv(master_path, index=False)
        logger.info(f"[{label}] Master file created with {len(new_df)} rows.")
        return len(new_df)


def run(editstat_df: pd.DataFrame, queuestat_df: pd.DataFrame) -> None:
    """
    Entry point for append stage.
    Accepts cleaned DataFrames, appends to master CSVs.
    """
    logger.info("Starting append...")
    append_to_master(editstat_df, EDITSTAT_MASTER, EDITSTAT_DEDUP_KEY, "EditStat")
    append_to_master(queuestat_df, QUEUESTAT_MASTER, QUEUESTAT_DEDUP_KEY, "QueueStat")
    logger.info("Append complete.")


if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
    from scripts.ingest import run as ingest_run
    from scripts.process import run as process_run

    es_raw, qs_raw = ingest_run()
    es_clean, qs_clean = process_run(es_raw, qs_raw)
    run(es_clean, qs_clean)