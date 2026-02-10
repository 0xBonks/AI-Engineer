# Project Research Summary

**Project:** AI Engineering Learning Platform
**Domain:** Technical Education / AI/ML Learning Repository
**Researched:** 2026-02-10
**Confidence:** HIGH

## Executive Summary

This project aims to build a comprehensive AI Engineering learning platform, following the successful model of repositories like Microsoft's AI-For-Beginners, mlabonne's LLM Course, and Anthropic's Courses. Research shows that successful AI learning platforms share core DNA: **code-first teaching** (not theory-first), **executable examples** in every lesson, **automated validation** for immediate feedback, and **portfolio-building emphasis** for job-readiness.

The recommended approach uses Python 3.11 with modern tooling (uv/Poetry, pytest, Docker), focuses on OpenAI/Anthropic APIs with LangChain for orchestration, and organizes content in **numbered modules** (01-python-fundamentals → 02-llms → 03-embeddings → 04-rag → 05-agents → 06-multimodal) with consistent structure: theory (README) → demo (notebook) → practice (exercises with tests). Each module should be completable in 3-7 days, with portfolio projects after every 2-3 modules to consolidate learning.

The critical risks are: (1) **API deprecation and breaking changes** — AI APIs evolve rapidly and will break exercises within months without version pinning and automated testing, (2) **API cost explosions** — learners can unknowingly spend $50-200 without cost warnings and guardrails, and (3) **environment setup hell** — Python/dependency issues cause 30%+ abandonment before lesson 1. Mitigation requires: exact version pinning with weekly automated tests, cost estimates on every exercise with budget-conscious model choices, and multiple setup paths (Colab, Docker, local) with validation scripts.

## Key Findings

### Recommended Stack

The AI engineering education domain has converged on a stable, modern stack centered around Python 3.11 (best balance of performance and library compatibility), OpenAI/Anthropic APIs for LLM access, and LangChain for agent orchestration. Critical decision: use **uv** for dependency management (10-100x faster than pip, perfect for teaching iteration speed in 2026) with exact version pinning for reproducibility.

**Core technologies:**
- **Python 3.11+**: Industry standard for AI/ML with 10-60% performance improvements over 3.10 — maximum library compatibility
- **JupyterLab 4.x**: Latest notebook interface with modular design — essential for exploratory learning and interactive demos
- **OpenAI Python SDK 1.x**: Primary LLM provider with simple API and excellent docs — all learners need API access
- **LangChain 0.3+**: Agent orchestration and RAG pipelines — mature ecosystem with provider-specific packages
- **Chroma 0.5+**: Vector database for RAG — simplest setup, runs in-process, perfect for learning
- **pytest 8.x + deepeval 1.x**: Testing framework plus AI-specific evaluation — enables automated validation
- **Docker 25.x+**: Development environment isolation — critical for reproducibility with complex AI dependencies
- **uv 0.5+ or Poetry 1.8+**: Dependency management — uv recommended for 2026 (Rust-based speed), Poetry as mature fallback

**Critical version requirements:**
- OpenAI SDK must be 1.x+ (breaking changes from 0.28.x, all new docs use v1 API)
- LangChain must be 0.3+ (major API restructure, provider packages split out)
- Python 3.11 recommended over 3.12 (better AI library ecosystem compatibility in Feb 2026)

**Avoid:**
- TensorFlow/Keras (declining, PyTorch dominant)
- pip alone (no lock files, dependency hell for learners)
- Python 3.8 or older (end of life, missing performance improvements)

### Expected Features

Successful AI learning platforms follow a proven pattern of **table stakes** (features users expect) and **differentiators** (what sets excellent platforms apart). The landscape shows learners expect hands-on executable code, not theory-only content.

