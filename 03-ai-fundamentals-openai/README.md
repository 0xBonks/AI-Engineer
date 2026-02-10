# Module 03: AI Fundamentals & OpenAI API

## Overview

Dive into the world of Large Language Models (LLMs) and learn to build applications using the OpenAI API. Understand LLM concepts, master prompt engineering, implement chat completions with streaming, and optimize for cost and performance.

## Learning Objectives

By completing this module, you will be able to:

- Explain when to use pre-trained models vs fine-tuning and understand capabilities/limitations of different LLMs
- Implement Chat Completions API with streaming, error handling, and cost tracking
- Apply prompt engineering techniques (few-shot, chain-of-thought, system prompts) to improve outputs
- Calculate token usage, optimize prompts for cost, and implement rate limiting
- Use OpenAI Playground effectively for experimentation and understand fine-tuning workflows

## Prerequisites

- **Completed**: Module 02 (Python Fundamentals)
- **Required**: OpenAI API key (see [ENV_SETUP.md](../ENV_SETUP.md))
- **Budget**: ~$5-10 for exercises (includes cost tracking practice)

## Estimated Time

**12-15 hours** to complete all exercises and demos

## Key Concepts

### 1. LLM Fundamentals
- What are Large Language Models?
- Pre-trained models vs fine-tuning
- Token limits and context windows
- Model capabilities and limitations
- Temperature, top_p, and other parameters
- Comparing GPT-4, GPT-3.5, and other models

### 2. OpenAI Chat Completions API
- API structure and authentication
- Messages format (system, user, assistant)
- Streaming responses for real-time UX
- Function calling / Tools API
- Response formats and parsing
- Error handling and retries

### 3. Prompt Engineering
- System prompts for behavior control
- Few-shot learning examples
- Chain-of-thought prompting
- Role prompting and personas
- Prompt templates and variables
- Negative prompting and constraints

### 4. Token Management & Cost Optimization
- Token counting with tiktoken
- Pricing models (GPT-4 vs GPT-3.5)
- Strategies to reduce token usage
- Caching and response reuse
- Batch processing for efficiency
- Cost tracking and budgets

### 5. Advanced Techniques
- JSON mode for structured output
- Seed parameter for reproducibility
- Multi-turn conversations and memory
- Rate limiting strategies
- Parallel API calls
- Error recovery patterns

## Structure

```
03-ai-fundamentals-openai/
├── README.md                          # This file
├── notebooks/                         # Interactive tutorials
│   ├── 01-llm-fundamentals.ipynb
│   ├── 02-chat-completions-basics.ipynb
│   ├── 03-streaming-responses.ipynb
│   ├── 04-prompt-engineering.ipynb
│   ├── 05-token-optimization.ipynb
│   └── 06-advanced-techniques.ipynb
├── exercises/                         # Hands-on challenges
│   ├── 01-first-api-call.py
│   ├── 02-streaming-chat.py
│   ├── 03-prompt-templates.py
│   ├── 04-cost-tracking.py
│   ├── 05-few-shot-learning.py
│   └── 06-function-calling.py
├── tests/                             # Automated validation
│   └── test_exercises.py
└── solutions/                         # Reference implementations
    └── solutions/
```

## Topics Covered

### Understanding LLMs
- **Concept**: Pre-trained models learn from massive text corpora
- **Use Case**: Choose the right model for your task (speed vs quality)
- **Example**: GPT-4 for complex reasoning, GPT-3.5 for simple tasks

### Chat Completions API
- **Concept**: Conversational interface to LLMs via API
- **Use Case**: Build chatbots, assistants, content generators
- **Example**: Multi-turn customer support bot

### Prompt Engineering
- **Concept**: Craft inputs to guide model behavior
- **Use Case**: Improve output quality without fine-tuning
- **Example**: Few-shot examples make the model follow format

### Token Optimization
- **Concept**: Tokens = cost; optimization = savings
- **Use Case**: Production systems with high volume
- **Example**: Reduce system prompt from 500 to 100 tokens

### Streaming Responses
- **Concept**: Receive output incrementally as it's generated
- **Use Case**: Better UX for long-form content
- **Example**: ChatGPT-like typing effect

## Exercises

### Exercise 1: First API Call
**File**: `exercises/01-first-api-call.py`

Make your first call to the OpenAI Chat Completions API.

**Success Criteria**:
- Successfully authenticate with API key
- Send a message and receive a response
- Handle errors gracefully

