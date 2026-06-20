# Architecture

## MVP Goal
Build a Persian-first AI assistant that can run locally and later become a full Iranian AI platform.

## Core Components

1. UI: Streamlit Persian chat interface
2. API: FastAPI service
3. LLM Provider: Ollama local model
4. Future RAG: document ingestion + vector database
5. Deployment: Docker/GitHub Actions later

## Why not train from scratch first?
Training a foundation model from scratch requires large datasets, GPU clusters, evaluation pipelines, safety filters, and millions of dollars in compute. The correct first step is a product-grade wrapper around existing open models, then fine-tuning or distillation after usage data exists.
