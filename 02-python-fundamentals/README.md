# Module 02: Python Fundamentals for AI

## Overview

Master the essential Python patterns used throughout AI engineering: async programming for concurrent API calls, type safety with Pydantic, production-grade error handling, and advanced patterns like decorators and context managers. This module bridges general Python knowledge to AI-specific applications.

## Learning Objectives

By completing this module, you will be able to:

- Write async code using async/await for concurrent API calls with proper error handling
- Use type hints and Pydantic for data validation in AI applications
- Implement production-grade logging and error handling patterns
- Interact with REST APIs, parse JSON, and handle file I/O for common AI data formats
- Understand OOP patterns (classes, decorators, context managers) used in AI frameworks

## Prerequisites

- **Completed**: Module 01 (Environment Setup)
- **Experience**: Basic Python knowledge (variables, functions, control flow)
- **Skills**: Comfortable with command line and code editors

## Estimated Time

**8-12 hours** to complete all exercises and demos

## Key Concepts

### 1. Async Programming
- async/await syntax and semantics
- Concurrent vs parallel execution
- asyncio event loops
- Handling multiple API calls efficiently
- Common pitfalls and debugging async code

### 2. Type Safety & Validation
- Type hints for function signatures
- Pydantic models for data validation
- Generic types and type checking
- Benefits for AI application development
- Using mypy for static type checking

### 3. Error Handling & Logging
- Try/except patterns and exception hierarchies
- Custom exceptions for AI errors
- Structured logging with context
- Error recovery strategies
- Retry logic with exponential backoff

### 4. API Interaction Patterns
- Using requests and httpx libraries
- Async HTTP clients
- JSON serialization/deserialization
- Rate limiting and throttling
- Response validation

### 5. Data Handling
- File I/O for datasets (CSV, JSON, JSONL)
- Streaming large files
- Path handling with pathlib
- Data validation and cleaning
- Working with AI-specific formats

### 6. Advanced Python Patterns
- Decorators for cross-cutting concerns
- Context managers for resource management
- Class design for AI components
- Functional programming patterns
- Generator expressions for memory efficiency

## Structure

```
02-python-fundamentals/
├── README.md                      # This file
├── notebooks/                     # Interactive tutorials
│   ├── 01-async-programming.ipynb
│   ├── 02-type-safety.ipynb
│   ├── 03-error-handling.ipynb
│   ├── 04-api-patterns.ipynb
│   ├── 05-data-handling.ipynb
│   └── 06-advanced-patterns.ipynb
├── exercises/                     # Hands-on challenges
│   ├── 01-async-api-calls.py
│   ├── 02-pydantic-models.py
│   ├── 03-logging-setup.py
│   ├── 04-rest-client.py
│   ├── 05-data-processing.py
│   └── 06-decorators.py
├── tests/                         # Automated validation
│   └── test_exercises.py
└── solutions/                     # Reference implementations
    └── solutions/
```

## Topics Covered

### Async Programming for AI
- **Why it matters**: AI applications make many I/O-bound API calls
- **Real-world use**: Batch processing with OpenAI API
- **Example**: Process 100 documents concurrently vs sequentially

### Type Safety with Pydantic
- **Why it matters**: Validate API responses and prevent runtime errors
- **Real-world use**: Parse OpenAI API responses safely
- **Example**: Define models for chat completions, embeddings, tool calls

### Production Logging
- **Why it matters**: Debug issues in production AI systems
- **Real-world use**: Track token usage, costs, and errors
- **Example**: Structured logging with request IDs and context

### API Interaction Patterns
- **Why it matters**: Most AI capabilities come from APIs
- **Real-world use**: Robust OpenAI API client with retries
- **Example**: Handle rate limits, timeouts, and transient failures

### Data Processing
- **Why it matters**: Prepare data for embeddings, fine-tuning, RAG
- **Real-world use**: Process large document collections
- **Example**: Stream and chunk 1GB dataset efficiently

### Advanced Patterns
- **Why it matters**: Used extensively in LangChain, LlamaIndex, etc.
- **Real-world use**: Implement cost tracking decorators
- **Example**: Context manager for API session management

## Exercises

### Exercise 1: Async API Calls
**File**: `exercises/01-async-api-calls.py`

Implement concurrent API calls using async/await to process multiple requests efficiently.

**Success Criteria**:
- Make 10 concurrent API calls
- Handle errors gracefully
- Compare performance to sequential calls

### Exercise 2: Pydantic Models
**File**: `exercises/02-pydantic-models.py`

Create Pydantic models to validate OpenAI API responses and configuration.

**Success Criteria**:
- Define models for chat completions
- Validate responses automatically
- Handle validation errors

### Exercise 3: Production Logging
**File**: `exercises/03-logging-setup.py`

Set up structured logging with appropriate levels and context.

**Success Criteria**:
- Configure logger with multiple handlers
- Log API calls with request context
- Implement log rotation

### Exercise 4: REST Client
**File**: `exercises/04-rest-client.py`

Build a robust REST client with retry logic and rate limiting.

**Success Criteria**:
- Implement exponential backoff
- Handle rate limits (429 errors)
- Add request/response logging

### Exercise 5: Data Processing
**File**: `exercises/05-data-processing.py`

Process AI datasets efficiently using streaming and chunking.

**Success Criteria**:
- Stream large files without loading into memory
- Chunk documents for embeddings
- Validate data format

### Exercise 6: Decorators & Context Managers
**File**: `exercises/06-decorators.py`

Implement decorators for cost tracking and context managers for resource management.

**Success Criteria**:
- Create cost tracking decorator
- Build API session context manager
- Apply patterns to existing code

## Resources

### Official Documentation
- [Python Async IO](https://docs.python.org/3/library/asyncio.html)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Python Logging](https://docs.python.org/3/library/logging.html)
- [Requests Library](https://requests.readthedocs.io/)
- [HTTPX (Async HTTP)](https://www.python-httpx.org/)

### Recommended Reading
- [Real Python: Async IO](https://realpython.com/async-io-python/)
- [FastAPI Type Hints](https://fastapi.tiangolo.com/python-types/)
- [Effective Python](https://effectivepython.com/) - Book by Brett Slatkin

### Utilities
- **utils/api_helpers.py**: Reference implementations
- **utils/cost_tracker.py**: Decorator examples

## Next Steps

After completing this module:

1. ✅ Verify all exercise tests pass
2. ✅ Review solution code for best practices
3. ➡️ Proceed to **Module 03: AI Fundamentals & OpenAI API**

## Common Patterns

### Async API Call Pattern
```python
import asyncio
import httpx

async def fetch_completion(prompt: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            json={"model": "gpt-4", "messages": [{"role": "user", "content": prompt}]},
            headers={"Authorization": f"Bearer {api_key}"}
        )
        return response.json()

# Run multiple concurrently
results = await asyncio.gather(*[fetch_completion(p) for p in prompts])
```

### Pydantic Validation Pattern
```python
from pydantic import BaseModel

class ChatResponse(BaseModel):
    id: str
    model: str
    choices: list[dict]
    
    def get_content(self) -> str:
        return self.choices[0]["message"]["content"]

# Auto-validates and provides type safety
response = ChatResponse(**api_response)
```

## Notes

- **Prerequisites Important**: Strong Python fundamentals accelerate all future modules
- **Practice Essential**: Work through all exercises; don't just read solutions
- **AI Context**: Every pattern taught applies directly to AI development
- **Reference Later**: You'll revisit these patterns throughout the curriculum

---

**Module Status**: 🚧 Content Development | ⬅️ Prev: Environment Setup | ⏭️ Next: AI Fundamentals
