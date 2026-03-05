# 😄 Simple Memory Saver Workflow

## 🎯 Overview
A minimal LangGraph persistence example that generates a joke and then explains it.

## 🔁 Workflow
`START -> joke -> explanation -> END`

## 🗂️ Files
### 🚀 Entry Point
- `main.py`: builds the graph, compiles with `InMemorySaver`, and runs one thread (`thread_id='1'`).

### 🤖 Model
- `model.py`: loads `ChatOllama` (`qwen3-next:80b-cloud`).

### 🧠 State
- `state_schema.py`: `JokeState` with `topic`, `joke`, `explanation`, and `model`.

### 🧩 Nodes
- `generate_joke.py`: creates a joke from the topic.
- `generate_joke_explanation.py`: explains the generated joke.
