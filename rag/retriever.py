"""
Semantic retrieval from ChromaDB.
"""

from rag.vector_store import VectorStore
from rag.embeddings import EmbeddingModel
from config import TOP_K_RESULTS


class Retriever:
    """
    Retrieves the most relevant chunks
    from the vector database.
    """

    def __init__(self):
        self.store = VectorStore()
        self.embedder = EmbeddingModel()

    def retrieve(self, question):
        """
        Convert the question into an embedding
        and retrieve the Top-K most relevant chunks.
        """

        query_embedding = (
            self.embedder.encode(
                [question]
            )[0]
        )

        results = (
            self.store.collection.query(
                query_embeddings=[
                    query_embedding.tolist()
                ],
                n_results=TOP_K_RESULTS,
                include=[
                    "documents",
                    "metadatas",
                    "distances",
                ],
            )
        )

        return results


def rerank_results(results):
    """
    Re-rank retrieved results by distance.

    Lower distance = more relevant.
    """

    docs = results["documents"][0]
    metas = results["metadatas"][0]
    distances = results["distances"][0]

    ranked = list(
        zip(
            docs,
            metas,
            distances,
        )
    )

    ranked.sort(
        key=lambda x: x[2]
    )

    return ranked
