# Phase 1 Plans: Environment Setup & Infrastructure

**Phase Goal:** Learners can set up development environment with zero friction and have infrastructure for cost tracking and version management

**Requirements Coverage:** ENV-01, ENV-02, ENV-03, ENV-04, ENV-05, STRUCT-01, STRUCT-02, STRUCT-03, STRUCT-04, STRUCT-05

**Success Criteria:**
1. Learner can run environment validation script that checks Python 3.11+, all dependencies, and API connectivity
2. Docker development environment starts with one command and includes JupyterLab, all AI libraries, and GPU support
3. Repository structure exists with numbered module folders following consistent layout (README, notebooks/, exercises/, tests/, solutions/)
4. .env.example template provided with clear instructions for all required API keys
5. CI/CD pipeline runs automated tests on every commit to catch breaking dependency changes

---

## Plan 01-01: Create Base Repository Structure
**Requirement:** STRUCT-01, STRUCT-02, STRUCT-03
**Estimated Effort:** 30 minutes
**Dependencies:** None

### Tasks:
1. Create numbered module directories (01- through 10-) with descriptive names
2. Create consistent subdirectory structure for each module:
   - README.md (module overview, learning objectives, theory)
   - notebooks/ (interactive Jupyter demos)
   - exercises/ (starter code and instructions)
   - tests/ (automated validation)
   - solutions/ (completed code with commentary)
3. Create shared utilities directory structure:
   - utils/validation.py (environment validation)
   - utils/cost_tracker.py (API cost tracking)
   - utils/api_helpers.py (common API patterns)
4. Create main README.md with curriculum overview

### Deliverables:
- [ ] Directory structure created following pattern
- [ ] Placeholder README files in each module directory
- [ ] Shared utils/ directory with structure
- [ ] Main repository README with overview

### Verification:
- Tree command shows consistent structure across all 10 modules
- Each module has required subdirectories (README.md, notebooks/, exercises/, tests/, solutions/)
- Shared utils/ directory exists

---

## Plan 01-02: Create Requirements and Dependency Management
**Requirement:** ENV-02
**Estimated Effort:** 45 minutes
**Dependencies:** 01-01

### Tasks:
1. Research current stable versions of all required AI libraries:
   - Python SDK: openai, anthropic, google-generativeai
   - Vector DBs: chromadb, pinecone-client, weaviate-client
   - Frameworks: langchain, llama-index, transformers
   - ML/AI: sentence-transformers, huggingface-hub
   - Utilities: tiktoken, pydantic, python-dotenv, pytest, jupyter
2. Create requirements.txt with pinned versions (==) and comments
3. Create requirements-dev.txt for development tools (black, ruff, mypy, pre-commit)
4. Document dependency update strategy and version pinning policy
5. Add dependency security considerations

### Deliverables:
- [ ] requirements.txt with pinned versions and comments
- [ ] requirements-dev.txt with development tools
- [ ] DEPENDENCIES.md documenting update strategy
- [ ] Security notes for dependency management

### Verification:
- All requirements files parse without errors
- Each dependency has pinned version with comment explaining purpose
- Documentation exists for updating dependencies safely

---

## Plan 01-03: Create .env Template and Configuration
**Requirement:** ENV-05
**Estimated Effort:** 20 minutes
**Dependencies:** 01-01

### Tasks:
1. Create .env.example with all required API keys:
   - OPENAI_API_KEY
   - ANTHROPIC_API_KEY (optional for comparisons)
   - HUGGINGFACE_API_KEY
   - Other service keys as needed
2. Add clear instructions and links to API key acquisition
3. Add configuration variables:
   - LOG_LEVEL
   - COST_TRACKING_ENABLED
   - MODEL_DEFAULTS
4. Create .gitignore to exclude .env and sensitive files
5. Document environment variable usage patterns

### Deliverables:
- [ ] .env.example with all keys and clear comments
- [ ] .gitignore excluding sensitive files
- [ ] ENV_SETUP.md with detailed API key instructions
- [ ] Configuration documentation

### Verification:
- .env.example contains all required variables with descriptions
- .gitignore prevents committing .env
- Documentation clearly explains how to obtain each API key

---

## Plan 01-04: Create Docker Development Environment
**Requirement:** ENV-01, ENV-04, STRUCT-04
**Estimated Effort:** 90 minutes
**Dependencies:** 01-02, 01-03

### Tasks:
1. Create Dockerfile with:
   - Python 3.11+ base image
   - All dependencies from requirements.txt
   - JupyterLab installation and configuration
   - GPU support (CUDA) for local model work
   - Development tools and utilities
