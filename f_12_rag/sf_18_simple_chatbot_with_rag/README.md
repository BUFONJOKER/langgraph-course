# 🧪 SF_18_SIMPLE_CHATBOT_WITH_RAG: Simple Chatbot With Rag

## Summary
Implements the Simple Chatbot With Rag sub-workflow for document-grounded RAG responses.


## 📌 Overview
Short example module for Simple Chatbot With Rag.

## 📂 File-by-File Explanation
- `__init__.py`: Marks this directory as a Python package for imports.
- `ch5.pdf`: Reference/source document used for RAG demos.
- `chat_node.py`: Implements chat handling logic for message flow.
- `document_loader.py`: Loads source documents into the RAG pipeline.
- `document_splitter.py`: Splits documents into chunks for embedding/retrieval.
- `generate_embeddings.py`: Generates embeddings for document chunks.
- `intro-to-ml.pdf`: Reference/source document used for RAG demos.
- `main.ipynb`: Notebook walkthrough for interactive experimentation.
- `main.py`: Primary entry script to run this workflow example.
- `model.py`: Configures and initializes the model used in this workflow.
- `retriever.py`: Retrieves relevant chunks for a user query.
- `state_schema.py`: Defines the workflow state structure passed between nodes.
- `tools.py`: Defines tools/functions the agent can call during execution.