**Must have (table stakes):**
- **Executable Jupyter notebooks** — industry standard; must run in Colab, local Jupyter, or cloud workbench
- **Progressive curriculum structure** — prevents cognitive overload; recommend: Fundamentals → Core → Advanced → Projects
- **Code examples with explanations** — every concept needs runnable code with inline comments explaining "why"
- **Exercise/challenge problems** — active learning beats passive reading; mix of guided and open-ended
- **Setup/environment instructions** — first 30 minutes determines completion rate; friction = abandonment
- **Clear learning objectives** — each lesson needs measurable outcomes ("after this, you'll be able to...")
- **Topic-based organization** — numbered folders (01-, 02-) make progression obvious and reduce overwhelm
- **Real datasets** — toy data teaches toy solutions; use Llama datasets, OpenAI API data, real scraped data

**Should have (competitive differentiators):**
- **Automated test validation** — immediate feedback loop with pytest; learners know they're correct
- **Portfolio projects** — 3-5 substantial projects that deploy real models for job-readiness proof
- **Progressive complexity tracking** — visual progress (bars, checkmarks) creates momentum and completion drive
- **Production-ready patterns** — bridge tutorial to professional work: error handling, logging, monitoring, deployment
- **Community forum/Discord** — peer learning accelerates understanding and reduces abandonment
- **Solution notebooks** — provided after initial attempt to prevent frustration-abandonment
- **Cost-conscious design** — free/low-cost GPU access determines who can complete; design for Colab free tier
- **CLI tools for progress** — terminal workflows feel professional: `ai-engineer status`, `ai-engineer test`

**Defer (v2+ / not essential for launch):**
- Multiple framework support (start PyTorch-only, add alternatives later)
- Spaced repetition quizzes (nice-to-have, not MVP critical)
- Video walkthroughs for every topic (time-intensive, focus on complex topics only)
- Leaderboards (potential distraction from learning)
- Mobile app (web-first sufficient)

### Architecture Approach

The standard architecture for AI learning repositories is a **topic-based module structure** with sequential learning paths. Research across Microsoft AI-For-Beginners (106k stars), mlabonne LLM Course (75k stars), Anthropic Courses, and LLM Zoomcamp shows clear consensus on numbered module organization.

**Major components:**
1. **Module Folders (01-python, 02-llms, etc.)** — organize content by topic in numbered directories; forces sequential order and makes dependencies clear
2. **README.md per module** — lesson content, theory, explanations with learning objectives and prerequisites
3. **Notebooks (.ipynb)** — interactive demos with executable cells; one concept per notebook (<100 cells)
4. **Tests (pytest or notebook-based)** — validate learner solutions automatically; tests provide immediate feedback
5. **Exercises** — practice challenges separated from lessons; clean separation between teaching and doing
6. **Solutions** — reference implementations in separate folder to prevent accidental spoilers
7. **Projects (root-level)** — portfolio-worthy capstone work; substantial, integrates multiple modules
8. **Utils (shared code)** — common functions reduce duplication and teach code reuse patterns

**Key architectural patterns:**
- **Progressive Complexity (Spiral Learning)**: Each module builds on previous, introducing one new concept while reinforcing earlier topics
- **Theory → Demo → Practice (TDP Loop)**: Every module follows: README theory → Notebook demo → Exercise challenge → Test validation
- **Test-Driven Learning**: Exercises come with automated tests providing immediate correctness feedback
- **Portfolio Project Milestones**: 3-5 substantial projects after every 2-3 modules to consolidate skills
- **Notebook-First, Then Refactor**: Teach in notebooks (exploration), then refactor to Python modules (production patterns)

**Recommended structure:**
```
ai-engineering-repo/
├── 00-setup/                    # Environment setup with validation
├── 01-python-fundamentals/      # Foundation
├── 02-llms-basics/              # First AI module
├── 03-embeddings-vectors/       # Vector concepts
├── 04-rag-systems/              # RAG implementation
├── 05-agents/                   # Agents and tools
├── 06-multimodal/              # Vision/audio
├── projects/                    # Portfolio work
│   ├── 01-chatbot/
│   ├── 02-rag-application/
│   └── 03-agent-system/
├── utils/                       # Shared utilities
└── docs/                        # Additional documentation
```

