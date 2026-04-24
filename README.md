# Highwatch RAG System

A **production-ready Retrieval Augmented Generation (RAG) system** that connects to **Google Drive**, processes documents, builds a **vector search index using Gemini embeddings**, and enables **context-aware Q&A via FastAPI + Groq LLM**.

---

## 🚀 Overview

This system allows you to:
1. Sync documents from Google Drive  
2. Process and chunk content intelligently  
3. Generate embeddings and store them in FAISS  
4. Ask natural language questions over your data  

**Flow:**
Google Drive → Parsing → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer

---

## 🏗️ Architecture
connectors/ → processing/ → embedding/ → search/ → api/

- **connectors/gdrive.py**  
  Handles Google Drive OAuth, file listing, downloading, and incremental sync (`synced_ids.json`)

- **processing/parser.py**  
  Extracts text from PDFs, TXT, and Google Docs

- **processing/chunker.py**  
  Splits text into overlapping chunks for better retrieval

- **embedding/embedder.py**  
  Generates embeddings using Gemini (`gemini-embedding-001`)

- **search/vector_store.py**  
  Stores and retrieves vectors using FAISS (`faiss_store/` persistence)

- **api/main.py**  
  FastAPI service exposing endpoints for sync and querying

---

## ✨ Features

- 📂 Google Drive integration (OAuth-based)
- 🔄 **Incremental sync** (process only new/updated files)
- 📄 Multi-format support (PDF, TXT, Docs)
- ✂️ Smart chunking with overlap
- 🧠 Semantic search using FAISS
- 🤖 Context-aware Q&A using Groq LLM
- ⚡ FastAPI backend with Swagger UI
- 🐳 Docker support for deployment

---

## ⚙️ Requirements

- Python 3.11+
- Google Cloud Project with **Drive API enabled**
- OAuth credentials (`credentials.json`)

---

## 🛠️ Setup (Local)

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd highwatch-rag

