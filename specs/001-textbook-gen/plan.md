# Implementation Plan: textbook-generation

**Branch**: `001-textbook-gen` | **Date**: 2025-12-05 | **Spec**: [specs/001-textbook-gen/spec.md](specs/001-textbook-gen/spec.md)
**Input**: Feature specification from `/specs/001-textbook-gen/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the implementation for the Physical AI & Humanoid Robotics — Essentials textbook, a Docusaurus-based AI-native learning resource with an integrated RAG chatbot. The technical approach involves Docusaurus for the frontend, a FastAPI backend, Qdrant for vector storage, Neon for PostgreSQL, and free-tier compatible embeddings, ensuring alignment with the project's core principles of simplicity, accuracy, minimalism, fast builds, and free-tier architecture, with RAG answers strictly confined to book content.

## Technical Context

**Language/Version**: Python 3.10+ (for FastAPI), Node.js (for Docusaurus)
**Primary Dependencies**: FastAPI, Uvicorn, Docusaurus, Qdrant client, Neon (PostgreSQL client), free-tier embedding library (e.g., Sentence Transformers)
**Storage**: Qdrant (vector embeddings), Neon (PostgreSQL for metadata/chapter content)
**Testing**: Python (pytest), JavaScript (Jest/Playwright for Docusaurus)
**Target Platform**: Local hosting (Docusaurus build for frontend, FastAPI/Qdrant/Neon for backend)
**Project Type**: Hybrid (web application with a static site generator frontend and an API backend)
**Performance Goals**: Docusaurus UI loads within 3 seconds; RAG chatbot responds within 5 seconds for basic queries; Embedding generation efficient within free-tier limits.
**Constraints**: No heavy GPU usage, minimal embeddings, free-tier services only.
**Scale/Scope**: 6 chapters initially, support for anticipated student usage (e.g., 1000 RAG queries/day).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Simplicity**: Prioritize straightforward solutions and designs. Avoid unnecessary complexity. (Plan adheres by favoring established tools and free-tier solutions).
- [x] **Accuracy**: Ensure all information presented, especially RAG answers, is factually correct and directly derivable from the book text. (Plan explicitly enforces RAG answers ONLY from book text).
- [x] **Minimalism**: Focus on essential features and content. Avoid bloat to maintain a lightweight and fast learning resource. (Plan focuses on core Docusaurus and RAG, avoiding complex features unless optional).
- [x] **Fast builds**: Design the project for quick compilation and deployment cycles. Optimize for developer and CI/CD efficiency. (Docusaurus is known for fast static builds; FastAPI is lightweight).
- [x] **Free-tier architecture**: All chosen technologies and deployment strategies must be compatible with free-tier services to minimize cost barriers. (Qdrant, Neon, Docusaurus are compatible with free-tier offerings).
- [x] **RAG answers ONLY from book text**: The RAG chatbot must strictly use the textbook content as its sole source of truth for generating answers. (Explicitly enforced in functional requirements and architecture).

## Project Structure

### Documentation (this feature)

```text
specs/001-textbook-gen/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
frontend/ # Docusaurus application
├── docs/ # Markdown files for book chapters
├── blog/
├── src/
│   ├── components/
│   ├── pages/
│   └── css/
├── static/
├── docusaurus.config.js
└── sidebar.js

backend/ # FastAPI application for RAG
├── app/
│   ├── main.py
│   ├── api/
│   ├── services/
│   └── models/
├── tests/
├── requirements.txt
└── Dockerfile # For deployment to cloud services

```

**Structure Decision**: The project will adopt a monorepo-like structure with `frontend/` for the Docusaurus application and `backend/` for the FastAPI RAG service. This clearly separates concerns and allows independent development and deployment while maintaining a unified project.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
|           |            |                                     |
