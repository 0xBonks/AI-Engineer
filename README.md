# AI Engineer Learning Repository

A comprehensive, hands-on learning repository that transforms intermediate developers into senior AI Engineers through portfolio-quality projects, interactive demos, and test-validated challenges.

## What You'll Build

By completing this repository, you'll have the knowledge and demonstrable portfolio to apply for **senior AI Engineering roles**, including:

- **Production RAG System** - Semantic search with embeddings, vector databases, and cost optimization
- **Multi-Agent System** - MCP implementation, tool use, ReAct prompting, and orchestration
- **Multimodal Application** - Integrating vision, audio, and speech with LLM reasoning
- **Fine-tuning Pipeline** - Custom model training, evaluation, and deployment
- **End-to-End Production System** - Complete AI system with monitoring and scaling

## Learning Path

```
Phase 1: Environment Setup & Infrastructure (10 modules, ~100 hours)
   ↓
01 → Python Fundamentals → Async, types, error handling, API patterns
   ↓
02 → AI Fundamentals & OpenAI API → LLMs, prompt engineering, cost optimization
   ↓
03 → Open Source AI & Safety → Hugging Face, Ollama, security best practices
   ↓
04 → Embeddings & Vector Databases → Semantic search, Chroma, similarity matching
   ↓
05 → RAG Systems → Production retrieval-augmented generation pipelines
   ↓
06 → AI Agents → MCP, tool use, ReAct, multi-agent orchestration
   ↓
07 → Multimodal AI → Vision, audio, speech integration
   ↓
08 → Advanced RAG & Optimization → Hybrid search, re-ranking, performance tuning
   ↓
09 → Production Deployment → Monitoring, scaling, operational best practices
   ↓
10 → Portfolio Projects → 5 production-ready projects for your portfolio
```

## Quick Start

### Prerequisites

- **Experience**: Intermediate programming (any language)
- **Python**: 3.11+ installed
- **API Keys**: OpenAI account (bring your own key)
- **Hardware**: Local machine with adequate GPU for fine-tuning (optional but recommended)
- **Time**: 3-6 months for completion

### Setup (3 options)

#### Option 1: Docker (Recommended)
```bash
# Clone repository
git clone <repository-url>
cd AI-Engineer

# Start development environment (includes JupyterLab, all dependencies, GPU support)
./start.sh

# Validate environment
python validate_env.py
```

#### Option 2: Local Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Validate environment
python validate_env.py
```

#### Option 3: Cloud Development Environment
See [DOCKER_SETUP.md](docs/DOCKER_SETUP.md) for cloud deployment options.

### Your First Exercise

```bash
# Navigate to Module 01
cd 01-python-fundamentals

# Start Jupyter
jupyter lab

# Open notebooks/01-async-basics.ipynb
# Complete exercises/01-async-challenge.py
# Run tests: pytest tests/test_async.py
```

## Repository Structure

```
AI-Engineer/
├── 01-python-fundamentals/          # Python patterns for AI engineering
├── 02-ai-fundamentals-openai/       # LLMs and OpenAI API
├── 03-open-source-ai-safety/        # Hugging Face, Ollama, security
├── 04-embeddings-vector-databases/  # Semantic search foundations
├── 05-rag-systems/                  # Production RAG pipelines
├── 06-ai-agents/                    # MCP, tool use, orchestration
├── 07-multimodal-ai/                # Vision, audio, speech
├── 08-advanced-rag-optimization/    # Hybrid search, re-ranking
├── 09-production-deployment/        # Monitoring, scaling
├── 10-portfolio-projects/           # 5 portfolio projects
├── utils/                           # Shared utilities
│   ├── validation.py                # Environment validation
│   ├── cost_tracker.py              # API cost tracking
│   └── api_helpers.py               # Retry logic, rate limiting
├── docs/                            # Documentation
└── tests/                           # Integration tests
```

Each module contains:
- `README.md` - Theory, learning objectives, resources
- `notebooks/` - Interactive Jupyter demos
- `exercises/` - Hands-on coding challenges
- `tests/` - Automated validation
- `solutions/` - Reference implementations with commentary

## Progress Tracking

Track your progress as you complete modules:

- [ ] **Module 01**: Python Fundamentals (8-10 hours)
- [ ] **Module 02**: AI Fundamentals & OpenAI API (12-15 hours)
- [ ] **Module 03**: Open Source AI & Safety (10-12 hours)
- [ ] **Module 04**: Embeddings & Vector Databases (10-12 hours)
- [ ] **Module 05**: RAG Systems (15-18 hours)
- [ ] **Module 06**: AI Agents (15-18 hours)
- [ ] **Module 07**: Multimodal AI (12-15 hours)
- [ ] **Module 08**: Advanced RAG & Optimization (12-15 hours)
- [ ] **Module 09**: Production Deployment (10-12 hours)
- [ ] **Module 10**: Portfolio Projects (40-50 hours)

**Total**: ~150-170 hours

## Key Features

### Cost Tracking
Every exercise includes estimated API costs upfront. Use built-in cost tracking utilities:

```python
from utils.cost_tracker import track_cost, estimate_cost

