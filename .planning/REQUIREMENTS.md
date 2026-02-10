# Requirements: AI Engineer Learning Repository

**Defined:** 2026-02-10
**Core Value:** By completing this repository, learners have both the knowledge and demonstrable portfolio to apply for senior AI Engineering roles.

## v1 Requirements

Requirements for initial release. Each maps to roadmap phases.

### Environment Setup

- [ ] **ENV-01**: Docker-based development environment with all dependencies
- [ ] **ENV-02**: Requirements.txt with pinned versions for all AI libraries
- [ ] **ENV-03**: Environment validation script that checks Python version, dependencies, and API connectivity
- [ ] **ENV-04**: Clear installation instructions for Docker setup
- [ ] **ENV-05**: .env.example template for API keys and configuration

### Python Fundamentals

- [ ] **PY-01**: Async programming module (async/await, concurrency for API calls)
- [ ] **PY-02**: Type safety module (type hints, Pydantic validation)
- [ ] **PY-03**: Error handling and logging patterns module
- [ ] **PY-04**: Environment and package management module
- [ ] **PY-05**: API interaction patterns module (requests, JSON handling)
- [ ] **PY-06**: Data handling module (file I/O, JSON, CSV formats)
- [ ] **PY-07**: OOP and advanced patterns module (classes, decorators, context managers)

### Pre-trained Models & Fundamentals

- [ ] **AI-01**: Understanding pre-trained models module (benefits, limitations, usage)
- [ ] **AI-02**: Common AI terminology module (AI vs AGI, LLMs, inference, training)
- [ ] **AI-03**: Introduction to embeddings and vector concepts
- [ ] **AI-04**: AI agents fundamentals module
- [ ] **AI-05**: RAG concepts overview module
- [ ] **AI-06**: OpenAI models capabilities and limitations
- [ ] **AI-07**: Other AI models comparison (Claude, Gemini, Hugging Face, etc.)

### OpenAI API

- [ ] **OAI-01**: Chat Completions API implementation with examples
- [ ] **OAI-02**: Prompt engineering techniques module
- [ ] **OAI-03**: Token management and counting
- [ ] **OAI-04**: Pricing optimization strategies
- [ ] **OAI-05**: OpenAI Playground exercises
- [ ] **OAI-06**: Fine-tuning workflow module

### Open Source AI

- [ ] **OSS-01**: Open vs closed source models comparison
- [ ] **OSS-02**: Hugging Face Hub navigation and model selection
- [ ] **OSS-03**: Inference SDK usage examples
- [ ] **OSS-04**: Transformers.js implementation
- [ ] **OSS-05**: Ollama local deployment setup
- [ ] **OSS-06**: Ollama SDK integration exercises

### AI Safety & Ethics

- [ ] **SAFE-01**: Prompt injection attack prevention techniques
- [ ] **SAFE-02**: Security and privacy best practices module
- [ ] **SAFE-03**: Bias and fairness considerations
- [ ] **SAFE-04**: OpenAI Moderation API integration
- [ ] **SAFE-05**: Adversarial testing examples
- [ ] **SAFE-06**: Input/output constraints implementation

### Embeddings & Vector Databases

- [ ] **EMB-01**: Creating embeddings with OpenAI API
- [ ] **EMB-02**: Sentence Transformers implementation
- [ ] **EMB-03**: Chroma vector database setup and usage
- [ ] **EMB-04**: Vector search and similarity matching exercises
- [ ] **EMB-05**: Indexing strategies and optimization
- [ ] **EMB-06**: Semantic search use case implementation
- [ ] **EMB-07**: Classification and recommendation examples

### RAG Systems

- [ ] **RAG-01**: RAG vs fine-tuning decision framework
- [ ] **RAG-02**: Document chunking strategies implementation
- [ ] **RAG-03**: Embedding pipeline for RAG
- [ ] **RAG-04**: Retrieval process optimization
- [ ] **RAG-05**: Generation with context integration
- [ ] **RAG-06**: LangChain RAG implementation
- [ ] **RAG-07**: LlamaIndex RAG implementation

### AI Agents

- [ ] **AGT-01**: Agent use cases and patterns
- [ ] **AGT-02**: ReAct prompting implementation
- [ ] **AGT-03**: Model Context Protocol (MCP) components
- [ ] **AGT-04**: Building MCP client
- [ ] **AGT-05**: Building MCP server
- [ ] **AGT-06**: OpenAI Functions/Tools implementation
- [ ] **AGT-07**: Multi-agent orchestration patterns

