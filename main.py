from fastapi import FastAPI
from typing import List
from sentence_transformers import CrossEncoder
import numpy as np

# Load the small re-ranker model from mixedbread.ai
model = CrossEncoder("mixedbread-ai/mxbai-rerank-xsmall-v1")

app = FastAPI(title="BreadRanker",
        description="A small reranker service for use with RAG workflows. It uses the mixedbread.ai reranker model.",
        version="1.0",
        contact={
            "name": "Pat Wendorf",
            "email": "pat.wendorf@mongodb.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/license/mit/",
    })

@app.get("/")
async def root():
    return {"message": "Reank some docs! See /docs for more info."}

@app.post("/rerank/")
async def rerank(query: str, documents: List[str], top_k: int):
    results = model.rank(query, documents, return_documents=True, top_k=top_k)
    # Clean up those float32's
    serializable_list = [{k: float(v) if isinstance(v, np.float32) else v for k, v in d.items()} for d in results]
    return {"query": query, "results": serializable_list}