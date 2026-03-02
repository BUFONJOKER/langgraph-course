# 🔄 LangGraph Workflows Module

A comprehensive collection of LangGraph workflow patterns, progressing from simple sequential execution to complex iterative feedback loops.

---

## 📁 Folder Structure

```
m_0_workflows/
├── f_01_sequential_workflows/
├── f_02_parallel_workflows/
├── f_03_conditional_workflows/
└── f_04_iterative_workflows/
```

---

## 1️⃣ Sequential Workflows — `f_01_sequential_workflows/`

> Nodes execute one after another in a fixed linear chain: `START → Node 1 → Node 2 → ... → END`

### 📂 Subfolders

#### 🧮 `sf_01_simple_workflow` — BMI Calculator
A simple workflow that calculates Body Mass Index and categorizes the result (underweight, normal, overweight, obese) using two sequential nodes.

#### 🤖 `sf_02_llm_based_workflows` — Question & Answer
A single-node LLM workflow that answers user questions. Supports both Ollama and HuggingFace model backends.

#### 📝 `sf_03_prompt_chaining` — Blog Generator
A multi-step prompt chaining workflow with a Streamlit UI that generates a blog outline, writes the full blog content, then evaluates the quality — all in sequence.

---

## 2️⃣ Parallel Workflows — `f_02_parallel_workflows/`

> Multiple independent nodes run concurrently (fan-out), then results are merged in a final aggregation node (fan-in).

### 📂 Subfolders

#### 🏏 `sf_04_simple_workflow` — Cricket Batsman Statistics
Calculates strike rate, boundary percentage, and balls-per-boundary simultaneously in parallel, then aggregates all metrics into a summary.

#### ✍️ `sf_05_llm_based` — Essay Evaluator
Uses an LLM to evaluate an essay on three criteria in parallel — clarity of thoughts, depth of analysis, and language quality — then produces a comprehensive overall feedback report via Streamlit.

---

## 3️⃣ Conditional Workflows — `f_03_conditional_workflows/`

> The workflow dynamically routes to different nodes based on state values using conditional edges.

### 📂 Subfolders

#### 🔢 `sf_06_simple_workflow` — Quadratic Equation Solver
Solves **ax² + bx + c = 0** by computing the discriminant and branching into one of three paths: two distinct real roots (Δ > 0), one repeated root (Δ = 0), or two complex roots (Δ < 0).

#### 💬 `sf_07_llm_based_workflow` — Customer Review Analyzer
Analyzes a customer review with an LLM to detect sentiment, then conditionally routes to a thank-you response (positive) or a diagnosis + empathetic apology pipeline (negative). Features a Streamlit UI.

---

## 4️⃣ Iterative Workflows — `f_04_iterative_workflows/`

> The workflow loops back on itself, refining output across multiple iterations until a quality threshold is met or a maximum iteration count is reached.

### 📂 Subfolders

#### 🐦 `sf_08_llm_based_tweet_generator` — Tweet Generator & Optimizer
Generates a tweet on a given topic, evaluates it against five quality criteria (relevance, clarity, engagement, conciseness, creativity), and optimizes it in a feedback loop — repeating until the tweet is approved or max iterations (default: 5) are reached. Uses HuggingFace for generation and Ollama for structured evaluation, with a Streamlit UI.

---

## 🎓 Workflow Patterns Summary

| Pattern | Description | Key API |
|---|---|---|
| **Sequential** | Linear node-to-node execution | `add_edge()` |
| **Parallel** | Fan-out to concurrent nodes, fan-in to aggregator | Multiple `add_edge(START, ...)` |
| **Conditional** | Dynamic routing based on state | `add_conditional_edges()` |
| **Iterative** | Loop with feedback until condition met | Conditional edge back to earlier node |

---

## 📦 Common Dependencies

```bash
pip install langgraph pydantic streamlit langchain-ollama langchain-huggingface
```
