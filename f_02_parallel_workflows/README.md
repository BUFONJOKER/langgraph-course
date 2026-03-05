# ⚡ Parallel Workflows

LangGraph workflows demonstrating parallel node execution where multiple nodes run simultaneously before merging results.

## 🎯 Overview

Parallel workflows execute multiple independent nodes concurrently, then combine their results in a final node:

```
                  ┌──> Node 1 ──┐
START ──> fanout ─┼──> Node 2 ──┼──> Aggregate ──> END
                  └──> Node 3 ──┘
```

## 📁 Projects

### 1️⃣ Simple Workflow - Cricket Batsman Statistics

**Path**: `s_04_simple_workflow/`

Calculates multiple cricket statistics in parallel.

**Workflow**:
```
                        ┌──> calculate_strike_rate ──────┐
START ──> (parallel) ───┼──> calculate_boundary_percent ─┼──> calculate_summary ──> END
                        └──> calculate_balls_per_boundary ┘
```

**Statistics Calculated**:
- 🏏 **Strike Rate**: (runs/balls) × 100
- 📊 **Boundary Percentage**: (boundaries/total balls) × 100
- 🎯 **Balls per Boundary**: balls / (4s + 6s)

**Usage**:
```python
python main.py

# Input: {'runs': 100, 'balls': 37, 'fours': 10, 'sixes': 5}
# Output: All statistics + summary
```

**Files**:
- `calculate_strike_rate.py` - Strike rate calculation
- `calculate_boundary_percent.py` - Boundary percentage
- `calculate_balls_per_boundary.py` - Balls per boundary ratio
- `calculate_summary.py` - Aggregate all metrics
- `batsmen_state.py` - State schema

---

### 2️⃣ LLM-Based - Essay Evaluator

**Path**: `s_05_llm_based/`

Evaluates essays on multiple criteria simultaneously using LLM.

**Workflow**:
```
                  ┌──> clarity_of_thoughts ──┐
START ──> (LLM) ──┼──> deep_analysis ────────┼──> overall_feedback ──> END
                  └──> language_quality ─────┘
```

**Evaluation Criteria**:
- 💭 **Clarity of Thoughts**: Logical flow and coherence
- 🔍 **Deep Analysis**: Critical thinking and insight depth
- 📝 **Language Quality**: Grammar, vocabulary, writing style

**Features**:
- ✨ Streamlit web interface
- 📊 Individual scores (1-10) for each criterion
- 📋 Comprehensive feedback for each aspect
- 🎓 Overall assessment and recommendations

**Usage**:
```bash
streamlit run main.py
```

**Files**:
- `clarity_of_thoughts.py` - Evaluate logical clarity
- `deep_analysis.py` - Assess analytical depth
- `language_quality.py` - Check language proficiency
- `overall_feedback.py` - Generate final assessment
- `model.py` - LLM configuration
- `model_output_schema.py` - Structured output schema

---

## 🚀 Quick Start

```bash
# Navigate to desired workflow
cd s_04_simple_workflow/

# Run the workflow
python main.py
```

## 🎓 Key Concepts

- **Parallel Execution**: Multiple nodes run simultaneously
- **Fan-out Pattern**: One input splits to multiple processors
- **Fan-in Pattern**: Multiple outputs merge to one aggregator
- **Efficiency**: Reduces total execution time for independent tasks

## 📦 Dependencies

```bash
pip install langgraph pydantic streamlit
# For LLM workflows: langchain-core langchain-ollama
```

## 🔗 Workflow Pattern

Parallel workflows use multiple edges from START:

```python
from langgraph.graph import StateGraph, START, END

graph = StateGraph(state_schema=YourState)

# Add parallel nodes
graph.add_node('task1', function1)
graph.add_node('task2', function2)
graph.add_node('task3', function3)
graph.add_node('aggregate', merge_function)

# Fan-out: START to multiple nodes
graph.add_edge(START, 'task1')
graph.add_edge(START, 'task2')
graph.add_edge(START, 'task3')

# Fan-in: Multiple nodes to aggregator
graph.add_edge('task1', 'aggregate')
graph.add_edge('task2', 'aggregate')
graph.add_edge('task3', 'aggregate')

graph.add_edge('aggregate', END)

workflow = graph.compile()
```

## ⚡ Performance Benefits

Parallel execution reduces total time when tasks are independent:
- Sequential: T1 + T2 + T3
- Parallel: max(T1, T2, T3)

---

**Part of**: LangGraph Course  
**Module**: Parallel Workflows
