# 1️⃣ Sequential Workflows

## 🎯 Concept
This module introduces sequential graph design in LangGraph, where each node runs in a fixed order and passes state to the next node. It is the best starting point for understanding deterministic workflow orchestration.

## 🧠 What You Learn
- How to model state and pass it through ordered nodes.
- How to split logic into focused node functions.
- How to chain LLM and non-LLM steps in a predictable pipeline.
- How to evaluate and refine outputs step by step.

## 🧩 Subfolders
### 🔹 sf_01_simple_workflow
Basic non-LLM workflow to calculate BMI and assign labels.

### 🔹 sf_02_llm_based_workflows
Sequential LLM workflow with model abstraction (Hugging Face and Ollama options).

### 🔹 sf_03_prompt_chaining
Multi-step content generation pipeline: outline -> blog draft -> evaluation.

## 🚀 Suggested Learning Path
1. Start with sf_01 to understand state and linear node execution.
2. Move to sf_02 to plug in LLM calls in the same pattern.
3. Finish with sf_03 to learn prompt chaining and output evaluation.
