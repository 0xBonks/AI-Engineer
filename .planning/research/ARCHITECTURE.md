# Architecture Research

**Domain:** AI Engineering Learning Repository
**Researched:** 2026-02-10
**Confidence:** HIGH

## Standard Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     LEARNING REPOSITORY                      │
├─────────────────────────────────────────────────────────────┤
│  Topic-Based Module Structure (Sequential Learning Path)    │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │ Module  │→ │ Module  │→ │ Module  │→ │ Module  │        │
│  │  01-*   │  │  02-*   │  │  03-*   │  │  04-*   │        │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘        │
│       ├───────────┬┴────────────┴┬────────────┤             │
├───────┴───────────┴──────────────┴────────────┴─────────────┤
│                 CONTENT LAYER (Per Module)                   │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ README   │  │ Notebooks│  │  Tests   │  │  Assets  │    │
│  │ (theory) │  │ (demos)  │  │(validate)│  │ (files)  │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
├─────────────────────────────────────────────────────────────┤
│                 SUPPORTING INFRASTRUCTURE                    │
│  ┌───────────────────┐  ┌───────────────────┐              │
│  │ Environment Setup │  │ Portfolio Projects │              │
│  │ (Docker, config)  │  │ (capstone work)    │              │
│  └───────────────────┘  └───────────────────┘              │
└─────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

| Component | Responsibility | Typical Implementation |
|-----------|----------------|------------------------|
| **Module Folders** | Organize content by topic (01-intro, 02-llms, etc.) | Numbered directories with descriptive names |
| **README.md** | Lesson content, theory, explanations | Markdown with diagrams, code snippets, links |
| **Notebooks** | Interactive demos, code examples | Jupyter notebooks (.ipynb) with executable cells |
| **Tests** | Validate learner solutions | pytest files or notebook-based validation |
| **Solution Files** | Reference implementations | Python scripts or notebooks (often in /solutions subfolder) |
| **Assets** | Supporting materials | Data files, images, diagrams, config files |
| **Projects** | Portfolio-building capstone work | Standalone folders with full application structure |
| **Docs** | Additional documentation | Setup guides, FAQs, architecture notes |

## Recommended Project Structure

```
ai-engineering-repo/
├── 00-setup/                    # Environment setup and prerequisites
│   ├── README.md                # Setup instructions
│   ├── requirements.txt         # Python dependencies
│   ├── docker-compose.yml       # Container setup (if needed)
│   └── environment-test.ipynb   # Verify environment works
│
├── 01-python-fundamentals/      # Foundation module
│   ├── README.md                # Module overview and learning objectives
│   ├── 01-basics.ipynb          # Sub-lesson: Python basics
│   ├── 02-data-structures.ipynb # Sub-lesson: Lists, dicts, etc.
│   ├── 03-functions.ipynb       # Sub-lesson: Functions
│   ├── exercises/               # Practice challenges
│   │   ├── exercise-01.ipynb    # Challenge with starter code
│   │   └── test_exercise.py     # Automated tests
│   ├── solutions/               # Reference solutions (often hidden)
│   │   └── exercise-01-solution.ipynb
│   └── assets/                  # Supporting files
│       └── data.csv
│
├── 02-llms-basics/              # First AI module
│   ├── README.md
│   ├── 01-understanding-llms.ipynb
│   ├── 02-prompting.ipynb
│   ├── 03-api-usage.ipynb
│   ├── exercises/
│   │   ├── prompt-engineering-challenge.ipynb
│   │   └── test_prompts.py
│   └── assets/
│       └── sample-prompts.txt
│
├── 03-embeddings-vectors/       # Vector/embedding module
│   ├── README.md
│   ├── 01-embeddings-intro.ipynb
│   ├── 02-vector-search.ipynb
│   ├── exercises/
│   └── assets/
│
├── 04-rag-systems/              # RAG implementation
│   ├── README.md
│   ├── 01-rag-architecture.ipynb
│   ├── 02-building-rag.ipynb
│   ├── exercises/
│   │   └── build-rag-system/
│   │       ├── challenge.md
│   │       ├── starter-code.py
│   │       └── test_rag.py
│   └── assets/
│
├── 05-agents/                   # Agents and tools
│   ├── README.md
│   ├── 01-agent-frameworks.ipynb
│   ├── 02-building-agents.ipynb
│   └── exercises/
│
├── 06-multimodal/              # Multimodal AI
│   ├── README.md
│   ├── 01-vision.ipynb
│   ├── 02-audio.ipynb
│   └── exercises/
│
├── projects/                   # Portfolio projects
│   ├── 01-chatbot/             # Starter project
│   │   ├── README.md           # Project requirements
│   │   ├── src/                # Application code
│   │   ├── tests/              # Project tests
│   │   └── requirements.txt
│   ├── 02-rag-application/     # Intermediate project
│   └── 03-agent-system/        # Advanced project
│
├── utils/                      # Shared utilities
│   ├── api_helpers.py          # API wrapper functions
│   ├── test_helpers.py         # Testing utilities
│   └── notebook_helpers.py     # Common notebook functions
│
├── docs/                       # Documentation
│   ├── architecture.md         # This document
│   ├── learning-path.md        # Recommended progression
│   ├── faq.md                  # Common questions
│   └── troubleshooting.md      # Common issues
│
├── .env.example                # Environment variable template
├── .gitignore                  # Exclude secrets, data, checkpoints
├── README.md                   # Repository overview
├── CONTRIBUTING.md             # How to contribute
└── requirements.txt            # Global dependencies
```

