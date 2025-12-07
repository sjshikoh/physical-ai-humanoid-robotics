<!--
Sync Impact Report:
Version change: 0.0.0 → 1.0.0 (MAJOR: Initial constitution generated)
Modified principles:
  - [PROJECT_NAME] → Physical AI & Humanoid Robotics — Essentials
  - [PRINCIPLE_1_NAME] → Simplicity
  - [PRINCIPLE_2_NAME] → Accuracy
  - [PRINCIPLE_3_NAME] → Minimalism
  - [PRINCIPLE_4_NAME] → Fast builds
  - [PRINCIPLE_5_NAME] → Free-tier architecture
  - [PRINCIPLE_6_NAME] → RAG answers ONLY from book text
Added sections:
  - Constraints
  - Key Features & Success Criteria
Removed sections:
  - None
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - .specify/templates/commands/*.md: ✅ updated
  - README.md: ✅ updated
Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics — Essentials Constitution

## Core Principles

### Simplicity
Prioritize straightforward solutions and designs. Avoid unnecessary complexity.

### Accuracy
Ensure all information presented, especially RAG answers, is factually correct and directly derivable from the book text.

### Minimalism
Focus on essential features and content. Avoid bloat to maintain a lightweight and fast learning resource.

### Fast builds
Design the project for quick compilation and deployment cycles. Optimize for developer and CI/CD efficiency.

### Free-tier architecture
All chosen technologies and deployment strategies must be compatible with free-tier services to minimize cost barriers.

### RAG answers ONLY from book text
The RAG chatbot must strictly use the textbook content as its sole source of truth for generating answers.

## Constraints

The project must adhere to the following constraints:
- No heavy GPU usage
- Minimal embeddings

## Key Features & Success Criteria

The project will deliver the following key features and meet these success criteria:

### Key Features
- Docusaurus textbook
- RAG chatbot (Qdrant + Neon + FastAPI)
- Select-text → Ask AI
- Optional Urdu / Personalize features

### Success Criteria
- Build success
- Accurate chatbot
- Clean UI
- Smooth GitHub Pages deployment

## Governance

This Constitution supersedes all other practices. Amendments require thorough documentation, explicit approval from stakeholders, and a clear migration plan for any breaking changes. All pull requests and code reviews must verify compliance with these principles. Justification is required for any increase in system complexity.

**Version**: 1.0.0 | **Ratified**: 2025-12-05 | **Last Amended**: 2025-12-05
