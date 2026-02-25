# 🏋️ BMI Calculator - Simple Sequential Workflow

A basic LangGraph workflow demonstrating sequential node execution with BMI calculation and categorization.

## 🎯 Overview

Calculates Body Mass Index (BMI) from weight and height, then categorizes the result into standard health categories.

## 🔄 Workflow

```
START → bmi_calculate → label_bmi → END
```

## 📊 BMI Categories

| BMI Range | Category |
|-----------|----------|
| < 18.5 | Underweight |
| 18.5 - 24.9 | Normal weight |
| 25.0 - 29.9 | Overweight |
| ≥ 30.0 | Obese |

## 🚀 Usage

```bash
python main.py
```

**Input Example**:
```
Enter weight in kg: 70
Enter height in meters: 1.75
```

**Output**:
```python
{
    'weight_kg': 70.0,
    'height_m': 1.75,
    'bmi': 22.86,
    'bmi_category': 'Normal weight'
}
```

## 📁 Files

- **`bmi_calculate.py`** - Calculate BMI using formula: `weight / (height²)`
- **`label_bmi.py`** - Categorize BMI into health categories
- **`bmi_state_class.py`** - Pydantic state schema defining workflow state
- **`main.py`** - Main workflow setup and execution

## 📐 Formula

```
BMI = weight (kg) / height² (m²)
```

## 🎓 Learning Points

- ✅ Sequential node execution
- ✅ State management with Pydantic
- ✅ Simple data transformation pipeline
- ✅ Basic graph construction with LangGraph

## 📦 Dependencies

```bash
pip install langgraph pydantic
```

---

**Part of**: LangGraph Course - Sequential Workflows  
**Type**: Simple Workflow (Non-LLM)
