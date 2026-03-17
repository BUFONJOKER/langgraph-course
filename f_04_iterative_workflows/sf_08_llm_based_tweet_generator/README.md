# 🧪 SF_08_LLM_BASED_TWEET_GENERATOR: Llm Based Tweet Generator

## Summary
Implements the Llm Based Tweet Generator sub-workflow for iterative improvement loops.


## 📌 Overview
Short example module for Llm Based Tweet Generator.

## 📂 File-by-File Explanation
- `__init__.py`: Marks this directory as a Python package for imports.
- `check_evaluation.py`: Checks whether tweet passes evaluation threshold or loops again.
- `evaluator_tweet.py`: Evaluates tweet quality against target criteria.
- `generator_tweet.py`: Generates initial tweet draft in iterative loop.
- `main.py`: Primary entry script to run this workflow example.
- `model.py`: Configures and initializes the model used in this workflow.
- `optimizer_tweet.py`: Refines tweet draft using evaluator feedback.
- `state_schema.py`: Defines the workflow state structure passed between nodes.
- `structured_output_schema.py`: Schema for structured output in iterative tweet workflow.