2. Create docker-compose.yml for orchestration:
   - Volume mounts for code and data
   - Port mappings (JupyterLab, API services)
   - Environment variable configuration
   - GPU device access
3. Create startup scripts:
   - start.sh for one-command setup
   - Health check script
4. Create comprehensive DOCKER_SETUP.md documentation:
   - Prerequisites (Docker, Docker Compose, GPU drivers if needed)
   - One-command startup instructions
   - Troubleshooting common issues
   - Alternative setups (CPU-only, cloud)

### Deliverables:
- [ ] Dockerfile with all dependencies and JupyterLab
- [ ] docker-compose.yml with proper configuration
- [ ] start.sh script for one-command startup
- [ ] DOCKER_SETUP.md with complete instructions

### Verification:
- Docker image builds successfully
- `./start.sh` launches environment with JupyterLab accessible
- All dependencies available in container
- GPU support works (if GPU available)

---

## Plan 01-05: Create Environment Validation Script
**Requirement:** ENV-03
**Estimated Effort:** 60 minutes
**Dependencies:** 01-02, 01-03

### Tasks:
1. Create utils/validation.py script that checks:
   - Python version (3.11+)
   - All required dependencies installed with correct versions
   - API connectivity tests (OpenAI, Hugging Face, etc.)
   - GPU availability (optional but reported)
   - Environment variables loaded correctly
2. Create validate_env.py CLI script in repository root
3. Add colored output for pass/fail status
4. Add detailed error messages with remediation steps
5. Add --fix flag to attempt automatic fixes where possible
6. Create VALIDATION.md documentation

### Deliverables:
- [ ] utils/validation.py with comprehensive checks
- [ ] validate_env.py CLI script
- [ ] Colored output with clear pass/fail indicators
- [ ] Detailed error messages and remediation guidance
- [ ] VALIDATION.md documentation

### Verification:
- Script runs and checks all requirements
- API connectivity tests work (with valid keys)
- Clear feedback on any missing dependencies
- --fix flag works for common issues

---

## Plan 01-06: Create Cost Tracking Utilities
**Requirement:** STRUCT-03 (shared utilities)
**Estimated Effort:** 75 minutes
**Dependencies:** 01-02, 01-03

### Tasks:
1. Create utils/cost_tracker.py with:
   - Token counting utilities (using tiktoken)
   - Cost calculation for OpenAI models (GPT-4, GPT-3.5, embeddings)
   - Session cost tracking and reporting
   - Cost estimation before API calls
   - Export cost reports to JSON/CSV
2. Create decorators for automatic cost tracking
3. Add cost limits and warnings
4. Create cost reporting dashboard utilities
5. Document cost tracking patterns in COST_TRACKING.md

### Deliverables:
- [ ] utils/cost_tracker.py with comprehensive cost tracking
- [ ] Decorators for automatic tracking
- [ ] Cost reporting and estimation functions
- [ ] COST_TRACKING.md documentation
- [ ] Example usage in notebooks/

### Verification:
- Token counting works accurately
- Cost calculations match OpenAI pricing
- Decorators properly track API calls
- Cost reports generate correctly

---

## Plan 01-07: Create API Helper Utilities
**Requirement:** STRUCT-03 (shared utilities)
**Estimated Effort:** 60 minutes
**Dependencies:** 01-02, 01-03, 01-06

### Tasks:
1. Create utils/api_helpers.py with:
   - Retry logic with exponential backoff
   - Rate limiting utilities
   - Error handling patterns
   - Logging integration
   - Response validation helpers
2. Create utils/model_helpers.py with:
   - Model selection utilities
   - Common prompt templates
   - Response parsing helpers
   - Streaming response handlers
3. Add comprehensive docstrings and type hints
4. Create API_PATTERNS.md documentation

### Deliverables:
- [ ] utils/api_helpers.py with retry/rate limiting
- [ ] utils/model_helpers.py with model utilities
- [ ] Type hints and docstrings throughout
- [ ] API_PATTERNS.md with usage examples

### Verification:
- Retry logic works with exponential backoff
- Rate limiting prevents API overuse
- Error handling catches common issues
- All functions have type hints and docs

---

## Plan 01-08: Create CI/CD Pipeline
**Requirement:** ENV-05, STRUCT-05
**Estimated Effort:** 75 minutes
**Dependencies:** 01-02, 01-05

### Tasks:
1. Create .github/workflows/ci.yml with:
   - Test workflow on push/PR to main
   - Python version matrix (3.11, 3.12)
   - Dependency installation and caching
   - Run environment validation
   - Run pytest on all tests
   - Code quality checks (ruff, mypy)
