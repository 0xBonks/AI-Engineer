# Stack Research

**Domain:** AI Engineering Learning Platform
**Researched:** 2026-02-10
**Confidence:** HIGH

## Recommended Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Python | 3.11+ | Primary language | Industry standard for AI/ML. Python 3.11+ offers significant performance improvements (10-60% faster than 3.10). 3.12+ is stable but 3.11 offers best balance of performance, stability, and library compatibility for AI work. |
| Docker | 25.x+ | Development environment | Ensures reproducibility across machines. Critical for AI/ML with complex dependencies (CUDA, system libraries). Current LTS with compose v2 integrated. |
| JupyterLab | 4.x | Interactive notebooks | Latest generation notebook interface. Modular design, better performance, real-time collaboration features. Essential for exploratory AI work and teaching. |
| Poetry / uv | 1.8+ / 0.5+ | Dependency management | Poetry: mature, widely adopted. uv: new Rust-based tool (10-100x faster than pip), excellent for teaching speed. Recommend uv for new projects in 2026. |

### AI Frameworks & Libraries

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| OpenAI Python SDK | 1.x | OpenAI API access | Primary LLM provider. Simple API, excellent docs. Use for: GPT models, embeddings, assistants API. Latest v1.x has responses API. |
| LangChain | 0.3+ | Agent orchestration | Use for: RAG pipelines, multi-step agents, tool integration. Modular design with provider-specific packages (langchain-openai, langchain-anthropic). Mature ecosystem. |
| LlamaIndex | 0.12+ | RAG framework | Alternative to LangChain. Better for: document-centric RAG, complex retrieval strategies, index management. Simpler abstractions than LangChain for basic RAG. |
| Hugging Face Transformers | 4.48+ | Model library | Access to 1M+ models. Use for: local inference, fine-tuning, model experimentation. Required for custom model work. |
| Hugging Face Datasets | 3.x | Dataset library | Standardized datasets, efficient loading, streaming. Essential for training exercises. |
| Anthropic Python SDK | 0.40+ | Claude API access | For Claude models. Better for: reasoning tasks, long context (200K tokens), prompt caching. |
| sentence-transformers | 3.x | Embeddings | Local embeddings generation. Use when: avoiding API costs, offline work, custom embedding models. |

### Vector Databases

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Chroma | 0.5+ | Vector DB (primary) | Simple setup, minimal dependencies, excellent for learning. Runs in-process or client-server. Best choice for demos and exercises. |
| Pinecone | Client 5.x | Managed vector DB | Production-grade, fully managed. Use for: scalability lessons, production deployment exercises. Free tier available. |
| Qdrant | 1.12+ | Vector DB (advanced) | High performance, rich filtering. Good for: advanced RAG exercises, hybrid search, production patterns. Can run locally or managed. |
| pgvector | 0.8+ (PostgreSQL) | Vector extension | Teach: combining structured + vector data, single database approach. Realistic production pattern. |

### Testing & Validation

| Tool | Version | Purpose | When to Use |
|------|---------|---------|-------------|
| pytest | 8.x | Test framework | Industry standard. Use for: all exercise validation, project testing. Rich ecosystem of plugins. |
| pytest-asyncio | 0.24+ | Async test support | Required for async AI operations (streaming, concurrent API calls). |
| deepeval | 1.x | LLM evaluation | Purpose-built for AI testing. Use for: RAG evaluation, prompt testing, model comparison. Better than generic test frameworks for AI. |
| pytest-cov | 6.x | Coverage reporting | Track test coverage. Teaching tool for best practices. |
| ruff | 0.8+ | Linting/formatting | Extremely fast Python linter (10-100x faster than pylint). Replaces pylint, flake8, isort, black. Single tool for code quality. |

### Development Tools

| Tool | Purpose | Notes |
|------|---------|-------|
| Git + GitHub | Version control | Standard. Teach: branches, PRs, collaboration. GitHub Actions for CI/CD exercises. |
| VS Code + Python Extension | IDE | Most popular Python IDE. Extensions: Python, Jupyter, Docker. Copilot integration for AI assistance. |
| Docker Compose | Multi-container orchestration | Define full stack (app, vector DB, monitoring) in single file. Teaching: microservices, deployment. |
| pre-commit | Git hooks | Enforce linting, formatting before commits. Teaching: code quality automation. |
| Rich | Terminal UI | Better CLI output, progress bars, tables. Makes learning CLI tools more engaging. |
| python-dotenv | Environment management | Load .env files. Essential for: API key management, configuration. Security teaching opportunity. |

### Observability & Debugging

