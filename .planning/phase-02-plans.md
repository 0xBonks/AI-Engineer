# Phase 2 Plans: Python Fundamentals for AI

**Phase Goal:** Learners master Python patterns essential for AI engineering (async, types, error handling)

**Requirements Coverage:** PY-01, PY-02, PY-03, PY-04, PY-05, PY-06, PY-07

**Success Criteria:**
1. Learner can write async code using async/await for concurrent API calls with proper error handling
2. Learner can use type hints and Pydantic for data validation in AI applications
3. Learner can implement production-grade logging and error handling patterns
4. Learner can interact with REST APIs, parse JSON, and handle file I/O for common AI data formats
5. Learner understands OOP patterns (classes, decorators, context managers) used in AI frameworks

---

## Plan 02-01: Async Programming Module
**Requirement:** PY-01
**Estimated Effort:** 3-4 hours
**Dependencies:** Phase 1 complete

### Tasks:
1. Create notebook demonstrating async/await basics
   - Event loop fundamentals
   - async/await syntax
   - Running async code in Jupyter
2. Create notebook for concurrent API calls
   - asyncio.gather for parallel execution
   - Comparison: sequential vs concurrent performance
   - Real example: fetching multiple URLs
3. Create exercise: Concurrent OpenAI API calls
   - Process multiple prompts in parallel
   - Measure performance improvement
   - Handle errors in concurrent context
4. Create notebook on async patterns for AI
   - Semaphores for rate limiting
   - asyncio.Queue for work distribution
   - Timeout handling with asyncio.wait_for
5. Write tests for async exercises
6. Document common async pitfalls and solutions

### Deliverables:
- [ ] `notebooks/01-async-basics.ipynb` - async/await fundamentals
- [ ] `notebooks/02-concurrent-api-calls.ipynb` - parallel execution patterns
- [ ] `notebooks/03-async-patterns-ai.ipynb` - AI-specific async patterns
- [ ] `exercises/01-async-api-calls.py` - concurrent OpenAI calls exercise
- [ ] `exercises/02-rate-limited-async.py` - async with rate limiting
- [ ] `tests/test_async_exercises.py` - automated tests
- [ ] Solutions with detailed explanations

### Verification:
- Notebooks run without errors in JupyterLab
- Exercises demonstrate 3-5x speedup over sequential
- Tests pass for async code patterns
- Error handling works correctly in concurrent scenarios

---

## Plan 02-02: Type Safety Module
**Requirement:** PY-02
**Estimated Effort:** 2-3 hours
**Dependencies:** 02-01 (async types used in examples)

### Tasks:
1. Create notebook on Python type hints
   - Basic types (int, str, list, dict)
   - Generic types (List[str], Dict[str, Any])
   - Optional and Union types
   - Type hints for functions and classes
2. Create notebook on Pydantic for AI applications
   - BaseModel basics
   - Field validation and constraints
   - Nested models
   - Parsing API responses with Pydantic
3. Create exercise: Model OpenAI API responses
   - ChatCompletion Pydantic model
   - Embedding response model
   - Function call response model
4. Create exercise: Validate configuration
   - Config model with Pydantic
   - Environment variable validation
   - Default values and constraints
5. Set up mypy for static type checking
6. Write tests validating Pydantic models

### Deliverables:
- [ ] `notebooks/01-type-hints.ipynb` - Python type hints guide
- [ ] `notebooks/02-pydantic-basics.ipynb` - Pydantic fundamentals
- [ ] `notebooks/03-pydantic-for-ai.ipynb` - AI-specific Pydantic patterns
- [ ] `exercises/01-openai-models.py` - Model OpenAI responses
- [ ] `exercises/02-config-validation.py` - Configuration validation
- [ ] `tests/test_type_exercises.py` - Pydantic validation tests
- [ ] mypy.ini configuration
- [ ] Solutions with type annotations

### Verification:
- All code passes mypy type checking
- Pydantic models validate API responses correctly
- Invalid data raises appropriate validation errors
- Type hints improve IDE autocomplete

---

