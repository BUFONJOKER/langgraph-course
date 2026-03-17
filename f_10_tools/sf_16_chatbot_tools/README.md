# 🧪 SF_16_CHATBOT_TOOLS: Chatbot Tools

## Summary
Implements the Chatbot Tools sub-workflow for practical tool-calling usage.


## 📌 Overview
Short example module for Chatbot Tools.

## 📂 File-by-File Explanation
- `__init__.py`: Marks this directory as a Python package for imports.
- `add_thread.py`: Adds/manages thread identifiers for conversation continuity.
- `chat.py`: Implements chat handling logic for message flow.
- `chatbot_checkpoints.db`: Local checkpoint/database artifact generated during runs.
- `chatbot_checkpoints.db-shm`: Local checkpoint/database artifact generated during runs.
- `chatbot_checkpoints.db-wal`: Local checkpoint/database artifact generated during runs.
- `database_connection.py`: Creates and manages database connections used by the workflow.
- `extract_tool_names.py`: Extracts/parses tool names used for routing or diagnostics.
- `load_conversation.py`: Loads saved conversation history for resume behavior.
- `main.py`: Primary entry script to run this workflow example.
- `model.py`: Configures and initializes the model used in this workflow.
- `reset_chat.py`: Resets chat state to start a fresh conversation.
- `state_schema.py`: Defines the workflow state structure passed between nodes.
- `thread_id.py`: Stores/helpers for current thread identifier handling.
- `tools.py`: Defines tools/functions the agent can call during execution.
- `workflow.py`: Builds and wires the LangGraph workflow execution path.
