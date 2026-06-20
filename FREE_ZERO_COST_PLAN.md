# Zero-Cost Build Plan

## Principle
No paid API. No rented server. No paid GPU.

## What runs for free

1. Local AI model via Ollama on your own laptop/PC.
2. FastAPI backend locally.
3. Streamlit UI locally.
4. GitHub repository for source code.
5. GitHub Actions for syntax/tests on public repository.
6. Optional public demo on Hugging Face Spaces CPU Basic.

## What will NOT be free

1. Training a foundation LLM from scratch.
2. High-speed GPU inference for many users.
3. Always-on production hosting with persistent storage.
4. Large document search at enterprise scale.

## Free MVP Architecture

```text
Your PC
 ├─ Ollama local model
 ├─ FastAPI backend
 └─ Streamlit UI

GitHub
 ├─ Source code repository
 └─ CI test workflow

Optional Hugging Face Space
 └─ Lightweight UI demo / portfolio demo
```

## Recommended free models

- `llama3.1:8b` if your system has enough RAM.
- `qwen2.5:7b` good general multilingual option.
- `gemma2:2b` lighter, weaker, faster.

## Persian-first improvement path

1. Create product UI and API.
2. Add Persian system prompt and rules.
3. Add local document RAG.
4. Collect Persian Q/A examples.
5. Evaluate answers manually.
6. Later fine-tune a small open model if you get free GPU access.

## Non-negotiable rule

Do not call it a trained Iranian foundation model. Call it a Persian-first local AI assistant until you actually train or fine-tune a model.
