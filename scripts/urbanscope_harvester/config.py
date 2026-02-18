from __future__ import annotations
import os, re

# NCBI / Eutils
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
NCBI_API_KEY = os.getenv("NCBI_API_KEY", "").strip()
TOOL_NAME = os.getenv("NCBI_TOOL", "urbanscope-srr-harvester")
NCBI_EMAIL = os.getenv("NCBI_EMAIL", "")

DEFAULT_QUERY = (
    '('
      # -----------------------------------
      # 1) MUST be cold / cryophilic context
      # -----------------------------------
      '('
        'cryophile OR cryophil* OR '
        'psychrophile OR psychrophil* OR '
        '"cold-adapted" OR "cold adapted" OR '
        '"cold-loving" OR '
        '"cold environment" OR '
        '"low temperature" OR '
        'permafrost OR '
        'glacier OR glacial OR '
        '"polar region" OR Arctic OR Antarctic OR '
        '"sea ice" OR '
        '"ice core" OR '
        '"cold seep" OR '
        'tundra OR '
        '"subzero" OR '
        '"freeze-thaw"'
      ') '
      'AND '

      # ------------------------------------------------
      # 2) ANY sequencing modality (expanded)
      # ------------------------------------------------
      '('
        # Shotgun / WGS
        '"whole genome shotgun" OR '
        '"shotgun metagenom*" OR '
        '"shotgun sequencing" OR '
        '"whole genome sequencing" OR '
        'metagenom* OR '
        'metatranscriptom* OR '
        'WGS OR '

        # Amplicon now INCLUDED
        '"16S" OR "16S rRNA" OR '
        '"ITS" OR '
        '"18S" OR '
        'amplicon OR '
        '"marker gene" OR '
        '"V3-V4" OR "V4 region" OR '
        'barcod*'
      ') '
      'AND '

      # ------------------------------------------------
      # 3) Microbial context
      # ------------------------------------------------
      '('
        'bacteria OR bacterial OR microb* OR '
        'prokaryot* OR microbiome OR microbiota OR '
        'fung*'
      ') '

      # -------------------------------
      # 4) HARD EXCLUSIONS (clean noise)
      # -------------------------------
      'NOT '
      '('
        '"single-cell" OR '
        'scRNA OR '
        '"whole exome" OR '
        'WES OR '
        'thermophil* OR '
        'hyperthermophil*'
      ')'
    ')'
)

# Paths
DATA_DIR = "data"
DOCS_DIR = "docs"
DB_DIR = f"{DOCS_DIR}/db"
CACHE_DIR = f"{DATA_DIR}/cache"
DEBUG_DIR = f"{DATA_DIR}/debug"
DOCS_DEBUG_DIR = f"{DOCS_DIR}/debug"

SEEN_SRA_UIDS = f"{DATA_DIR}/seen_sra_uids.txt"
SEEN_SRR_RUNS = f"{DATA_DIR}/seen_srr_runs.txt"

BIOSAMPLE_CACHE = f"{CACHE_DIR}/biosample.json"
BIOPROJECT_CACHE = f"{CACHE_DIR}/bioproject.json"
BIOPROJECT_UID_CACHE = f"{CACHE_DIR}/bioproject_uid.json"

DOCS_LATEST_SRR = f"{DOCS_DIR}/latest_srr.json"
DOCS_LATEST_DEBUG = f"{DOCS_DEBUG_DIR}/latest_report.json"

BIOPROJECT_RE = re.compile(r"\bPRJ(?:NA|EB|DB)\d+\b", re.I)

# 50MB limit
MAX_OUTPUT_BYTES = 50 * 1024 * 1024
