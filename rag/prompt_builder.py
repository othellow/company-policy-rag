"""
Prompt construction.
"""

from config import (
    MAX_RESPONSE_WORDS,
    MAX_CONTEXT_CHUNKS,
)


def build_prompt(
    question,
    retrieved_chunks,
):
    """
    Build the final prompt sent to the LLM.
    """

    context = ""

    for i, item in enumerate(
        retrieved_chunks[:MAX_CONTEXT_CHUNKS],
        start=1,
    ):
        document = item[1]["document"]
        section = item[1]["section"]
        text = item[0]

        context += (
            f"\n[Source {i}]\n"
            f"Document: {document}\n"
            f"Section: {section}\n"
            f"{text}\n"
        )

    prompt = f"""
You are a Company Policy Assistant.

Use ONLY the information contained
in the provided context.

Do not use outside knowledge.

If the answer cannot be found in
the context, respond exactly:

"I can only answer questions about
the company policies contained in
the knowledge base."

Maximum response length:
{MAX_RESPONSE_WORDS} words.

Always cite the sources used.

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt
