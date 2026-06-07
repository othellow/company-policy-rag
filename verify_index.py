
from rag.vector_store import VectorStore


def main():

    store = VectorStore()

    count = store.collection.count()

    print(
        f"Indexed Chunks: {count}"
    )


if __name__ == "__main__":
    main()