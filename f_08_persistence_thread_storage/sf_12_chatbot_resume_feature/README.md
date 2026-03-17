# 🧪 SF_12_CHATBOT_RESUME_FEATURE: Chatbot Resume Feature

## Summary
Implements the Chatbot Resume Feature sub-workflow for thread-aware persistence.


## 📌 Overview
Short example module for Chatbot Resume Feature.

## 📂 File-by-File Explanation
- `__init__.py`: Marks this directory as a Python package for imports.
- `add_thread.py`: Adds/manages thread identifiers for conversation continuity.
- `chat.py`: Implements chat handling logic for message flow.
- `load_conversation.py`: Loads saved conversation history for resume behavior.
- `main.py`: Primary entry script to run this workflow example.
- `model.py`: Configures and initializes the model used in this workflow.
- `reset_chat.py`: Resets chat state to start a fresh conversation.
- `state_schema.py`: Defines the workflow state structure passed between nodes.
- `thread_id.py`: Stores/helpers for current thread identifier handling.
- `workflow.py`: Builds and wires the LangGraph workflow execution path.
