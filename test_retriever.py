from rag.retriever import (
    Retriever,
    rerank_results,
)

retriever = Retriever()

results = retriever.retrieve(
    "What is the annual leave policy?"
)

ranked = rerank_results(results)

print(f"Retrieved: {len(ranked)} chunks")

for i, item in enumerate(ranked, start=1):
    print("\n" + "=" * 50)
    print(f"Rank {i}")
    print("Distance:", item[2])

    if "source" in item[1]:
        print("Source:", item[1]["source"])

    print(item[0][:200])
