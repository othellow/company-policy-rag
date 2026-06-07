"""
Latency benchmark.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

import time
import statistics


from rag.rag_pipeline import (
    RAGPipeline
)

rag = RAGPipeline()

questions = [
    "What is annual leave?",
    "What is the password policy?",
    "Can employees work remotely?",
    "How is overtime handled?",
    "What are AI usage guidelines?"
]

times = []

for question in questions:

    start = time.time()

    rag.ask(question)

    end = time.time()

    times.append(
        end - start
    )

times.sort()

p50 = statistics.median(
    times
)

p95 = times[
    int(len(times) * 0.95) - 1
]

print(
    f"P50: {p50:.2f}s"
)

print(
    f"P95: {p95:.2f}s"
)