### Exercise 2: Streaming Chat
**File**: `exercises/02-streaming-chat.py`

Implement streaming responses for real-time output.

**Success Criteria**:
- Stream responses chunk by chunk
- Display incremental output
- Track tokens for streamed responses

### Exercise 3: Prompt Templates
**File**: `exercises/03-prompt-templates.py`

Create reusable prompt templates with variables.

**Success Criteria**:
- Define system and user prompt templates
- Inject variables safely
- Version control prompts

### Exercise 4: Cost Tracking
**File**: `exercises/04-cost-tracking.py`

Track token usage and calculate costs accurately.

**Success Criteria**:
- Count tokens before API calls
- Track actual usage from responses
- Generate cost reports

### Exercise 5: Few-Shot Learning
**File**: `exercises/05-few-shot-learning.py`

Use few-shot examples to teach the model specific patterns.

**Success Criteria**:
- Provide 2-5 example inputs/outputs
- Model follows the pattern
- Compare with zero-shot performance

### Exercise 6: Function Calling
**File**: `exercises/06-function-calling.py`

Implement OpenAI Functions/Tools for structured outputs.

**Success Criteria**:
- Define function schemas
- Model returns function calls
- Execute functions and return results

## Resources

### Official Documentation
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [OpenAI Playground](https://platform.openai.com/playground)
- [Chat Completions Guide](https://platform.openai.com/docs/guides/chat)
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Token Counting](https://platform.openai.com/tokenizer)

### Recommended Reading
- [OpenAI Cookbook](https://cookbook.openai.com/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [LangChain Prompts](https://python.langchain.com/docs/modules/model_io/prompts/)

### Tools
- [tiktoken](https://github.com/openai/tiktoken) - Token counting library
- **utils/cost_tracker.py**: Cost tracking utilities
- **utils/api_helpers.py**: API interaction helpers

## Next Steps

After completing this module:

1. ✅ Complete all exercises with cost tracking
2. ✅ Experiment in OpenAI Playground
3. ➡️ **Choose Your Path**:
   - Module 04: Open Source AI & Safety
   - Module 05: Embeddings & Vector Databases (can run parallel)

## Prompt Engineering Patterns

### System Prompt Pattern
```python
system_prompt = """You are a helpful AI assistant that specializes in Python programming.
Always provide code examples when relevant.
Explain complex concepts simply."""

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "How do I read a CSV file?"}
    ]
)
```

### Few-Shot Pattern
```python
messages = [
    {"role": "system", "content": "Convert sentences to JSON."},
    {"role": "user", "content": "John is 30 years old."},
    {"role": "assistant", "content": '{"name": "John", "age": 30}'},
    {"role": "user", "content": "Sarah lives in Boston."},
    {"role": "assistant", "content": '{"name": "Sarah", "city": "Boston"}'},
    {"role": "user", "content": "Mike works at Google."}
]
```

### Chain-of-Thought Pattern
```python
prompt = """Solve this step by step:
1. First, identify what we know
2. Then, determine what we need to find
3. Finally, solve and explain

Question: If a train travels 60 miles in 45 minutes, what's its speed in mph?"""
```

## Cost Optimization Tips

1. **Use GPT-3.5 for simple tasks**: 10x cheaper than GPT-4
2. **Optimize system prompts**: Shorter = cheaper
3. **Cache common responses**: Store frequently used outputs
4. **Batch processing**: Group similar requests
5. **Set max_tokens**: Prevent runaway generation
6. **Track and alert**: Monitor spending in real-time

## Common Issues

### Rate Limit Errors (429)
- Implement exponential backoff
- Use tier-appropriate rate limits
- Consider batching requests

### Token Limit Exceeded
- Count tokens before sending (tiktoken)
- Truncate or summarize long inputs
- Use appropriate model (8k vs 32k vs 128k)

### Inconsistent Outputs
- Set temperature lower (0.0-0.3)
- Use seed parameter for reproducibility
- Add more specific instructions

## Notes

- **API Costs**: Budget $5-10 for this module's exercises
- **Playground**: Experiment freely; it shows token counts
- **Best Practices**: Always use cost tracking from utils/
- **Model Choice**: Default to GPT-3.5 for learning; upgrade when needed

---

**Module Status**: 🚧 Content Development | ⬅️ Prev: Python Fundamentals | ⏭️ Next: Open Source AI & Safety
