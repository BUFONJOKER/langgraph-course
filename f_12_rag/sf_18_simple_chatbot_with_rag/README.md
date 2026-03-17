# 📚 SF 18: Simple Chatbot With RAG

## 📌 Overview

This folder demonstrates a simple Retrieval-Augmented Generation (RAG) chatbot pipeline using document loading, splitting, embedding creation, retrieval, and response generation.

## 📂 Files

### 🧠 Chat Flow

- `main.py`: Script entry point.
- `chat_node.py`: Chat node orchestration logic.
- `state_schema.py`: Graph state schema.

### 📄 RAG Pipeline

- `document_loader.py`: Loads source documents.
- `document_splitter.py`: Splits documents into chunks.
- `generate_embeddings.py`: Creates vector embeddings.
- `retriever.py`: Retrieves relevant chunks for queries.
- `tools.py`: RAG-related tool functions.

### 🤖 Model

- `model.py`: Model setup and invocation.

### 🧪 Notebook

- `main.ipynb`: Notebook walkthrough of the RAG chatbot.

## ▶️ How To Run

### Run Python script

```bash
python main.py
```

### Run notebook

Open `main.ipynb` in VS Code and execute cells.
