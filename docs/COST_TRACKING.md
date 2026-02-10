# Cost Tracking Guide

## Overview

This guide explains how to track and manage API costs while using the AI Engineer Learning Repository. All utilities are built-in and ready to use.

## Why Track Costs?

- **Budget awareness** - Know exactly what you're spending
- **Optimization** - Identify expensive operations
- **Learning** - Understand token usage patterns
- **Safety** - Prevent unexpected bills

**Estimated Total Repository Cost:** $50-150 (varies by model choices and usage)

## Quick Start

### Enable Cost Tracking

Edit `.env`:
```bash
COST_TRACKING_ENABLED=true
COST_WARNING_THRESHOLD=10.0   # Warn at $10
COST_MAX_THRESHOLD=50.0        # Block at $50
```

### Basic Usage

```python
from utils.cost_tracker import estimate_cost, track_cost

# Estimate before calling
cost = estimate_cost(
    prompt="Your prompt here",
    model="gpt-3.5-turbo",
    max_tokens=1000
)
print(f"Estimated cost: ${cost:.4f}")

# Automatic tracking with decorator
@track_cost
def my_ai_function():
    response = client.chat.completions.create(...)
    return response
```

## Token Counting

### What are Tokens?

- Tokens are pieces of words used by AI models
- ~4 characters = 1 token (English)
- ~750 words = 1000 tokens
- Count varies by language and model

### Count Tokens

```python
from utils.cost_tracker import count_tokens

text = "This is a sample text to count tokens."
tokens = count_tokens(text, model="gpt-3.5-turbo")
print(f"Tokens: {tokens}")
```

### Estimate Cost

```python
from utils.cost_tracker import estimate_cost

# Simple estimation
cost = estimate_cost(
    prompt="Write a short story",
    model="gpt-4",
    max_tokens=500
)
print(f"Max cost: ${cost:.4f}")
```

## Cost Calculation

### Manual Calculation

```python
from utils.cost_tracker import calculate_cost

cost = calculate_cost(
    prompt_tokens=100,
    completion_tokens=50,
    model="gpt-3.5-turbo"
)
print(f"Cost: ${cost:.6f}")
```

### Model Pricing (as of 2026-02-10)

| Model | Input (per 1K tokens) | Output (per 1K tokens) |
|-------|----------------------|------------------------|
| GPT-4 | $0.03 | $0.06 |
| GPT-4 Turbo | $0.01 | $0.03 |
| GPT-3.5-turbo | $0.0005 | $0.0015 |
| text-embedding-3-small | $0.00002 | $0 |
| text-embedding-3-large | $0.00013 | $0 |

