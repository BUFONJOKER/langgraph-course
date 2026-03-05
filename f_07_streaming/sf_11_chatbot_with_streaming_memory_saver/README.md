# 💬 Streaming Chatbot with Memory Saver

## 🎯 Overview
A Streamlit chatbot using LangGraph with in-memory checkpointing and token streaming.

## 🔁 Workflow
`START -> chat -> END`

## 🗂️ Files
### 🚀 App & Flow
- `main.py`: Streamlit UI, chat history rendering, user input handling, and streaming assistant output.
- `workflow.py`: creates and compiles the graph with `InMemorySaver`.

### 🧩 Node
- `chat.py`: prompt + message history -> LLM response.

### 🤖 Model & State
- `model.py`: loads `ChatOllama` (`qwen3.5:cloud`).
- `state_schema.py`: `ChatState` with `model` and aggregated `messages`.
