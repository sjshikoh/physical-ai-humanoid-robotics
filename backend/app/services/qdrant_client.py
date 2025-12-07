import os
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", "")

def get_qdrant_client() -> QdrantClient:
    """Initializes and returns a Qdrant client."""
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    return client

def ensure_collection_exists(client: QdrantClient, collection_name: str, vector_size: int = 768, distance: Distance = Distance.COSINE):
    """Ensures that a Qdrant collection with the given parameters exists."""
    if not client.collection_exists(collection_name=collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=distance),
        )
        print(f"Collection '{collection_name}' created with vector size {vector_size} and distance {distance.value}.")
    else:
        print(f"Collection '{collection_name}' already exists.")