**Note:** Prices subject to change. Check [OpenAI Pricing](https://openai.com/pricing) for latest.

## Session Tracking

### Create Tracker

```python
from utils.cost_tracker import CostTracker

# Create named session
tracker = CostTracker(session_name="my_experiment")

# Track API calls
response = client.chat.completions.create(...)
tracker.track_from_response(response)

# Get total cost
print(f"Session cost: ${tracker.get_total_cost():.4f}")

# Print summary
tracker.print_summary()
```

### Track Multiple Calls

```python
tracker = CostTracker()

# Call 1
response1 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)
tracker.track_from_response(response1)

# Call 2
response2 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Goodbye"}]
)
tracker.track_from_response(response2)

# View report
report = tracker.get_session_report()
print(f"Total calls: {report['total_calls']}")
print(f"Total cost: ${report['total_cost']:.4f}")
print(f"Total tokens: {report['total_tokens']:,}")
```

## Automatic Tracking

### Using Decorator

```python
from utils.cost_tracker import track_cost

@track_cost
def generate_summary(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize this text."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

# Use function normally - cost is tracked automatically
summary = generate_summary("Long text here...")

# View global tracker summary
from utils.cost_tracker import print_global_summary
print_global_summary()
```

### Global Tracker

```python
from utils.cost_tracker import get_global_tracker

# Get global tracker instance
tracker = get_global_tracker()

# Access session data
print(f"Total spent: ${tracker.get_total_cost():.4f}")

# Reset if needed
from utils.cost_tracker import reset_global_tracker
reset_global_tracker()
```

## Export Reports

### Save to JSON

```python
tracker = CostTracker()

# ... make API calls ...

# Export report
tracker.export_report("cost_report.json", format="json")
```

JSON format:
```json
{
  "session_name": "my_session",
  "total_calls": 10,
  "total_cost": 0.0123,
  "total_tokens": 1500,
  "by_model": {
    "gpt-3.5-turbo": {
      "calls": 10,
      "cost": 0.0123,
      "tokens": 1500
    }
  },
  "calls": [...]
}
```

### Save to CSV

```python
tracker.export_report("cost_report.csv", format="csv")
```

CSV columns:
- timestamp
- model
- prompt_tokens
- completion_tokens
- total_tokens
- cost

## Cost Limits

### Warning Threshold

Set in `.env`:
```bash
COST_WARNING_THRESHOLD=10.0
```

When exceeded:
```
Warning: Session cost ($10.50) has exceeded warning threshold ($10.00)
```

### Maximum Threshold

Set in `.env`:
```bash
COST_MAX_THRESHOLD=50.0
```

When exceeded:
```python
from utils.cost_tracker import CostLimitExceeded

try:
    # ... API calls ...
except CostLimitExceeded as e:
    print(f"Cost limit reached: {e}")
```

### OpenAI Usage Limits

Set in [OpenAI Dashboard](https://platform.openai.com/account/billing/limits):

1. **Hard limit** - Absolute maximum spending
2. **Soft limit** - Warning threshold
3. **Email alerts** - Get notified

## Cost Optimization Tips

### 1. Use Cheaper Models

```python
# Expensive
response = client.chat.completions.create(
    model="gpt-4",  # $0.03/1K input
    messages=[...]
)

# Cheaper (good for learning)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # $0.0005/1K input
    messages=[...]
)
```

### 2. Optimize Prompt Length

```python
from utils.cost_tracker import count_tokens

# Check prompt length
prompt = "Your prompt here"
tokens = count_tokens(prompt)

if tokens > 1000:
    print(f"Warning: Long prompt ({tokens} tokens)")
```

### 3. Reduce Max Tokens

```python
# Instead of:
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[...],
    max_tokens=2000  # More expensive
)

# Use:
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[...],
    max_tokens=500  # Cheaper, often sufficient
)
```

### 4. Cache Responses

```python
import json
import hashlib

def cache_response(prompt, model="gpt-3.5-turbo", cache_file="cache.json"):
    # Load cache
    try:
        with open(cache_file, 'r') as f:
            cache = json.load(f)
    except FileNotFoundError:
        cache = {}
    
    # Generate cache key
    key = hashlib.md5(f"{prompt}{model}".encode()).hexdigest()
    
    # Check cache
    if key in cache:
        print("Using cached response (no cost)")
        return cache[key]
    
    # Make API call
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message.content
    
    # Save to cache
    cache[key] = result
    with open(cache_file, 'w') as f:
        json.dump(cache, f)
    
    return result
```

### 5. Use Local Models

For experimentation:

```bash
# Install Ollama
# Run local models for free
ollama run llama2

# Use in code
import ollama
response = ollama.chat(model='llama2', messages=[...])
```

## Monitoring Usage

### View OpenAI Dashboard

1. Go to [OpenAI Usage](https://platform.openai.com/account/usage)
2. View daily/monthly costs
3. Download detailed usage report
4. Set up billing alerts

### Track by Exercise

```python
tracker = CostTracker(session_name="exercise_01")

# Do exercise
# ... 

tracker.print_summary()
tracker.export_report(f"costs/exercise_01.json")
```

### Aggregate Reports

```python
import json
import glob

total_cost = 0.0

for report_file in glob.glob("costs/*.json"):
    with open(report_file) as f:
        report = json.load(f)
        total_cost += report['total_cost']

print(f"Total repository cost: ${total_cost:.2f}")
```

## Cost Estimates by Module

Estimated costs if using GPT-3.5-turbo for all exercises:

| Module | Est. Cost | Notes |
|--------|-----------|-------|
| 01 - Python Fundamentals | $1-2 | Minimal API usage |
| 02 - AI Fundamentals & OpenAI | $5-10 | Learning API calls |
| 03 - Open Source AI & Safety | $3-5 | Testing and examples |
| 04 - Embeddings & Vector DBs | $5-8 | Embedding generation |
| 05 - RAG Systems | $10-15 | Multiple retrievals |
| 06 - AI Agents | $10-15 | Tool use and iterations |
| 07 - Multimodal AI | $5-10 | Vision and audio |
| 08 - Advanced RAG | $8-12 | Complex queries |
| 09 - Production Deployment | $3-5 | Testing and monitoring |
| 10 - Portfolio Projects | $20-40 | Substantial work |

**Total:** $70-122 (using GPT-3.5-turbo)

**If using GPT-4:** 2-3x higher costs

## Real-World Examples

### Example 1: Simple Chat

```python
from utils.cost_tracker import CostTracker

tracker = CostTracker()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=10
)

tracker.track_from_response(response)
# Cost: ~$0.000015 (less than a cent)
```

### Example 2: Long Document Summary

```python
tracker = CostTracker()

long_doc = "..." * 2000  # 2000 words ≈ 2667 tokens

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Summarize this document."},
        {"role": "user", "content": long_doc}
    ],
    max_tokens=200
)

tracker.track_from_response(response)
# Cost: ~$0.00164 (prompt) + ~$0.0003 (completion) = ~$0.00194
```

### Example 3: RAG Pipeline

```python
tracker = CostTracker(session_name="rag_pipeline")

# 1. Generate embeddings for 100 chunks
for chunk in chunks:  # 100 chunks, 500 tokens each
    embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )
    tracker.track_tokens(
        prompt_tokens=500,
        completion_tokens=0,
        model="text-embedding-3-small"
    )

# Cost so far: 50,000 tokens * $0.00002/1K = $0.001

# 2. Query (retrieve + generate)
query_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Query with retrieved context..."}],
    max_tokens=500
)
tracker.track_from_response(query_response)

# Additional cost: ~$0.002
# Total: ~$0.003
```

## Best Practices

1. **Always estimate first**
   ```python
   cost = estimate_cost(prompt, model, max_tokens)
   if cost > 0.10:
       print(f"Warning: High cost ${cost:.4f}")
   ```

2. **Track all sessions**
   ```python
   tracker = CostTracker(session_name=f"experiment_{date}")
   ```

3. **Export regular reports**
   ```python
   tracker.export_report(f"reports/{date}.json")
   ```

4. **Review monthly**
   - Check OpenAI dashboard
   - Analyze cost reports
   - Identify optimization opportunities

5. **Set conservative limits**
   - Start with low thresholds
   - Increase as comfortable
   - Always have hard limits

## Troubleshooting

**Problem:** Cost tracking not working

**Solution:**
```python
# Enable in .env
COST_TRACKING_ENABLED=true

# Verify
import os
print(os.getenv("COST_TRACKING_ENABLED"))
```

**Problem:** Inaccurate cost estimates

**Solution:**
- Ensure latest pricing in `utils/cost_tracker.py`
- Check model name is correct
- Update pricing constants if API changes

**Problem:** Cost exceeds estimates

**Solution:**
- Actual completions may be longer than max_tokens estimate
- Multiple calls add up quickly
- Check for retry loops

## Resources

- [OpenAI Pricing](https://openai.com/pricing)
- [OpenAI Usage Dashboard](https://platform.openai.com/account/usage)
- [Token Counting Guide](https://help.openai.com/en/articles/4936856)
- [Cost Optimization Tips](https://platform.openai.com/docs/guides/production-best-practices/cost-optimization)

---

**Last Updated:** 2026-02-10  
**Pricing as of:** 2026-02-10