2. Create .github/workflows/dependency-check.yml:
   - Weekly dependency security scans
   - Alert on outdated dependencies
3. Configure branch protection rules documentation
4. Create CI_CD.md documentation

### Deliverables:
- [ ] .github/workflows/ci.yml with comprehensive testing
- [ ] .github/workflows/dependency-check.yml for security
- [ ] CI_CD.md with pipeline documentation
- [ ] Example test files that pass in CI

### Verification:
- CI pipeline runs successfully on push
- All checks pass (validation, tests, quality)
- Dependency scans work
- Documentation clear for contributors

---

## Plan 01-09: Create Main Repository README
**Requirement:** STRUCT-01, Documentation
**Estimated Effort:** 45 minutes
**Dependencies:** All previous plans

### Tasks:
1. Create comprehensive main README.md with:
   - Project overview and value proposition
   - Learning path visualization (10 phases)
   - Quick start guide (Docker setup → validation → first exercise)
   - Prerequisites and learner background
   - Repository structure explanation
   - Progress tracking section
   - Contributing guidelines
   - License information
2. Add badges for CI status, Python version, etc.
3. Create CONTRIBUTING.md for future contributors
4. Create LICENSE file (MIT or appropriate)

### Deliverables:
- [ ] Main README.md with comprehensive content
- [ ] Learning path visualization
- [ ] CONTRIBUTING.md for contributors
- [ ] LICENSE file

### Verification:
- README clear and inviting for learners
- Quick start guide works for new users
- All links and references valid
- Professional presentation

---

## Plan 01-10: Create Initial Module README Templates
**Requirement:** STRUCT-02, Documentation
**Estimated Effort:** 60 minutes
**Dependencies:** 01-01, 01-09

### Tasks:
1. Create README template for module directories
2. Populate initial content for each module README:
   - Module overview and objectives
   - Prerequisites (which earlier modules needed)
   - Estimated completion time
   - Key concepts covered
   - Resources and references
   - Exercise overview
3. Create placeholders for notebooks, exercises, solutions
4. Ensure consistent formatting across all modules

### Deliverables:
- [ ] README_TEMPLATE.md for modules
- [ ] README.md populated for all 10 modules
- [ ] Consistent structure and formatting
- [ ] Clear learning objectives per module

### Verification:
- All 10 modules have comprehensive READMEs
- Prerequisites clearly stated
- Learning objectives specific and measurable
- Consistent formatting and structure

---

## Plan 01-11: Integration Testing and Documentation Review
**Requirement:** All Phase 1 requirements
**Estimated Effort:** 45 minutes
**Dependencies:** All previous plans

### Tasks:
1. End-to-end test of setup process:
   - Clone repository
   - Run Docker setup
   - Run validation script
   - Verify all utilities work
   - Check documentation accuracy
2. Create SETUP_GUIDE.md with complete walkthrough
3. Test on clean environment (fresh VM or container)
4. Document any issues and create fixes
5. Create troubleshooting FAQ
6. Review all Phase 1 success criteria

### Deliverables:
- [ ] SETUP_GUIDE.md with end-to-end walkthrough
- [ ] TROUBLESHOOTING.md with common issues
- [ ] All integration tests pass
- [ ] Phase 1 success criteria verified

### Verification:
- Complete setup works on clean environment
- All 5 success criteria met:
  1. ✓ Validation script checks everything
  2. ✓ Docker starts with one command
  3. ✓ Repository structure complete
  4. ✓ .env.example provided
  5. ✓ CI/CD pipeline functional
- Documentation complete and accurate
- Ready for Phase 2 work

---

## Summary

**Total Plans:** 11
**Estimated Total Effort:** ~10 hours
**Critical Path:** 01-01 → 01-02 → 01-04 → 01-11

**Key Deliverables:**
- Complete repository structure (10 modules)
- Docker development environment
- Environment validation tooling
- Cost tracking utilities
- API helper utilities
- CI/CD pipeline
- Comprehensive documentation

**Success Criteria Mapping:**
- Criterion 1 (validation script): Plans 01-05, 01-11
- Criterion 2 (Docker environment): Plans 01-04, 01-11
- Criterion 3 (repository structure): Plans 01-01, 01-10, 01-11
- Criterion 4 (.env template): Plans 01-03, 01-11
- Criterion 5 (CI/CD pipeline): Plans 01-08, 01-11

**Phase 1 Completion:** When all 11 plans delivered and verified, Phase 1 requirements (ENV-01 to ENV-05, STRUCT-01 to STRUCT-05) will be complete.
