# 🤖 LLM-Based Review Analysis Workflow

## 📋 Overview

This project implements a **conditional workflow** using LangGraph to analyze customer reviews, determine sentiment, and generate appropriate responses. It demonstrates how to build intelligent, branching workflows that adapt based on AI-driven analysis.

## ✨ Features

- 🎯 **Sentiment Analysis**: Automatically detects positive or negative sentiment in reviews
- 🔀 **Conditional Routing**: Different processing paths based on sentiment
- 🔍 **Diagnosis System**: For negative reviews, analyzes issue type, tone, and urgency
- 💬 **Smart Responses**: Generates contextual responses for both positive and negative feedback
- 🖥️ **Streamlit UI**: Interactive web interface for testing the workflow

## 🏗️ Workflow Architecture

```
START → Find Sentiment → Check Sentiment
                              ├─ Positive → Positive Response → END
                              └─ Negative → Run Diagnosis → Negative Response → END
```

### Workflow Steps:

1. **Find Sentiment** 📊: Analyzes the review using LLM with structured output
2. **Check Sentiment** 🔀: Conditional router that determines the next step
3. **Positive Response** 😊: Generates a thank-you message for positive reviews
4. **Run Diagnosis** 🔍: For negative reviews, identifies issue type, tone, and urgency
5. **Negative Response** 😞: Creates an empathetic apology based on diagnosis

## 📁 File Structure

### Core Workflow Files

#### `main.py` 🚀
Main Streamlit application that:
- Builds the LangGraph workflow
- Provides the web interface
- Displays analysis results with sentiment, diagnosis, and suggested responses

#### `review_state_schema.py` 📝
Defines the `ReviewState` class that tracks:
- LLM models (base and structured)
- Customer review text
- Sentiment classification
- Diagnosis details
- Generated response

### Node Functions

#### `find_sentiment.py` 🎯
First node that analyzes review sentiment using structured LLM output.

#### `check_sentiment.py` 🔀
Conditional edge function that routes to:
- `positive_response` for positive reviews
- `run_diagnosis` for negative reviews

#### `positive_response.py` ✅
Generates thank-you messages and encourages customers to share their experience.

#### `run_diagnosis.py` 🩺
Analyzes negative reviews to extract:
- **Issue Type**: ux, bug, battery, or other
- **Tone**: angry, sad, or neutral
- **Urgency**: low, medium, or high

#### `negative_response.py` ❌
Creates personalized apology responses based on diagnosis findings.

### Configuration Files

#### `model.py` 🧠
Loads the Ollama LLM model (`qwen3-next:80b-cloud`).

#### `output_schema.py` 📊
Defines `SentimentSchema` with positive/negative classification.

#### `diagonsis_output_schema.py` 🔬
Defines `DiagnosisOutput` schema with issue_type, tone, and urgency fields.

## 🚀 How to Run

### Prerequisites
- Python environment with dependencies installed
- Ollama running with `qwen3-next:80b-cloud` model

### Run the Application

```bash
streamlit run main.py
```

### Usage
1. Enter a customer review in the text input
2. Click "Analyze Review"
3. View the sentiment, diagnosis (if negative), and suggested response

## 💡 Example

**Positive Review:**
```
"Great product! Works perfectly and exceeded my expectations."
```
- Sentiment: Positive 😊
- Response: Thank-you message encouraging sharing

**Negative Review:**
```
"The app keeps crashing and draining my battery. Very frustrating!"
```
- Sentiment: Negative 😞
- Diagnosis:
  - Issue Type: bug
  - Tone: angry
  - Urgency: high
- Response: Personalized apology addressing the specific issues

## 🎓 Learning Objectives

This workflow demonstrates:
- ✅ Building conditional workflows with LangGraph
- ✅ Using structured outputs from LLMs
- ✅ Implementing dynamic routing based on AI analysis
- ✅ Combining multiple LLM calls in a stateful workflow
- ✅ Creating interactive AI applications with Streamlit

## 🔗 Dependencies

- `langgraph`: Workflow orchestration
- `langchain-ollama`: LLM integration
- `pydantic`: Schema validation
- `streamlit`: Web interface

---

*Part of the LangGraph Course - Conditional Workflows Module*
