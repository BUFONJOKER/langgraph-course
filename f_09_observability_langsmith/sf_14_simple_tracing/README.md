# 🗄️ Chatbot with SQLite Checkpointing

## 🎯 Overview
A Streamlit + LangGraph chatbot that persists conversations in SQLite using `SqliteSaver`.

## ✨ Key Feature
Thread history survives app restarts by reading and writing checkpoints to a database file.

## 🗂️ Files
### 🚀 App & Workflow
- `main.py`: chatbot UI, thread switching, and streaming assistant responses.
- `workflow.py`: compiles graph with `SqliteSaver`, calls `setup()`, and loads existing thread IDs.
- `chat.py`: chat node that generates AI replies from message history.

### 💾 Persistence
- `database_connection.py`: creates SQLite connection (`chatbot_checkpoints.db`).
- `load_conversation.py`: fetches messages for a selected thread.

### 🧵 Thread Utilities
- `thread_id.py`: generates UUID thread IDs.
- `add_thread.py`: adds thread IDs to session state.
- `reset_chat.py`: resets messages and starts a new thread.

### 🤖 Model & State
- `model.py`: loads `ChatOllama` (`qwen3.5:cloud`).
- `state_schema.py`: `ChatState` schema for model + messages.
