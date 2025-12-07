// frontend/src/pages/rag-chat.jsx

import React, { useState } from 'react';
import Layout from '@theme/Layout';
import { queryRAG } from '../services/rag'; // Adjust path if necessary

function RagChat() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;

    setLoading(true);
    setError(null);
    setResponse(null); // Clear previous response

    try {
      const result = await queryRAG(question);
      setResponse(result);
    } catch (err) {
      setError(err.message || 'An unexpected error occurred.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout title="RAG Chatbot" description="Chat with your Physical AI & Humanoid Robotics textbook.">
      <header className="hero hero--primary">
        <div className="container">
          <h1 className="hero__title">Physical AI Book Chat</h1>
          <p className="hero__subtitle">Ask questions about the textbook!</p>
        </div>
      </header>
      <main className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset-2">
            <form onSubmit={handleSubmit} className="margin-bottom--lg">
              <div className="margin-bottom--md">
                <input
                  type="text"
                  className="input input--lg"
                  placeholder="Ask a question about the book..."
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  disabled={loading}
                  style={{ width: '100%', padding: '10px' }}
                />
              </div>
              <button type="submit" className="button button--primary button--lg" disabled={loading}>
                {loading ? 'Thinking...' : 'Get Answer'}
              </button>
            </form>

            {error && (
              <div className="alert alert--danger" role="alert">
                <strong>Error:</strong> {error}
              </div>
            )}

            {response && (
              <div className="card margin-top--lg">
                <div className="card__header">
                  <h3>AI Response</h3>
                </div>
                <div className="card__body">
                  <p>{response.response_text}</p>
                  {response.source_chapters && response.source_chapters.length > 0 && (
                    <div className="margin-top--md">
                      <strong>Source Chapters:</strong>
                      <ul>
                        {response.source_chapters.map((chapter, index) => (
                          <li key={index}>{chapter}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                  <small className="text--right d-block">
                    Timestamp: {new Date(response.timestamp).toLocaleString()}
                  </small>
                </div>
              </div>
            )}
          </div>
        </div>
      </main>
    </Layout>
  );
}

export default RagChat;
