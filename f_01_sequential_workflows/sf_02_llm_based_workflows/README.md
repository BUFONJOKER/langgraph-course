# 🤖 LLM Question & Answer - Sequential Workflow

A simple LangGraph workflow demonstrating LLM integration with sequential execution.

## 🎯 Overview

Basic question-answering system using Large Language Models (Ollama or Hugging Face) in a sequential workflow.

## 🔄 Workflow

```
START → llm_qa → END
```

Simple single-node workflow that processes a question through an LLM and returns the answer.

## 🚀 Usage

```bash
python main.py
```

**Example**:
```python
# Input question
question = "What is the capital of France?"

# Output
{
    'question': 'What is the capital of France?',
    'answer': 'The capital of France is Paris...'
}
```

## 📁 Files

- **`llm_question_answer.py`** - LLM invocation node that processes questions
- **`llm_state_class.py`** - Pydantic state schema for question/answer
- **`model_ollama.py`** - Ollama model configuration
- **`model_huggingface.py`** - Hugging Face model configuration
- **`main.py`** - Main workflow setup and execution
- **`main.ipynb`** - Jupyter notebook interface

## 🔧 Model Configuration

### Ollama
```python
from model_ollama import load_model
model = load_model()  # Uses local Ollama
```

### Hugging Face
```python
from model_huggingface import load_model
model = load_model()  # Uses HF models
```

## 🎓 Learning Points

- ✅ LLM integration with LangGraph
- ✅ Model abstraction with interchangeable backends
- ✅ Basic prompt construction
- ✅ State management for Q&A systems

## 📦 Dependencies

```bash
pip install langgraph pydantic langchain-ollama
# OR
pip install langgraph pydantic langchain-huggingface
```

## ⚙️ Prerequisites

- Ollama installed and running (for Ollama backend)
- OR Hugging Face API key (for HF backend)

---

**Part of**: LangGraph Course - Sequential Workflows  
**Type**: LLM-Based Workflow