# Estimate before running
estimate_cost(prompt="Your prompt", model="gpt-4")

# Track actual usage
@track_cost
def my_ai_function():
    # Your code here
    pass
```

### Automated Validation
All exercises have automated tests to verify your work:

```bash
# Run validation for specific exercise
pytest 01-python-fundamentals/tests/test_async.py

# Run all tests for a module
pytest 01-python-fundamentals/tests/

# Run validation across entire repository
pytest
```

### Production Patterns
Learn industry best practices from day one:
- Error handling and retry logic
- Rate limiting and cost optimization
- Logging and monitoring
- Security and safety considerations
- Scalable architecture patterns

## Documentation

- [Setup Guide](docs/SETUP_GUIDE.md) - Complete setup walkthrough
- [Docker Setup](docs/DOCKER_SETUP.md) - Docker environment details
- [Environment Variables](docs/ENV_SETUP.md) - API key configuration
- [Cost Tracking](docs/COST_TRACKING.md) - Monitor API expenses
- [Validation](docs/VALIDATION.md) - Environment validation guide
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions
- [Contributing](CONTRIBUTING.md) - Contribution guidelines
- [API Patterns](docs/API_PATTERNS.md) - Common API usage patterns
- [Dependencies](docs/DEPENDENCIES.md) - Dependency management strategy

## Technologies

**Core AI Stack:**
- OpenAI API (GPT-4, GPT-3.5, embeddings, DALL-E, Whisper)
- Hugging Face (Transformers, Inference SDK)
- Ollama (Local model deployment)

**Frameworks:**
- LangChain (Agent and RAG frameworks)
- LlamaIndex (RAG and indexing)

**Vector Databases:**
- Chroma (Primary)
- Pinecone, Weaviate (Advanced modules)

**Python Libraries:**
- tiktoken (Token counting)
- Pydantic (Data validation)
- sentence-transformers (Embeddings)
- pytest (Testing)
- JupyterLab (Interactive development)

## Learning Philosophy

This repository follows proven educational principles:

1. **Hands-on First** - Learn by building, not just reading
2. **Incremental Complexity** - Each module builds on previous knowledge
3. **Immediate Feedback** - Automated tests validate understanding
4. **Real Tools** - Use actual APIs and production libraries
5. **Portfolio Focus** - Build projects you can show employers
6. **Production Mindset** - Learn best practices from the start

## Cost Considerations

Estimated total API costs: **$50-150** (varies by model choices and usage patterns)

Tips to minimize costs:
- Use GPT-3.5-turbo for learning exercises
- Implement cost tracking from day one
- Leverage free tier offerings where available
- Use local models (Ollama) for experimentation

## Support

- **Issues**: Open a GitHub issue for bugs or questions
- **Discussions**: Use GitHub Discussions for general questions
- **Contributions**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

Built following industry best practices and inspired by:
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [LangChain Documentation](https://python.langchain.com/)
- [Hugging Face Course](https://huggingface.co/learn)
- Real-world AI engineering experience

---

**Ready to become a senior AI Engineer?** Start with [Module 01: Python Fundamentals](01-python-fundamentals/)

Last updated: 2026-02-10
