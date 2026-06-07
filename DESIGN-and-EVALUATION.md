## System Architecture

The application uses a Retrieval-Augmented Generation (RAG) architecture
to answer questions about company policies and procedures.

The workflow consists of:

1. Policy documents are ingested and cleaned.
2. Documents are chunked into retrieval-friendly sections.
3. Chunks are embedded using a local embedding model.
4. Embeddings are stored in ChromaDB.
5. User questions are embedded and matched against the vector database.
6. Top-k relevant chunks are retrieved.
7. Retrieved context is injected into a prompt.
8. A local LLM (Qwen3 via Ollama) generates the final answer.
9. Source citations are returned alongside the answer.


## Embedding Model

The project uses a local sentence-transformer embedding model
to convert policy text into dense vector representations.

Reasons for this choice:

- Completely free to use
- Runs locally without API costs
- Produces high-quality semantic embeddings
- Suitable for enterprise policy retrieval tasks
- Supports offline operation

Using local embeddings also improves privacy because company
documents never leave the local environment.


## Chunking Strategy

Documents were chunked using a heading-aware strategy.

Instead of splitting documents into arbitrary fixed-size blocks,
sections were divided according to policy headings and subsections.

Benefits:

- Preserves policy context
- Keeps related information together
- Improves retrieval relevance
- Produces more interpretable citations

A moderate overlap was maintained between chunks to reduce
context fragmentation.

## Vector Database

ChromaDB was selected as the vector database.

Reasons:

- Open-source
- Free
- Simple local deployment
- LangChain compatibility
- Persistent storage support
- Suitable for small and medium-sized document collections

The vector index is stored locally and reused across sessions,
eliminating the need to re-embed documents for every run.

## Retrieval Strategy

The system retrieves the top 5 most relevant chunks
for each user query.

A value of K=5 was selected because it provided a
balance between:

- Retrieval completeness
- Response groundedness
- Prompt size efficiency

Smaller K values occasionally omitted relevant context,
while larger values increased prompt length without
meaningful improvements in answer quality.

## Prompt Design

The prompt is structured to include:

- System instructions
- Retrieved policy context
- User question
- Citation requirements

The model is instructed to:

1. Answer only from retrieved context.
2. Refuse questions outside the policy corpus.
3. Provide source citations.
4. Avoid hallucinating information.

This approach improves groundedness and citation accuracy.

## Guardrails

Basic guardrails were implemented to improve reliability.

The application:

- Refuses questions outside the company policy corpus.
- Limits answer length.
- Requires source citations.
- Uses retrieved evidence as the primary knowledge source.

These controls reduce hallucinations and improve answer trustworthiness.

## Language Model

The system uses Qwen3 running locally through Ollama.

Reasons:

- No API costs
- Fully local execution
- Good instruction-following capability
- Strong performance on retrieval-augmented tasks
- Privacy-preserving architecture

Using a local model ensured the project remained completely free
while maintaining acceptable answer quality.


## Evaluation Summary

A 25-question evaluation dataset was created covering Human Resources, Compensation and Benefits, Operations, Information Technology, Information Security, AI Governance, Data Privacy, Finance, and Remote Work policies.
These were automated using scripts under /evaluation folder.

ANSWER QUALITY:

1. Groundedness 64%
    - Grounded Answers ~ 16
    - Questionable / Potentially Unsupported ~ 9
Groundedness computation was based on the output of evaluation_output.csv and manually estimated % of answers whose answers is factually consistent with and fully supported by the retrieved evidence.


2. Citation Accuracy 44%
Citation accuracy was measured by comparing the expected source document for each question against the documents returned by the retrieval pipeline. The system achieved a citation accuracy of 44% (11 out of 25 questions). Analysis of incorrect citations showed that the retriever frequently returned adjacent policy documents with semantically related content, such as Information Technology policies instead of AI Governance policies, or Company Overview documents instead of Human Resources policies.

* Retrieval quality is the primary bottleneck.
* AI Governance, Security, Privacy, Finance, and Remote Work questions frequently retrieve adjacent policies rather than the intended policy document.
* The model generally avoids hallucinating when evidence is weak and often falls back to policy-aware refusals.
* Improving metadata filtering, chunking strategy, and retrieval ranking would likely increase both Groundedness and Citation Accuracy.


3. Exact / Partial Match (optional) - n/a



SYSTEM METRICS:

1. Latency:
    - P50: 20.55 seconds
    - P95: 21.81 seconds
Latency testing was performed using five representative policy questions. The system achieved a median (P50) response time of 20.55 seconds and a P95 latency of 21.81 seconds. The higher latency is attributable to local inference using Ollama and Qwen3, combined with retrieval, reranking, and prompt construction overhead.

2. Ablations: n/a (optional)



The evaluation demonstrates that the system successfully retrieves and answers policy-related questions, while also identifying opportunities for future improvement in retrieval precision, metadata filtering, and document ranking.




## Architecture Diagram

                ┌────────────────────┐
                │ Policy Documents   │
                │ 15 Markdown Files  │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Chunking Pipeline   │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Embedding Model     │
                │ all-MiniLM-L6-v2    │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ ChromaDB            │
                │ Vector Store        │
                └──────────┬─────────┘
                           │
User Question ─────────────┤
                           ▼
                ┌────────────────────┐
                │ Top-K Retrieval     │
                │ K = 5               │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Prompt Builder      │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Qwen3 via Ollama    │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Answer + Citations │
                └────────────────────┘


