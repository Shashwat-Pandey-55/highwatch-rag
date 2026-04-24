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

```text
connectors/ → processing/ → embedding/ → search/ → api/
```

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
- 🔄 Incremental sync to skip already processed files
- 📄 Support for multiple file types:
  - PDF
  - TXT
- ✂️ Intelligent chunking with overlap for better retrieval
- 🧠 Semantic search using FAISS
- 🔍 Retrieval-Augmented Generation (RAG) workflow
- 🤖 Context-aware question answering using Groq LLM
- 🐳 Docker support for containerized deployment

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
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Google Credentials

Place `credentials.json` in the project root (from Google Cloud Console)

### 4. Create Environment File

```env
GEMINI_API_KEY=your-gemini-key
GROQ_API_KEY=your-groq-key
```

### 5. Run Server

```bash
uvicorn api.main:app --reload --port 8000
```

### 6. Open API Docs

- http://localhost:8000/docs

---

⚙️ System Components (Detailed)

### 📄 Document Processing

- Parses PDF, TXT, and Google Docs
- Extracts clean text content
- Handles different file formats uniformly
- Prepares data for chunking

---

### ✂️ Chunking

- Splits text into smaller chunks
- Maintains overlap between chunks
- Preserves context across boundaries
- Improves retrieval quality

---

### 🧠 Embedding Generation

- Uses Gemini (`gemini-embedding-001`)
- Converts text chunks into vector representations
- Ensures semantic similarity search
- Stores embeddings for retrieval

---

### 🔍 Vector Search (FAISS)

- Stores embeddings in FAISS index
- Supports fast nearest-neighbor search
- Retrieves top-k relevant chunks
- Persists index locally (`faiss_store/`)

---

### 🤖 Query & Generation (RAG Pipeline)

**Endpoint:** `POST /ask`

- Accepts user query
- Converts query into embedding
- Retrieves relevant chunks from FAISS
- Sends context + query to Groq LLM
- Returns final generated answer

## 🔄 Incremental Sync (Key Feature)

### Endpoint: `POST /sync-drive`

- Fetches files from Google Drive
- Loads `synced_ids.json`
- Skips already processed files
- Processes only new files
- Updates sync state

### Force Full Re-sync

```bash
rm synced_ids.json
rm -rf faiss_store/
```

---

## 📡 API Endpoints

| Method |    Endpoint     |               Description             |
|  ---   |       ---       |                  ---                  |
|  POST  |   `/sync-drive` | Sync + index Google Drive documents   |  
|  POST  |      `/ask`     | Ask questions based on indexed data   |
|  GET   |     `/health`   | Check system health + indexed chunks  |

---

## 💬 Example Queries

- "What is this document about?"
- "Summarize the key points"
- "What are the main topics covered?"

---

## 🐳 Docker (Deployment Ready)

### Build Image

```bash
docker build -t highwatch-rag .
```

### Run Container

```bash
docker run --rm -p 8000:8000 \
  --env-file .env \
  -v $(pwd)/token.json:/app/token.json \
  -v $(pwd)/credentials.json:/app/credentials.json \
  highwatch-rag
```

### Access

- API: http://localhost:8000
- Docs: http://localhost:8000/docs

### Notes

- Port mapping: `8000 → 8000`
- Mounting `token.json` avoids repeated OAuth login

---

## 🧠 Tech Stack

- Backend: FastAPI (Python)
- LLM: Groq (`llama-3.3-70b-versatile`)
- Embeddings: Gemini (`gemini-embedding-001`)
- Vector DB: FAISS
- Storage: Local filesystem
- Integration: Google Drive API (OAuth)

---

## 📌 Design Decisions

- **FAISS over cloud vector DB** → faster local development, no external dependency
- **Incremental sync** → avoids redundant processing, improves efficiency
- **Chunk overlap** → improves retrieval quality for long documents
- **Separation of concerns** → modular architecture for scalability

---

## 🚧 Future Improvements

- Add metadata filtering (file type, date, owner)
- Support more file formats (DOCX, HTML)
- Add streaming responses for `/ask`
- Integrate UI (React frontend)
- Replace FAISS with scalable vector DB (Pinecone / Weaviate)

---

## 🧪 Demo Flow (Quick Start)

1. Call `/sync-drive` → index documents  
2. Call `/ask` → query knowledge base  
3. System retrieves relevant chunks → sends to LLM → returns answer
