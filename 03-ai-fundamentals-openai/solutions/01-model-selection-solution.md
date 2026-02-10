# Solution: Model Selection Exercise

## Scenario 1: Startup Chatbot

**Model:** GPT-3.5 Turbo

**Reasoning:**
- **Volume calculation:** 100k messages × (50 input + 100 output) tokens = 15M tokens/month
- **Cost with GPT-3.5:** Input: 5M × $0.0015 = $7.50, Output: 10M × $0.002 = $20, **Total: $27.50/month** ✅
- **Cost with GPT-4 Turbo:** Input: 5M × $0.01 = $50, Output: 10M × $0.03 = $300, **Total: $350/month** ❌ (exceeds budget)
- **Speed:** GPT-3.5 provides 2-5s responses, meeting the <3s requirement for most queries
- **Task complexity:** Customer support queries are generally straightforward, not requiring GPT-4 level reasoning

**Alternative consideration:** Could use Claude 3 Haiku (even cheaper at ~$4/month) but GPT-3.5 has more mature ecosystem and tooling.

---

## Scenario 2: Legal Document Analysis

**Model:** Claude 3 Opus

**Reasoning:**
- **Context window:** Legal contracts are 20-50 pages (10k-25k words ≈ 13k-33k tokens). Claude's 200k context handles this easily in one pass
- **Accuracy:** High accuracy is critical for legal work. Opus is comparable to GPT-4 in quality
- **Document understanding:** Claude is particularly strong at nuanced text analysis and long documents
- **Cost:** 100 docs/month × 30k avg tokens input = 3M tokens input/month = $45/month input (output minimal for extraction). Total ~$100/month, well within budget since "not primary concern"

**Why not GPT-4 Turbo:** Could work (128k context sufficient) but Claude 3 Opus specializes in long-form document analysis and has larger context margin.

---

## Scenario 3: Code Review Assistant

**Model:** GPT-4 Turbo

**Reasoning:**
- **Task complexity:** Code review requires understanding logic, identifying bugs, suggesting improvements - complex reasoning task
- **Quality matters:** Bad code review wastes developer time. Need high accuracy
- **Speed:** 10-20s response time acceptable (developers review while waiting)
- **Volume calculation:** 500 reviews/month, assume avg 2k tokens in (code) + 500 out (suggestions) = 1.25M tokens/month
- **Cost:** Input: 1M × $0.01 = $10, Output: 0.25M × $0.03 = $7.50, **Total: ~$18/month** ✅ (well under budget)
- **Coding expertise:** GPT-4 Turbo is best-in-class for code understanding

**Why not GPT-3.5:** Too many missed bugs and less helpful suggestions would frustrate developers.

---

## Scenario 4: Healthcare Application

**Model:** Llama 3 70B (Local Deployment)

**Reasoning:**
- **HIPAA Compliance:** Patient data CANNOT be sent to external APIs (OpenAI, Anthropic, Google). This immediately rules out all cloud models
- **Privacy:** Running locally ensures data never leaves hospital network
- **Medical terminology:** While Llama 3 70B is less capable than GPT-4, it can be fine-tuned on medical terminology if needed
- **No API costs:** One-time setup cost, then free to run (hospital likely has GPUs for medical imaging already)
- **Air-gapped:** Can run completely offline, essential for secure hospital networks

**No alternatives:** Privacy requirements dictate local deployment. Could consider other open-source models (Mistral, etc.) but Llama 3 70B offers best balance of capability and ease of deployment.

---

## Scenario 5: Content Generation Platform

**Model:** GPT-3.5 Turbo (or GPT-4 Turbo for premium tier)

**Reasoning:**
- **Volume calculation:** 10k posts/month × 750 words avg = 7.5M words ≈ 10M tokens output
- Assuming prompts are small (100 tokens each = 1M tokens input)
- **Cost with GPT-3.5:** Input: 1M × $0.0015 = $1.50, Output: 10M × $0.002 = $20, **Total: $21.50/month** ✅
- **Quality threshold:** "Good enough, not perfect" - GPT-3.5 is sufficient for blog posts
- **Creative writing:** Temperature 0.9-1.2 with GPT-3.5 produces creative, varied content

**Multi-tier strategy:**
- **Free/Basic tier:** GPT-3.5 Turbo
- **Premium tier:** GPT-4 Turbo (charge users $10/month, use better model)
- **Cost:** If 20% use premium (2k posts), premium adds ~$60, total ~$80/month, still under budget

