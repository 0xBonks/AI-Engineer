# Module 09: Testing & Validation Infrastructure

## Overview

Build comprehensive testing infrastructure for AI applications. Learn to test LLM outputs with LLM-as-judge, validate embeddings and RAG systems, test agent behavior, and implement automated test runners that track learner progress across all exercises.

## Learning Objectives

By completing this module, you will be able to:

- Configure pytest framework with test templates for each module type
- Create automated test runner that tracks learner progress across all exercises
- Write clear, documented success criteria that tests validate
- Implement LLM-as-judge for evaluating generative tasks where deterministic testing is insufficient
- Display cost estimation for each exercise before execution

## Prerequisites

- **Completed**: Module 02 (Python Fundamentals)
- **Recommended**: Modules 03, 05, 06, 07 for domain-specific testing
- **Required**: Understanding of pytest and testing concepts

## Estimated Time

**8-10 hours** to complete all exercises and demos

## Key Concepts

### 1. Testing AI Applications
- Why AI testing is different
- Deterministic vs probabilistic outputs
- Test categories: unit, integration, evaluation
- Test-driven development for AI
- Continuous evaluation
- Regression testing for AI

### 2. Pytest for AI
- Pytest basics and fixtures
- Parametrized tests for AI
- Async test support
- Custom assertions for AI outputs
- Test organization and discovery
- Reporting and coverage

### 3. LLM-as-Judge
- Using LLMs to evaluate LLM outputs
- Prompt templates for evaluation
- Scoring rubrics and criteria
- Bias in LLM judges
- Cost-effective evaluation strategies
- Validation and ground truth

### 4. Testing LLM Applications
- Prompt testing patterns
- Output format validation
- Semantic similarity checks
- Cost and latency monitoring
- Safety and moderation tests
- Edge case testing

### 5. Testing RAG Systems
- Retrieval quality metrics
- Generation faithfulness
- End-to-end RAG evaluation
- Test datasets and ground truth
- Chunking strategy validation
- Performance benchmarking

### 6. Testing AI Agents
- Tool selection accuracy
- ReAct loop validation
- Multi-agent coordination tests
- Safety and constraint checking
- Determinism and reproducibility
- Cost and iteration limits

## Structure

```
09-testing-validation/
├── README.md                                  # This file
├── notebooks/                                 # Interactive tutorials
│   ├── 01-pytest-basics.ipynb
│   ├── 02-llm-testing.ipynb
│   ├── 03-llm-as-judge.ipynb
│   ├── 04-rag-testing.ipynb
│   ├── 05-agent-testing.ipynb
│   └── 06-progress-tracking.ipynb
├── exercises/                                 # Hands-on challenges
│   ├── 01-basic-tests.py
│   ├── 02-llm-output-tests.py
│   ├── 03-llm-judge-implementation.py
│   ├── 04-rag-evaluation.py
│   ├── 05-agent-tests.py
│   ├── 06-cost-tracking-tests.py
│   └── 07-progress-tracker.py
├── tests/                                     # Automated validation
│   └── test_exercises.py
└── solutions/                                 # Reference implementations
    └── solutions/
```

## Topics Covered

### Why AI Testing is Different
- **Challenge**: Non-deterministic outputs
- **Solution**: Probabilistic assertions, semantic checks
- **Example**: Test "humor" not exact joke text

### LLM-as-Judge
- **Concept**: Use LLM to evaluate LLM outputs
- **Use Case**: When ground truth unavailable or subjective
- **Example**: "Rate this summary on accuracy, coherence"

### RAG Evaluation
- **Retrieval**: Precision, recall, MRR
- **Generation**: Faithfulness, relevance, completeness
- **Example**: Does answer use only retrieved context?

### Agent Testing
- **Behavior**: Does agent select right tools?
- **Safety**: Does agent respect constraints?
- **Example**: Test agent doesn't exceed iteration limit

### Cost Tracking in Tests
- **Concept**: Estimate and track API costs per test
- **Use Case**: Prevent expensive test suites
- **Example**: Skip expensive tests in CI

## Exercises

### Exercise 1: Basic Tests
**File**: `exercises/01-basic-tests.py`

Write pytest tests for AI utility functions.

**Success Criteria**:
- Test token counting accuracy
- Test cost calculation
- Test chunking functions

### Exercise 2: LLM Output Tests
**File**: `exercises/02-llm-output-tests.py`

Test LLM outputs with semantic assertions.

**Success Criteria**:
- Validate output format (JSON, etc.)
- Check semantic similarity
- Test edge cases

