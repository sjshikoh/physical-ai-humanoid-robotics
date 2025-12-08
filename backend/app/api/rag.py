from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Set
from qdrant_client import QdrantClient
from datetime import datetime
import os
from dotenv import load_dotenv

from .embeddings import get_embedding

# NEW: Google Gemini
import google.generativeai as genai

load_dotenv()
router = APIRouter()

# -----------------------
# QDRANT SETUP
# -----------------------
qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)
QDRANT_COLLECTION_NAME = "my_book"

# -----------------------
# GOOGLE GEMINI SETUP
# -----------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("⚠️ WARNING: GEMINI_API_KEY not set — RAG will return chunks only.")

# Gemini model
GEMINI_MODEL = "gemini-2.5-flash"


# -----------------------
# Request & Response Models
# -----------------------

class QueryRequest(BaseModel):
    text: str

class RAGResponse(BaseModel):
    response_text: str
    retrieved_chunks: List[str]
    source_chapters: List[str]
    timestamp: str


# -----------------------
# RAG Endpoint
# -----------------------

@router.post("/query", response_model=RAGResponse)
async def rag_query(request: QueryRequest):
    """
    Full RAG pipeline:
    - Embed query
    - Retrieve top 3 chunks from Qdrant
    - Send chunks + query to Gemini
    - Return LLM answer + chapter sources
    """
    try:
        # 1. Embed query
        query_embedding = get_embedding(request.text)

        # 2. Search Qdrant
        search_result = qdrant_client.search(
            collection_name=QDRANT_COLLECTION_NAME,
            query_vector=query_embedding,
            limit=3,
            with_payload=True
        )

        chunks = []
        source_chapters: Set[str] = set()

        for hit in search_result:
            if not hit.payload:
                continue

            if "text" in hit.payload:
                chunks.append(hit.payload["text"])

            if "chapter" in hit.payload:
                source_chapters.add(hit.payload["chapter"])

        # Edge case: No data retrieved
        if not chunks:
            return RAGResponse(
                response_text="No relevant sections found in the book.",
                retrieved_chunks=[],
                source_chapters=[],
                timestamp=datetime.utcnow().isoformat() + "Z"
            )

        # ------------------------------------------
        # 3. Build prompt for Gemini LLM
        # ------------------------------------------

        context_text = "\n\n".join(chunks)

        prompt = f"""
You are a helpful textbook assistant. You answer ONLY based on the provided context.

USER QUESTION:
{request.text}

CONTEXT TEXT (from the textbook):
{context_text}

RULES:
- If the answer is not in the context, reply: "The book does not contain the answer."
- Do NOT hallucinate.
- Keep answers short, factual, and based ONLY on the context.
"""

        # ------------------------------------------
        # 4. Generate Answer (Gemini)
        # ------------------------------------------

        if GEMINI_API_KEY:
            model = genai.GenerativeModel(GEMINI_MODEL)
            llm_response = model.generate_content(prompt)
            answer_text = llm_response.text
        else:
            answer_text = "Gemini API key missing. Returning raw chunks only."

        # 5. Timestamp
        timestamp = datetime.utcnow().isoformat(timespec="milliseconds") + "Z"

        return RAGResponse(
            response_text=answer_text,
            retrieved_chunks=chunks,
            source_chapters=sorted(list(source_chapters)),
            timestamp=timestamp
        )

    except Exception as e:
        print("RAG ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))

