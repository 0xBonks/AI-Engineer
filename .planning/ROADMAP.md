# Roadmap: AI Engineer Learning Repository

## Overview

This roadmap transforms a learner from intermediate developer to senior AI Engineer through 10 progressive phases, starting with bulletproof environment setup and Python foundations, advancing through LLM APIs and embeddings, building production RAG systems and AI agents, adding multimodal capabilities, and culminating in 5 portfolio-quality projects backed by comprehensive testing infrastructure and documentation. Each phase delivers a coherent, verifiable capability that builds toward job-ready expertise.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Environment Setup & Infrastructure** - Bulletproof development environment with validation
- [ ] **Phase 2: Python Fundamentals for AI** - Essential Python skills with async, types, error handling
- [ ] **Phase 3: AI Fundamentals & OpenAI API** - Pre-trained models, LLM concepts, OpenAI integration
- [ ] **Phase 4: Open Source AI & Safety** - Hugging Face, Ollama, security best practices
- [ ] **Phase 5: Embeddings & Vector Databases** - Semantic search foundations with vector stores
- [ ] **Phase 6: RAG Systems** - Production-ready retrieval-augmented generation
- [ ] **Phase 7: AI Agents** - MCP, tool use, multi-agent orchestration
- [ ] **Phase 8: Multimodal AI** - Vision, audio, speech integration
- [ ] **Phase 9: Testing & Validation Infrastructure** - Automated exercise validation with LLM-as-judge
- [ ] **Phase 10: Documentation & Portfolio Projects** - Learning materials and 5 portfolio projects

## Phase Details

### Phase 1: Environment Setup & Infrastructure
**Goal**: Learners can set up development environment with zero friction and have infrastructure for cost tracking and version management
**Depends on**: Nothing (first phase)
**Requirements**: ENV-01, ENV-02, ENV-03, ENV-04, ENV-05, STRUCT-01, STRUCT-02, STRUCT-03, STRUCT-04, STRUCT-05
**Success Criteria** (what must be TRUE):
  1. Learner can run environment validation script that checks Python 3.11+, all dependencies, and API connectivity
  2. Docker development environment starts with one command and includes JupyterLab, all AI libraries, and GPU support
  3. Repository structure exists with numbered module folders following consistent layout (README, notebooks/, exercises/, tests/, solutions/)
  4. .env.example template provided with clear instructions for all required API keys
  5. CI/CD pipeline runs automated tests on every commit to catch breaking dependency changes
**Plans**: See .planning/phase-01-plans.md

Plans:
- [ ] 01-01: Create Base Repository Structure
- [ ] 01-02: Create Requirements and Dependency Management
- [ ] 01-03: Create .env Template and Configuration
- [ ] 01-04: Create Docker Development Environment
- [ ] 01-05: Create Environment Validation Script
- [ ] 01-06: Create Cost Tracking Utilities
- [ ] 01-07: Create API Helper Utilities
- [ ] 01-08: Create CI/CD Pipeline
- [ ] 01-09: Create Main Repository README
- [ ] 01-10: Create Initial Module README Templates
- [ ] 01-11: Integration Testing and Documentation Review

### Phase 2: Python Fundamentals for AI
**Goal**: Learners master Python patterns essential for AI engineering (async, types, error handling)
**Depends on**: Phase 1
**Requirements**: PY-01, PY-02, PY-03, PY-04, PY-05, PY-06, PY-07
**Success Criteria** (what must be TRUE):
  1. Learner can write async code using async/await for concurrent API calls with proper error handling
  2. Learner can use type hints and Pydantic for data validation in AI applications
  3. Learner can implement production-grade logging and error handling patterns
  4. Learner can interact with REST APIs, parse JSON, and handle file I/O for common AI data formats
  5. Learner understands OOP patterns (classes, decorators, context managers) used in AI frameworks
**Plans**: TBD

Plans:
- [ ] 02-01: TBD

### Phase 3: AI Fundamentals & OpenAI API
**Goal**: Learners understand LLM concepts and can build applications using OpenAI APIs with cost optimization
**Depends on**: Phase 2
**Requirements**: AI-01, AI-02, AI-03, AI-04, AI-05, AI-06, AI-07, OAI-01, OAI-02, OAI-03, OAI-04, OAI-05, OAI-06
**Success Criteria** (what must be TRUE):
  1. Learner can explain when to use pre-trained models vs fine-tuning and the capabilities/limitations of different LLMs
  2. Learner can implement Chat Completions API with streaming, error handling, and cost tracking
  3. Learner can apply prompt engineering techniques (few-shot, chain-of-thought, system prompts) to improve outputs
  4. Learner can calculate token usage, optimize prompts for cost, and implement rate limiting
  5. Learner can use OpenAI Playground effectively for experimentation and fine-tuning workflows
**Plans**: TBD

Plans:
- [ ] 03-01: TBD

### Phase 4: Open Source AI & Safety
**Goal**: Learners can work with open source models locally and implement AI safety best practices
**Depends on**: Phase 3
**Requirements**: OSS-01, OSS-02, OSS-03, OSS-04, OSS-05, OSS-06, SAFE-01, SAFE-02, SAFE-03, SAFE-04, SAFE-05, SAFE-06
**Success Criteria** (what must be TRUE):
  1. Learner can navigate Hugging Face Hub, select appropriate models, and use Inference SDK and Transformers.js
  2. Learner can deploy and run models locally using Ollama with SDK integration
  3. Learner can identify and prevent prompt injection attacks with input validation
  4. Learner can implement OpenAI Moderation API and design input/output constraints
  5. Learner can apply security, privacy, and bias mitigation best practices in AI applications
**Plans**: TBD

