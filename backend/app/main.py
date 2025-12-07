import os
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from .api import rag

app = FastAPI()

origins = [
    "http://localhost:3000",  # Docusaurus frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # allows POST, OPTIONS, GET, etc.
    allow_headers=["*"],
)

# Main API router
api_router = APIRouter()

@api_router.get("/health")
async def health_check():
    return {"status": "ok"}

@api_router.get("/")
async def read_root():
    return {"message": "Hello from FastAPI backend!"}

# Include RAG API router
api_router.include_router(rag.router, prefix="/rag", tags=["RAG Chatbot"])

app.include_router(api_router)
