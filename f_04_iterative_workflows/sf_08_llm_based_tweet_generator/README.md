# 🐦 LLM-Based Tweet Generator & Optimizer

An intelligent iterative workflow for generating, evaluating, and optimizing tweets using multiple LLM models and LangGraph.

---

## 📋 Overview

This project implements an **iterative workflow** that:
1. 📝 **Generates** tweets based on a given topic using HuggingFace LLM
2. ✅ **Evaluates** tweets against quality criteria using Ollama LLM
3. 🔄 **Optimizes** tweets based on feedback if they need improvement
4. 🔁 **Repeats** the process until the tweet meets approval criteria or max iterations reached

---

## 🏗️ Architecture

### Workflow Nodes

```
START → generate_tweet → evaluate_tweet ↘
                             ↓            ↘
                      check_evaluation     → END (approved)
                             ↓
                      optimize_tweet ↓
                             ↑__________↓
```

- **Generate**: Creates a fresh tweet from scratch
- **Evaluate**: Assesses tweet quality (relevance, clarity, engagement, conciseness, creativity)
- **Optimize**: Refines tweet based on evaluation feedback
- **Check Evaluation**: Routes to END if approved, else back to Optimize

---

## 📁 Project Files

### Core Workflow Files

| File | Purpose |
|------|---------|
| **main.py** | 🚀 Streamlit app entry point with workflow orchestration |
| **main.ipynb** | 📓 Jupyter notebook for testing and experimentation |
| **generator_tweet.py** | ✍️ Generates initial tweets from topics |
| **evaluator_tweet.py** | 🔍 Evaluates tweets against quality criteria |
| **optimizer_tweet.py** | 🎯 Optimizes tweets based on feedback |
| **check_evaluation.py** | ✔️ Routes workflow based on evaluation results |

### Configuration Files

| File | Purpose |
|------|---------|
| **state_schema.py** | 🗂️ Defines TweetState TypedDict with all workflow fields |
| **structured_output_schema.py** | 📦 Pydantic models for LLM structured output |
| **model.py** | 🤖 Model loaders for HuggingFace and Ollama |

### Other

| File | Purpose |
|------|---------|
| **__init__.py** | 📦 Package initialization |
| **__pycache__/** | 🗑️ Python bytecode cache |

---

## 🔧 State Schema

The workflow maintains a `TweetState` with:

```python
{
    'topic': str              # Topic for tweet generation
    'model': Any              # HuggingFace chat model
    'structured_model': Any   # Ollama structured model
    'tweet': str              # Current generated tweet
    'evaluation': str         # 'approved' or 'needs_improvement'
    'feedback': str           # Evaluation feedback
    'iteration': int          # Current iteration count
    'max_iterations': int     # Maximum iterations allowed (default: 5)
    'tweet_history': List     # History of generated tweets
    'feedback_history': List  # History of feedback
}
```

---

## 🚀 Usage

### Streamlit Web Interface
```bash
streamlit run main.py
```
- Enter a topic
- Click generate to start the workflow
- View tweet improvements across iterations

---

## 📊 Models Used

- **Generator**: `zai-org/GLM-4.7-Flash` (HuggingFace)
- **Evaluator**: Ollama `qwen3-next:80b-cloud` model with structured output
- Both support iterative refinement and feedback integration

---

## ⚙️ How It Works

### 1️⃣ Generation Phase
- Takes topic as input
- Generates engaging, concise tweet (max 280 chars)
- Adds hashtags and relevant mentions

### 2️⃣ Evaluation Phase
Evaluates on 5 criteria:
- ✨ **Relevance**: Topic alignment
- 📖 **Clarity**: Easy to understand
- 💬 **Engagement**: Interactive and interesting
- 📏 **Conciseness**: Under 280 characters
- 🎨 **Creativity**: Original, avoids clichés

### 3️⃣ Feedback Loop
If tweet needs improvement:
- Receives specific feedback
- Gets optimized version
- Re-evaluated in next iteration
- Repeats until approved or max iterations reached

---

## 🎯 Evaluation Criteria

| Criterion | Details |
|-----------|---------|
| **Relevance** | Must align with provided topic |
| **Clarity** | Clear message, easy to understand |
| **Engagement** | Encourages interaction/retweets |
| **Conciseness** | Ideally under 280 characters |
| **Creativity** | Original, non-cliche content |

---

## 🔄 Iterative Process

The workflow handles multiple refinement cycles:
- 🔁 Loop until tweet is approved
- 📦 Maintains history of all tweets and feedback
- 🛑 Stops at max_iterations (default: 5)
- 📈 Each iteration improves tweet quality

---

## 📝 Notes

- Both models must be available and configured
- HuggingFace model requires `langchain_huggingface`
- Ollama model must be running locally
- Structured output requires `function_calling` method support

