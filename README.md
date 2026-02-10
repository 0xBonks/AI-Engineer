# AI Engineer Learning Repository

**Your complete, hands-on path from intermediate developer to senior AI Engineer.**

[![Status](https://img.shields.io/badge/Status-Ready%20to%20Learn-brightgreen)]()
[![Phases Complete](https://img.shields.io/badge/Phases-3%2F10%20Complete-blue)]()
[![Last Updated](https://img.shields.io/badge/Updated-Feb%202026-orange)]()

---

## 🎯 What Is This?

A **professional-grade learning repository** that teaches you to build production AI applications through hands-on practice. This isn't just tutorials—it's a complete curriculum with interactive notebooks, real exercises, working solutions, and production-ready projects.

**What makes this different:**
- ✅ **Learn by building** - Every concept has working code
- ✅ **Production-ready** - Best practices, error handling, testing
- ✅ **Complete curriculum** - Structured path from basics to advanced
- ✅ **Self-paced** - Work through at your own speed
- ✅ **Portfolio projects** - Build 5 showcase applications

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+ installed
- Basic programming knowledge (variables, functions, loops)
- OpenAI API key (for Phase 3+)

### Setup (5 minutes)

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd AI-Engineer

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and add your API keys

# 5. Verify setup
python utils/validation.py

# 6. Start learning!
jupyter notebook
```

**You're ready! Start with Phase 1 →**

---

## 📚 Learning Path

### Phase 1: Environment Setup & Infrastructure ✅
**Status:** Complete | **Time:** 4 hours

Set up your bulletproof development environment.

**What You'll Build:**
- Docker development environment
- Environment validation scripts
- Cost tracking utilities
- CI/CD pipeline

**Start Here:**
```bash
cd 01-environment-setup
jupyter notebook notebooks/
```

**Key Files:**
- `notebooks/` - Setup guides and tutorials
- `scripts/validate_env.py` - Check your setup
- `docker-compose.yml` - One-command dev environment

---

### Phase 2: Python Fundamentals for AI ✅
**Status:** Complete | **Time:** 6-8 hours

Master Python patterns essential for AI engineering.

**What You'll Learn:**
- Async programming for concurrent API calls
- Type hints and Pydantic validation
- Production logging and error handling
- REST API patterns
- Data handling (JSON, CSV, file I/O)
- OOP patterns (classes, decorators, context managers)

**Start Here:**
```bash
cd 02-python-fundamentals
jupyter notebook notebooks/
```

**Exercises:**
- Build async API caller
- Create type-safe data models
- Implement error handling patterns
- Work with real data files

**Test Your Knowledge:**
```bash
pytest tests/
```

---

### Phase 3: AI Fundamentals & OpenAI API ✅
**Status:** Complete | **Time:** 18-25 hours

Build real AI applications with OpenAI.

**What You'll Build:**
1. **Streaming chat applications** with real-time responses
2. **Conversation managers** with history and context
3. **Cost tracking systems** to monitor spending
4. **AI Writing Assistant** (complete mini-project)

**Learning Modules:**

#### 📘 AI Fundamentals (Notebooks 1-3)
- Pre-trained models vs fine-tuning
- LLM terminology and concepts  
- Model comparison (GPT-4, Claude, Gemini, Llama)

#### 📘 Chat Completions API (Notebooks 4-6)
- API structure and authentication
- Making your first API calls
- Managing multi-turn conversations

#### 📘 Streaming (Notebooks 7-8)
- Real-time token-by-token display
- Progress indicators and animations
- Async concurrent streaming

#### 📘 Prompt Engineering (Notebooks 9-12)
- System prompts for behavior control
- Few-shot learning
- Chain-of-thought reasoning
- Advanced techniques (templates, constraints)

#### 📘 Optimization (Notebooks 13-16)
- Token counting with tiktoken
- Cost calculation and optimization
- JSON mode and structured outputs
- Function calling for tool use

**Start Here:**
```bash
cd 03-ai-fundamentals-openai
jupyter notebook notebooks/01-pretrained-models.ipynb
```

**Exercises & Solutions:**
```bash
# Work through exercises
ls exercises/

# Check solutions when stuck
ls solutions/

# Run the mini-project
cd projects/ai-writing-assistant
python assistant.py
```

---

## 🎓 How to Use This Repository

### For Beginners

**Week 1-2: Foundation**
1. Complete Phase 1 (environment setup)
2. Verify everything works with `python utils/validation.py`

**Week 3-4: Python Skills**
1. Work through Phase 2 notebooks
2. Complete all exercises
3. Run tests to verify understanding

**Week 5-8: AI Fundamentals**
1. Get OpenAI API key ($5 credit is enough to start)
2. Work through Phase 3 notebooks sequentially
3. Complete exercises after each section
4. Build the AI Writing Assistant project

### For Experienced Developers

**Fast Track (1-2 weeks):**
1. Skim Phase 1, ensure setup complete
2. Review Phase 2 notebooks, focus on gaps
3. **Deep dive Phase 3** - this is the core content
4. Build the mini-project to cement learning

### Learning Tips

✅ **DO:**
- Work through notebooks in order
- Type code yourself (don't copy-paste)
- Experiment with examples
- Complete exercises before checking solutions
- Build the projects

❌ **DON'T:**
- Skip fundamentals (they compound)
- Just read without coding
- Move on if confused (ask for help!)
- Ignore error messages

---

## 📂 Repository Structure

```
AI-Engineer/
├── .planning/                    # Project planning docs
│   ├── ROADMAP.md               # Complete curriculum plan
│   ├── STATE.md                 # Current progress
│   └── phases/                  # Phase-specific plans
│
├── 01-environment-setup/        # Phase 1: Setup
│   ├── notebooks/               # Setup guides
│   ├── scripts/                 # Validation scripts
│   └── docker/                  # Docker configs
│
├── 02-python-fundamentals/      # Phase 2: Python
│   ├── notebooks/               # Learning notebooks (10)
│   ├── exercises/               # Practice problems (15)
│   ├── solutions/               # Reference solutions
│   └── tests/                   # Automated tests
│
├── 03-ai-fundamentals-openai/   # Phase 3: OpenAI API
│   ├── notebooks/               # Learning notebooks (16)
│   ├── exercises/               # Practice exercises (10)
│   ├── solutions/               # Complete solutions (10)
│   ├── tests/                   # Test suites
│   ├── docs/                    # Reference documentation
│   └── projects/                # Mini-project
│       └── ai-writing-assistant/
│
├── utils/                       # Shared utilities
│   ├── validation.py            # Environment validator
│   ├── cost_tracker.py          # API cost tracking
│   └── api_helpers.py           # API utilities
│
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment template
├── docker-compose.yml           # Dev environment
└── README.md                    # This file!
```

---

## 🛠️ Key Tools & Technologies

**Languages & Frameworks:**
- Python 3.11+
- Jupyter Notebooks
- Pydantic for data validation

**AI/ML:**
- OpenAI API (GPT-3.5, GPT-4)
- tiktoken (token counting)
- OpenAI Python SDK

**Development:**
- Docker & Docker Compose
- Git & GitHub
- pytest for testing
- python-dotenv for config

**Future Phases Will Add:**
- Hugging Face Transformers
- ChromaDB, Pinecone (vector databases)
- LangChain, LlamaIndex (RAG frameworks)
- Ollama (local models)

---

## 💡 What You'll Build

### Phase 3 Projects (Available Now)

**1. Simple Chat Interface**
- CLI chat with OpenAI
- Conversation history
- Token tracking

**2. Streaming Chat App**
- Real-time responses
- Progress indicators
- Typing animations

**3. Conversation Manager**
- Context window management
- Auto-trimming old messages
- Save/load conversations

**4. AI Writing Assistant** (Mini-Project)
- Multiple writing modes (creative, technical, simple)
- Streaming responses
- Cost tracking
- Production-ready code

### Future Portfolio Projects (Coming in Phase 10)

1. **Production RAG System** - Document Q&A with semantic search
2. **Multi-Agent System** - Coordinated AI agents with MCP
3. **Multimodal Application** - Vision + audio + text
4. **Fine-tuning Pipeline** - Custom model training
5. **End-to-End Production System** - Complete AI application

---

## 📊 Progress Tracking

**Completed Phases:** ✅✅✅ (3/10)

| Phase | Status | Time Estimate | Your Progress |
|-------|--------|---------------|---------------|
| 1. Environment Setup | ✅ Complete | 4 hours | [ ] |
| 2. Python Fundamentals | ✅ Complete | 6-8 hours | [ ] |
| 3. AI Fundamentals & OpenAI | ✅ Complete | 18-25 hours | [ ] |
| 4. Open Source AI & Safety | 📋 Planned | TBD | [ ] |
| 5. Embeddings & Vector DBs | 📋 Planned | TBD | [ ] |
| 6. RAG Systems | 📋 Planned | TBD | [ ] |
| 7. AI Agents | 📋 Planned | TBD | [ ] |
| 8. Multimodal AI | 📋 Planned | TBD | [ ] |
| 9. Testing Infrastructure | 📋 Planned | TBD | [ ] |
| 10. Portfolio Projects | 📋 Planned | TBD | [ ] |

**Your Learning Log:**
```bash
# Track your progress
echo "Completed Phase 1: $(date)" >> my-progress.log
echo "Completed Phase 2: $(date)" >> my-progress.log
```

---

## 🆘 Getting Help

### Common Issues

**"Import errors when running notebooks"**
```bash
# Make sure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

**"OpenAI API key not found"**
```bash
# Check .env file exists and has your key
cat .env | grep OPENAI_API_KEY
# Should show: OPENAI_API_KEY=sk-...
```

**"Notebooks won't start"**
```bash
# Install Jupyter if missing
pip install jupyter notebook
jupyter notebook
```

**"Tests failing"**
```bash
# Install test dependencies
pip install pytest pytest-asyncio
pytest -v
```

### Resources

- **OpenAI Documentation:** https://platform.openai.com/docs
- **Python Async Guide:** https://realpython.com/async-io-python/
- **Prompt Engineering Guide:** https://www.promptingguide.ai/

### Ask Questions

If you're stuck:
1. Check the solutions/ directory for reference
2. Review notebook comments and documentation
3. Search error messages online
4. Experiment with small code changes

---

## 💰 Cost Management

**Phase 3 uses OpenAI API** - here's what to expect:

**Estimated Costs:**
- Working through Phase 3: **$2-5**
- All exercises: **~$1**
- Mini-project testing: **~$1**
- Experimentation: **$2-3**

**OpenAI gives $5 free credit** for new accounts!

**Track Your Spending:**
```python
# Built-in cost tracker
from utils.cost_tracker import CostTracker

tracker = CostTracker()
# Automatically tracks all API calls
```

**Cost Optimization Tips:**
- Use GPT-3.5 Turbo for learning (20x cheaper)
- Set max_tokens to limit response length
- Use the cost tracker to monitor spending
- Test with small examples first

---

## 🎯 Success Criteria

**You're ready for real-world AI engineering when you can:**

✅ Build a streaming chat application from scratch  
✅ Manage conversation context and history  
✅ Apply prompt engineering to solve problems  
✅ Calculate and optimize API costs  
✅ Handle errors and edge cases gracefully  
✅ Explain when to use different models  
✅ Build production-ready AI features  

**After Phase 3, you should be able to:**
- Add AI features to existing applications
- Build customer-facing chatbots
- Integrate OpenAI into web/mobile apps
- Optimize for cost and performance
- Apply professional best practices

---

## 🚀 Next Steps

### After Completing Phase 3:

**Option 1: Start Building**
- Add AI to your existing projects
- Build a portfolio project
- Contribute to open source AI projects

**Option 2: Continue Learning** (when Phases 4-10 are ready)
- Phase 4: Open source models (Hugging Face, Ollama)
- Phase 5: Embeddings and vector search
- Phase 6: RAG systems for document Q&A
- Phase 7: AI agents with tool use
- Phase 8: Multimodal (vision, audio, speech)

**Option 3: Specialize**
- Deep dive into prompt engineering
- Master RAG system architecture
- Become an AI agent expert
- Build production-scale systems

---

## 📝 License & Usage

This is a learning repository. Feel free to:
- ✅ Use for personal learning
- ✅ Modify and experiment
- ✅ Build on these concepts
- ✅ Share with others learning AI

---

## 🙏 Acknowledgments

Built with professional AI engineering practices and inspired by real-world production systems.

**Key Resources:**
- OpenAI Documentation
- OpenAI Cookbook
- Real-world AI engineering experience
- Community best practices

---

## 📞 Support

**Found a bug?** Check solutions/ first, then review error messages carefully.

**Have a suggestion?** Great! This is a living learning resource.

**Want to contribute?** Follow the existing structure and quality standards.

---

**🎓 Ready to become an AI Engineer? Start with Phase 1!**

```bash
cd 01-environment-setup
jupyter notebook notebooks/
```

**Happy Learning! 🚀**
