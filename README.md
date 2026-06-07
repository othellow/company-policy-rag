    Company Policy RAG Assistant
    Overview
    This project implements a Retrieval-Augmented Generation (RAG) application that answers employee questions using company policy and procedure documents.
    The system uses:
        ○ Markdown company policies
        ○ Sentence Transformers embeddings
        ○ ChromaDB vector database
        ○ Ollama local LLM
        ○ Flask web application
    
    Features
        ○ Retrieval-Augmented Generation
        ○ Source citations
        ○ Company policy search
        ○ Local LLM inference
        ○ Automated testing
        ○ CI/CD pipeline
    
    Project Structure
    company-policy-rag/
    data/policies/ - policy corpus
    rag/ - retrieval pipeline
    tests/ - automated tests
    app.py - Flask application
    
    Setup
    Create Virtual Environment
    python -m venv .venv
    
    Activate Environment
    Windows:
    .venv\Scripts\activate
    Mac/Linux:
    source .venv/bin/activate
    
    Install Dependencies
    pip install -r requirements.txt
    Install Ollama
    Install Ollama and pull the model:
    ollama pull qwen3:8b
    
    Run Application
    python app.py
    Open:
    http://localhost:5000
    
    Run Tests
    pytest
    
    Evaluation
    The application will be evaluated using:
        ○ Retrieval Accuracy
        ○ Answer Accuracy
        ○ Hallucination Rate
        ○ Response Time
    
    Author
    Billy Mac Deus
    An AI Engineering Project
