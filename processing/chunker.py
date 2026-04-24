# processing/chunker.py
from typing import List

def chunk_text(text: str, chunk_size: int = 500,
               overlap: int = 100) -> List[str]:
    """Split text into overlapping chunks by word count.
    overlap ensures context isn't lost at chunk boundaries."""
    words = text.split()
    if not words:
        return []
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = ' '.join(words[start:end])
        if chunk.strip():
            chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

        