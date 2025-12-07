from qdrant_client import QdrantClient, models
import os
from dotenv import load_dotenv

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

# Initialize Qdrant client
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

COLLECTION_NAME = "my_book"
VECTOR_SIZE = 384 # This will be updated based on the embedding model output dimension

def create_qdrant_collection():
    """
    Creates the Qdrant collection if it doesn't already exist.
    """
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=VECTOR_SIZE, distance=models.Distance.COSINE),
    )
    print(f"Collection '{COLLECTION_NAME}' created with vector size {VECTOR_SIZE} and cosine similarity.")

if __name__ == "__main__":
    create_qdrant_collection()
