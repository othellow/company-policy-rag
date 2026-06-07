"""
End-to-end RAG pipeline.
"""

from rag.retriever import (
    Retriever,
    rerank_results,
)

from rag.prompt_builder import (
    build_prompt,
)

from rag.generator import (
    Generator,
)

from rag.guardrails import (
    is_policy_question,
)


class RAGPipeline:
    """
    Complete Retrieval-Augmented
    Generation pipeline.
    """

    def __init__(self):
        self.retriever = Retriever()
        self.generator = Generator()

    def ask(self, question):
        """
        Process a user question
        through the complete RAG flow.
        """

        # Retrieve
        results = (
            self.retriever.retrieve(
                question
            )
        )

        # Guardrail #1
        if not is_policy_question(
            results
        ):
            return {
                "answer": (
                    "I can only answer "
                    "questions about "
                    "the company policies "
                    "contained in the "
                    "knowledge base."
                ),
                "sources": [],
            }

        # Re-rank
        ranked = (
            rerank_results(
                results
            )
        )

        # Build Prompt
        prompt = build_prompt(
            question,
            ranked,
        )

        # Generate
        answer = (
            self.generator.generate(
                prompt
            )
        )

        # Guardrail #3
        sources = sorted(
            {
                item[1]["document"]
                for item in ranked
            }
        )

        return {
            "answer": answer,
            "sources": sources,
        }
    
