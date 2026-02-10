# Exercise: AI & LLM Terminology Quiz

## Objective
Test your understanding of key AI and LLM concepts.

## Instructions
Answer all questions. Some require short explanations, others are multiple choice.

---

## Part 1: Definitions (20 points)

### 1. What is a token? (2 points)
```
Answer:



```

### 2. Explain the difference between AI and AGI. (2 points)
```
Answer:



```

### 3. What is a context window? (2 points)
```
Answer:



```

### 4. What does "inference" mean in the context of LLMs? (2 points)
```
Answer:



```

### 5. Explain the difference between pre-training and fine-tuning. (2 points)
```
Answer:



```

### 6. What is temperature and how does it affect outputs? (2 points)
```
Answer:



```

### 7. What is top-p sampling? (2 points)
```
Answer:



```

### 8. What is a prompt? (2 points)
```
Answer:



```

### 9. What is a completion? (2 points)
```
Answer:



```

### 10. How many words is approximately 1000 tokens? (2 points)
```
Answer:



```

---

## Part 2: Multiple Choice (15 points)

### 11. Which temperature setting produces the most deterministic (consistent) outputs?
- [ ] a) 0.0
- [ ] b) 0.5
- [ ] c) 1.0
- [ ] d) 2.0

### 12. GPT-4's approximate parameter count is:
- [ ] a) 175 billion
- [ ] b) 500 billion
- [ ] c) 1.7 trillion
- [ ] d) 10 trillion

### 13. Which model has the largest context window?
- [ ] a) GPT-3.5 (16k tokens)
- [ ] b) GPT-4 Turbo (128k tokens)
- [ ] c) Claude 3 (200k tokens)
- [ ] d) Gemini Pro (1M tokens)

### 14. What does a higher frequency_penalty do?
- [ ] a) Makes responses longer
- [ ] b) Makes responses shorter
- [ ] c) Reduces word repetition
- [ ] d) Increases creativity

### 15. Which statement about pre-trained models is FALSE?
- [ ] a) They have a fixed knowledge cutoff date
- [ ] b) They can learn from conversations
- [ ] c) They're trained on diverse internet text
- [ ] d) They require no training from users

---

## Part 3: Calculations (10 points)

### 16. Token Calculation (5 points)
A prompt has 500 words. Approximately how many tokens is this?
```
Calculation:


Answer: _______ tokens
```

### 17. Cost Calculation (5 points)
You make 1000 API calls to GPT-3.5 Turbo:
- Each request: 100 tokens input
- Each response: 200 tokens output
- Pricing: $0.0015 per 1k input tokens, $0.002 per 1k output tokens

What's the total cost?
```
Input cost calculation:


Output cost calculation:


Total cost: $________
```

---

## Part 4: Scenarios (15 points)

### 18. When to use temperature 0.0? (5 points)
List 3 use cases where you would set temperature to 0.0:
```
1.

2.

3.
```

### 19. When to use high temperature (1.5-2.0)? (5 points)
List 3 use cases where you would use high temperature:
```
1.

2.

3.
```

### 20. Context Window Planning (5 points)
You're building a chatbot with conversation history. GPT-3.5 has 16k token context.
- Average user message: 50 tokens
- Average assistant response: 150 tokens
- System prompt: 200 tokens

How many conversation turns can you fit?
```
Calculation:




Answer: _______ turns
```

---

## Part 5: True/False (10 points)

### 21-30. Mark each statement as True or False:

21. [ ] Tokens are always single words
22. [ ] Higher temperature = more randomness
23. [ ] LLMs have real-time internet access by default
24. [ ] Fine-tuning changes the base model's weights
25. [ ] top-p and temperature can be used together
26. [ ] All OpenAI models cost the same per token
27. [ ] Context window includes both input and output tokens
28. [ ] Parameters are the same as tokens
29. [ ] Inference and training use similar compute resources
30. [ ] Prompt engineering can improve outputs without fine-tuning

---

## Scoring Guide
- **54-60 points:** Excellent! You have a strong grasp of LLM concepts
- **45-53 points:** Good! Review the areas you missed
- **36-44 points:** Fair. Go back through the notebooks
- **Below 36:** Review all material again

## Submission
Save your answers and check against `solutions/02-terminology-quiz-answers.md`

## Success Criteria
- [ ] Answered all questions
- [ ] Showed calculations for math problems
- [ ] Explained reasoning where asked
- [ ] Scored 45+ points (75%)
