# 🧪 SF_19_CHATBOT_WITH_RAG_TOOLS_UI: Chatbot With Rag Tools Ui

## Summary
Implements the Chatbot With Rag Tools Ui sub-workflow for document-grounded RAG responses.


## 📌 Overview
Short example module for Chatbot With Rag Tools Ui.

## 📂 File-by-File Explanation
- `__init__.py`: Marks this directory as a Python package for imports.
- `add_thread_id.py`: Adds/manages thread identifiers for conversation continuity.
- `ch5.pdf`: Reference/source document used for RAG demos.
- `chat_node.py`: Implements chat handling logic for message flow.
- `chatbot_checkpoint.db`: Local checkpoint/database artifact generated during runs.
- `database_connection.py`: Creates and manages database connections used by the workflow.
- `document_loader.py`: Loads source documents into the RAG pipeline.
- `document_splitter.py`: Splits documents into chunks for embedding/retrieval.
- `generate_embeddings.py`: Generates embeddings for document chunks.
- `get_retriever.py`: Constructs or fetches a configured retriever instance.
- `get_retriever_thread_id.py`: Returns a thread-aware retriever for the active thread context.
- `ingest_pdf.py`: Ingests PDF files into the retrieval/indexing workflow.
- `intro-to-ml.pdf`: Reference/source document used for RAG demos.
- `load_conversation.py`: Loads saved conversation history for resume behavior.
- `main.ipynb`: Notebook walkthrough for interactive experimentation.
- `main.py`: Primary entry script to run this workflow example.
- `model.py`: Configures and initializes the model used in this workflow.
- `reset_chat.py`: Resets chat state to start a fresh conversation.
- `retriever.py`: Retrieves relevant chunks for a user query.
- `retriever_state.py`: Defines the workflow state structure passed between nodes.
- `state_schema.py`: Defines the workflow state structure passed between nodes.
- `thread_document_metadata.py`: Tracks and returns document metadata for each thread.
- `thread_has_documents.py`: Checks whether a thread has ingested documents for retrieval.
- `thread_id.py`: Stores/helpers for current thread identifier handling.
- `tools.py`: Defines tools/functions the agent can call during execution.
- `workflow.py`: Builds and wires the LangGraph workflow execution path.
