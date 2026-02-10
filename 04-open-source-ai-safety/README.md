# Module 04: Open Source AI & Safety

## Overview

Explore the world of open source AI models and learn essential safety practices. Work with Hugging Face Hub, run models locally with Ollama, and implement security measures to protect against prompt injection, bias, and other AI risks.

## Learning Objectives

By completing this module, you will be able to:

- Navigate Hugging Face Hub, select appropriate models, and use Inference SDK and Transformers.js
- Deploy and run models locally using Ollama with SDK integration
- Identify and prevent prompt injection attacks with input validation
- Implement OpenAI Moderation API and design input/output constraints
- Apply security, privacy, and bias mitigation best practices in AI applications

## Prerequisites

- **Completed**: Module 03 (AI Fundamentals & OpenAI API)
- **Required**: Understanding of LLM basics and API interaction
- **Optional**: Local GPU for faster inference (CPU works but slower)

## Estimated Time

**10-12 hours** to complete all exercises and demos

## Key Concepts

### 1. Open Source vs Closed Source Models
- Benefits and tradeoffs of each approach
- Licensing considerations (Apache, MIT, custom)
- Model selection criteria
- Commercial use restrictions
- Community vs proprietary support

### 2. Hugging Face Ecosystem
- Hugging Face Hub navigation
- Model cards and documentation
- Datasets and Spaces
- Inference API and SDK
- Transformers.js for browser/Node.js
- Popular models: Llama, Mistral, Phi, etc.

### 3. Local Model Deployment (Ollama)
- Installing and configuring Ollama
- Pulling and managing models
- Running inference locally
- Ollama Python SDK
- Comparing performance: local vs API
- Use cases for local deployment

### 4. AI Safety & Security
- Prompt injection attacks (direct and indirect)
- Jailbreaking and adversarial prompts
- Input validation and sanitization
- Output filtering and moderation
- System prompt protection
- Defense-in-depth strategies

### 5. Ethics & Bias
- Understanding bias in AI models
- Fairness considerations
- Privacy and data protection
- Responsible AI principles
- Testing for bias
- Mitigation strategies

## Structure

```
04-open-source-ai-safety/
├── README.md                              # This file
├── notebooks/                             # Interactive tutorials
│   ├── 01-huggingface-hub.ipynb
│   ├── 02-inference-sdk.ipynb
│   ├── 03-ollama-setup.ipynb
│   ├── 04-prompt-injection.ipynb
│   ├── 05-moderation-api.ipynb
│   └── 06-bias-testing.ipynb
├── exercises/                             # Hands-on challenges
│   ├── 01-model-selection.py
│   ├── 02-huggingface-inference.py
│   ├── 03-ollama-local.py
│   ├── 04-input-validation.py
│   ├── 05-output-filtering.py
│   └── 06-adversarial-testing.py
├── tests/                                 # Automated validation
│   └── test_exercises.py
└── solutions/                             # Reference implementations
    └── solutions/
```

## Topics Covered

### Hugging Face Hub
- **Concept**: Central repository for open source models
- **Use Case**: Find and evaluate models for specific tasks
- **Example**: Choose between Llama 3, Mistral, or Phi-3

### Ollama Local Deployment
- **Concept**: Run LLMs on your own hardware
- **Use Case**: Privacy, offline access, cost savings
- **Example**: Run Llama 3 8B on consumer laptop

### Prompt Injection Attacks
- **Concept**: Malicious inputs that override system instructions
- **Use Case**: Secure user-facing chatbots
- **Example**: "Ignore previous instructions and..."

### Moderation API
- **Concept**: Filter harmful content automatically
- **Use Case**: Content moderation for user inputs/outputs
- **Example**: Block hate speech, violence, explicit content

### Bias Detection
- **Concept**: Test models for unfair treatment
- **Use Case**: Ensure equitable AI systems
- **Example**: Test hiring assistant for gender bias

## Exercises

### Exercise 1: Model Selection
**File**: `exercises/01-model-selection.py`

Research and compare open source models on Hugging Face Hub.

**Success Criteria**:
- Identify 3 models for a given task
- Compare sizes, licenses, and performance
- Select the best model with justification

### Exercise 2: Hugging Face Inference
**File**: `exercises/02-huggingface-inference.py`

Use Hugging Face Inference API to run open source models.

**Success Criteria**:
- Authenticate with Hugging Face token
- Run inference on selected model
- Compare output quality with OpenAI