### Critical Pitfalls

Research identified 7 critical pitfalls that cause learning platform failures. The top 3 are preventable with upfront investment in infrastructure.

1. **Outdated API dependencies and breaking changes** — AI APIs change rapidly; OpenAI v0.28→v1.0 broke all old code. Without exact version pinning (`openai==1.12.0` not `openai>=1.0`) and weekly automated tests, exercises break within 3-6 months, causing abandonment and reputation damage. Prevention: Pin exact versions, build automated CI/CD test suite, maintain "Known Issues" document, use wrapper functions for easy central updates.

2. **API cost explosions** — Learners can unknowingly spend $50-200 running exercises that call GPT-4 in loops or process large documents. Authors with company API keys don't notice costs during testing. Prevention: Display estimated cost on every exercise (e.g., "~$0.50 to complete"), use cost-efficient models by default (gpt-4o-mini not gpt-4), implement max_tokens limits, provide local model alternatives, document total expected course cost upfront ($20-50).

3. **Environment setup hell** — Learners spend hours fighting Python versions, dependency conflicts, API key setup before writing any code. 30%+ abandon before lesson 1. Prevention: Provide setup validator script (`setup_validator.py` checks Python version, dependencies, API keys), offer multiple paths (Colab zero-setup, Docker reproducibility, local with detailed guide), test on fresh Windows/Mac/Linux VMs, include troubleshooting guide with screenshots.

4. **Exercises that don't teach concepts** — Focus on API mechanics ("call this endpoint") without teaching underlying AI concepts (embeddings, attention, prompting strategies). Learners copy-paste code but can't apply knowledge to novel problems. Prevention: Structure as Concept → Example → Guided Exercise → Independent Challenge; include "why does this work?" explanations; add conceptual quizzes before hands-on; require implementation without full starter code.

5. **Poor learning progression and difficulty spikes** — Difficulty jumps dramatically ("Hello World" → "Build RAG system"). Prevention: Assign difficulty levels (Beginner/Intermediate/Advanced), test curriculum with target audience, build scaffolded exercises (guided → semi-guided → independent), add checkpoint projects before new topics.

6. **Exercises without clear success criteria** — Learners don't know if their solution is correct. AI outputs are non-deterministic, making testing challenging. Prevention: Build pytest suites for every exercise, define clear metrics ("retrieval accuracy >80%", "cost <$0.50"), use LLM-as-judge for subjective evaluation, provide "Good/Acceptable/Needs Improvement" example outputs.

7. **Portfolio projects that don't demonstrate real skills** — Toy examples (chatbot that says "hello") won't impress hiring managers. Prevention: Design projects solving real business problems with constraints (cost, latency, reliability), include production concerns (error handling, rate limiting, monitoring), require documentation and deployment, integrate multiple concepts, have industry professionals review project specs.

## Implications for Roadmap

Based on research, suggested phase structure follows the proven pattern of **Foundation → Core AI → Advanced → Production**. This ordering is based on:
- Dependency analysis from ARCHITECTURE.md (Python before LLMs before RAG before Agents)
- Feature prioritization from FEATURES.md (table stakes first, differentiators progressively)
- Pitfall prevention from PITFALLS.md (environment setup before any content)

### Phase 0: Environment Setup & Prerequisites (Week 1)
**Rationale:** Environment setup must be bulletproof before learners attempt anything. Research shows 30%+ abandon if first 30 minutes are frustrating. This is the #1 critical pitfall.

**Delivers:** 
- Multiple setup paths: Colab (zero-setup), Docker (reproducible), local (detailed guide)
- Setup validator script checking Python version, dependencies, API keys, GPU availability
- Troubleshooting guide with screenshots for Windows/Mac/Linux
- "Environment test" notebook proving setup works

