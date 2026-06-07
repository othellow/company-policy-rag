from rag.retriever import (
    Retriever,
    rerank_results,
)

from rag.prompt_builder import (
    build_prompt,
)

retriever = Retriever()

results = retriever.retrieve(
    "What is the annual leave policy?"
)

ranked = rerank_results(results)

prompt = build_prompt(
    "What is the annual leave policy?",
    ranked,
)

print(prompt[:2000])