### Structure Rationale

- **Numbered modules (01-, 02-)**: Forces sequential learning order, makes dependencies clear
- **Per-module README**: Each module is self-contained with learning objectives, prerequisites, and resources
- **Exercises separated from lessons**: Clean separation between teaching content and practice
- **Solutions in separate folder**: Prevents accidental spoilers, can be excluded from initial clone
- **Projects at root level**: Signals these are substantial, portfolio-worthy work distinct from exercises
- **Shared utils/**: Reduces code duplication, teaches code reuse patterns
- **Docker configuration**: Isolates environment, ensures consistency across machines

## Architectural Patterns

### Pattern 1: Progressive Complexity (Spiral Learning)

**What:** Each module builds on previous modules, introducing one new concept at a time while reinforcing earlier topics.

**When to use:** Always - this is the foundational pattern for learning repositories.

**Trade-offs:** 
- ✅ Learners never feel overwhelmed
- ✅ Natural reinforcement of concepts
- ❌ Advanced learners may want to skip ahead (mitigate with clear prerequisites per module)

**Example:**
```
Module 01: Python basics (functions, data structures)
Module 02: API calls (uses Python from 01)
Module 03: LLM basics (uses APIs from 02, Python from 01)
Module 04: RAG (uses LLMs from 03, vectors introduced fresh)
Module 05: Agents (combines RAG from 04, LLMs from 03)
```

### Pattern 2: Theory → Demo → Practice (TDP Loop)

**What:** Every module follows: README theory → Notebook demo → Exercise challenge.

**When to use:** For every substantive topic in every module.

**Trade-offs:**
- ✅ Multiple learning modalities (read, watch, do)
- ✅ Immediate application of concepts
- ❌ Requires 3x content creation effort

**Example:**
```python
# In 03-rag-systems/
README.md            # Theory: What is RAG? Architecture diagrams
01-rag-demo.ipynb    # Demo: Build simple RAG, see it work
exercises/           # Practice: Build your own RAG with different data
  rag-challenge.ipynb
  test_rag.py        # Automated validation
```

### Pattern 3: Test-Driven Learning

**What:** Exercises come with automated tests that validate correctness, providing immediate feedback.

**When to use:** For any exercise with objectively correct answers (code challenges, system building).

**Trade-offs:**
- ✅ Learners know immediately if solution is correct
- ✅ Encourages experimentation without fear
- ✅ Teaches testing as a practice
- ❌ Not suitable for open-ended creative tasks
- ❌ Requires test maintenance

**Example:**
```python
# exercises/test_embeddings.py
def test_embedding_dimension():
    """Verify learner's embedding function returns correct shape"""
    result = create_embedding("test text")
    assert result.shape == (1536,), "OpenAI embeddings should be 1536-dim"

def test_similarity_calculation():
    """Verify cosine similarity implementation"""
    vec1 = np.array([1, 0, 0])
    vec2 = np.array([0, 1, 0])
    assert abs(cosine_similarity(vec1, vec2) - 0.0) < 0.01
```

### Pattern 4: Portfolio Project Milestones

**What:** 3-5 substantial projects that build a portfolio, increasing in complexity.

**When to use:** After every 2-3 learning modules to consolidate skills.

**Trade-offs:**
- ✅ Creates job-ready portfolio artifacts
- ✅ Integrates multiple concepts into cohesive systems
- ✅ Motivation through building real things
- ❌ Requires significant time investment
- ❌ May frustrate learners who struggle with integration

**Recommended Project Progression:**
1. **Chatbot (after modules 1-2)**: Apply LLM basics, prompt engineering
2. **RAG Application (after modules 3-4)**: Integrate embeddings, vector search, retrieval
3. **Intelligent Agent (after modules 5-6)**: Combine RAG, function calling, multi-step reasoning
4. **Multimodal System (after module 7)**: Add vision/audio capabilities
5. **Full Production System (capstone)**: Deploy, monitor, optimize

### Pattern 5: Notebook-First, Then Refactor

**What:** Teach concepts in notebooks for interactivity, then refactor to proper Python modules for production patterns.

**When to use:** Progression from learning (modules 1-3) to production (modules 4+).

**Trade-offs:**
- ✅ Notebooks lower barrier to entry
- ✅ Teaches both exploration and production patterns
- ❌ Can create confusion about "which style to use when"

**Example:**
```
Module 02-03: All code in notebooks (.ipynb)
  - Focus on concepts, immediate visual feedback
  
Module 04: Introduce structure
  - Notebook demonstrates concept
  - Exercise: "Refactor this notebook to .py modules"
  
Module 05+: Production patterns
  - src/ folder with proper Python packages
  - Notebooks import from src/ for documentation
  - Projects use module structure
```

## Data Flow

### Learning Progression Flow

```
Prerequisites Check
       ↓
Module Theory (README)
       ↓
Interactive Demo (Notebook)
       ↓
Guided Exercise (Notebook + Tests)
       ↓
    [Pass Tests?] ─NO→ Review Demo → Retry Exercise
       YES↓
Independent Challenge
       ↓
Peer/Community Review
       ↓
    [Ready for Next?]
       YES↓
Next Module
```

### Content Discovery Flow

```
Learner arrives at repository
       ↓
README.md: Overview, prerequisites, learning path
       ↓
[Has environment?] ─NO→ 00-setup/ → Environment configured
       YES↓
Module 01 README: Learning objectives, time estimate
       ↓
Watch intro video (if available)
       ↓
Work through notebooks sequentially
       ↓
Complete exercises → Run tests
       ↓
[Tests pass?] ─NO→ Check solutions/ → Understand gaps
       YES↓
[Module complete] → Next module or Project
```

### Test Validation Flow

```
Learner writes code in exercise notebook
       ↓
Runs test suite (pytest or notebook cells)
       ↓
Tests execute against learner's implementation
       ↓
    [All pass?]
     ↙     ↘
   YES      NO
    ↓        ↓
Success    Detailed error message
feedback   shows what failed
    ↓        ↓
Continue   Fix and retry
```

## Scaling Considerations

| Scale | Architecture Adjustments |
|-------|--------------------------|
| **Individual learner** | All content in single repository, run locally or in Colab, minimal infrastructure |
| **Small cohort (10-50)** | Add Discord/Slack for community, office hours, consider hosted notebooks (Colab, Binder), automated grading via GitHub Actions |
| **Large cohort (100-1000)** | Dedicated platform (Jupyter Hub, Coursera, etc.), structured forums, TA support, auto-grading infrastructure, usage analytics |
| **MOOC scale (10K+)** | Cloud-hosted notebooks (isolate learners), CDN for assets, automated feedback, discussion moderators, certificates, tiered support |

### Scaling Priorities

1. **First bottleneck: Environment setup**
   - Problem: Different OS, Python versions, dependency conflicts
   - Solution: Docker containers, cloud notebooks (Colab, Binder), or codespaces
   
2. **Second bottleneck: Getting help**
   - Problem: Many learners stuck on same issues, can't scale 1:1 help
   - Solution: Comprehensive FAQ, troubleshooting docs, community forums, AI teaching assistant

3. **Third bottleneck: Test infrastructure**
   - Problem: Tests run on learner machines, inconsistent results
   - Solution: GitHub Actions for automated testing, provide test environments

## Anti-Patterns

### Anti-Pattern 1: The Monolithic Notebook

**What people do:** Put entire module in one massive 500+ cell notebook.

**Why it's wrong:** 
- Overwhelming for learners
- Hard to navigate
- Doesn't teach code organization
- Poor Git diffs

**Do this instead:** Break into focused notebooks (< 100 cells each), one concept per notebook. Use clear naming: `01-concept-intro.ipynb`, `02-concept-advanced.ipynb`.

### Anti-Pattern 2: Hidden Prerequisites

**What people do:** Assume learners "just know" certain concepts, jump straight to advanced material.

**Why it's wrong:**
- Learners get stuck and frustrated
- Can't identify what's missing
- Reinforces imposter syndrome

**Do this instead:** Explicit prerequisites section in every module README. Link to prerequisite content. Provide "test your prerequisites" exercises in module 00.

### Anti-Pattern 3: Solutions Without Explanation

**What people do:** Provide working code solutions with no commentary.

**Why it's wrong:**
- Learners copy-paste without understanding
- Doesn't teach problem-solving process
- Misses teaching opportunity

**Do this instead:** Solutions should be heavily commented, explain *why* each decision was made, show alternative approaches, include "common mistakes" section.

### Anti-Pattern 4: No Tests or Only Manual Testing

**What people do:** "Try it yourself and see if it works" or "compare your output to this screenshot."

**Why it's wrong:**
- Subjective, learners unsure if they're correct
- Doesn't scale
- Doesn't teach testing culture

**Do this instead:** Provide automated tests for objective correctness, rubrics for subjective quality, show how to write tests themselves.

### Anti-Pattern 5: Flat Structure (Everything at Root)

**What people do:**
```
repo/
├── notebook1.ipynb
├── notebook2.ipynb
├── notebook3.ipynb
... (50 files)
```

**Why it's wrong:**
- No clear learning path
- Overwhelming
- No logical grouping
- Hard to find things

**Do this instead:** Use numbered modules with clear topics. Each module is a folder. Makes progression obvious and content discoverable.

### Anti-Pattern 6: Dependency Hell

**What people do:** Install everything globally, no version pinning, "just pip install whatever errors tell you to."

**Why it's wrong:**
- Breaks later when packages update
- Irreproducible environments
- Wastes hours debugging

**Do this instead:** 
- Pin all versions in requirements.txt
- Use virtual environments
- Provide Docker option for consistency
- Include environment validation script

### Anti-Pattern 7: GPU-Required Exercises

**What people do:** Require expensive GPU for every exercise.

**Why it's wrong:**
- Excludes learners without hardware
- High cost barrier
- Not pedagogically necessary for most concepts

**Do this instead:**
- Use small models or API calls for exercises
- Mark GPU-optional content clearly
- Provide free tier API alternatives (Colab free tier, etc.)
- Save GPU-intensive work for optional advanced projects

## Integration Points

### External Services

| Service | Integration Pattern | Notes |
|---------|---------------------|-------|
| **OpenAI API** | Environment variables in .env, helper wrapper functions | Teach API key management, rate limiting, error handling |
| **Hugging Face** | Direct API or transformers library | Show both inference API and local model loading |
| **Vector DBs (Pinecone, Weaviate, Chroma)** | Docker compose for local, credentials for cloud | Teach trade-offs of local vs. hosted |
| **GitHub** | Clone repo, open in Codespaces or Binder | Provide one-click cloud options |
| **Jupyter** | .ipynb files, nbconvert for testing | Standard notebook format, can execute in Colab or local |
| **pytest** | Test discovery in exercises/ folders | Teach standard Python testing |

### Internal Boundaries

| Boundary | Communication | Notes |
|----------|---------------|-------|
| **Module → Module** | Prerequisites clearly documented | Explicit imports of utility functions from prior modules |
| **Theory → Practice** | Notebooks reference README sections | READMEs link to specific notebook cells/sections |
| **Exercise → Test** | Test imports learner's code | Tests validate function signatures, outputs, behavior |
| **Notebook → Python module** | %load or import from src/ | Teach transition from exploration to production |
| **Local → Cloud** | Environment parity via Docker or requirements.txt | Same code runs in Colab, local, or cloud |

## Build Order and Dependencies

### Phase 1: Foundation (Modules 1-2)
- **01-python-fundamentals**: No dependencies
- **02-llm-basics**: Depends on Python basics
- **First checkpoint**: Build simple chatbot

### Phase 2: Core AI Techniques (Modules 3-4)
- **03-embeddings-vectors**: Depends on LLM basics
- **04-rag-systems**: Depends on embeddings + vectors
- **Second checkpoint**: Build RAG application

### Phase 3: Advanced Capabilities (Modules 5-6)
- **05-agents**: Depends on RAG, LLMs, function calling
- **06-multimodal**: Depends on LLM basics, can be parallel to agents
- **Third checkpoint**: Build intelligent agent

### Phase 4: Production & Polish (Modules 7-8)
- **07-deployment**: Depends on having built projects
- **08-monitoring-optimization**: Depends on deployment
- **Final checkpoint**: Production-ready system

### Dependency Graph

```
01-python ──────────→ 02-llms ──────────→ 03-embeddings
                         │                      │
                         ↓                      ↓
                    [Chatbot]              04-rag ──────→ 05-agents
                                               │             │
                                               ↓             ↓
                                          [RAG App]    [Agent System]
                                               │             │
06-multimodal ──────────────────────────┬─────┴─────────────┤
                                        ↓                     ↓
                                   07-deployment ────→ 08-monitoring
                                        │                     │
                                        └──────────┬──────────┘
                                                   ↓
                                           [Portfolio System]
```

## Testing Architecture

### Test Layers

1. **Environment Tests** (00-setup/)
   - Validate Python version
   - Check package installations
   - Verify API keys (without exposing them)
   - Test notebook execution environment

2. **Exercise Tests** (per-module)
   - Unit tests for individual functions
   - Integration tests for small systems
   - Property-based tests for algorithm correctness
   - Example: `test_embedding_dimension()`, `test_rag_retrieval()`

3. **Project Tests** (projects/)
   - End-to-end tests for full applications
   - API endpoint tests
   - Performance benchmarks
   - Example: Test complete RAG pipeline retrieves relevant docs

4. **Notebook Tests** (optional, via nbconvert)
   - Execute all notebooks to verify they run
   - Check for errors in cell execution
   - Validate outputs match expected patterns

### Test Execution Patterns

**Local Development:**
```bash
# Run tests for current module
pytest 03-embeddings/exercises/

# Run all tests
pytest

# Run with verbose output
pytest -v
```

**CI/CD (GitHub Actions):**
```yaml
# Automated on every push
- Run all notebook executions
- Run pytest suite
- Check for broken links in READMEs
- Validate requirements.txt installs
```

**Learner Workflow:**
```python
# In notebook
from exercises.test_exercise import test_my_function
test_my_function()  # Immediate feedback

# Or via command line
!pytest exercises/test_exercise.py -v
```

## Sources

- **Microsoft Generative AI for Beginners**: https://github.com/microsoft/generative-ai-for-beginners
  - Confidence: HIGH (official Microsoft course with 106k stars)
  - Structure: 21 numbered lesson folders, each with README, notebooks, assignments
  - Pattern: Theory (README) → Code (notebooks) → Practice (assignments)
  
- **LLM Course by Maxime Labonne**: https://github.com/mlabonne/llm-course
  - Confidence: HIGH (75k stars, comprehensive LLM learning path)
  - Structure: Organized by learning track (Fundamentals, Scientist, Engineer)
  - Notebooks and tools for hands-on practice
  
- **Anthropic's Courses**: https://github.com/anthropics/courses
  - Confidence: HIGH (official Anthropic educational materials)
  - Structure: 5 separate course folders, each self-contained
  - Jupyter notebooks with interactive tutorials
  
- **LLM Zoomcamp by DataTalks.Club**: https://github.com/DataTalksClub/llm-zoomcamp
  - Confidence: HIGH (4.6k stars, cohort-based learning)
  - Structure: Numbered modules with homework, community support
  - Real-world applications focus (RAG, vector search, monitoring)

---

*Architecture research for: AI Engineering Learning Repository*
*Researched: 2026-02-10*
*Research notes: All sources are established educational repositories with proven learning patterns. Structure recommendations are based on commonalities across all four major courses plus established pedagogical principles.*
