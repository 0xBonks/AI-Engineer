# Exercise: Model Selection

## Objective
Learn to select the right AI model for different use cases by evaluating requirements and constraints.

## Instructions
For each scenario below, choose the most appropriate model and explain your reasoning. Consider:
- Task complexity
- Budget constraints
- Speed requirements
- Context length needs
- Privacy requirements

## Scenarios

### Scenario 1: Startup Chatbot
**Requirements:**
- Customer support chatbot
- Budget: $500/month
- Expected: 100k messages/month
- Average message: 50 tokens input, 100 tokens output
- Response time: <3 seconds

**Your Selection:**
```
Model: ___________
Reasoning:



```

### Scenario 2: Legal Document Analysis
**Requirements:**
- Analyze contracts (20-50 pages each)
- Extract key terms and risks
- High accuracy critical
- Budget: Not the primary concern
- Volume: 100 documents/month

**Your Selection:**
```
Model: ___________
Reasoning:



```

### Scenario 3: Code Review Assistant
**Requirements:**
- Review pull requests
- Suggest improvements
- Explain complex code
- Speed matters (developers waiting)
- Budget: $1000/month
- Volume: 500 reviews/month

**Your Selection:**
```
Model: ___________
Reasoning:



```

### Scenario 4: Healthcare Application
**Requirements:**
- Patient data processing
- MUST be HIPAA compliant
- Cannot send data to external APIs
- Hospital network only
- Medical terminology understanding needed

**Your Selection:**
```
Model: ___________
Reasoning:



```

### Scenario 5: Content Generation Platform
**Requirements:**
- Generate blog posts (500-1000 words)
- Creative writing
- Volume: 10k posts/month
- Quality: Good enough, not perfect
- Budget: $2000/month

**Your Selection:**
```
Model: ___________
Reasoning:



```

### Scenario 6: Research Paper Summarization
**Requirements:**
- Summarize academic papers (8000-12000 words)
- Need detailed, accurate summaries
- Technical language preservation
- Volume: 50 papers/month
- Budget: $800/month

**Your Selection:**
```
Model: ___________
Reasoning:



```

## Bonus Challenge

### Multi-Model Strategy
Design a system that uses MULTIPLE models strategically:

**Scenario:** AI Writing Platform
- Initial draft generation (high volume)
- Grammar checking
- Style improvement
- Final polish (complex editing)

**Your Multi-Model Strategy:**
```
Task 1 (______): Model ______ because:


Task 2 (______): Model ______ because:


Task 3 (______): Model ______ because:


Task 4 (______): Model ______ because:


Estimated monthly cost for 1000 articles:


```

## Submission
Save your answers in `solutions/01-model-selection-answers.md` and compare with the provided solution.

## Success Criteria
- [ ] Considered all relevant factors (cost, speed, accuracy, privacy)
- [ ] Justified each selection with specific reasoning
- [ ] Calculated approximate costs where applicable
- [ ] Recognized when privacy/compliance dictates model choice
- [ ] Bonus: Designed effective multi-model strategy
