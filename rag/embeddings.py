"""
Embedding model wrapper.
"""

from sentence_transformers import (
    SentenceTransformer
)

from config import EMBEDDING_MODEL


class EmbeddingModel:
    """
    Wrapper around SentenceTransformer.
    """

    def __init__(self):

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    def encode(self, texts):
        """
        Generate embeddings for a list of texts.
        """

        return self.model.encode(
            texts,
            show_progress_bar=True,
        )
