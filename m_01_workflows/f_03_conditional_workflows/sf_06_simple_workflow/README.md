# 🔢 Quadratic Equation Solver

A LangGraph workflow that solves quadratic equations using conditional branching based on the discriminant value.

## 🎯 Overview

Solves **ax² + bx + c = 0** by calculating discriminant **Δ = b² - 4ac** and routing to:
- ✅ Two distinct real roots (Δ > 0)
- 🔁 One repeated root (Δ = 0)
- 🌀 Two complex roots (Δ < 0)

## 🔄 Workflow

```
START → show_equation → calculate_discriminant → calculate_roots (conditional)
                                                   ├─→ distinct_roots → END
                                                   ├─→ repeated_root → END
                                                   └─→ complex_roots → END
```

## 🚀 Usage

```python
from main import workflow

result = workflow.invoke({'a': 1, 'b': 4, 'c': 4})
print(result)
# Output: {'a': 1, 'b': 4, 'c': 4, 'result': 'One real repeated root is -2.0'}
```

Run: `python main.py`

## 📊 Examples

| a | b | c | Discriminant | Result |
|---|---|---|--------------|--------|
| 1 | -5 | 6 | 1 (> 0) | Two distinct real roots: 3.0 and 2.0 |
| 1 | 4 | 4 | 0 | One real repeated root: -2.0 |
| 4 | 4 | 3 | -32 (< 0) | Two complex roots |

## 📁 Files

- `main.py` - Main workflow execution
- `state_schema.py` - Pydantic state model
- `calculate_discriminant.py` - Calculate Δ = b² - 4ac
- `calculate_roots.py` - Conditional routing logic
- `distinct_roots.py`, `repeated_root.py`, `complex_roots.py` - Root handlers

## 🎓 Key Concepts

- Conditional edges with `add_conditional_edges()`
- State management with Pydantic
- Dynamic routing based on discriminant value
