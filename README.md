# Iranian AI Assistant MVP

A production-oriented Persian-first AI assistant starter project.

## What this is
This is **not** a fake AI demo. It is a working MVP skeleton for:

- Persian chat interface
- FastAPI backend
- Pluggable LLM provider
- Local/offline LLM option via Ollama
- Document-based RAG-ready structure
- GitHub-ready repository

## Architecture

```text
User -> Streamlit UI -> FastAPI API -> LLM Provider
                              |
                              -> Future RAG / Vector DB
```

## Quick Start

### 1. Install Python
Python 3.11+ recommended.

### 2. Create virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Ollama locally
Install Ollama, then pull a model:

```bash
ollama pull llama3.1:8b
```

### 5. Run API

```bash
uvicorn app.main:app --reload --port 8000
```

### 6. Run UI

```bash
streamlit run app/ui.py
```

## Environment Variables
Copy `.env.example` to `.env`.

```bash
cp .env.example .env
```


## Zero-cost mode

This repository is designed to run with no paid API:

- Local model: Ollama
- Local backend: FastAPI
- Local UI: Streamlit
- Free source hosting: GitHub
- Free CI for public repository: GitHub Actions

Windows one-command setup:

```powershell
.\setup_windows.ps1
```

Run locally:

```powershell
.\run_local.ps1
```

## Local Knowledge Base

Put Persian Markdown files in `knowledge_base/`. The app will search them with a tiny zero-cost keyword retriever before calling the model.

## Roadmap

- [x] Persian-first assistant skeleton
- [x] FastAPI backend
- [x] Streamlit frontend
- [x] Local LLM provider using Ollama
- [ ] RAG document ingestion
- [ ] Authentication
- [ ] Admin dashboard
- [ ] Telegram bot connector
- [ ] Docker deployment
- [ ] Persian evaluation dataset

## License
MIT