### Exercise 3: LLM-as-Judge Implementation
**File**: `exercises/03-llm-judge-implementation.py`

Implement LLM-as-judge for evaluating generative outputs.

**Success Criteria**:
- Create evaluation prompts
- Score outputs on multiple criteria
- Validate against human judgments

### Exercise 4: RAG Evaluation
**File**: `exercises/04-rag-evaluation.py`

Build comprehensive RAG system tests.

**Success Criteria**:
- Test retrieval quality
- Test generation faithfulness
- Measure end-to-end accuracy

### Exercise 5: Agent Tests
**File**: `exercises/05-agent-tests.py`

Test AI agent behavior and safety.

**Success Criteria**:
- Validate tool selection
- Test iteration limits
- Check safety constraints

### Exercise 6: Cost Tracking Tests
**File**: `exercises/06-cost-tracking-tests.py`

Implement cost tracking for all tests.

**Success Criteria**:
- Track API costs per test
- Report total costs
- Skip expensive tests optionally

### Exercise 7: Progress Tracker
**File**: `exercises/07-progress-tracker.py`

Build automated progress tracker for learners.

**Success Criteria**:
- Track completed exercises
- Generate progress reports
- Display module completion status

## Resources

### Official Documentation
- [Pytest Documentation](https://docs.pytest.org/)
- [OpenAI Evals](https://github.com/openai/evals)
- [LangChain Evaluation](https://python.langchain.com/docs/guides/evaluation/)

### Testing Frameworks
- [pytest](https://pytest.org/) - Python testing framework
- [pytest-asyncio](https://pytest-asyncio.readthedocs.io/) - Async tests
- [hypothesis](https://hypothesis.readthedocs.io/) - Property-based testing

### Recommended Reading
- [Testing LLM Applications](https://www.confident-ai.com/blog/the-definitive-guide-to-testing-llm-applications)
- [RAG Evaluation](https://docs.ragas.io/)
- [LLM Evaluation Best Practices](https://github.com/openai/evals/blob/main/docs/eval-templates.md)

## Next Steps

After completing this module:

1. ✅ Write tests for your previous exercises
2. ✅ Implement cost tracking across all modules
3. ➡️ Proceed to **Module 10: Documentation & Portfolio Projects**

## Code Patterns

### Basic Pytest Pattern
```python
import pytest
from utils.cost_tracker import count_tokens

def test_token_counting():
    """Test token counting accuracy."""
    text = "Hello, world!"
    tokens = count_tokens(text)
    
    assert tokens > 0
    assert tokens < 10
    assert isinstance(tokens, int)

@pytest.mark.parametrize("text,expected_range", [
    ("Hello", (1, 3)),
    ("A longer text that should have more tokens", (5, 15)),
])
def test_token_counting_parametrized(text, expected_range):
    tokens = count_tokens(text)
    assert expected_range[0] <= tokens <= expected_range[1]
```

### LLM Output Test Pattern
```python
from openai import OpenAI
import json

client = OpenAI()

def test_llm_json_output():
    """Test that LLM returns valid JSON."""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": "Return a JSON object with name and age fields"
        }],
        response_format={"type": "json_object"}
    )
    
    content = response.choices[0].message.content
    
    # Parse JSON
    data = json.loads(content)
    
    # Validate structure
    assert "name" in data
    assert "age" in data
    assert isinstance(data["age"], int)
```

### LLM-as-Judge Pattern
```python
def llm_as_judge(output: str, criteria: str) -> dict:
    """Evaluate output using LLM as judge."""
    
    eval_prompt = f"""Evaluate the following output based on these criteria:
{criteria}

Output to evaluate:
{output}

Provide scores (1-5) for each criterion and brief justification.
Return as JSON with format: {{"criterion": {{"score": int, "reason": str}}}}"""
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": eval_prompt}],
        response_format={"type": "json_object"},
        temperature=0
    )
    
    return json.loads(response.choices[0].message.content)

def test_summary_quality():
    """Test summary using LLM-as-judge."""
    
    summary = generate_summary(long_text)
    
    evaluation = llm_as_judge(
        summary,
        criteria="""
        1. Accuracy: Does summary capture key points?
        2. Brevity: Is summary concise?
        3. Coherence: Is summary well-written?
        """
    )
    
    # Assert minimum scores
    assert evaluation["Accuracy"]["score"] >= 4
    assert evaluation["Brevity"]["score"] >= 3
    assert evaluation["Coherence"]["score"] >= 4
```

### RAG Evaluation Pattern
```python
def test_rag_retrieval_quality():
    """Test RAG retrieval precision."""
    
    test_cases = [
        {
            "query": "What is the refund policy?",
            "relevant_doc_ids": ["doc_5", "doc_12"]
        },
        # More test cases...
    ]
    
    for case in test_cases:
        results = rag_system.retrieve(case["query"], k=5)
        retrieved_ids = [r["id"] for r in results]
        
        # Calculate precision
        relevant_retrieved = set(retrieved_ids) & set(case["relevant_doc_ids"])
        precision = len(relevant_retrieved) / len(retrieved_ids)
        
        assert precision >= 0.6  # At least 60% precision

def test_rag_faithfulness():
    """Test that RAG answer is faithful to context."""
    
    answer = rag_system.query("What is the refund policy?")
    context = answer["context"]
    
    # Use LLM to check faithfulness
    eval_prompt = f"""Does this answer contain only information from the context?
    
Context: {context}

Answer: {answer['text']}

Respond with YES or NO and brief explanation."""
    
    evaluation = llm_call(eval_prompt)
    assert "YES" in evaluation
```

### Agent Test Pattern
```python
def test_agent_tool_selection():
    """Test that agent selects correct tools."""
    
    agent = create_agent(tools=[calculator, weather, search])
    
    # Test cases with expected tool
    test_cases = [
        ("What is 15 * 23?", "calculator"),
        ("What's the weather in Paris?", "weather"),
        ("Who won the 2020 election?", "search"),
    ]
    
    for query, expected_tool in test_cases:
        result = agent.run(query)
        
        # Check tool usage from logs
        assert expected_tool in result["tools_used"]

def test_agent_iteration_limit():
    """Test that agent respects iteration limits."""
    
    agent = create_agent(max_iterations=5)
    
    # Give impossible task
    result = agent.run("Solve the halting problem")
    
    # Should stop at limit
    assert result["iterations"] <= 5
    assert not result["completed"]
```

### Cost Tracking Pattern
```python
import pytest

@pytest.fixture
def cost_tracker():
    """Track costs for tests."""
    tracker = CostTracker()
    yield tracker
    # Report costs after test
    print(f"\nTest cost: ${tracker.total_cost:.4f}")

def test_with_cost_tracking(cost_tracker):
    """Test that tracks API costs."""
    
    with cost_tracker:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Hello"}]
        )
    
    # Assert cost is reasonable
    assert cost_tracker.total_cost < 0.01

@pytest.mark.expensive
def test_expensive_operation():
    """Test marked as expensive, can be skipped."""
    # This test costs more than $1
    pass

# Run with: pytest -m "not expensive"  # Skip expensive tests
```

## Test Organization

```
tests/
├── conftest.py              # Shared fixtures
├── test_utils/              # Test utilities
│   ├── test_cost_tracker.py
│   └── test_validation.py
├── test_llm/                # LLM tests
│   ├── test_prompts.py
│   └── test_outputs.py
├── test_rag/                # RAG tests
│   ├── test_retrieval.py
│   └── test_generation.py
└── test_agents/             # Agent tests
    ├── test_tools.py
    └── test_behavior.py
```

## Evaluation Metrics

### Retrieval Metrics
- **Precision@K**: Relevant retrieved / Total retrieved
- **Recall@K**: Relevant retrieved / Total relevant
- **MRR**: Mean Reciprocal Rank
- **NDCG**: Normalized Discounted Cumulative Gain

### Generation Metrics
- **BLEU/ROUGE**: Text similarity (for ground truth)
- **Semantic Similarity**: Embedding distance
- **Faithfulness**: Uses only context
- **Relevance**: Addresses the question

### LLM-as-Judge Criteria
- **Accuracy**: Factually correct
- **Completeness**: Covers all aspects
- **Coherence**: Well-structured
- **Relevance**: On-topic

## Common Issues

### Flaky Tests
- Use temperature=0 for consistency
- Set random seeds
- Use retry logic for transient failures
- Mock external services when possible

### Expensive Test Suites
- Mark expensive tests with pytest.mark.expensive
- Cache LLM responses
- Use cheaper models for tests
- Run full suite only on main branch

### LLM-as-Judge Bias
- Validate against human judgments
- Use multiple judges
- Check for systematic biases
- Document limitations

## Notes

- **Test Early**: Write tests as you build
- **Cost Aware**: Track and optimize test costs
- **Continuous**: Run tests on every commit
- **Document**: Clear success criteria for every test
- **Foundation**: Good tests enable confident iteration

---

**Module Status**: 🚧 Content Development | ⬅️ Prev: Multimodal AI | ⏭️ Next: Documentation & Portfolio