## Plan 02-03: Error Handling and Logging Module
**Requirement:** PY-03
**Estimated Effort:** 2-3 hours
**Dependencies:** 02-01 (async error handling), 02-02 (typed exceptions)

### Tasks:
1. Create notebook on Python exception handling
   - try/except/finally patterns
   - Custom exceptions
   - Exception hierarchies
   - Context managers for cleanup
2. Create notebook on production logging
   - logging module setup
   - Log levels (DEBUG, INFO, WARNING, ERROR)
   - Structured logging with context
   - Log formatting and handlers
3. Create notebook on AI-specific error patterns
   - API errors (rate limits, timeouts)
   - Retry logic with exponential backoff
   - Circuit breaker pattern
   - Graceful degradation
4. Create exercise: Robust API client
   - Handle all OpenAI API errors
   - Implement retry with backoff
   - Log all API interactions
   - Track error metrics
5. Create exercise: Production logging setup
   - Configure multi-level logging
   - Add request IDs for tracing
   - Log to file with rotation
6. Write tests for error handling

### Deliverables:
- [ ] `notebooks/01-exception-handling.ipynb` - Exception patterns
- [ ] `notebooks/02-production-logging.ipynb` - Logging setup
- [ ] `notebooks/03-ai-error-patterns.ipynb` - AI-specific patterns
- [ ] `exercises/01-robust-api-client.py` - Error-resilient client
- [ ] `exercises/02-logging-setup.py` - Production logging config
- [ ] `exercises/03-retry-logic.py` - Exponential backoff implementation
- [ ] `tests/test_error_handling.py` - Error handling tests
- [ ] Solutions with comprehensive error handling

### Verification:
- API client handles all error types gracefully
- Retry logic implements exponential backoff correctly
- Logs contain sufficient context for debugging
- Tests cover error scenarios

---

## Plan 02-04: Environment and Package Management Module
**Requirement:** PY-04
**Estimated Effort:** 1-2 hours
**Dependencies:** Phase 1 (building on existing setup)

### Tasks:
1. Create notebook on virtual environments
   - venv basics and best practices
   - When to use vs Docker
   - Activating and deactivating
2. Create notebook on dependency management
   - requirements.txt best practices
   - Version pinning strategies
   - requirements-dev.txt separation
   - Using pip-tools for dependency resolution
3. Create notebook on environment variables
   - python-dotenv usage
   - .env file patterns
   - Environment-specific configuration
   - Secret management best practices
4. Create exercise: Multi-environment setup
   - dev/staging/prod configurations
   - Environment-specific .env files
   - Config validation with Pydantic
5. Document dependency update process
6. Create checklist for dependency security

### Deliverables:
- [ ] `notebooks/01-virtual-environments.ipynb` - Virtual env guide
- [ ] `notebooks/02-dependency-management.ipynb` - Dependency best practices
- [ ] `notebooks/03-environment-config.ipynb` - Config management
- [ ] `exercises/01-multi-env-setup.py` - Multiple environment configs
- [ ] `exercises/02-dependency-audit.py` - Check for outdated packages
- [ ] `docs/DEPENDENCY_MANAGEMENT.md` - Process documentation
- [ ] Solutions with security best practices

### Verification:
- Virtual environment setup works on all platforms
- Dependency pinning prevents version conflicts
- Environment variables load correctly
- Security best practices documented

---

## Plan 02-05: API Interaction Patterns Module
**Requirement:** PY-05
**Estimated Effort:** 3-4 hours
**Dependencies:** 02-01 (async), 02-02 (types), 02-03 (errors)

### Tasks:
1. Create notebook on requests library
   - GET, POST, PUT, DELETE methods
   - Headers and authentication
   - Query parameters and request bodies
   - Response handling
2. Create notebook on httpx (async HTTP)
   - Async HTTP client
   - Connection pooling
   - Timeout configuration
   - Streaming responses
3. Create notebook on REST API patterns for AI
   - OpenAI API structure
   - Anthropic API comparison
   - Pagination patterns
   - Rate limiting headers
4. Create exercise: Build HTTP client wrapper
   - Async client with retry logic
   - Automatic error handling
   - Request/response logging
   - Cost tracking integration
