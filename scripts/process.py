"""
process.py
----------
Responsibility: Clean and validate raw DataFrames from ingest stage.

Operations:
- Strip whitespace from string columns
- Cast columns to correct types (dates, ints, floats)
- Flag or drop rows with nulls / invalid values
- Add a LOAD_TIMESTAMP column for traceability

Returns: Two cleaned DataFrames ready for append stage.
"""

import pandas as pd
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def process_editstat(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and type-cast the EditStat DataFrame."""
    df = df.copy()

    # Strip whitespace from all string/object columns dynamically
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].str.strip()

    # Cast types
    df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
    df["RECORDS_PROCESSED"] = pd.to_numeric(df["RECORDS_PROCESSED"], errors="coerce")
    df["ERROR_COUNT"] = pd.to_numeric(df["ERROR_COUNT"], errors="coerce")
    df["RUNTIME_SECS"] = pd.to_numeric(df["RUNTIME_SECS"], errors="coerce")

    # Log rows that failed type casting (will have NaT or NaN after coerce)
    bad_rows = df[df["DATE"].isna() | df["RECORDS_PROCESSED"].isna()]
    if not bad_rows.empty:
        logger.warning(f"[EditStat] {len(bad_rows)} rows with unparseable values — dropping.")
        df = df.dropna(subset=["DATE", "RECORDS_PROCESSED"])

    # Add traceability column
    df["LOAD_TIMESTAMP"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    logger.info(f"[EditStat] Processed {len(df)} clean rows.")
    return df


def process_queuestat(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and type-cast the QueueStat DataFrame."""
    df = df.copy()

    # Strip whitespace from all string/object columns dynamically
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].str.strip()

    # Cast types
    df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
    df["ITEMS_IN"] = pd.to_numeric(df["ITEMS_IN"], errors="coerce")
    df["ITEMS_OUT"] = pd.to_numeric(df["ITEMS_OUT"], errors="coerce")
    df["PENDING"] = pd.to_numeric(df["PENDING"], errors="coerce")
    df["AVG_HANDLE_TIME"] = pd.to_numeric(df["AVG_HANDLE_TIME"], errors="coerce")

    # Drop rows where critical fields failed to parse
    bad_rows = df[df["DATE"].isna() | df["AGENT_ID"].isna()]
    if not bad_rows.empty:
        logger.warning(f"[QueueStat] {len(bad_rows)} rows with unparseable values — dropping.")
        df = df.dropna(subset=["DATE", "AGENT_ID"])

    # Add traceability column
    df["LOAD_TIMESTAMP"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    logger.info(f"[QueueStat] Processed {len(df)} clean rows.")
    return df


def run(editstat_df: pd.DataFrame, queuestat_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Entry point for process stage.
    Accepts raw DataFrames, returns cleaned DataFrames.
    """
    logger.info("Starting processing...")
    clean_editstat = process_editstat(editstat_df)
    clean_queuestat = process_queuestat(queuestat_df)
    logger.info("Processing complete.")
    return clean_editstat, clean_queuestat


if __name__ == "__main__":
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
    from scripts.ingest import run as ingest_run

    es_raw, qs_raw = ingest_run()
    es_clean, qs_clean = run(es_raw, qs_raw)

    print("\n--- EditStat Clean ---")
    print(es_clean.dtypes)
    print(es_clean.head())

    print("\n--- QueueStat Clean ---")
    print(qs_clean.dtypes)
    print(qs_clean.head())