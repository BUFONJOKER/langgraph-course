# 🚀 LangGraph Course

## Summary

Hands-on LangGraph learning repository covering end-to-end workflow patterns from fundamentals to advanced production-like agent architectures.

## 🎯 Project Overview

This repository is organized as a progressive course. Each top-level folder (`f_01` to `f_15`) focuses on one LangGraph concept, and each subfolder (`sf_*`) contains runnable examples with focused code modules.

The goal is to help you move from basic graph execution to advanced agent capabilities such as tool use, retrieval, memory, persistence, observability, human-in-the-loop, and subgraph composition.

## 🧭 Learning Path (f_01 to f_15)

- `f_01_sequential_workflows`: Linear, step-by-step graph execution.
- `f_02_parallel_workflows`: Fan-out/fan-in parallel branches.
- `f_03_conditional_workflows`: Branching based on computed or model outputs.
- `f_04_iterative_workflows`: Loop-based generate-evaluate-refine patterns.
- `f_05_chatbot_workflows`: Core chatbot state and response flow.
- `f_06_persistence`: Persisting state between interactions.
- `f_07_streaming`: Streaming responses from graph-driven chatbots.
- `f_08_persistence_thread_storage`: Thread-aware conversation persistence and resume.
- `f_09_observability_langsmith`: Tracing and observability for workflow debugging.
- `f_10_tools`: Tool-calling fundamentals and chatbot tools integration.
- `f_11_mcp`: MCP-based tool integration with external capability servers.
- `f_12_rag`: Retrieval-Augmented Generation pipelines and RAG chatbots.
- `f_13_human_in_the_loop`: Human checkpoints in autonomous flows.
- `f_14_subgraphs`: Modular graph composition with reusable subgraphs.
- `f_15_short_term_memory`: Memory strategies and token-budget handling.

## 🗺️ Which Folder For What?

- Want to learn basic graph flow? -> `f_01_sequential_workflows`
- Want parallel branches and merge patterns? -> `f_02_parallel_workflows`
- Want if/else style routing in graphs? -> `f_03_conditional_workflows`
- Want generate-evaluate-refine loops? -> `f_04_iterative_workflows`
- Want to build a basic chatbot? -> `f_05_chatbot_workflows`
- Want state persistence between turns? -> `f_06_persistence`
- Want streaming token/event responses? -> `f_07_streaming`
- Want multi-thread chat resume support? -> `f_08_persistence_thread_storage`
- Want tracing and observability? -> `f_09_observability_langsmith`
- Want function/tool calling agents? -> `f_10_tools`
- Want MCP integration with external tools? -> `f_11_mcp`
- Want document-grounded RAG chatbots? -> `f_12_rag`
- Want human approval/control in workflows? -> `f_13_human_in_the_loop`
- Want reusable graph components? -> `f_14_subgraphs`
- Want memory trimming and token control? -> `f_15_short_term_memory`

## 🧭 Which Subfolder For What?

- Want a first simple graph example? -> `sf_01_simple_workflow`
- Want sequential LLM Q&A flow? -> `sf_02_llm_based_workflows`
- Want prompt chaining (outline -> draft -> evaluate)? -> `sf_03_prompt_chaining`
- Want parallel metric calculations? -> `sf_04_simple_workflow`
- Want parallel LLM evaluation? -> `sf_05_llm_based`
- Want conditional branching from math/state? -> `sf_06_simple_workflow`
- Want conditional branching from LLM sentiment? -> `sf_07_llm_based_workflow`
- Want iterative generation refinement? -> `sf_08_llm_based_tweet_generator`
- Want a basic chatbot baseline? -> `sf_09_simple_chatbot`
- Want memory saver persistence? -> `sf_10_simple_memory_saver_based`
- Want streaming chatbot output? -> `sf_11_chatbot_with_streaming_memory_saver`
- Want resume-by-thread chat? -> `sf_12_chatbot_resume_feature`
- Want SQLite checkpoints? -> `sf_13_chatbot_sqlite_checkpoint`
- Want LangSmith tracing example? -> `sf_14_simple_tracing`
- Want tool-calling fundamentals? -> `sf_15_fundamentals`
- Want chatbot with practical tools? -> `sf_16_chatbot_tools`
- Want MCP-integrated chatbot? -> `sf_17_chatbot_with_mcp`
- Want simple RAG chatbot? -> `sf_18_simple_chatbot_with_rag`
- Want RAG + tools + UI helpers? -> `sf_19_chatbot_with_rag_tools_ui`
- Want human-in-the-loop basic flow? -> `sf_20_simple`
- Want human-in-the-loop with tools? -> `sf_21_advanced_with_tools`
- Want simple subgraph composition? -> `sf_22_simple_subgraph`
- Want shared reusable subgraphs? -> `sf_23_shared_subgraphs`
- Want short-term memory saver variant? -> `sf_24_with_memory_saver`
- Want PostgreSQL-backed memory? -> `sf_25_memory_postgres_database`
- Want token trimming strategy? -> `sf_26_tokens_trimming`

## 🏗️ Repository Structure

- `main.py`: Root-level starter script.
- `main.ipynb`: Root-level notebook for exploration.
- `pyproject.toml`: Python project metadata and dependencies.
- `settings.json`: Project settings/configuration.
- `todo.txt`: Work notes/tasks.
- `f_*/`: Concept modules.
- `f_*/sf_*/`: Scenario-level examples.

Each module and submodule has its own `README.md` with:

- A summary of what the folder does.
- File-by-file explanation.
- Concept context for that example.

## ⚙️ Setup

### Prerequisites

- Python 3.10+ (recommended)
- `uv` installed
- API/model credentials as needed by your selected examples

### Install Dependencies (uv)

```bash
uv sync
```

### Run Commands With uv

Use `uv run` so commands execute in the project environment without manual activation.

```bash
uv run python --version
uv run python main.py
```

## ▶️ How To Run Examples

Run any module or submodule script directly:

```bash
uv run python f_01_sequential_workflows/sf_01_simple_workflow/main.py
uv run python f_12_rag/sf_18_simple_chatbot_with_rag/main.py
```

Open notebooks for interactive experimentation:

```bash
uv run jupyter notebook
```

## 🧠 Core Concepts Implemented

- State schemas for typed graph state transitions.
- Node-based graph orchestration patterns.
- Model abstraction for backend flexibility.
- Conditional and iterative control flow.
- Tool invocation loops and agent-style interactions.
- Retrieval + embedding pipelines for grounded answers.
- Persistence/checkpoint strategies (memory saver, SQLite, PostgreSQL).
- Thread-based multi-session conversation management.
- Tracing/observability integration.
- Human-in-the-loop checkpoints.

## 🔐 Environment and Configuration

- Keep secrets in `.env` (do not commit).
- Configure model providers according to the module you run.
- Some folders include local DB artifacts (`*.db`, checkpoints) generated during execution.

## 📌 Recommended Study Order

1. `f_01` -> `f_04` for core graph mechanics.
2. `f_05` -> `f_09` for chatbot, persistence, streaming, and observability.
3. `f_10` -> `f_12` for tools, MCP, and RAG.
4. `f_13` -> `f_15` for human control, subgraphs, and memory optimization.

## ✅ Notes

- Examples are intentionally modular; many patterns are reusable across folders.
- For folder-specific implementation details, read that folder's `README.md` first.

Happy learning and building with LangGraph.
