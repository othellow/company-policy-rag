"""
Global project configuration.

All configurable values are centralized here
to make the project reproducible.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data", "policies")
CHROMA_DB_DIR = os.path.join(BASE_DIR, "chroma_db")

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
OLLAMA_MODEL = "qwen3:8b"

TOP_K_RESULTS = 5

MAX_CONTEXT_CHUNKS = 5

MAX_RESPONSE_WORDS = 250

MIN_RELEVANCE_SCORE = 1.5

RANDOM_SEED = 42

