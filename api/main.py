# # api/main.py
# import os
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from openai import OpenAI
# from dotenv import load_dotenv

# from connectors.gdrive import get_drive_service, list_files, download_file
# from processing.parser import extract_text
# from processing.chunker import chunk_text
# from embedding.embedder import get_embeddings_batch, get_embedding
# from search.vector_store import vector_store

# load_dotenv()
# app = FastAPI(title='Highwatch RAG API')
# client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# class QueryRequest(BaseModel):
#     query: str

# @app.post('/sync-drive')
# def sync_drive():
#     service = get_drive_service()
#     files = list_files(service)
#     if not files:
#         return {'message': 'No files found', 'synced': 0}

#     all_chunks, all_meta = [], []
#     for file in files:
#         try:
#             content = download_file(service, file['id'], file['mimeType'])
#             text = extract_text(content, file['mimeType'], file['name'])
#             if not text.strip():
#                 continue
#             chunks = chunk_text(text)
#             for i, chunk in enumerate(chunks):
#                 all_chunks.append(chunk)
#                 all_meta.append({
#                     'doc_id': file['id'],
#                     'file_name': file['name'],
#                     'source': 'gdrive',
#                     'chunk_index': i,
#                     'chunk_text': chunk
#                 })
#             print(f'Processed: {file["name"]} -> {len(chunks)} chunks')
#         except Exception as e:
#             print(f'Error with {file["name"]}: {e}')

#     # Batch embed (more efficient + cheaper)
#     BATCH = 100
#     all_embeddings = []
#     for i in range(0, len(all_chunks), BATCH):
#         batch = all_chunks[i:i+BATCH]
#         embs = get_embeddings_batch(batch)
#         all_embeddings.extend(embs)
#         print(f'Embedded batch {i//BATCH + 1}')

#     vector_store.add(all_embeddings, all_meta)
#     vector_store.save()
#     return {'message': 'Sync complete', 'synced': len(files),
#             'chunks': len(all_chunks)}

# @app.post('/ask')
# def ask(request: QueryRequest):
#     query_emb = get_embedding(request.query)
#     results = vector_store.search(query_emb, top_k=5)
#     if not results:
#         raise HTTPException(status_code=404,
#                            detail='No documents synced yet. Call /sync-drive first.')

#     context = '\n\n'.join([r['chunk_text'] for r in results])
#     sources = list(set([r['file_name'] for r in results]))

#     response = client.chat.completions.create(
#         model='gpt-3.5-turbo',
#         messages=[
#             {'role': 'system', 'content': 'Answer based only on the context provided.'},
#             {'role': 'user', 'content': f'Context:\n{context}\n\nQuestion: {request.query}'}
#         ]
#     )
#     return {
#         'answer': response.choices[0].message.content,
#         'sources': sources
#     }

# @app.get('/health')
# def health():
#     return {'status': 'ok',
#             'chunks_indexed': len(vector_store.metadata)}















# api/main.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from groq import Groq
from dotenv import load_dotenv

from connectors.gdrive import get_drive_service, list_files, download_file
from processing.parser import extract_text
from processing.chunker import chunk_text
from embedding.embedder import get_embeddings_batch, get_embedding
from search.vector_store import vector_store

load_dotenv()
gemini_client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
groq_client = Groq(api_key=os.getenv('GROQ_API_KEY'))
app = FastAPI(title='Highwatch RAG API')

class QueryRequest(BaseModel):
    query: str

@app.post('/sync-drive')
def sync_drive():
    service = get_drive_service()
    files = list_files(service)
    if not files:
        return {'message': 'No files found', 'synced': 0}

    all_chunks, all_meta = [], []
    for file in files:
        try:
            content = download_file(service, file['id'], file['mimeType'])
            text = extract_text(content, file['mimeType'], file['name'])
            if not text.strip():
                continue
            chunks = chunk_text(text)
            for i, chunk in enumerate(chunks):
                all_chunks.append(chunk)
                all_meta.append({
                    'doc_id': file['id'],
                    'file_name': file['name'],
                    'source': 'gdrive',
                    'chunk_index': i,
                    'chunk_text': chunk
                })
            print(f'Processed: {file["name"]} -> {len(chunks)} chunks')
        except Exception as e:
            print(f'Error with {file["name"]}: {e}')

    BATCH = 100
    all_embeddings = []
    for i in range(0, len(all_chunks), BATCH):
        batch = all_chunks[i:i+BATCH]
        embs = get_embeddings_batch(batch)
        all_embeddings.extend(embs)
        print(f'Embedded batch {i//BATCH + 1}')

    vector_store.add(all_embeddings, all_meta)
    vector_store.save()
    return {'message': 'Sync complete', 'synced': len(files),
            'chunks': len(all_chunks)}

@app.post('/ask')
def ask(request: QueryRequest):
    query_emb = get_embedding(request.query)
    results = vector_store.search(query_emb, top_k=5)
    if not results:
        raise HTTPException(status_code=404,
                           detail='No documents synced yet. Call /sync-drive first.')

    context = '\n\n'.join([r['chunk_text'] for r in results])
    sources = list(set([r['file_name'] for r in results]))

    response = groq_client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {'role': 'system', 'content': 'Answer based only on the context provided.'},
            {'role': 'user', 'content': f'Context:\n{context}\n\nQuestion: {request.query}'}
        ]
    )
    return {
        'answer': response.choices[0].message.content,
        'sources': sources
    }

@app.get('/health')
def health():
    return {'status': 'ok',
            'chunks_indexed': len(vector_store.metadata)}