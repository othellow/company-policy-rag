"""
Evaluation runner for Quantic RAG system.
"""


from pathlib import Path

# Adjust import if needed
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(PROJECT_ROOT))

import csv

from rag.rag_pipeline import RAGPipeline


def main():

    rag = RAGPipeline()

    questions_file = Path("evaluation/questions.csv")
    output_file = Path("evaluation/evaluation_output.csv")

    results = []

    with open(questions_file, "r", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            question = row["question"]
            gold_answer = row["gold_answer"]
            expected_policy = row["policy"]

            print(f"Evaluating: {question}")

            response = rag.ask(question)

            answer = response.get("answer", "")

            sources = response.get(
                "sources",
                []
            )

            source_text = "; ".join(
                str(s)
                for s in sources
            )

            results.append(
                {
                    "question": question,
                    "gold_answer": gold_answer,
                    "expected_policy": expected_policy,
                    "answer": answer,
                    "sources": source_text,
                }
            )

    with open(
        output_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=[
                "question",
                "gold_answer",
                "expected_policy",
                "answer",
                "sources",
            ],
        )

        writer.writeheader()
        writer.writerows(results)

    print()
    print(f"Saved results to: {output_file}")


if __name__ == "__main__":
    main()


