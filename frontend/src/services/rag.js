// frontend/src/services/rag.js

const RAG_ENDPOINT = 'http://localhost:8000/rag/query';

/**
 * Sends a user query to the RAG backend and returns the response.
 * @param {string} text The user's query text.
 * @returns {Promise<{response_text: string, source_chapters: string[], timestamp: string}>} The RAG response.
 */
export async function queryRAG(text) {
  try {
    const response = await fetch(RAG_ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Failed to fetch RAG response');
    }

    return await response.json();
  } catch (error) {
    console.error('Error querying RAG backend:', error);
    throw error;
  }
}
