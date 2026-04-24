# Highwatch RAG System

A RAG (Retrieval Augmented Generation) system that answers questions from your Google Drive documents.

## Architecture
connectors/ → processing/ → embedding/ → search/ → api/

- **connectors/gdrive.py** - Google Drive OAuth integration
- **processing/parser.py** - PDF and text extraction
- **processing/chunker.py** - Text chunking with overlap
- **embedding/embedder.py** - Gemini embeddings
- **search/vector_store.py** - FAISS vector storage
- **api/main.py** - FastAPI endpoints

## Setup
1. Clone this repo
2. Run: `pip install -r requirements.txt`
3. Add `credentials.json` from Google Cloud Console
4. Create `.env` with your API keys:

GEMINI_API_KEY=your-gemini-key
GROQ_API_KEY=your-groq-key

5. Run: `uvicorn api.main:app --reload --port 8000`

## API Endpoints
- `POST /sync-drive` — fetch and index Google Drive docs
- `POST /ask` — ask a question
- `GET /health` — check indexed chunk count
- `POST /sync-drive` — fetch and index Google Drive docs (incremental - skips already synced files)

## Sample Queries
- "What is this document about?"
- "What are the main topics covered?"
- "Summarize the key points"

## Tech Stack
- FastAPI + Python
- Google Drive API (OAuth)
- Gemini Embeddings
- FAISS vector store
- Groq LLM (llama-3.3-70b)
