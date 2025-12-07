# Quickstart Guide: Physical AI & Humanoid Robotics Textbook

**Feature Branch**: `001-textbook-gen`
**Created**: 2025-12-05
**Plan**: [specs/001-textbook-gen/plan.md](specs/001-textbook-gen/plan.md)

This guide will help you set up and run the Physical AI & Humanoid Robotics textbook project locally, including both the Docusaurus frontend and the FastAPI RAG chatbot backend.

## Prerequisites

Ensure you have the following installed:

*   **Python 3.10+**
*   **Node.js LTS (Long Term Support)**
*   **npm** (Node Package Manager, usually comes with Node.js)
*   **Docker Desktop** (for running Qdrant and Neon locally)

## 1. Setup Backend Services (Qdrant & Neon)

This project uses Qdrant for vector search and Neon (PostgreSQL) for metadata storage. You can run these services locally using Docker.

### 1.1. Start Qdrant and Neon with Docker Compose (To be defined in the future)

Currently, you will need to start Qdrant and Neon services separately or by a docker-compose file (which will be provided in the future).

**For Qdrant**: (Future `docker-compose.yml` will handle this, manual for now)

```bash
docker run -p 6333:6333 -p 6334:6334 -v $(pwd)/qdrant_data:/qdrant/storage qdrant/qdrant
```

**For Neon (PostgreSQL)**: You can sign up for a free Neon account and get connection details. For local development, you could also run a PostgreSQL container.

```bash
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```

Remember to configure your backend `backend/.env` file with the correct connection strings for Qdrant and Neon.

## 2. Setup Backend (FastAPI)

Navigate to the `backend/` directory and set up the FastAPI application.

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` directory with your environment variables (e.g., Qdrant host, Neon connection string, embedding model path).

Run the FastAPI application:

```bash
uvicorn app.main:app --reload
```

The backend API will be available at `http://127.0.0.1:8000` (or as configured).

## 3. Setup Frontend (Docusaurus)

Navigate to the `frontend/` directory and set up the Docusaurus application.

```bash
cd frontend
npm install
```

Start the Docusaurus development server:

```bash
npm start
```

The Docusaurus textbook will be available at `http://localhost:3000`.

## 4. Initializing RAG Content (Future Step)

To make the RAG chatbot functional, you will need to ingest the textbook content into Qdrant. This will involve:

1.  Processing Markdown files (`frontend/docs/`).
2.  Generating embeddings for text chunks.
3.  Storing embeddings and metadata in Qdrant.

An ingestion script or process will be provided in a later phase to automate this.
