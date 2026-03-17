# 🧪 SF_13_CHATBOT_SQLITE_CHECKPOINT: Chatbot Sqlite Checkpoint

## Summary
Implements the Chatbot Sqlite Checkpoint sub-workflow for thread-aware persistence.


## 📌 Overview
Short example module for Chatbot Sqlite Checkpoint.

## 📂 File-by-File Explanation
- `__init__.py`: Marks this directory as a Python package for imports.
- `add_thread.py`: Adds/manages thread identifiers for conversation continuity.
- `chat.py`: Implements chat handling logic for message flow.
- `chatbot_checkpoints.db`: Local checkpoint/database artifact generated during runs.
- `chatbot_checkpoints.db-shm`: Local checkpoint/database artifact generated during runs.
- `chatbot_checkpoints.db-wal`: Local checkpoint/database artifact generated during runs.
- `chatbot_checkpoints.db-x-checkpoints-1-checkpoint.bin`: Local checkpoint/database artifact generated during runs.
- `chatbot_checkpoints.db-x-checkpoints-2-checkpoint.bin`: Local checkpoint/database artifact generated during runs.
- `chatbot_checkpoints.db-x-checkpoints-3-checkpoint.bin`: Local checkpoint/database artifact generated during runs.
- `database_connection.py`: Creates and manages database connections used by the workflow.
- `load_conversation.py`: Loads saved conversation history for resume behavior.
- `main.py`: Primary entry script to run this workflow example.
- `model.py`: Configures and initializes the model used in this workflow.
- `reset_chat.py`: Resets chat state to start a fresh conversation.
- `state_schema.py`: Defines the workflow state structure passed between nodes.
- `thread_id.py`: Stores/helpers for current thread identifier handling.
- `workflow.py`: Builds and wires the LangGraph workflow execution path.
