from config import DATA_DIR

from rag.loader import load_all_markdown
from rag.chunker import chunk_documents
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


def main():
    """
    Build the ChromaDB index from policy documents.
    """

    print("Loading documents...")
    docs = load_all_markdown(DATA_DIR)

    print(f"Loaded {len(docs)} documents.")

    print("Chunking documents...")
    chunks = chunk_documents(docs)

    print(f"Created {len(chunks)} chunks.")

    print("Initializing vector store...")
    store = VectorStore()

    existing_count = store.count()

    print(f"Existing vectors in collection: {existing_count}")

    if existing_count > 0:
        print(
            "Collection already contains data. "
            "Delete the existing collection first if you want to rebuild."
        )
        return

    print("Generating embeddings...")
    embedder = EmbeddingModel()

    texts = [
        chunk["content"]
        for chunk in chunks
    ]

    embeddings = embedder.encode(texts)

    print("Saving vectors to ChromaDB...")

    store.add_documents(
        chunks,
        embeddings,
    )

    print()
    print("Index build complete.")
    print(f"Indexed {len(chunks)} chunks.")
    print(f"Collection count: {store.count()}")


if __name__ == "__main__":
    main()