5. Create exercise: API response parsing
   - JSON deserialization
   - Pydantic validation
   - Error response handling
6. Create exercise: Streaming API responses
   - Server-sent events (SSE)
   - Chunked response handling
   - Real-time token streaming
7. Write integration tests with mock API

### Deliverables:
- [ ] `notebooks/01-requests-basics.ipynb` - requests library guide
- [ ] `notebooks/02-async-http.ipynb` - httpx async patterns
- [ ] `notebooks/03-rest-api-patterns.ipynb` - REST API best practices
- [ ] `notebooks/04-streaming-responses.ipynb` - Streaming patterns
- [ ] `exercises/01-http-client-wrapper.py` - Robust HTTP client
- [ ] `exercises/02-api-response-parser.py` - Response parsing
- [ ] `exercises/03-streaming-handler.py` - Streaming implementation
- [ ] `tests/test_api_exercises.py` - API interaction tests
- [ ] Solutions with production-grade patterns

### Verification:
- HTTP client handles all common scenarios
- Async requests perform faster than sync
- Streaming responses work correctly
- Tests use mocking to avoid real API calls
- Cost tracking integrated

---

## Plan 02-06: Data Handling Module
**Requirement:** PY-06
**Estimated Effort:** 2-3 hours
**Dependencies:** 02-02 (types for data validation)

### Tasks:
1. Create notebook on file I/O patterns
   - Reading/writing text files
   - pathlib for path handling
   - Context managers for file safety
   - Encoding and character sets
2. Create notebook on JSON handling
   - json module basics
   - JSONL format for LLM training
   - Streaming large JSON files
   - JSON schema validation
3. Create notebook on CSV/tabular data
   - csv module basics
   - pandas for data manipulation
   - Reading large datasets efficiently
   - Data cleaning for AI inputs
4. Create notebook on AI-specific formats
   - Embeddings file formats
   - Vector database exports
   - Fine-tuning data formats
   - Chunking strategies
5. Create exercise: Process large dataset
   - Stream 1GB+ file without loading to memory
   - Chunk documents for embeddings
   - Validate data format
   - Export to JSONL
6. Create exercise: Dataset preparation
   - Clean and validate training data
   - Convert formats (CSV → JSONL)
   - Split train/validation sets
7. Write tests for data processing

### Deliverables:
- [ ] `notebooks/01-file-io-patterns.ipynb` - File I/O guide
- [ ] `notebooks/02-json-handling.ipynb` - JSON processing
- [ ] `notebooks/03-csv-tabular-data.ipynb` - Tabular data handling
- [ ] `notebooks/04-ai-data-formats.ipynb` - AI-specific formats
- [ ] `exercises/01-large-file-processing.py` - Stream large files
- [ ] `exercises/02-document-chunking.py` - Chunking implementation
- [ ] `exercises/03-dataset-preparation.py` - Training data prep
- [ ] `tests/test_data_exercises.py` - Data processing tests
- [ ] Solutions with memory-efficient patterns

### Verification:
- Large files processed without memory issues
- Data validation catches format errors
- Chunking produces appropriate sizes
- All data transformations reversible
- Tests include edge cases

---

## Plan 02-07: OOP and Advanced Patterns Module
**Requirement:** PY-07
**Estimated Effort:** 3-4 hours
**Dependencies:** All previous plans (uses all patterns)

### Tasks:
1. Create notebook on Python classes for AI
   - Class design principles
   - Inheritance and composition
   - Abstract base classes
   - Dataclasses for data structures
2. Create notebook on decorators
   - Function decorators
   - Class decorators
   - Parameterized decorators
   - Real example: cost tracking decorator
3. Create notebook on context managers
   - `with` statement
   - `__enter__` and `__exit__`
   - contextlib.contextmanager decorator
   - Real example: API session manager
4. Create notebook on design patterns for AI
   - Factory pattern for model selection
   - Strategy pattern for prompts
   - Observer pattern for monitoring
   - Singleton for configuration
5. Create exercise: Build reusable AI components
   - LLMClient abstract base class
   - OpenAIClient implementation
   - Cost tracking decorator
   - Session context manager
