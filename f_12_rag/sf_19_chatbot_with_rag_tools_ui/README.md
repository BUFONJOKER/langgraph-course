# 🖥️ SF 19: Chatbot With RAG, Tools, and UI

## 📌 Overview

This folder extends the RAG chatbot with tool integration, conversation/thread handling, and UI-oriented workflow utilities.

## 📂 Files

### 🧠 Workflow and Chat

- `main.py`: Main entry script.
- `workflow.py`: Graph/workflow composition.
- `chat_node.py`: Chat node implementation.
- `state_schema.py`: Shared state schema.

### 📄 Retrieval and Ingestion

- `document_loader.py`: Loads source documents.
- `document_splitter.py`: Splits text into chunks.
- `generate_embeddings.py`: Embedding generation logic.
- `retriever.py`: Retrieval layer.
- `get_retriever.py`: Retriever builder/loader.
- `get_retriever_thread_id.py`: Thread-aware retriever accessor.
- `ingest_pdf.py`: PDF ingestion pipeline.

### 🧵 Thread and Conversation Utilities

- `thread_id.py`: Thread identifier helpers.
- `add_thread_id.py`: Thread assignment logic.
- `thread_has_documents.py`: Checks document availability by thread.
- `thread_document_metadata.py`: Per-thread document metadata logic.
- `load_conversation.py`: Conversation history loader.
- `reset_chat.py`: Conversation reset utility.
- `retriever_state.py`: Retriever state model.

### 🔧 Tools and Data

- `tools.py`: Tool definitions.
- `database_connection.py`: Database connection management.
- `model.py`: Model setup.

### 🧪 Notebook

- `main.ipynb`: Interactive notebook for experimentation.

## ▶️ How To Run

### Run Python script

```bash
python main.py
```

### Run notebook

Open `main.ipynb` in VS Code and execute cells.
