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
