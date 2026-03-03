
---

# 📝 LLM-Based Parallel Essay Evaluation System

## 🎯 Overview

This project implements an **AI-powered essay evaluation system** using **LangGraph** parallel workflows and **Ollama**. The system leverages a multi-agent approach to analyze essays across three distinct academic dimensions simultaneously, providing structured feedback and a final synthesized report via a **Streamlit** web interface.

---

## 🏗️ Architecture

### Workflow Design

The system uses a **fan-out/fan-in parallel architecture**. When an essay is submitted, it is processed by three independent specialized agents before being consolidated.

**Key Features:**

* ⚡ **Parallel Evaluation**: Three evaluation nodes (`Clarity`, `Deep Analysis`, `Language Quality`) run concurrently to minimize latency.
* 🔄 **State Management**: A centralized `EssayState` (Pydantic) tracks the essay content, model instances, accumulated feedback strings, and a list of numerical scores.
* 🤖 **Advanced LLM**: Configured to use the `qwen3-next:80b-cloud` model for high-reasoning capabilities.
* 🎨 **Web Interface**: Built with **Streamlit** for a professional user experience, featuring real-time analysis spinners and interactive metric cards.

---

## 📁 File Structure & Descriptions

### Core Logic & State

| File | Purpose |
| --- | --- |
| **main.py** | 🚀 **Streamlit Entry Point**. Defines the UI, assembles the LangGraph, and executes the workflow. |
| **essay_state.py** | 📦 Defines `EssayState`, using `Annotated[list, operator.add]` for the `individual_scores` to allow parallel nodes to append scores safely. |
| **model.py** | 🤖 Configures `ChatOllama` to connect to the `qwen3-next:80b-cloud` endpoint. |
| **model_output_schema.py** | 📋 Pydantic schema (`OutputSchema`) ensuring LLMs return a JSON with exactly a `feedback` (str) and `score` (float). |

### Evaluation Nodes

Each node is a specialized Python function that uses a targeted system prompt:

* **`clarity_of_thoughts.py`**: Focuses on logical progression, thesis strength, and coherence.
* **`deep_analysis.py`**: Evaluates the "why" and "how," evidence support, and acknowledgment of counter-arguments.
* **`language_quality.py`**: Assesses vocabulary diversity, grammatical precision, and stylistic flow.
* **`overall_feedback.py`**: The "Supervisor" node. It synthesizes the three feedback strings into a cohesive narrative and calculates the final `avg_score`.

---

## 🔧 Workflow Configuration

### State Reducer

One of the most critical parts of the system is the score aggregation in `essay_state.py`:

```python
individual_scores: Annotated[list[float], operator.add] = Field(
    default_factory=list, description="Scores of all feedback on a scale of 1 to 10"
)

```

This allows the three parallel nodes to return `{'individual_scores': [score]}` and have LangGraph automatically merge them into a single list of three values.

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have **Ollama** installed and the specific model pulled:

```bash
ollama pull qwen3-next:80b-cloud

```

### 2. Installation

```bash
pip install streamlit langgraph langchain-ollama langchain-huggingface pydantic python-dotenv

```

### 3. Running the App

Launch the Streamlit interface:

```bash
streamlit run main.py

```

---

## 📊 UI Features

* **Metric Cards**: Instantly view scores for Clarity, Depth, and Language.
* **Detailed Expanders**: Click to read the specific technical analysis from each AI agent.
* **Synthesis Summary**: A final "Academic Mentor" report that highlights strengths and specific paths for improvement.
* **Dynamic Averaging**: Automatically calculates and displays the mean score across all rubrics.

---

## 🛠️ Customization

To change the grading criteria, simply edit the `USER_CONTENT` string in the respective node file (e.g., `deep_analysis.py`). The `OutputSchema` ensures that as long as your prompt asks for a "feedback" and "score," the system will remain stable.

---

**Happy Grading!** 🚀✍️ Check out `main.ipynb` for a breakdown of the graph's internal state during execution.

