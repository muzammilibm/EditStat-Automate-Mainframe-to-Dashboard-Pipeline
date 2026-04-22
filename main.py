"""
main.py
-------
Pipeline orchestrator. Runs all 4 stages in order:
  1. Ingest  — load raw TXT files
  2. Process — clean and type-cast
  3. Append  — write to master CSV (with dedup)
  4. Export  — generate Excel report

Run: python main.py
"""

import logging
import sys
import os

# Make sure scripts/ is importable
sys.path.insert(0, os.path.dirname(__file__))

from scripts import ingest, process, append, export_excel

# --- Logging setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout
)
logger = logging.getLogger(__name__)


def run_pipeline():
    logger.info("=" * 50)
    logger.info("EditStat Pipeline — Starting")
    logger.info("=" * 50)

    # Stage 1: Ingest
    logger.info("[Stage 1/4] Ingestion")
    editstat_raw, queuestat_raw = ingest.run()

    # Stage 2: Process
    logger.info("[Stage 2/4] Processing")
    editstat_clean, queuestat_clean = process.run(editstat_raw, queuestat_raw)

    # Stage 3: Append
    logger.info("[Stage 3/4] Appending to master")
    append.run(editstat_clean, queuestat_clean)

    # Stage 4: Export
    logger.info("[Stage 4/4] Exporting Excel report")
    report_path = export_excel.run()

    logger.info("=" * 50)
    logger.info(f"Pipeline complete. Report: {report_path}")
    logger.info("=" * 50)


if __name__ == "__main__":
    run_pipeline()