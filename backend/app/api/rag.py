from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Set
from qdrant_client import QdrantClient
from datetime import datetime
import os
import sys
from dotenv import load_dotenv
# Add backend root path so we can import embeddings.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from embeddings import get_embedding



load_dotenv()
router = APIRouter()

# Qdrant setup

qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL"), 
    api_key=os.getenv("QDRANT_API_KEY")
)
QDRANT_COLLECTION_NAME = "my_book"


# -----------------------
# Request & Response Models
# -----------------------

class QueryRequest(BaseModel):
    text: str

class RAGResponse(BaseModel):
    response_text: str
    source_chapters: List[str]
    timestamp: str


# -----------------------
# RAG Query Endpoint
# -----------------------

@router.post("/query", response_model=RAGResponse)
async def rag_query(request: QueryRequest):

    """
    RAG endpoint: searches Qdrant using the query text and returns
    the best matching chunks + their chapter names.
    """
    try:
        # 1. Embed the query
        query_embedding = get_embedding(request.text)

        # 2. Search collection (top 3 chunks)
        search_result = qdrant_client.search(
            collection_name=QDRANT_COLLECTION_NAME,
            query_vector=query_embedding,
            limit=3,
            with_payload=True
        )

        response_text_chunks = []
        source_chapters: Set[str] = set()

        # 3. Extract payload fields YOU ACTUALLY STORED
        for hit in search_result:
            if not hit.payload:
                continue

            # The chunk text
            if "text" in hit.payload:
                response_text_chunks.append(hit.payload["text"])

            # Chapter file name (e.g. 5-vision-language-action.md)
            if "chapter" in hit.payload:
                source_chapters.add(hit.payload["chapter"])

        # Combine retrieved chunk text
        combined_response_text = " ".join(response_text_chunks).strip()

        # Generate timestamp
        current_timestamp = datetime.utcnow().isoformat(timespec='milliseconds') + "Z"

        return RAGResponse(
            response_text=combined_response_text,
            source_chapters=sorted(list(source_chapters)),
            timestamp=current_timestamp
        )

    except Exception as e:
        print(f"RAG ERROR: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

