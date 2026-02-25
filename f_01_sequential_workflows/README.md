# 📊 Sequential Workflows

LangGraph workflows demonstrating sequential node execution patterns, from simple calculations to LLM-based applications.

## 🎯 Overview

This module contains three sequential workflow examples that execute nodes one after another in a linear chain:

```
START → Node 1 → Node 2 → Node 3 → END
```

## 📁 Projects

### 1️⃣ Simple Workflow - BMI Calculator

**Path**: `sf_01_simple_workflow/`

Calculates Body Mass Index and categorizes it.

**Workflow**: `START → bmi_calculate → label_bmi → END`

**Usage**:
```python
python main.py
# Enter weight in kg: 70
# Enter height in meters: 1.75
```

**Files**:
- `bmi_calculate.py` - Calculate BMI = weight/(height²)
- `label_bmi.py` - Categorize BMI (underweight, normal, overweight, obese)
- `bmi_state_class.py` - Pydantic state model

---

### 2️⃣ LLM-Based Workflow - Question & Answer

**Path**: `sf_02_llm_based_workflows/`

Simple LLM question answering system.

**Workflow**: `START → llm_qa → END`

**Usage**:
```python
python main.py
# Uses Ollama or Hugging Face models
```

**Files**:
- `llm_question_answer.py` - LLM invocation node
- `model_ollama.py` - Ollama model configuration
- `model_huggingface.py` - Hugging Face model configuration
- `llm_state_class.py` - State schema

---

### 3️⃣ Prompt Chaining - Blog Generator

**Path**: `sf_03_prompt_chaining/`

Generates complete blog posts using multi-step LLM prompting.

**Workflow**: `START → generate_outline → generate_blog → evaluation → END`

**Usage**:
```bash
streamlit run main.py
```

**Features**:
- 📝 Generate blog outline from topic
- ✍️ Write complete blog from outline
- ⭐ Evaluate blog quality
- 🎨 Streamlit web interface

**Files**:
- `generate_outline.py` - Create blog structure
- `generate_blog.py` - Write full blog content
- `evaluation.py` - Assess blog quality
- `model.py` - LLM configuration

## 🚀 Quick Start

```bash
# Navigate to desired workflow
cd sf_01_simple_workflow/

# Run the workflow
python main.py
```

## 🎓 Key Concepts

- **Sequential Execution**: Nodes run in fixed order
- **State Management**: Passing data between nodes
- **Prompt Chaining**: Breaking complex tasks into steps
- **Graph Construction**: Using `add_edge()` for linear flows

## 📦 Dependencies

```bash
pip install langgraph pydantic streamlit
# For LLM workflows: langchain-ollama or langchain-huggingface
```

## 🔗 Workflow Pattern

All workflows follow this pattern:
```python
from langgraph.graph import StateGraph, START, END

graph = StateGraph(state_schema=YourState)
graph.add_node('node1', function1)
graph.add_node('node2', function2)

graph.add_edge(START, 'node1')
graph.add_edge('node1', 'node2')
graph.add_edge('node2', END)

workflow = graph.compile()
result = workflow.invoke(input_state)
```

---

**Part of**: LangGraph Course  
**Module**: Sequential Workflows
