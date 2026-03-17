# 🐘 SF 25: Short-Term Memory With PostgreSQL

## 📌 Overview

This folder demonstrates storing short-term memory/checkpoints using PostgreSQL for more durable state handling.

## 📂 Files

### 🧠 Core Files

- `main.py`: Main script for PostgreSQL-backed memory flow.
- `main.ipynb`: Notebook walkthrough.

### 🗄️ Database Setup

- `docker-compose.yml`: Local PostgreSQL service definition.

## ▶️ How To Run

### Start PostgreSQL

```bash
docker compose up -d
```

### Run Python script

```bash
python main.py
```

### Run notebook

Open `main.ipynb` in VS Code and execute cells.
