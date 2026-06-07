"""
ChromaDB operations.
"""

import chromadb

from config import CHROMA_DB_DIR


class VectorStore:
    """
    Wrapper around ChromaDB.
    """

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=CHROMA_DB_DIR
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="company_policies"
            )
        )

    def count(self):

        return self.collection.count()

    def add_documents(
        self,
        chunks,
        embeddings,
    ):
        """
        Store chunks and embeddings.
        """

        ids = []
        documents = []
        metadatas = []

        for chunk in chunks:

            ids.append(
                chunk["chunk_id"]
            )

            documents.append(
                chunk["content"]
            )

            metadatas.append(
                {
                    "document": chunk["document"],
                    "section": chunk["section"],
                }
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas,
        )