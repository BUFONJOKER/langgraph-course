# 🚀 LangGraph Course

Welcome to the LangGraph Course repository! This project explores sequential workflows and advanced orchestration using LangGraph framework.

---

## 📁 Project Structure

### 🏠 Root Directory

The root directory contains essential project configuration and entry point files.

#### 📄 Files

- **`main.py`** 📝: Main entry point script for the project
- **`main.ipynb`** 📓: Jupyter Notebook for interactive exploration and testing
- **`pyproject.toml`** ⚙️: Python project configuration and dependency management
- **`README.md`** 📖: Project documentation (this file)
- **`uv.lock`** 🔒: Dependency lock file for reproducible environments
- **`.python-version`** 🐍: Python version specification for the project
- **`.env`** 🔐: Environment variables configuration (not tracked in git)
- **`.gitignore`** 🚫: Git ignore patterns for version control
- **`.git/`** 📚: Git repository metadata and history

#### 🗂️ Directories

- **`f_01_sequential_workflows/`** ⚙️: Main module containing sequential workflow implementations

---

## 📦 f_01_sequential_workflows

This folder contains the core implementation of sequential workflows using LangGraph.

### 📄 Root Module Files

- **`__init__.py`** 💫: Python package initialization file

### 📂 Subfolders

#### 1️⃣ sf_01_simple_workflow

A simple workflow demonstrating basic sequential operations with BMI (Body Mass Index) calculation.

**📄 Files:**

- **`main.py`** 🎯: Main workflow orchestration script
- **`bmi_calculate.py`** 🧮: BMI calculation logic
- **`bmi_state_class.py`** 📊: State management class for BMI workflow
- **`label_bmi.py`** 🏷️: BMI classification and labeling logic
- **`graph.png`** 🖼️: Visual representation of the workflow graph

---

#### 2️⃣ sf_02_llm_based_workflows

LLM-based sequential workflows demonstrating question-answering systems with different model backends.

**📄 Files:**

- **`main.py`** 🎯: Main LLM workflow script
- **`main.ipynb`** 📓: Interactive Jupyter Notebook for LLM workflows
- **`llm_question_answer.py`** 🤖: Question-answering implementation
- **`llm_state_class.py`** 📊: State management class for LLM workflows
- **`model_huggingface.py`** 🤗: Hugging Face model integration
- **`model_ollama.py`** 🦙: Ollama model integration
- **`__init__.py`** 💫: Package initialization file

---

#### 3️⃣ sf_03_prompt_chaining

Advanced prompt chaining workflows for blog generation with outline evaluation.

**📄 Files:**

- **`main.py`** 🎯: Main prompt chaining orchestration script
- **`main.ipynb`** 📓: Interactive Jupyter Notebook for prompt chaining
- **`blog_state.py`** 📝: State management class for blog generation workflow
- **`generate_outline.py`** 📋: Outline generation logic
- **`generate_blog.py`** ✍️: Blog post generation logic
- **`evaluation.py`** ⭐: Evaluation and validation of generated content
- **`model.py`** 🔌: Model configuration and initialization
- **`__init__.py`** 💫: Package initialization file

---

## 🎯 Key Features

### ✨ Sequential Workflows
- **Simple Workflows**: Basic workflow operations with BMI calculations
- **LLM Integration**: Integration with multiple LLM backends (Hugging Face, Ollama)
- **Prompt Chaining**: Advanced multi-step prompt chains for complex tasks like blog generation

### 🔄 State Management
- Structured state classes for each workflow module
- Type-safe state transitions
- Efficient state handling across workflow steps

### 🧠 Model Support
- Hugging Face models integration
- Ollama local model support
- Flexible model configuration

---

## 🛠️ Development Setup

### Requirements
- Python 3.x
- Virtual environment (`.venv/`)
- Dependencies specified in `pyproject.toml`

### Quick Start
1. Activate the virtual environment: `.venv/Scripts/Activate.ps1`
2. Run the main script: `python main.py`
3. Or explore with Jupyter: `jupyter notebook main.ipynb`

---

## 📚 Workflow Modules

### Module 1: Simple Workflow
Calculate and classify BMI values through a sequential workflow.

### Module 2: LLM-Based Workflow
Ask questions to LLMs and receive answers from different model backends.

### Module 3: Prompt Chaining
Generate complete blog posts by chaining multiple prompts together with evaluation.

---

## 🔧 Configuration

- **`pyproject.toml`**: Manage project dependencies and metadata
- **`.env`**: Set environment variables and API keys
- **`.python-version`**: Specify Python version requirement

---

## 📔 Interactive Notebooks

Explore the workflows interactively using Jupyter Notebooks:
- `main.ipynb` (Root level)
- `sf_02_llm_based_workflows/main.ipynb`
- `sf_03_prompt_chaining/main.ipynb`

---

## 🚀 Getting Started

To get started with this LangGraph course:

1. **Set up environment**: Install dependencies from `pyproject.toml`
2. **Explore examples**: Start with `sf_01_simple_workflow` for basic concepts
3. **Try LLM integration**: Move to `sf_02_llm_based_workflows` for model usage
4. **Master prompt chaining**: Finish with `sf_03_prompt_chaining` for advanced techniques

---

**Happy Learning! 🎓**