Plans:
- [ ] 04-01: TBD

### Phase 5: Embeddings & Vector Databases
**Goal**: Learners can create embeddings and implement semantic search using vector databases
**Depends on**: Phase 3
**Requirements**: EMB-01, EMB-02, EMB-03, EMB-04, EMB-05, EMB-06, EMB-07
**Success Criteria** (what must be TRUE):
  1. Learner can generate embeddings using OpenAI API and Sentence Transformers
  2. Learner can set up and use Chroma vector database for storing and querying embeddings
  3. Learner can implement vector similarity search and understand cosine similarity
  4. Learner can apply appropriate chunking and indexing strategies for performance
  5. Learner can build semantic search, classification, and recommendation use cases using embeddings
**Plans**: TBD

Plans:
- [ ] 05-01: TBD

### Phase 6: RAG Systems
**Goal**: Learners can design and implement production-ready RAG pipelines with evaluation metrics
**Depends on**: Phase 5
**Requirements**: RAG-01, RAG-02, RAG-03, RAG-04, RAG-05, RAG-06, RAG-07
**Success Criteria** (what must be TRUE):
  1. Learner can explain RAG vs fine-tuning tradeoffs and when to use each approach
  2. Learner can implement document chunking strategies optimized for retrieval quality
  3. Learner can build complete RAG pipeline (chunk → embed → store → retrieve → generate)
  4. Learner can use LangChain and LlamaIndex frameworks for RAG implementation
  5. Learner can evaluate RAG system performance and optimize retrieval relevance
**Plans**: TBD

Plans:
- [ ] 06-01: TBD

### Phase 7: AI Agents
**Goal**: Learners can build AI agents with tool use, MCP implementation, and multi-agent orchestration
**Depends on**: Phase 6
**Requirements**: AGT-01, AGT-02, AGT-03, AGT-04, AGT-05, AGT-06, AGT-07
**Success Criteria** (what must be TRUE):
  1. Learner can identify appropriate use cases for AI agents and implement ReAct prompting patterns
  2. Learner can understand Model Context Protocol (MCP) components and architecture
  3. Learner can build both MCP clients and servers for agent communication
  4. Learner can implement OpenAI Functions/Tools for agent tool use
  5. Learner can design and implement multi-agent orchestration patterns
**Plans**: TBD

Plans:
- [ ] 07-01: TBD

### Phase 8: Multimodal AI
**Goal**: Learners can integrate vision, audio, and speech capabilities into AI applications
**Depends on**: Phase 3
**Requirements**: MM-01, MM-02, MM-03, MM-04, MM-05, MM-06, MM-07
**Success Criteria** (what must be TRUE):
  1. Learner can generate images using DALL-E API with prompt engineering for visual outputs
  2. Learner can implement image understanding using Vision API for analysis tasks
  3. Learner can process audio with text-to-speech and speech-to-text (Whisper API)
  4. Learner understands video understanding basics and multimodal data processing
  5. Learner can build multimodal applications using LangChain integrations
**Plans**: TBD

Plans:
- [ ] 08-01: TBD

### Phase 9: Testing & Validation Infrastructure
**Goal**: Learners have automated test validation for all exercises with clear success criteria
**Depends on**: Phase 2
**Requirements**: TEST-01, TEST-02, TEST-03, TEST-04, TEST-05, TEST-06
**Success Criteria** (what must be TRUE):
  1. Pytest framework configured with test templates for each module type
  2. Automated test runner tracks learner progress across all exercises
  3. Every exercise has clear, documented success criteria that tests validate
  4. LLM-as-judge implementation evaluates generative tasks where deterministic testing insufficient
  5. Cost estimation displayed for each exercise before execution
**Plans**: TBD

Plans:
- [ ] 09-01: TBD

### Phase 10: Documentation & Portfolio Projects
**Goal**: Comprehensive learning materials exist and learners can build 5 portfolio-quality projects
**Depends on**: Phase 6, Phase 7, Phase 8
**Requirements**: DOC-01, DOC-02, DOC-03, DOC-04, DOC-05, DOC-06, PROJ-01, PROJ-02, PROJ-03, PROJ-04, PROJ-05
**Success Criteria** (what must be TRUE):
  1. Every module has README with theory, learning objectives, and Jupyter notebooks with interactive demos
  2. All exercises have starter code with clear instructions and solution notebooks with commentary
  3. Main repository README shows curriculum overview with progress tracking visualization
  4. Learner can build production RAG system demonstrating semantic search, embeddings, vector DB, chunking, and cost optimization
  5. Learner can build multi-agent system with MCP implementation, tool use, ReAct prompting, and orchestration
  6. Learner can build multimodal application integrating vision, audio, and speech capabilities
  7. Learner can implement fine-tuning workflow with custom model training and evaluation
  8. Learner can build end-to-end production system combining multiple techniques with monitoring and deployment
**Plans**: TBD

Plans:
- [ ] 10-01: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Environment Setup & Infrastructure | 0/11 | Ready to execute | - |
| 2. Python Fundamentals for AI | 0/TBD | Not started | - |
| 3. AI Fundamentals & OpenAI API | 0/TBD | Not started | - |
| 4. Open Source AI & Safety | 0/TBD | Not started | - |
| 5. Embeddings & Vector Databases | 0/TBD | Not started | - |
| 6. RAG Systems | 0/TBD | Not started | - |
| 7. AI Agents | 0/TBD | Not started | - |
| 8. Multimodal AI | 0/TBD | Not started | - |
| 9. Testing & Validation Infrastructure | 0/TBD | Not started | - |
| 10. Documentation & Portfolio Projects | 0/TBD | Not started | - |
