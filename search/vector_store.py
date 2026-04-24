# search/vector_store.py
import faiss
import numpy as np
import pickle, os
from typing import List, Dict

STORE_PATH = 'faiss_store'

class VectorStore:
    def __init__(self):
        self.index = None
        self.metadata: List[Dict] = []
        # self.dimension = 1536  # text-embedding-3-small
        self.dimension = 3072

    def build(self, embeddings: List[list], metadata: List[Dict]):
        vectors = np.array(embeddings, dtype='float32')
        faiss.normalize_L2(vectors)
        self.index = faiss.IndexFlatIP(self.dimension)
        self.index.add(vectors)
        self.metadata = metadata

    def add(self, embeddings: List[list], metadata: List[Dict]):
        vectors = np.array(embeddings, dtype='float32')
        faiss.normalize_L2(vectors)
        if self.index is None:
            self.index = faiss.IndexFlatIP(self.dimension)
        self.index.add(vectors)
        self.metadata.extend(metadata)

    def search(self, query_embedding: list, top_k: int = 5) -> List[Dict]:
        if self.index is None:
            return []
        vec = np.array([query_embedding], dtype='float32')
        faiss.normalize_L2(vec)
        scores, indices = self.index.search(vec, top_k)
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx >= 0:
                result = dict(self.metadata[idx])
                result['score'] = float(score)
                results.append(result)
        return results

    def save(self):
        os.makedirs(STORE_PATH, exist_ok=True)
        faiss.write_index(self.index, f'{STORE_PATH}/index.faiss')
        with open(f'{STORE_PATH}/metadata.pkl', 'wb') as f:
            pickle.dump(self.metadata, f)

    def load(self):
        idx_path = f'{STORE_PATH}/index.faiss'
        meta_path = f'{STORE_PATH}/metadata.pkl'
        if os.path.exists(idx_path) and os.path.exists(meta_path):
            self.index = faiss.read_index(idx_path)
            with open(meta_path, 'rb') as f:
                self.metadata = pickle.load(f)
            return True
        return False

vector_store = VectorStore()
vector_store.load()