### Multimodal AI

- [ ] **MM-01**: Image generation with DALL-E API
- [ ] **MM-02**: Image understanding with Vision API
- [ ] **MM-03**: Audio processing fundamentals
- [ ] **MM-04**: Text-to-speech implementation
- [ ] **MM-05**: Speech-to-text with Whisper API
- [ ] **MM-06**: Video understanding basics
- [ ] **MM-07**: Multimodal application with LangChain

### Testing & Validation Infrastructure

- [ ] **TEST-01**: Pytest setup for exercise validation
- [ ] **TEST-02**: Test templates for each module type
- [ ] **TEST-03**: Automated test runner for progress tracking
- [ ] **TEST-04**: Clear success criteria documentation per exercise
- [ ] **TEST-05**: LLM-as-judge implementation for generative tasks
- [ ] **TEST-06**: Cost estimation per exercise

### Documentation & Learning Materials

- [ ] **DOC-01**: README for each module with theory and objectives
- [ ] **DOC-02**: Jupyter notebooks with interactive demos
- [ ] **DOC-03**: Exercise starter code with clear instructions
- [ ] **DOC-04**: Solution notebooks with commentary
- [ ] **DOC-05**: Main repository README with curriculum overview
- [ ] **DOC-06**: Progress tracking in main README

### Repository Structure

- [ ] **STRUCT-01**: Numbered module folders (01-, 02-, etc.)
- [ ] **STRUCT-02**: Consistent folder structure per module (README, notebooks/, exercises/, tests/, solutions/)
- [ ] **STRUCT-03**: Shared utilities folder for common code
- [ ] **STRUCT-04**: Docker configuration files
- [ ] **STRUCT-05**: CI/CD pipeline for automated testing

### Portfolio Projects (5 Major Projects)

- [ ] **PROJ-01**: Production RAG system (semantic search, embeddings, vector DB, chunking strategies, cost optimization)
- [ ] **PROJ-02**: Multi-agent system (MCP implementation, tool use, ReAct prompting, agent orchestration)
- [ ] **PROJ-03**: Multimodal application (vision + audio + speech integration, multi-input processing)
- [ ] **PROJ-04**: Fine-tuning & optimization (custom model training, performance tuning, evaluation metrics)
- [ ] **PROJ-05**: End-to-end production system (combines multiple techniques, monitoring, deployment, error handling)

## v2 Requirements

Deferred to future release. Tracked but not in current roadmap.

### Alternative Setup Paths

- **ENV-07**: Google Colab setup instructions and notebooks
- **ENV-08**: Local setup without Docker (native installation)
- **ENV-09**: One-command setup scripts for all platforms

### Community Features

- **COMM-01**: Discord server setup and moderation
- **COMM-02**: GitHub Discussions integration
- **COMM-03**: Community contribution guidelines
- **COMM-04**: Peer review system for solutions

### Enhanced Learning Materials

- **DOC-07**: Video walkthroughs for complex topics
- **DOC-08**: Interactive quizzes and assessments
- **DOC-09**: Cheat sheets and quick reference guides

### Gamification & Progress

- **PROG-01**: Completion badges and certificates
- **PROG-02**: Visual progress dashboard (web UI)
- **PROG-03**: Leaderboard and achievements

### Advanced Tooling

- **TOOL-01**: Cost tracking dashboard
- **TOOL-02**: Automated dependency updates
- **TOOL-03**: Performance benchmarking tools
- **TOOL-04**: AI code review integration

## Out of Scope

Explicitly excluded. Documented to prevent scope creep.