**Addresses:**
- **Table stakes feature**: Setup/environment instructions
- **Critical pitfall #3**: Environment setup hell

**Avoids:** Learner abandonment before lesson 1; establishes testing culture early

---

### Phase 1: Foundation Setup & Infrastructure (Weeks 1-2)
**Rationale:** Before creating any content, establish version management, testing infrastructure, and cost controls. Research shows these are Day 1 requirements, not "we'll add it later."

**Delivers:**
- Exact version pinning strategy (requirements.txt with pinned versions)
- Automated test suite framework (pytest configuration, CI/CD with GitHub Actions)
- Cost tracking and estimation utilities
- Shared utilities package (api_helpers.py, test_helpers.py)
- Repository structure (numbered modules, consistent layout)

**Addresses:**
- **Critical pitfall #1**: Outdated API dependencies — prevented by version pinning and automated testing from day 1
- **Critical pitfall #2**: API cost explosions — cost estimation tools built before creating expensive exercises
- **Differentiator**: Automated test validation — infrastructure ready for every exercise

**Avoids:** Technical debt from "quick and dirty" content creation; prevents needing expensive refactoring later

---

### Phase 2: Python Fundamentals for AI (Weeks 2-4)
**Rationale:** Cannot teach AI without solid Python foundation. Research shows explicit prerequisites prevent frustration. Module 01-python establishes the Theory→Demo→Practice pattern used throughout.

**Delivers:**
- Module 01-python-fundamentals: basics, data structures, functions, classes
- First exercises with automated tests (teaches test-driven learning pattern)
- JupyterLab notebook introduction
- README theory → notebook demo → exercise challenge pattern established
- First "quick win" exercise completable in <10 minutes

**Addresses:**
- **Table stakes**: Code examples with explanations, exercise/challenge problems
- **Critical pitfall #4**: Teaching concepts, not just APIs — establishes conceptual teaching pattern
- **Critical pitfall #5**: Difficulty progression — starts at appropriate beginner level

**Implements:**
- **Architecture pattern**: Theory→Demo→Practice (TDP Loop)
- **Architecture pattern**: Test-Driven Learning

**Stack elements:** Python 3.11, JupyterLab 4.x, pytest 8.x, ruff (linting)

---

### Phase 3: LLM Basics & API Integration (Weeks 4-6)
**Rationale:** First AI module. Introduce LLM concepts before RAG/agents complexity. Research shows starting with OpenAI API (simplest, best-documented) then expanding to alternatives.

**Delivers:**
- Module 02-llms-basics: understanding LLMs, prompt engineering, API usage
- OpenAI SDK integration with cost tracking and error handling examples
- First AI exercises: prompt engineering, API calls, streaming responses
- Cost estimates on every exercise ("~$0.50 to complete")
- Introduction to LangSmith for debugging (observability early)

**Addresses:**
- **Table stakes**: Real datasets (API responses), clear learning objectives per lesson
- **Critical pitfall #2**: Cost management — cost estimates and guardrails from first AI exercise
- **Critical pitfall #4**: Concept teaching — explain prompting strategies, not just API mechanics

**Uses:** OpenAI Python SDK 1.x, python-dotenv (API key management), loguru (logging)

**Checkpoint:** First portfolio project — **Simple Chatbot** with cost tracking, error handling, basic prompt engineering

---

### Phase 4: Embeddings & Vector Search (Weeks 6-8)
**Rationale:** RAG foundation. Must understand embeddings and similarity search before building RAG systems. Research shows teaching vector concepts before database abstractions.

**Delivers:**
- Module 03-embeddings-vectors: what are embeddings, similarity search, chunking strategies
- Hands-on exercises: generate embeddings, calculate cosine similarity, implement basic search
- Chroma DB introduction (simplest setup for learning)
- Batching patterns for performance (addresses performance trap from pitfalls)