6. Create exercise: Implement decorator patterns
   - Retry decorator
   - Cache decorator
   - Timing decorator
   - Logging decorator
7. Create capstone exercise combining all patterns
   - Production-ready RAG component
   - Uses async, types, errors, logging
   - Context managers for resources
   - Decorators for cross-cutting concerns
8. Write comprehensive tests

### Deliverables:
- [ ] `notebooks/01-classes-for-ai.ipynb` - Class design guide
- [ ] `notebooks/02-decorators.ipynb` - Decorator patterns
- [ ] `notebooks/03-context-managers.ipynb` - Context manager patterns
- [ ] `notebooks/04-design-patterns-ai.ipynb` - AI design patterns
- [ ] `exercises/01-ai-components.py` - Reusable AI classes
- [ ] `exercises/02-decorator-patterns.py` - Decorator implementations
- [ ] `exercises/03-context-managers.py` - Context manager exercises
- [ ] `exercises/04-capstone-integration.py` - Integration exercise
- [ ] `tests/test_oop_exercises.py` - OOP pattern tests
- [ ] Solutions demonstrating best practices

### Verification:
- Classes follow SOLID principles
- Decorators work with async functions
- Context managers handle errors correctly
- Capstone exercise demonstrates all patterns
- Code is maintainable and extensible
- Tests achieve >80% coverage

---

## Plan 02-08: Integration and Testing
**Requirement:** All Phase 2 requirements
**Estimated Effort:** 2-3 hours
**Dependencies:** All previous plans (02-01 through 02-07)

### Tasks:
1. Create end-to-end integration examples
   - Complete async API workflow
   - Full data processing pipeline
   - Production-grade error handling
2. Verify all notebooks run without errors
   - Test in fresh Jupyter environment
   - Fix any dependency issues
   - Ensure consistent formatting
3. Verify all exercises have tests
   - pytest runs all tests successfully
   - Coverage reports generated
   - Edge cases covered
4. Create progress tracker for Phase 2
   - Checklist for learners
   - Self-assessment quiz
   - Practice projects
5. Update module README with final content
   - Add notebook links
   - Add exercise descriptions
   - Add troubleshooting tips
6. Create Phase 2 completion verification script
   - Check all exercises completed
   - Verify test passage
   - Generate progress report
7. Document common mistakes and solutions
8. Create suggested learning path variations

### Deliverables:
- [ ] `notebooks/99-integration-examples.ipynb` - E2E examples
- [ ] All notebooks tested and verified
- [ ] All exercises have passing tests
- [ ] `docs/PHASE_2_COMPLETION.md` - Completion guide
- [ ] `scripts/verify_phase2.py` - Verification script
- [ ] Updated module README with all content
- [ ] `docs/COMMON_MISTAKES.md` - Troubleshooting
- [ ] Integration tests passing in CI/CD

### Verification:
- All 7 module requirements (PY-01 through PY-07) complete
- All 5 success criteria demonstrable
- Pytest suite passes with >80% coverage
- Notebooks run error-free in clean environment
- Documentation complete and accurate
- Ready for Phase 3

---

## Summary

**Total Plans:** 8
**Estimated Total Effort:** 18-26 hours
**Critical Path:** 02-01 → 02-02 → 02-03 → 02-05 → 02-07 → 02-08

**Key Deliverables:**
- 20+ interactive Jupyter notebooks
- 15+ hands-on exercises
- Comprehensive test suite
- Production-grade code examples
- Integration with Phase 1 infrastructure

**Success Criteria Mapping:**
- Criterion 1 (async code): Plan 02-01
- Criterion 2 (types/Pydantic): Plan 02-02
- Criterion 3 (logging/errors): Plan 02-03
- Criterion 4 (REST APIs/file I/O): Plans 02-05, 02-06
- Criterion 5 (OOP patterns): Plan 02-07
- Integration: Plan 02-08

**Phase 2 Completion:** When all 8 plans delivered and verified, Phase 2 requirements (PY-01 to PY-07) will be complete, and learners will have mastered Python fundamentals for AI engineering.
