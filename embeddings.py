from typing import List
from sentence_transformers import SentenceTransformer

model_name = "sentence-transformers/all-MiniLM-L6-v2"
model = SentenceTransformer(model_name)

def get_embedding(text: str) -> List[float]:
    """
    Generates a numerical vector (embedding) for a given text.
    """
    return model.encode(text).tolist()

def get_vector_size() -> int:
    """
    Returns the dimension of the embedding vectors.
    """
    return model.get_sentence_embedding_dimension()
    
    
    
    
# -------------------------
# Manual Test Runner
# -------------------------
if __name__ == "__main__":
    if model is None:
        print("❌ Embedding model FAILED to load.")
    else:
        print("✅ Embedding model loaded successfully!")

        test_text = "This is a test sentence."
        embedding = get_embedding(test_text)

        print("\nSample Text:", test_text)
        print("Embedding (first 5 dims):", embedding[:5])
        print("Vector size:", get_vector_size())