**Addresses:**
- **Table stakes**: Real datasets (documents to embed and search)
- **Integration gotcha**: "Not explaining why vectors matter before using Pinecone/Chroma"

**Implements:**
- **Architecture component**: Vector search foundation for RAG

**Uses:** OpenAI embeddings API, Chroma 0.5+, sentence-transformers (local alternative)

---

### Phase 5: RAG Systems (Weeks 8-11)
**Rationale:** Most practical AI application for businesses. Combines LLMs (Phase 3) + vectors (Phase 4). Research shows RAG is highly sought skill.

**Delivers:**
- Module 04-rag-systems: RAG architecture, building RAG pipelines, evaluation
- LangChain integration for RAG orchestration
- Exercises on chunking strategies, retrieval quality, relevance scoring
- Introduction to deepeval for RAG evaluation
- Production patterns: caching, error handling, monitoring

**Addresses:**
- **Differentiator**: Production-ready patterns — show professional RAG implementation
- **Critical pitfall #6**: Success criteria — RAG exercises have clear evaluation metrics
- **Integration gotcha**: "Using RAG without teaching retrieval fundamentals" — Phase 4 covers foundation

**Uses:** LangChain 0.3+, langchain-openai, langchain-chroma, deepeval 1.x

**Checkpoint:** Second portfolio project — **RAG Application** with document ingestion, vector search, evaluation metrics, deployment guide

---

### Phase 6: AI Agents (Weeks 11-14)
**Rationale:** Advanced capability building on RAG + LLMs. Research shows agents are cutting-edge skill for 2026 job market.

**Delivers:**
- Module 05-agents: agent frameworks, tool use, function calling, multi-step reasoning
- LangChain agents implementation
- Exercises: build agents with multiple tools, debug agent loops, handle failures
- Agent observability with LangSmith (tracing multi-step reasoning)

**Addresses:**
- **Differentiator**: Advanced agent capabilities
- **Integration gotcha**: "Building agents before understanding limitations" — include failure mode teaching

**Uses:** LangChain agents, OpenAI function calling, LangSmith (observability)

---

### Phase 7: Multimodal AI (Weeks 14-16)
**Rationale:** Expanding beyond text. Can be parallel to agents (independent concepts). Research shows multimodal is growing area.

**Delivers:**
- Module 06-multimodal: vision (GPT-4 Vision, CLIP), audio, image generation (DALL-E 3)
- Exercises: image understanding, audio transcription, multimodal applications
- Local alternatives (Hugging Face multimodal models)

**Addresses:**
- **Differentiator**: Multimodal capabilities beyond text-only learning

**Uses:** OpenAI GPT-4 Vision, DALL-E 3, Whisper; Hugging Face Transformers for local alternatives

**Checkpoint:** Third portfolio project — **Multimodal Agent System** combining vision/audio with reasoning

---

### Phase 8: Production & Deployment (Weeks 16-18)
**Rationale:** Job-readiness requires deployment skills. Research shows hiring managers value production experience.

**Delivers:**
- Module 07-deployment: FastAPI for APIs, Docker containerization, cloud deployment (AWS/GCP/Azure)
- Module 08-monitoring: logging, observability, cost tracking, performance optimization
- Exercises: deploy projects from Phases 3,5,7 to production
- Monitoring dashboard, error tracking, usage analytics

**Addresses:**
- **Differentiator**: Production-ready patterns, deployment skills
- **Critical pitfall #7**: Portfolio projects must demonstrate real skills — deployment proves production-readiness

**Uses:** FastAPI, Docker Compose, PostgreSQL+pgvector (production vector DB), Prometheus+Grafana (monitoring)

**Final Checkpoint:** **Production System** — fully deployed, monitored, scalable AI application

---

### Phase 9: Community & Polish (Weeks 18-20)
**Rationale:** Differentiation through community engagement and learner support infrastructure.