---

## Scenario 6: Research Paper Summarization

**Model:** Claude 3 Sonnet

**Reasoning:**
- **Context window:** Papers are 8k-12k words (10k-16k tokens). Claude's 200k context easily fits full paper
- **Volume:** 50 papers/month × 13k tokens avg = 650k tokens input, ~100k tokens output (summaries)
- **Cost:** Input: 650k × $0.003 = $1.95, Output: 100k × $0.015 = $1.50, **Total: ~$3.50/month** ✅
- **Quality:** Sonnet offers good quality (better than GPT-3.5) at lower cost than Opus
- **Technical preservation:** Claude maintains technical language well
- **Long-form understanding:** Claude specializes in this

**Why not Gemini Pro:** Could work (1M context, even cheaper), but Claude has proven track record for academic text. Could A/B test.

**Why not GPT-4 Turbo:** Overkill for summarization task, 5-10x more expensive with minimal quality improvement for this use case.

---

## Bonus Challenge: Multi-Model Strategy

**AI Writing Platform Strategy:**

### Task 1: Initial Draft Generation (high volume)
**Model:** GPT-3.5 Turbo  
**Because:**
- Need to generate 1000 drafts/month × 1000 words = 1.3M tokens output
- Cost: ~$2.60/month for this stage
- Speed: 2-5s, good UX for initial generation
- Quality: Sufficient for rough drafts

### Task 2: Grammar & Style Checking
**Model:** GPT-3.5 Turbo (specialized prompt)  
**Because:**
- Grammar checking doesn't need GPT-4 capability
- Fast processing (users waiting for edits)
- Cost-effective for all 1000 articles
- Can use temperature 0 for consistent suggestions
- Cost: ~$3/month (reading + minimal output)

### Task 3: Content Enhancement
**Model:** GPT-4 Turbo (for top 30% of articles)  
**Because:**
- Not all articles need deep enhancement
- Route "premium" articles or user-requested enhancements to GPT-4
- Better suggestions for structure, argumentation, flow
- 300 articles/month × 1.5k tokens in/out = 900k tokens
- Cost: ~$36/month for this tier

### Task 4: Final Polish & Fact-Check
**Model:** GPT-4 Turbo (for top 10% of articles)  
**Because:**
- Only highest-value articles get expensive final polish
- GPT-4's reasoning best for fact-checking and ensuring logical consistency
- 100 articles/month × 2k tokens in/out = 400k tokens
- Cost: ~$20/month

### Estimated Monthly Cost for 1000 articles:
```
Stage 1 (GPT-3.5):     $2.60
Stage 2 (GPT-3.5):     $3.00
Stage 3 (GPT-4 30%):   $36.00
Stage 4 (GPT-4 10%):   $20.00
-------------------------
TOTAL:                 $61.60/month
```

**Comparison to alternatives:**
- **All GPT-4 Turbo:** Would cost ~$200/month (3.2x more expensive)
- **All GPT-3.5:** Would cost ~$10/month but lower quality, higher churn

**ROI:** The multi-model strategy provides 80% of GPT-4 quality at 30% of the cost by routing intelligently.

**Implementation:**
```python
def route_to_model(article, stage):
    if stage == "draft":
        return "gpt-3.5-turbo"
    elif stage == "grammar":
        return "gpt-3.5-turbo"
    elif stage == "enhance":
        # Route premium users or high-value articles to GPT-4
        if article.is_premium or article.word_count > 2000:
            return "gpt-4-turbo"
        return "gpt-3.5-turbo"
    elif stage == "final":
        # Only top tier gets GPT-4 fact-check
        if article.is_premium and article.importance == "high":
            return "gpt-4-turbo"
        return "skip"
```

---

## Key Takeaways

1. **Budget constraints often dictate model choice** - GPT-3.5 handles most tasks at 1/20th the cost
2. **Privacy/compliance trumps capability** - HIPAA/regulated industries must use local models
3. **Context length matters** - Long documents need Claude or Gemini Pro
4. **Task complexity guides selection** - Simple tasks don't need GPT-4
5. **Multi-model strategies optimize cost/quality tradeoff** - Route by complexity
6. **Speed requirements matter** - Real-time apps need faster models
7. **Volume amplifies cost differences** - At 1M requests/month, small price differences matter hugely
