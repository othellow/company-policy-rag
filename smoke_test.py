"""
Smoke test for retrieval pipeline.
"""

from rag.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "What is annual leave?"
)

assert len(
    results["documents"][0]
) > 0

print(
    "Retrieval smoke test passed"
)