**Delivers:**
- Discord/GitHub Discussions community setup
- Solution notebooks for all exercises
- Video walkthroughs for complex topics
- FAQ and troubleshooting expanded from beta feedback
- Certification criteria (80% test pass + 2 portfolio projects)

**Addresses:**
- **Differentiators**: Community forum, solution notebooks, video walkthroughs, certification

---

### Phase Ordering Rationale

1. **Phase 0 first (Environment)**: Research shows 30%+ abandonment if setup is friction-heavy; must be perfect before content
2. **Phase 1 before content (Infrastructure)**: Prevents technical debt from "quick content creation"; version pinning and testing prevent Critical Pitfall #1
3. **Foundation → Core → Advanced**: Natural dependency chain from architecture research (Python before LLMs before RAG before Agents)
4. **Portfolio projects after every 2-3 modules**: Consolidates learning, maintains motivation, builds job-ready proof
5. **Production skills near end**: Requires completed projects to deploy; caps curriculum with job-readiness
6. **Community last**: Needs content to exist first; polish phase uses beta learner feedback

**Dependencies:**
- Phase 2 (Python) is foundation for everything
- Phase 3 (LLMs) required for Phases 5,6,7 (RAG, Agents, Multimodal)
- Phase 4 (Embeddings) required for Phase 5 (RAG)
- Phase 5 (RAG) + Phase 3 (LLMs) required for Phase 6 (Agents)
- Phase 8 (Production) requires completed projects from Phases 3,5,6,7

### Research Flags

**Phases likely needing deeper research during planning:**
- **Phase 6 (Agents)**: Agent frameworks evolving rapidly; will need research on current best practices (LangGraph, CrewAI, AutoGPT patterns)
- **Phase 7 (Multimodal)**: Multimodal model APIs changing frequently; need research on latest capabilities
- **Phase 8 (Production/Deployment)**: Many deployment options; need research on best beginner-friendly cloud platforms and monitoring tools

**Phases with standard patterns (skip research-phase):**
- **Phase 0 (Environment Setup)**: Well-established patterns for Python environment setup
- **Phase 2 (Python Fundamentals)**: Standard Python teaching, extensive documentation
- **Phase 3 (LLM Basics)**: OpenAI API well-documented, prompt engineering patterns established
- **Phase 4 (Embeddings)**: Vector concepts well-understood, Chroma documentation solid
- **Phase 5 (RAG)**: LangChain RAG patterns mature and documented

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | **HIGH** | Core technologies (Python, OpenAI, LangChain, pytest) have official documentation, active maintenance, and proven usage in education. Version choices validated across multiple successful platforms. uv recommendation is MEDIUM-HIGH (newer tool but gaining rapid adoption). |
| Features | **HIGH** | Table stakes and differentiators identified from analysis of 7+ successful platforms (Microsoft AI-For-Beginners 106k stars, mlabonne 75k stars, etc.). Clear patterns emerge across all platforms: code-first, executable notebooks, automated validation, portfolio emphasis. |
| Architecture | **HIGH** | Module-based structure with Theory→Demo→Practice pattern is universal across all major AI learning platforms reviewed. Numbered folders, separate exercises, project structure all validated by established courses with 10k+ learners. |
| Pitfalls | **HIGH** | API deprecation, cost explosions, and environment setup are well-documented pain points with clear evidence from GitHub issues, learner complaints, and platform postmortems. Pedagogical pitfalls (progression, success criteria) based on education research and observed patterns. |

**Overall confidence:** **HIGH**

The convergence across multiple successful platforms (Microsoft, Anthropic, mlabonne, DataTalks.Club) provides strong validation. Stack choices verified with official documentation. Feature patterns consistent across platforms with 10k+ GitHub stars. Architecture patterns proven with 100k+ learners.

### Gaps to Address