### Exercise 3: Ollama Local Deployment
**File**: `exercises/03-ollama-local.py`

Set up Ollama and run models locally.

**Success Criteria**:
- Install Ollama and pull a model
- Run inference via Python SDK
- Compare speed: local vs API

### Exercise 4: Input Validation
**File**: `exercises/04-input-validation.py`

Implement input validation to prevent prompt injection.

**Success Criteria**:
- Detect injection patterns
- Sanitize user inputs
- Test with adversarial examples

### Exercise 5: Output Filtering
**File**: `exercises/05-output-filtering.py`

Use OpenAI Moderation API to filter harmful outputs.

**Success Criteria**:
- Call Moderation API on outputs
- Block flagged content
- Log moderation results

### Exercise 6: Adversarial Testing
**File**: `exercises/06-adversarial-testing.py`

Test your AI system against adversarial inputs.

**Success Criteria**:
- Create test suite of attacks
- Document vulnerabilities
- Implement defenses

## Resources

### Official Documentation
- [Hugging Face Hub](https://huggingface.co/models)
- [Hugging Face Inference API](https://huggingface.co/docs/api-inference/)
- [Ollama Documentation](https://ollama.ai/docs)
- [OpenAI Moderation API](https://platform.openai.com/docs/guides/moderation)

### Security Resources
- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Prompt Injection Primer](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/)
- [AI Security Best Practices](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development)

### Model Resources
- [Llama Models](https://huggingface.co/meta-llama)
- [Mistral AI](https://huggingface.co/mistralai)
- [Microsoft Phi](https://huggingface.co/microsoft/phi-3-mini-4k-instruct)

## Next Steps

After completing this module:

1. ✅ Set up Ollama for local development
2. ✅ Implement safety checks in all AI code
3. ➡️ Proceed to **Module 05: Embeddings & Vector Databases**

## Safety Patterns

### Input Validation Pattern
```python
import re

def validate_input(user_input: str) -> bool:
    """Detect potential prompt injection attempts."""
    
    # Check for instruction override attempts
    injection_patterns = [
        r"ignore\s+(previous|above|prior)\s+instructions",
        r"you\s+are\s+now",
        r"new\s+instructions",
        r"disregard\s+",
        r"<\s*system\s*>",
    ]
    
    for pattern in injection_patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return False
    
    return True

# Use before sending to LLM
if not validate_input(user_input):
    raise SecurityError("Potential prompt injection detected")
```

### Moderation Pattern
```python
from openai import OpenAI

client = OpenAI()

def moderate_content(text: str) -> dict:
    """Check content against OpenAI's moderation API."""
    
    response = client.moderations.create(input=text)
    result = response.results[0]
    
    return {
        "flagged": result.flagged,
        "categories": result.categories.model_dump(),
        "safe": not result.flagged
    }

# Use on user inputs and model outputs
if not moderate_content(user_input)["safe"]:
    return "This content violates our policies."
```

### Ollama Local Pattern
```python
import ollama

def local_inference(prompt: str, model: str = "llama3") -> str:
    """Run inference on local Ollama instance."""
    
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["message"]["content"]

# Privacy-sensitive use case
result = local_inference("Analyze this private document...")
```

## Open Source Model Comparison

| Model | Size | Context | License | Best For |
|-------|------|---------|---------|----------|
| Llama 3 8B | 8B | 8k | Llama 3 | General purpose |
| Mistral 7B | 7B | 32k | Apache 2.0 | Long context |
| Phi-3 Mini | 3.8B | 4k | MIT | Low resource |
| Gemma 7B | 7B | 8k | Gemma | Google ecosystem |

## Common Issues

### Ollama Installation Issues
- Ensure system meets requirements (4GB+ RAM)
- Check port 11434 is available
- See [Ollama Troubleshooting](https://ollama.ai/docs/troubleshooting)

### Slow Local Inference
- Use smaller models (3B-7B range)
- Enable GPU acceleration if available
- Adjust context window size

### False Positives in Moderation
- Review flagged content manually
- Adjust thresholds if needed
- Consider domain-specific moderation

## Notes

- **Local Models**: Require 4-16GB RAM depending on size
- **Privacy**: Local deployment = no data leaves your machine
- **Cost**: Open source models free to run (hardware cost only)
- **Safety First**: Always implement input validation and moderation

---

**Module Status**: 🚧 Content Development | ⬅️ Prev: AI Fundamentals & OpenAI API | ⏭️ Next: Embeddings & Vector Databases
