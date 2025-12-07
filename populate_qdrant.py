import os
import uuid
from init_qdrant import client, COLLECTION_NAME, create_qdrant_collection
from embeddings import get_embedding

# Folder where your book markdown files live
BOOK_FOLDER = "frontend/docs"

# Optional: chunk size (split long paragraphs for better RAG search)
CHUNK_SIZE = 500  # characters per chunk

def read_md_files(folder_path):
    """Recursively read all .md/.mdx files and return list of (filepath, content)"""
    files_content = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith((".md", ".mdx")):
                full_path = os.path.join(root, file)
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    files_content.append((full_path, content))
    return files_content

def chunk_text(text, chunk_size=CHUNK_SIZE):
    """Split text into smaller chunks"""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def populate_qdrant():
    # Ensure collection exists (recreates if needed)
    create_qdrant_collection()
    
    # Read all markdown files
    files = read_md_files(BOOK_FOLDER)
    
    total_points = 0

    for filepath, content in files:
        chunks = chunk_text(content)
        for chunk in chunks:
            vector = get_embedding(chunk)
            point_id = str(uuid.uuid4())  # ✅ UUID-safe ID
            payload = {
                "chapter": os.path.basename(filepath),
                "filepath": filepath,
                "text": chunk
            }
            client.upsert(
                collection_name=COLLECTION_NAME,
                points=[{
                    "id": point_id,
                    "vector": vector,
                    "payload": payload
                }]
            )
            total_points += 1

    print(f"Inserted {total_points} points into Qdrant collection '{COLLECTION_NAME}'.")

if __name__ == "__main__":
    populate_qdrant()

