# ✍️ Blog Generator - Prompt Chaining

A LangGraph workflow demonstrating prompt chaining with multi-step LLM-based blog generation.

## 🎯 Overview

Generates complete, high-quality blog posts using a three-step process: outline generation → blog writing → evaluation.

## 🔄 Workflow

```
START → generate_outline → generate_blog → evaluation → END
```

Each step builds on the previous, demonstrating **prompt chaining** for complex content generation.

## ✨ Features

- 📝 **Smart Outline Generation** - Creates structured blog outline from topic
- ✍️ **Content Generation** - Writes full blog based on outline
- ⭐ **Quality Evaluation** - Assesses blog quality and provides feedback
- 🎨 **Streamlit Interface** - Beautiful web UI for easy interaction

## 🚀 Usage

```bash
streamlit run main.py
```

**Web Interface**:
1. Enter blog title/topic
2. Click "Generate"
3. Get complete blog with outline and evaluation

**Jupyter Notebook**:
```python
# main.ipynb
from main import workflow

result = workflow.invoke({
    'topic': 'Introduction to Machine Learning',
    'model': model
})

print(result['blog_complete'])
```

## 📁 Files

- **`generate_outline.py`** - Step 1: Create blog structure/outline
- **`generate_blog.py`** - Step 2: Write full blog from outline
- **`evaluation.py`** - Step 3: Evaluate blog quality
- **`model.py`** - LLM configuration and model loader
- **`blog_state.py`** - Pydantic state schema
- **`main.py`** - Streamlit app and workflow setup
- **`main.ipynb`** - Jupyter notebook interface

## 🔗 Prompt Chaining Flow

```
Topic → LLM (Outline) → Outline
                ↓
        LLM (Blog) → Blog Content
                ↓
        LLM (Eval) → Quality Feedback
```

## 📊 State Management

The workflow maintains state across all nodes:
```python
{
    'topic': str,           # User input topic
    'model': LLM,          # Language model instance
    'blog_outline': str,   # Generated outline
    'blog_complete': str,  # Final blog content
    'evaluation': str      # Quality assessment
}
```

## 🎓 Learning Points

- ✅ **Prompt Chaining** - Breaking complex tasks into steps
- ✅ **Sequential LLM Calls** - Each step uses previous output
- ✅ **State Accumulation** - Building context across nodes
- ✅ **Streamlit Integration** - Creating interactive UIs

## 📦 Dependencies

```bash
pip install langgraph pydantic streamlit langchain-ollama
# OR
pip install langgraph pydantic streamlit langchain-huggingface
```

## 💡 Tips

- Use specific, clear topics for better outlines
- The evaluation step helps improve future prompts
- Each chain step can be customized independently

---

**Part of**: LangGraph Course - Sequential Workflows  
**Type**: LLM-Based Prompt Chaining
