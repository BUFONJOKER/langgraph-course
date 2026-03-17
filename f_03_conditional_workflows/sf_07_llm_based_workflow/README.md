# 🧪 SF_07_LLM_BASED_WORKFLOW: Llm Based Workflow

## Summary
Implements the Llm Based Workflow sub-workflow for conditional routing behavior.


## 📌 Overview
Short example module for Llm Based Workflow.

## 📂 File-by-File Explanation
- `__init__.py`: Marks this directory as a Python package for imports.
- `check_sentiment.py`: Routes flow based on detected sentiment class.
- `diagonsis_output_schema.py`: Structured schema for diagnosis stage output.
- `find_sentiment.py`: Infers sentiment from review/input text.
- `main.ipynb`: Notebook walkthrough for interactive experimentation.
- `main.py`: Primary entry script to run this workflow example.
- `model.py`: Configures and initializes the model used in this workflow.
- `negative_response.py`: Generates branch-specific response for negative sentiment.
- `output_schema.py`: Structured output schema for primary workflow response.
- `positive_response.py`: Generates branch-specific response for positive sentiment.
- `review_state_schema.py`: Defines the workflow state structure passed between nodes.
- `run_diagnosis.py`: Runs diagnosis step used in conditional LLM workflow.