| Feature | Reason |
|---------|--------|
| Web-based IDE | Focus is on local development skills; learners should use their own IDEs |
| Paid certification | Value is in portfolio projects, not certificates; keep free and accessible |
| Mobile app | Desktop development is industry standard for AI engineering |
| Live instructor sessions | Self-paced learning model; async support via documentation |
| Job placement service | Focus on skill-building; job search is separate concern |
| Custom learning platform | GitHub repository is sufficient; avoid building custom infrastructure |
| Data science theory | Focus is practical AI engineering, not academic ML theory |
| TensorFlow/PyTorch from scratch | Use high-level APIs; deep framework knowledge not required for AI engineering |
| Frontend UI development | Portfolio projects focus on AI/backend; frontend is out of scope |
| Kubernetes deployment | Learner already has K8s experience; focus on AI concepts not infrastructure |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| ENV-01 | Phase 1 | Pending |
| ENV-02 | Phase 1 | Pending |
| ENV-03 | Phase 1 | Pending |
| ENV-04 | Phase 1 | Pending |
| ENV-05 | Phase 1 | Pending |
| PY-01 | Phase 2 | Pending |
| PY-02 | Phase 2 | Pending |
| PY-03 | Phase 2 | Pending |
| PY-04 | Phase 2 | Pending |
| PY-05 | Phase 2 | Pending |
| PY-06 | Phase 2 | Pending |
| PY-07 | Phase 2 | Pending |
| AI-01 | Phase 3 | Pending |
| AI-02 | Phase 3 | Pending |
| AI-03 | Phase 3 | Pending |
| AI-04 | Phase 3 | Pending |
| AI-05 | Phase 3 | Pending |
| AI-06 | Phase 3 | Pending |
| AI-07 | Phase 3 | Pending |
| OAI-01 | Phase 3 | Pending |
| OAI-02 | Phase 3 | Pending |
| OAI-03 | Phase 3 | Pending |
| OAI-04 | Phase 3 | Pending |
| OAI-05 | Phase 3 | Pending |
| OAI-06 | Phase 3 | Pending |
| OSS-01 | Phase 4 | Pending |
| OSS-02 | Phase 4 | Pending |
| OSS-03 | Phase 4 | Pending |
| OSS-04 | Phase 4 | Pending |
| OSS-05 | Phase 4 | Pending |
| OSS-06 | Phase 4 | Pending |
| SAFE-01 | Phase 4 | Pending |
| SAFE-02 | Phase 4 | Pending |
| SAFE-03 | Phase 4 | Pending |
| SAFE-04 | Phase 4 | Pending |
| SAFE-05 | Phase 4 | Pending |
| SAFE-06 | Phase 4 | Pending |
| EMB-01 | Phase 5 | Pending |
| EMB-02 | Phase 5 | Pending |
| EMB-03 | Phase 5 | Pending |
| EMB-04 | Phase 5 | Pending |
| EMB-05 | Phase 5 | Pending |
| EMB-06 | Phase 5 | Pending |
| EMB-07 | Phase 5 | Pending |
| RAG-01 | Phase 6 | Pending |
| RAG-02 | Phase 6 | Pending |
| RAG-03 | Phase 6 | Pending |
| RAG-04 | Phase 6 | Pending |
| RAG-05 | Phase 6 | Pending |
| RAG-06 | Phase 6 | Pending |
| RAG-07 | Phase 6 | Pending |
| AGT-01 | Phase 7 | Pending |
| AGT-02 | Phase 7 | Pending |
| AGT-03 | Phase 7 | Pending |
| AGT-04 | Phase 7 | Pending |
| AGT-05 | Phase 7 | Pending |
| AGT-06 | Phase 7 | Pending |
| AGT-07 | Phase 7 | Pending |
| MM-01 | Phase 8 | Pending |
| MM-02 | Phase 8 | Pending |
| MM-03 | Phase 8 | Pending |
| MM-04 | Phase 8 | Pending |
| MM-05 | Phase 8 | Pending |
| MM-06 | Phase 8 | Pending |
| MM-07 | Phase 8 | Pending |
| TEST-01 | Phase 9 | Pending |
| TEST-02 | Phase 9 | Pending |
| TEST-03 | Phase 9 | Pending |
| TEST-04 | Phase 9 | Pending |
| TEST-05 | Phase 9 | Pending |
| TEST-06 | Phase 9 | Pending |
| DOC-01 | Phase 10 | Pending |
| DOC-02 | Phase 10 | Pending |
| DOC-03 | Phase 10 | Pending |
| DOC-04 | Phase 10 | Pending |
| DOC-05 | Phase 10 | Pending |
| DOC-06 | Phase 10 | Pending |
| STRUCT-01 | Phase 1 | Pending |
| STRUCT-02 | Phase 1 | Pending |
| STRUCT-03 | Phase 1 | Pending |
| STRUCT-04 | Phase 1 | Pending |
| STRUCT-05 | Phase 1 | Pending |
| PROJ-01 | Phase 10 | Pending |
| PROJ-02 | Phase 10 | Pending |
| PROJ-03 | Phase 10 | Pending |
| PROJ-04 | Phase 10 | Pending |
| PROJ-05 | Phase 10 | Pending |

**Coverage:**
- v1 requirements: 76 total
- Mapped to phases: 76 ✓
- Unmapped: 0 ✓

---
*Requirements defined: 2026-02-10*
*Last updated: 2026-02-10 after initial definition*
