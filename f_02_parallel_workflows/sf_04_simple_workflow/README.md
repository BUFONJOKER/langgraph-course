# 🏏 Cricket Batsman Statistics - Parallel Workflow

A LangGraph workflow demonstrating parallel execution by calculating multiple cricket statistics simultaneously.

## 🎯 Overview

Analyzes a batsman's innings by computing three key statistics in parallel, then aggregating them into a comprehensive summary.

## 🔄 Workflow

```
                        ┌──> calculate_strike_rate ──────┐
START ──> (parallel) ───┼──> calculate_boundary_percent ─┼──> calculate_summary ──> END
                        └──> calculate_balls_per_boundary ┘
```

## 📊 Statistics Calculated

### 1️⃣ Strike Rate
```
Strike Rate = (Runs / Balls) × 100
```
Measures scoring speed - higher is better

### 2️⃣ Boundary Percentage
```
Boundary % = (Boundary Runs / Total Runs) × 100
```
Shows percentage of runs from boundaries (4s and 6s)

### 3️⃣ Balls per Boundary
```
Balls/Boundary = Balls Faced / (Fours + Sixes)
```
Average balls between boundaries - lower is better

## 🚀 Usage

```bash
python main.py
```

**Input Example**:
```python
input_state = {
    'runs': 100,
    'balls': 37,
    'fours': 10,
    'sixes': 5
}
```

**Output**:
```python
{
    'runs': 100,
    'balls': 37,
    'fours': 10,
    'sixes': 5,
    'strike_rate': 270.27,
    'boundary_percent': 70.0,
    'balls_per_boundary': 2.47,
    'summary': 'Summary of Batsmen Innings...'
}
```

## 📁 Files

- **`calculate_strike_rate.py`** - Calculate scoring rate
- **`calculate_boundary_percent.py`** - Calculate boundary contribution
- **`calculate_balls_per_boundary.py`** - Calculate boundary frequency
- **`calculate_summary.py`** - Aggregate all statistics
- **`batsmen_state.py`** - Pydantic state schema
- **`main.py`** - Workflow setup and execution
- **`main.ipynb`** - Jupyter notebook interface

## ⚡ Parallel Execution

All three calculations run **simultaneously** because they are independent:
- Sequential time: T1 + T2 + T3
- Parallel time: max(T1, T2, T3)

## 🎓 Learning Points

- ✅ **Fan-out pattern** - Split from START to multiple nodes
- ✅ **Fan-in pattern** - Merge multiple nodes to aggregator
- ✅ **Parallel execution** - Independent calculations run concurrently
- ✅ **State accumulation** - Each node adds to shared state

## 📦 Dependencies

```bash
pip install langgraph pydantic
```

## 🏆 Example Innings

| Batsman | Runs | Balls | 4s | 6s | Strike Rate | Boundary % |
|---------|------|-------|----|----|-------------|------------|
| Aggressive | 100 | 37 | 10 | 5 | 270.27 | 70.0% |
| Conservative | 50 | 60 | 6 | 0 | 83.33 | 48.0% |

---

**Part of**: LangGraph Course - Parallel Workflows  
**Type**: Simple Workflow (Non-LLM)
