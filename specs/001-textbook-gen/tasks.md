# Tasks: textbook-generation

**Input**: Design documents from `/specs/001-textbook-gen/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 [P] Initialize Docusaurus project in frontend/
- [x] T002 [P] Initialize FastAPI project in backend/
- [x] T003 Configure basic Docker Compose for Qdrant and Neon in docker-compose.yml
- [x] T004 Create and configure .env files for frontend/ and backend/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Define Qdrant client connection and basic operations in backend/app/services/qdrant_client.py
- [x] T006 Define Neon (PostgreSQL) client connection and basic operations in backend/app/services/neon_client.py
- [x] T007 Setup FastAPI application structure in backend/app/main.py, backend/app/api/, backend/app/services/, backend/app/models/
- [x] T008 Configure Docusaurus for auto sidebar generation in frontend/docusaurus.config.js and frontend/sidebar.js

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Read Textbook Content (Priority: P1) 🎯 MVP

**Goal**: Enable users to read textbook content in a clean, navigable Docusaurus UI.

**Independent Test**: Navigate through all 6 chapters, verify content display, and check auto-sidebar functionality. Delivers fundamental educational value.

### Implementation for User Story 1

- [x] T009 [US1] Create Introduction to Physical AI chapter in frontend/docs/1-intro-physical-ai.md
- [x] T010 [P] [US1] Create Basics of Humanoid Robotics chapter in frontend/docs/2-basics-humanoid-robotics.md
- [x] T011 [P] [US1] Create ROS 2 Fundamentals chapter in frontend/docs/3-ros2-fundamentals.md
- [x] T012 [P] [US1] Create Digital Twin Simulation chapter in frontend/docs/4-digital-twin-simulation.md
- [x] T013 [P] [US1] Create Vision-Language-Action Systems chapter in frontend/docs/5-vision-language-action.md
- [x] T014 [P] [US1] Create Capstone: Simple AI-Robot Pipeline chapter in frontend/docs/6-capstone-ai-robot-pipeline.md
- [x] T015 [US1] Verify Docusaurus navigation and auto sidebar functionality for all chapters in frontend/docusaurus.config.js

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Ask AI about Textbook Content (Priority: P1)

**Goal**: Provide an interactive RAG chatbot that answers questions based solely on the textbook.

**Independent Test**: Ask various questions to the chatbot, verify accuracy, source attribution (if applicable), and contextual query functionality. Delivers an enhanced interactive learning experience.

### Implementation for User Story 2

- [x] T016 [US2] Implement FastAPI endpoint /chat (submitQuery) in backend/app/api/rag.py
- [x] T017 [US2] Implement FastAPI endpoint /contextual-chat (submitContextualQuery) in backend/app/api/rag.py
- [ ] T018 [US2] Develop RAG service for embedding generation in backend/app/services/rag_service.py
- [ ] T019 [US2] Develop RAG service for vector search (Qdrant) in backend/app/services/rag_service.py
- [ ] T020 [US2] Develop RAG service for response synthesis in backend/app/services/rag_service.py
- [ ] T021 [US2] Integrate RAG chatbot UI component into Docusaurus frontend/src/components/Chatbot.js
- [ ] T022 [US2] Implement text selection and contextual query initiation in Docusaurus frontend/src/theme/DocItem/Content/index.js (or similar)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Optional: Translate Content to Urdu (Priority: P2)

**Goal**: (Optional) Allow users to view textbook content in Urdu for improved accessibility.

**Independent Test**: Enable Urdu translation and verify accurate translation of sample textbook content. Delivers localized content value.

### Implementation for User Story 3

- [ ] T023 [US3] Develop a translation service/middleware (e.g., using a free-tier translation API or static translations) in backend/app/services/translation_service.py or frontend/src/utils/i18n.js
- [ ] T024 [US3] Integrate Urdu translation toggle and display into Docusaurus UI in frontend/src/theme/Navbar/Content/index.js (or similar)

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Optional: Personalize Learning (Priority: P2)

**Goal**: (Optional) Provide a personalized learning experience (e.g., adaptive content, progress tracking).

**Independent Test**: Create a user profile and observe personalized content delivery or tracking features (if implemented). Delivers a customized learning path.

### Implementation for User Story 4

- [ ] T025 [US4] Develop basic personalization logic (e.g., tracking chapter completion) in backend/app/services/personalization_service.py
- [ ] T026 [US4] Integrate personalization features (e.g., progress display) into Docusaurus UI in frontend/src/components/UserProfile.js (or similar)

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T027 Refine quickstart.md with complete Docker Compose instructions and environment variable guidance
- [ ] T028 Add comprehensive unit and integration tests for backend services in backend/tests/
- [ ] T029 Add E2E tests for Docusaurus UI and RAG chatbot interaction in frontend/tests/
- [ ] T030 Implement content ingestion script (process markdown, generate embeddings, store in Qdrant/Neon) in backend/scripts/ingest.py
- [ ] T031 Implement CI/CD for GitHub Pages deployment (Docusaurus) in .github/workflows/deploy.yml
- [ ] T032 Create Dockerfile for backend services in backend/Dockerfile

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Tasks T009-T014 in User Story 1 can run in parallel
- Tasks T023-T024 in User Story 3 can run in parallel
- Tasks T025-T026 in User Story 4 can run in parallel

---

## Parallel Example: User Story 1

```bash
# All chapter creation tasks for User Story 1 can run in parallel:
Task: "Create Introduction to Physical AI chapter in frontend/docs/1-intro-physical-ai.md"
Task: "Create Basics of Humanoid Robotics chapter in frontend/docs/2-basics-humanoid-robotics.md"
Task: "Create ROS 2 Fundamentals chapter in frontend/docs/3-ros2-fundamentals.md"
Task: "Create Digital Twin Simulation chapter in frontend/docs/4-digital-twin-simulation.md"
Task: "Create Vision-Language-Action Systems chapter in frontend/docs/5-vision-language-action.md"
Task: "Create Capstone: Simple AI-Robot Pipeline chapter in frontend/docs/6-capstone-ai-robot-pipeline.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1
4.  **STOP and VALIDATE**: Test User Story 1 independently
5.  Deploy/demo if ready

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3.  Add User Story 2 → Test independently → Deploy/Demo
4.  Add User Story 3 → Test independently → Deploy/Demo
5.  Add User Story 4 → Test independently → Deploy/Demo
6.  Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together
2.  Once Foundational is done:
    -   Developer A: User Story 1
    -   Developer B: User Story 2
    -   Developer C: User Story 3
    -   Developer D: User Story 4
3.  Stories complete and integrate independently

---

## Notes

-   [P] tasks = different files, no dependencies
-   [Story] label maps task to specific user story for traceability
-   Each user story should be independently completable and testable
-   Verify tests fail before implementing
-   Commit after each task or logical group
-   Stop at any checkpoint to validate story independently
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
