# AI Model Capabilities Reference

Last Updated: February 2026

## Quick Reference Table

| Model | Provider | Context | Input Cost | Output Cost | Speed | Best For |
|-------|----------|---------|------------|-------------|-------|----------|
| GPT-4 Turbo | OpenAI | 128k | $0.01/1k | $0.03/1k | Medium | Complex reasoning, coding |
| GPT-4 | OpenAI | 8k-32k | $0.03/1k | $0.06/1k | Slow | Highest accuracy tasks |
| GPT-3.5 Turbo | OpenAI | 16k | $0.0015/1k | $0.002/1k | Fast | High volume, simple tasks |
| Claude 3 Opus | Anthropic | 200k | $0.015/1k | $0.075/1k | Medium | Long documents, analysis |
| Claude 3 Sonnet | Anthropic | 200k | $0.003/1k | $0.015/1k | Fast | Balanced performance |
| Claude 3 Haiku | Anthropic | 200k | $0.00025/1k | $0.00125/1k | Very Fast | High volume, cost-sensitive |
| Gemini Pro | Google | 1M | $0.00025/1k | $0.0005/1k | Fast | Multimodal, long context |
| Gemini Ultra | Google | 1M | TBD | TBD | Medium | Most capable Gemini |
| Llama 3 70B | Meta | 8k | Free (local) | Free (local) | Fast | Privacy, offline use |
| Llama 3 8B | Meta | 8k | Free (local) | Free (local) | Very Fast | Edge devices, low resource |

## Detailed Comparison

### OpenAI Models

#### GPT-4 Turbo
**Released:** November 2023  
**Context Window:** 128,000 tokens (~96,000 words)  
**Parameters:** Estimated 1.7 trillion  

**Strengths:**
- Excellent reasoning and analysis
- Strong coding capabilities
- Large context window
- Multimodal (vision + text)
- More affordable than GPT-4

**Weaknesses:**
- Still expensive at scale
- Slower than GPT-3.5
- Knowledge cutoff (April 2023)

**Best Use Cases:**
- Complex analysis tasks
- Long document processing
- Advanced coding assistance
- Multi-step reasoning
- When accuracy is critical

**Pricing Example:**
- 1M input tokens + 1M output tokens = $40
- 10,000 API calls (200 tokens in, 500 out) = $13

---

#### GPT-4
**Released:** March 2023  
**Context Window:** 8k or 32k tokens  

**Strengths:**
- Highest accuracy
- Best for complex tasks
- Strong safety features

**Weaknesses:**
- Most expensive
- Slowest responses
- Smaller context than Turbo

**Best Use Cases:**
- Critical accuracy requirements
- Complex reasoning tasks
- When cost is not primary concern

**Note:** GPT-4 Turbo recommended for most new applications.

---

#### GPT-3.5 Turbo
**Released:** March 2023 (continuously updated)  
**Context Window:** 16,000 tokens  
**Parameters:** 175 billion  

**Strengths:**
- 20x cheaper than GPT-4
- Very fast responses (2-5 seconds)
- Good for most common tasks
- Lower rate limits

**Weaknesses:**
- Less capable reasoning
- Shorter context than newer models
- Lower accuracy on complex tasks

**Best Use Cases:**
- Chatbots with simple queries
- Content generation at scale
- Quick drafting and editing
- Cost-sensitive applications
- High-volume processing

**Pricing Example:**
- 1M input tokens + 1M output tokens = $3.50
- 10,000 API calls (200 tokens in, 500 out) = $1.30

---

### Anthropic Models

#### Claude 3 Opus
**Released:** March 2024  
**Context Window:** 200,000 tokens (~150,000 words)  

**Strengths:**
- Massive context window
- Excellent for long documents
- Nuanced writing style
- Strong safety features
- Good at following complex instructions

**Weaknesses:**
- More expensive than GPT-4 Turbo
- API availability varies by region

**Best Use Cases:**
- Legal document analysis
- Book-length text processing
- Complex research tasks
- Detailed content analysis

---

#### Claude 3 Sonnet
**Context Window:** 200,000 tokens  

**Strengths:**
- Balanced performance/cost
- Still has huge context window
- Fast responses
- Good quality outputs

**Best Use Cases:**
- General-purpose applications
- When you need long context but not highest capability
- Cost-conscious applications

---

#### Claude 3 Haiku
**Context Window:** 200,000 tokens  

**Strengths:**
- Extremely cost-effective
- Very fast
- Still maintains 200k context
- Good for simple tasks

**Best Use Cases:**
- High-volume simple tasks
- Real-time applications
- Cost-sensitive chatbots

---

### Google Models

#### Gemini Pro
**Released:** December 2023  
**Context Window:** 1,000,000 tokens (1M!)  

**Strengths:**
- Largest context window available
- Multimodal (text + images + video)
- Very cost-effective
- Fast processing
- Free tier available

**Weaknesses:**
- Newer ecosystem (fewer integrations)
- Performance varies by task type

**Best Use Cases:**
- Extremely long documents
- Multimodal applications
- Video analysis
- Cost-sensitive large-scale applications

---