**During Planning:**
1. **Agent framework choice** — LangChain agents, LangGraph, CrewAI, or AutoGPT patterns? Will need Phase 6 research to determine current best practice in 2026.
2. **Multimodal API stability** — GPT-4 Vision, DALL-E 3, Whisper APIs may have changed. Need Phase 7 research to verify current capabilities and costs.
3. **Deployment platform recommendation** — Many options (AWS, GCP, Azure, Heroku, Fly.io, Railway). Need Phase 8 research to pick most learner-friendly with free tier.
4. **Cost optimization techniques** — Prompt caching, batch APIs, and other cost controls evolving. Verify latest OpenAI/Anthropic cost optimization features during Phase 1.

**During Execution:**
5. **Beta learner feedback** — Test with 5-10 target audience members during Phases 2-3 to validate difficulty progression and time estimates.
6. **API version validation** — Manually verify pinned versions still work with current model versions (gpt-4o, claude-3.5-sonnet) at start of each phase.
7. **Industry portfolio review** — Have 2-3 hiring managers review portfolio project specs in Phase 5, 6, 7 to ensure job-market alignment.

**Known Limitations:**
- Research conducted Feb 2026; AI ecosystem moves fast, recommendations may need adjustment if starting implementation after March 2026
- Cost estimates based on current OpenAI pricing; will need updates if pricing changes
- No research conducted on specialized topics (reinforcement learning, fine-tuning) — these are Phase 2+ additions not covered in initial scope

## Sources

### Primary (HIGH confidence)

**Official Documentation:**
- OpenAI Python SDK: https://platform.openai.com/docs/quickstart (v1.x API, verified Feb 2026)
- LangChain: https://python.langchain.com/docs/introduction/ (v0.3 architecture)
- LlamaIndex: https://docs.llamaindex.ai/en/stable/ (v0.12 stable)
- Hugging Face Transformers: https://github.com/huggingface/transformers (156k stars, actively maintained)
- pytest: https://docs.pytest.org/en/stable/ (v8.x documentation)
- Docker: https://docs.docker.com/get-started/ (25.x documentation)

**Established Learning Platforms (Architecture & Features validation):**
- Microsoft AI-For-Beginners: https://github.com/microsoft/generative-ai-for-beginners (106k stars, official Microsoft course, 21 lesson structure)
- mlabonne LLM Course: https://github.com/mlabonne/llm-course (74.9k stars, comprehensive roadmap with clear prerequisites)
- Anthropic Courses: https://github.com/anthropics/courses (official Anthropic educational materials, 5 self-contained courses)
- DataTalksClub LLM Zoomcamp: https://github.com/DataTalksClub/llm-zoomcamp (14.2k stars, cohort-based with homework validation)
- Karpathy nn-zero-to-hero: https://github.com/karpathy/nn-zero-to-hero (20.2k stars, code-from-scratch teaching)
- Full Stack Deep Learning: Production ML workflows course
- DeepLearning.AI: Professional AI courses with certificates

### Secondary (MEDIUM confidence)

**Pitfalls Research:**
- GitHub issue patterns across AI learning repositories (common complaints about setup, costs, broken code)
- OpenAI Cookbook patterns: https://github.com/openai/openai-cookbook (API usage examples)
- API versioning patterns from OpenAI, Anthropic documentation (deprecation notices, migration guides)

**Cost and Performance:**
- OpenAI pricing page (current as of Feb 2026)
- Production AI engineering best practices (prompt caching, batching, cost optimization)
- LangSmith observability documentation

### Tertiary (LOW confidence, needs validation)

**Emerging Tools:**
- uv package manager: Very new (2024-2025), gaining rapid adoption, but less mature than Poetry
- deepeval: Purpose-built for LLM evaluation, but fewer real-world validations than pytest

---

*Research completed: 2026-02-10*  
*Ready for roadmap: **YES***  
*Next step: Roadmap creation with 9 phases suggested above*