| Tool | Purpose | Notes |
|------|---------|-------|
| LangSmith | LLM tracing | Official LangChain observability. Essential for: debugging agents, understanding chains, cost tracking. Free tier available. |
| Weights & Biases | Experiment tracking | Track training runs, hyperparameters, metrics. Industry standard for ML experiments. Free for individuals. |
| loguru | Logging | Better than stdlib logging. Easier to teach, better default formatting, less boilerplate. |

## Installation

### Project Setup
```bash
# Create project with uv (recommended for 2026)
uv init ai-engineering-repo
cd ai-engineering-repo
uv venv
source .venv/bin/activate  # Linux/Mac
# or .venv\Scripts\activate  # Windows

# Core dependencies
uv pip install \
    "openai>=1.0" \
    "langchain>=0.3.0" \
    "langchain-openai" \
    "langchain-chroma" \
    "chromadb>=0.5.0" \
    "tiktoken" \
    "python-dotenv"

# Jupyter and interactive
uv pip install \
    "jupyterlab>=4.0" \
    "ipywidgets" \
    "matplotlib" \
    "pandas"

# Testing and quality
uv pip install \
    "pytest>=8.0" \
    "pytest-asyncio" \
    "pytest-cov" \
    "deepeval" \
    "ruff" \
    "pre-commit"

# Additional AI frameworks (as needed per project)
uv pip install \
    "transformers>=4.48" \
    "sentence-transformers" \
    "datasets" \
    "anthropic"

# Observability
uv pip install \
    "langsmith" \
    "loguru" \
    "rich"
```

### Alternative: Poetry Setup
```bash
# If using Poetry instead of uv
poetry init
poetry add openai langchain langchain-openai chromadb
poetry add --group dev pytest ruff pre-commit
poetry add --group jupyter jupyterlab ipywidgets
```

### Docker Setup
```dockerfile
# Dockerfile for reproducible environment
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
```

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| LangChain | LlamaIndex | Prefer LlamaIndex when: focus is purely on RAG, want simpler abstractions, less boilerplate needed. |
| OpenAI | Anthropic Claude | Use Claude when: teaching reasoning models, need long context (200K+), want to show API diversity. |
| Chroma | FAISS | Use FAISS when: teaching low-level vector concepts, no persistence needed, maximum performance for in-memory operations. |
| Docker | Virtual environments only | Skip Docker when: learners are Docker-unfamiliar, focus is purely on Python/AI concepts, resource-constrained machines. |
| uv | pip/pip-tools | Use pip when: maximum stability required, uv has compatibility issues with specific packages. |
| pytest | unittest | Use unittest when: teaching standard library, no external dependencies allowed. pytest is superior for all other cases. |
| JupyterLab | Jupyter Notebook Classic | Use Classic when: teaching notebook fundamentals first, learners overwhelmed by Lab interface. |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| TensorFlow/Keras | Declining in 2026. PyTorch dominant for new projects. Transformers library uses PyTorch. | PyTorch + Hugging Face Transformers |
| pip alone | Slow, no lock files, dependency conflicts. Poor experience for learners. | uv (fast, modern) or Poetry (mature, stable) |
| LangChain < 0.3 | Major API changes in 0.3. Old tutorials incompatible. Provider packages split out. | LangChain 0.3+ with provider packages |
| OpenAI < 1.0 | Breaking API change at 1.0. Legacy API deprecated. All new docs use 1.x. | OpenAI SDK 1.x+ |
| Python 3.8 or older | End of life. No longer gets security updates. Missing performance improvements. | Python 3.11+ (3.12+ for cutting edge) |
| Pinecone for local dev | Requires internet, API keys, quotas. Bad for offline learning, local experimentation. | Chroma or Qdrant for local development |
| venv + requirements.txt | No dependency resolution, version conflicts common, hard to reproduce. | uv or Poetry with lock files |
| Custom notebooks from scratch | Reinventing wheel. Poor learner experience with missing features. | JupyterLab 4.x (battle-tested, rich ecosystem) |

## Stack Patterns by Use Case

**For Python Fundamentals Module:**
- Python 3.11 + pytest + ruff
- JupyterLab for interactive exploration
- Rich for engaging CLI output
- Focus: Core Python, testing patterns, tooling
- Skip: AI frameworks initially

**For RAG System Project:**
- LangChain + OpenAI SDK + Chroma
- pytest + deepeval for evaluation
- LangSmith for debugging
- Docker for reproducibility
- Alternative stack: LlamaIndex + sentence-transformers (local-first)

**For AI Agents Project:**
- LangChain agents + OpenAI function calling
- Multiple tools integration (web search, calculators, APIs)
- LangSmith for trace visualization
- Docker Compose for multi-service setup