### Meta Models (Llama)

#### Llama 3 70B
**Released:** 2024  
**Context Window:** 8,000 tokens  
**Parameters:** 70 billion  

**Strengths:**
- Free to use (run locally)
- Complete privacy (no data leaves your server)
- No API rate limits
- Open source - can modify
- Can run offline

**Weaknesses:**
- Requires significant GPU resources
- Smaller context window
- Less capable than GPT-4
- Need to manage infrastructure

**Best Use Cases:**
- Privacy-critical applications (healthcare, legal)
- High-volume processing (no per-token costs)
- Offline/air-gapped environments
- Custom fine-tuning needs

#### Llama 3 8B
**Parameters:** 8 billion  

**Strengths:**
- Runs on consumer GPUs
- Very fast inference
- Free to use
- Good for simple tasks

**Best Use Cases:**
- Edge devices
- Real-time processing
- Simple classification/extraction
- Development and testing

---

## Selection Decision Tree

### Start Here: What's your primary concern?

#### 1. **Privacy/Compliance Required?**
→ **Use Llama** (local deployment)

#### 2. **Extremely Long Context (>100k tokens)?**
→ **Gemini Pro** (1M context) or **Claude 3** (200k context)

#### 3. **Budget Very Limited?**
→ **GPT-3.5 Turbo** or **Claude 3 Haiku** or **Gemini Pro**

#### 4. **Need Highest Accuracy?**
→ **GPT-4 Turbo** or **Claude 3 Opus**

#### 5. **High Volume Simple Tasks?**
→ **GPT-3.5 Turbo** or **Claude 3 Haiku**

#### 6. **Multimodal (Images/Video)?**
→ **GPT-4 Turbo** (vision) or **Gemini Pro** (video too)

#### 7. **Complex Coding Tasks?**
→ **GPT-4 Turbo**

#### 8. **Legal/Contract Analysis?**
→ **Claude 3 Opus** (long context + nuanced understanding)

---

## Multi-Model Strategies

Many production applications use **multiple models** strategically:

### Strategy 1: Routing by Complexity
```
Simple Query → GPT-3.5 Turbo ($)
Complex Query → GPT-4 Turbo ($$$$)

Saves: 60-80% on costs
```

### Strategy 2: Two-Stage Processing
```
Stage 1: Extract/Summarize → GPT-3.5 Turbo (fast, cheap)
Stage 2: Deep Analysis → GPT-4 Turbo (accurate)

Reduces tokens sent to expensive model
```

### Strategy 3: High-Volume + Quality Check
```
Generate 100 outputs → GPT-3.5 Turbo
Quality check best 10 → GPT-4 Turbo

Best of both worlds
```

### Strategy 4: Local + Cloud Hybrid
```
Initial processing → Llama 3 (free, private)
Complex cases → GPT-4 Turbo (cloud, when needed)

Privacy + capability
```

---

## Performance Benchmarks

### Response Speed (Typical)
- **GPT-3.5 Turbo:** 2-5 seconds
- **GPT-4 Turbo:** 10-20 seconds
- **GPT-4:** 30-60 seconds
- **Claude 3 Haiku:** 2-4 seconds
- **Claude 3 Sonnet:** 5-10 seconds
- **Claude 3 Opus:** 15-25 seconds
- **Gemini Pro:** 3-8 seconds
- **Llama 3 70B:** 1-3 seconds (local GPU)

### Quality Rankings (Complex Tasks)
1. GPT-4 Turbo / Claude 3 Opus (tied)
2. GPT-4
3. Claude 3 Sonnet
4. Gemini Pro
5. GPT-3.5 Turbo
6. Claude 3 Haiku
7. Llama 3 70B
8. Llama 3 8B

### Cost Rankings (Cheapest to Most Expensive)
1. Llama (free, local)
2. Claude 3 Haiku ($0.00025 input)
3. Gemini Pro ($0.00025 input)
4. GPT-3.5 Turbo ($0.0015 input)
5. Claude 3 Sonnet ($0.003 input)
6. GPT-4 Turbo ($0.01 input)
7. Claude 3 Opus ($0.015 input)
8. GPT-4 ($0.03 input)

---

## Context Window Practical Limits

While models advertise large context windows, practical considerations:

| Model | Max Context | Practical Limit | Reason |
|-------|-------------|-----------------|---------|
| GPT-3.5 | 16k | 12k | Need room for response |
| GPT-4 Turbo | 128k | 100k | Cost escalates, slower |
| Claude 3 | 200k | 180k | Performance may degrade |
| Gemini Pro | 1M | 500k | Still experimental |

**Best Practice:** Use smallest context needed for task.

---

## Update History

- **Feb 2026:** Initial version created
- Updated with latest pricing and capabilities
- Added Gemini Pro 1M context

**Note:** AI model landscape changes rapidly. Verify current pricing and capabilities before production deployment.

## Resources

- [OpenAI Pricing](https://openai.com/pricing)
- [Anthropic Pricing](https://www.anthropic.com/pricing)
- [Google AI Pricing](https://ai.google.dev/pricing)
- [Llama Models](https://llama.meta.com/)
