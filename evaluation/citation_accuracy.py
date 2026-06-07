"""
Citation Accuracy Evaluation
"""

import pandas as pd

df = pd.read_csv(
    "evaluation/evaluation_output.csv"
)

correct = 0

for _, row in df.iterrows():

    expected = str(
        row["expected_policy"]
    )

    sources = str(
        row["sources"]
    )

    if expected in sources:
        correct += 1

total = len(df)

accuracy = (
    correct / total
) * 100

print(
    f"Correct Citations: "
    f"{correct}/{total}"
)

print(
    f"Citation Accuracy: "
    f"{accuracy:.2f}%"
)