**For Fine-tuning Project:**
- Hugging Face Transformers + Datasets
- Weights & Biases for experiment tracking
- GPU-enabled Docker container
- Dataset preparation and evaluation pipelines

**For Multimodal Project:**
- OpenAI GPT-4 Vision + DALL-E 3
- Or: Hugging Face multimodal models (local)
- Gradio for UI (simpler than Streamlit for demos)
- Image preprocessing libraries (Pillow, OpenCV)

**For Production System Project:**
- FastAPI for API layer
- Docker + Docker Compose
- PostgreSQL + pgvector
- Redis for caching
- Monitoring: Prometheus + Grafana (optional)

## Version Compatibility Matrix

| Core Package | Compatible OpenAI | Compatible LangChain | Notes |
|--------------|-------------------|----------------------|-------|
| langchain 0.3.x | openai >= 1.0 | Use langchain-openai 0.2+ | Provider package required |
| langchain 0.2.x | openai >= 1.0 | N/A (deprecated) | Upgrade to 0.3 |
| chromadb 0.5.x | Any | langchain-chroma 0.1.4+ | In-process mode works out of box |
| transformers 4.48+ | Any (for embeddings) | Any | Requires PyTorch 2.0+ |

### Python Version Support

| Package | Python 3.11 | Python 3.12 | Python 3.13 |
|---------|-------------|-------------|-------------|
| OpenAI SDK | ✅ | ✅ | ✅ |
| LangChain | ✅ | ✅ | ⚠️ (limited testing) |
| Transformers | ✅ | ✅ | ⚠️ (some deps lag) |
| pytest | ✅ | ✅ | ✅ |
| JupyterLab | ✅ | ✅ | ✅ |

**Recommendation:** Python 3.11 for maximum compatibility. Python 3.12 is safe but some AI libraries still catching up.

## Critical Dependencies Notes

**CUDA/GPU Support:**
- For GPU-accelerated training: Need CUDA 12+ compatible PyTorch
- Install: `uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124`
- Docker: Use `nvidia/cuda:12.4.0-runtime-ubuntu22.04` base image
- Most learners can skip GPU for this repo (inference via APIs)

**Native Dependencies:**
- Chroma: Requires build tools (gcc, python3-dev) for native extensions
- transformers: Can use CPU-only (no CUDA required for inference)
- sentence-transformers: Downloads models (~500MB) on first use

**Token Limits:**
- OpenAI embeddings: text-embedding-3-small (8191 tokens)
- Claude: 200K context window (expensive, use strategically)
- Local models: Check model card for context limits

## Sources

**Verified with Official Documentation:**
- OpenAI Python SDK: https://platform.openai.com/docs/quickstart (v1.x API, Feb 2026)
- LangChain: https://python.langchain.com/docs/introduction/ (v0.3 architecture)
- LlamaIndex: https://docs.llamaindex.ai/en/stable/ (v0.12 stable)
- Hugging Face Transformers: https://github.com/huggingface/transformers (156k stars, actively maintained)
- pytest: https://docs.pytest.org/en/stable/ (v8.x documentation)
- Docker: https://docs.docker.com/get-started/ (25.x documentation)
- Jupyter: https://jupyter.org/ (JupyterLab 4.x latest)

**Vector Database Comparison:**
- LangChain integrations list: https://python.langchain.com/docs/integrations/vectorstores/
- Personal assessment based on learning use case (local-first, minimal setup)

**Confidence Levels:**
- Python, pytest, Docker, Jupyter: HIGH (stable, well-documented, industry standard)
- OpenAI SDK, LangChain, Transformers: HIGH (official docs, active maintenance)
- Vector DB choices: MEDIUM (based on integration quality and learning UX)
- uv recommendation: MEDIUM-HIGH (newer tool, very fast, but Poetry more mature)

**Key Decision Rationales:**
1. **Python 3.11 over 3.12:** Better library compatibility in AI ecosystem (Feb 2026)
2. **uv over Poetry:** 2026 recommendation. 10-100x faster, gaining adoption. Poetry still excellent fallback.
3. **Chroma over FAISS:** Persistence, better DX, more realistic for production learning
4. **LangChain + LlamaIndex both:** Show both paradigms. LangChain for agents, LlamaIndex as RAG alternative.
5. **pytest + deepeval:** pytest for general testing, deepeval specifically for LLM evaluation
6. **JupyterLab 4 over Classic:** Modern interface, better for 2026 learning. Classic available if needed.
7. **Docker required:** AI dependencies are complex. Reproducibility is critical for learning platform.

---
*Stack research for: AI Engineering Learning Platform*
*Researched: 2026-02-10*
*Overall confidence: HIGH*
