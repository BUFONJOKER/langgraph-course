# 🧵 Chatbot Resume Feature (Thread Memory)

## 🎯 Overview
A multi-thread Streamlit chatbot where each conversation can be reopened by `thread_id`.

## ✨ Key Feature
Resume older chats from the sidebar by selecting a stored thread.

## 🗂️ Files
### 🚀 App & Flow
- `main.py`: full Streamlit app (sidebar threads, new chat, streaming replies).
- `workflow.py`: LangGraph workflow compiled with `InMemorySaver`.
- `chat.py`: response generation node.

### 🧵 Thread Management
- `thread_id.py`: creates UUID thread IDs.
- `add_thread.py`: tracks thread IDs in session state.
- `load_conversation.py`: loads message history from workflow state.
- `reset_chat.py`: starts a fresh thread and clears messages.

### 🤖 Model & State
- `model.py`: loads `ChatOllama` (`qwen3.5:cloud`).
- `state_schema.py`: `ChatState` for `model` and `messages`.
