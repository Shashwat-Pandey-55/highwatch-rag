# # embedding/embedder.py
# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# import numpy as np

# load_dotenv()
# client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# def get_embedding(text: str) -> list:
#     response = client.embeddings.create(
#         input=text,
#         model='text-embedding-3-small'
#     )
#     return response.data[0].embedding

# def get_embeddings_batch(texts: list) -> list:
#     response = client.embeddings.create(
#         input=texts,
#         model='text-embedding-3-small'
#     )
#     return [item.embedding for item in response.data]






# embedding/embedder.py
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def get_embedding(text: str) -> list:
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return result.embeddings[0].values

def get_embeddings_batch(texts: list) -> list:
    embeddings = []
    for text in texts:
        result = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )
        embeddings.append(result.embeddings[0].values)
    return embeddings