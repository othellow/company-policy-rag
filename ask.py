from rag.rag_pipeline import (
    RAGPipeline,
)


def main():
    rag = RAGPipeline()

    question = input(
        "Ask a question: "
    )

    response = rag.ask(
        question
    )

    print("\n" + "=" * 60)
    print("ANSWER")
    print("=" * 60)

    print(
        response["answer"]
    )

    print("\nSOURCES")

    if response["sources"]:
        for source in response["sources"]:
            print(
                f"- {source}"
            )
    else:
        print(
            "No sources available."
        )


if __name__ == "__main__":
    main()
