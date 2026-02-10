# Phase 3 Plans: AI Fundamentals & OpenAI API

**Phase Goal:** Learners understand LLM concepts and can build applications using OpenAI APIs with cost optimization

**Requirements Coverage:** AI-01, AI-02, AI-03, AI-04, AI-05, AI-06, AI-07, OAI-01, OAI-02, OAI-03, OAI-04, OAI-05, OAI-06

**Success Criteria:**
1. Learner can explain when to use pre-trained models vs fine-tuning and the capabilities/limitations of different LLMs
2. Learner can implement Chat Completions API with streaming, error handling, and cost tracking
3. Learner can apply prompt engineering techniques (few-shot, chain-of-thought, system prompts) to improve outputs
4. Learner can calculate token usage, optimize prompts for cost, and implement rate limiting
5. Learner can use OpenAI Playground effectively for experimentation and fine-tuning workflows

---

## Plan 03-01: AI Fundamentals - Pre-trained Models & LLM Concepts
**Requirements:** AI-01, AI-02, AI-06, AI-07
**Estimated Effort:** 2-3 hours
**Dependencies:** Phase 2 complete

### Tasks:
1. Create notebook on pre-trained models
   - What are pre-trained models?
   - Benefits: No training required, ready to use, general knowledge
   - Limitations: Fixed knowledge cutoff, can't learn new info
   - When to use vs fine-tuning
2. Create notebook on LLM terminology
   - AI vs AGI vs narrow AI
   - LLM (Large Language Model)
   - Inference vs training
   - Parameters, tokens, context window
   - Temperature, top_p, and sampling
3. Create notebook comparing AI models
   - OpenAI (GPT-4, GPT-3.5)
   - Anthropic (Claude)
   - Google (Gemini)
   - Meta (Llama)
   - Model selection criteria
4. Create exercise: Model comparison matrix
5. Create quiz on terminology
6. Document model capabilities table

### Deliverables:
- [ ] `notebooks/01-pretrained-models.ipynb` - Pre-trained model concepts
- [ ] `notebooks/02-llm-terminology.ipynb` - AI terminology guide
- [ ] `notebooks/03-model-comparison.ipynb` - Compare AI models
- [ ] `exercises/01-model-selection.md` - Model selection exercise
- [ ] `exercises/02-terminology-quiz.md` - Terminology quiz
- [ ] `docs/MODEL_CAPABILITIES.md` - Model comparison table
- [ ] Solutions with explanations

### Verification:
- Notebooks explain concepts clearly
- Model comparison is accurate and current
- Exercise has clear selection criteria
- Terminology quiz covers all key concepts

---

## Plan 03-02: Chat Completions API Basics
**Requirements:** OAI-01
**Estimated Effort:** 3-4 hours
**Dependencies:** 03-01

### Tasks:
1. Create notebook on Chat Completions API structure
   - API authentication
   - Messages format (system, user, assistant)
   - Model selection
   - Basic parameters (temperature, max_tokens)
   - Response structure
2. Create notebook on making first API call
   - Setup OpenAI client (sync and async)
   - Simple completion request
   - Parsing response
   - Error handling
3. Create notebook on conversation patterns
   - Multi-turn conversations
   - Message history management
   - Context window limits
   - Conversation state
4. Create exercise: Build chat interface
5. Create exercise: Conversation manager
6. Add tests for API interactions

### Deliverables:
- [ ] `notebooks/01-chat-api-structure.ipynb` - API structure guide
- [ ] `notebooks/02-first-api-call.ipynb` - First OpenAI call tutorial
- [ ] `notebooks/03-conversations.ipynb` - Multi-turn patterns
- [ ] `exercises/01-simple-chat.py` - Basic chat interface
- [ ] `exercises/02-conversation-manager.py` - Manage conversation history
- [ ] `tests/test_chat_api.py` - API interaction tests
- [ ] Solutions with complete implementations

### Verification:
- API calls work with valid key
- Conversations maintain context
- Error handling is robust
- Tests pass without requiring API calls (mocked)

---

## Plan 03-03: Streaming Responses
**Requirements:** OAI-01
**Estimated Effort:** 2 hours
**Dependencies:** 03-02

### Tasks:
1. Create notebook on streaming basics
   - Why streaming matters (UX)
   - Stream parameter
   - Processing chunks
   - Token counting with streaming
2. Create notebook on streaming patterns
   - Real-time output display
   - Cancellation handling
   - Error handling in streams
   - Combining with async
3. Create exercise: Streaming chat application
4. Create exercise: Progress indicator for streaming
5. Add streaming tests

### Deliverables:
- [ ] `notebooks/01-streaming-basics.ipynb` - Streaming fundamentals
- [ ] `notebooks/02-streaming-patterns.ipynb` - Production patterns
- [ ] `exercises/01-streaming-chat.py` - Chat with streaming
- [ ] `exercises/02-stream-progress.py` - Progress tracking
- [ ] `tests/test_streaming.py` - Streaming tests
- [ ] Solutions

### Verification:
- Streaming works correctly
- Tokens counted accurately
- Errors handled gracefully
- Real-time display works

---

## Plan 03-04: Prompt Engineering Techniques
**Requirements:** OAI-02
**Estimated Effort:** 3-4 hours
**Dependencies:** 03-02

### Tasks:
1. Create notebook on system prompts
   - Role and purpose of system prompts
   - Behavioral instructions
   - Output format control
   - Best practices
2. Create notebook on few-shot learning
   - What is few-shot learning?
   - Providing examples (0-shot, 1-shot, few-shot)
   - Format consistency
   - When to use
3. Create notebook on chain-of-thought
   - Step-by-step reasoning
   - Think-then-answer pattern
   - Self-consistency
   - Applications
4. Create notebook on advanced techniques
   - Role prompting
   - Prompt templates
   - Negative prompting
   - Constraints and guardrails
5. Create exercise: Prompt engineering challenges
6. Create prompt library

### Deliverables:
- [ ] `notebooks/01-system-prompts.ipynb` - System prompt guide
- [ ] `notebooks/02-few-shot-learning.ipynb` - Few-shot techniques
- [ ] `notebooks/03-chain-of-thought.ipynb` - CoT prompting
- [ ] `notebooks/04-advanced-prompting.ipynb` - Advanced techniques
- [ ] `exercises/01-prompt-challenges.py` - Prompt engineering exercises
- [ ] `exercises/02-prompt-library.py` - Reusable prompts
- [ ] `tests/test_prompts.py` - Prompt tests
- [ ] Solutions with examples

### Verification:
- Techniques demonstrably improve outputs
- Examples work with real API
- Prompt library is reusable
- Best practices documented

---

## Plan 03-05: Token Management & Cost Optimization
**Requirements:** OAI-03, OAI-04
**Estimated Effort:** 2-3 hours
**Dependencies:** 03-02

### Tasks:
1. Create notebook on token counting
   - What are tokens?
   - tiktoken library usage
   - Counting before API calls
   - Different encodings (cl100k_base, p50k_base)
2. Create notebook on pricing and costs
   - OpenAI pricing models
   - Cost calculation formulas
   - Tracking costs over time
   - Budget alerts
3. Create notebook on optimization strategies
   - Reduce system prompt length
   - Use GPT-3.5 vs GPT-4 strategically
   - Cache responses
   - Optimize max_tokens
   - Batch processing
4. Create exercise: Cost tracking system
5. Create exercise: Prompt optimization
6. Integrate with Phase 1 cost_tracker utility

### Deliverables:
- [ ] `notebooks/01-token-counting.ipynb` - Token fundamentals
- [ ] `notebooks/02-pricing-costs.ipynb` - Cost calculation
- [ ] `notebooks/03-optimization-strategies.ipynb` - Cost optimization
- [ ] `exercises/01-cost-tracker.py` - Build cost tracking
- [ ] `exercises/02-prompt-optimizer.py` - Optimize prompts for cost
- [ ] `tests/test_token_management.py` - Token counting tests
- [ ] Solutions

### Verification:
- Token counting is accurate
- Cost calculations match OpenAI pricing
- Optimization strategies reduce costs
- Integration with existing utils works

---

## Plan 03-06: OpenAI Playground & Experimentation
**Requirements:** OAI-05
**Estimated Effort:** 1-2 hours
**Dependencies:** 03-02, 03-04

### Tasks:
1. Create guide for OpenAI Playground
   - Navigation and interface
   - Model selection
   - Parameter tuning
   - Viewing token usage
   - Saving and sharing prompts
2. Create experimentation exercises
   - Test different temperatures
   - Compare models (GPT-4 vs GPT-3.5)
   - Test system prompts
   - Experiment with parameters
3. Document best practices for experimentation
4. Create template for experiments

### Deliverables:
- [ ] `notebooks/01-playground-guide.ipynb` - Playground tutorial
- [ ] `exercises/01-playground-experiments.md` - Guided experiments
- [ ] `exercises/02-experiment-template.md` - Experiment documentation template
- [ ] `docs/PLAYGROUND_GUIDE.md` - Reference guide
- [ ] Solutions with experiment results

### Verification:
- Guide is clear and actionable
- Experiments cover key parameters
- Template is useful for documentation
- Best practices included

---

## Plan 03-07: Advanced API Features
**Requirements:** OAI-01, OAI-06
**Estimated Effort:** 2-3 hours
**Dependencies:** 03-02, 03-04

### Tasks:
1. Create notebook on JSON mode
   - Structured output with JSON mode
   - response_format parameter
   - Pydantic integration
   - Use cases
2. Create notebook on function calling / tools
   - Function/tool definitions
   - Tool choice parameter
   - Multi-tool scenarios
   - Processing tool calls
3. Create notebook on fine-tuning overview
   - When to fine-tune
   - Data preparation
   - Training process
   - Evaluation
   - Deployment
4. Create exercise: Structured output extractor
5. Create exercise: Tool-using agent
6. Document fine-tuning workflow

### Deliverables:
- [ ] `notebooks/01-json-mode.ipynb` - Structured outputs
- [ ] `notebooks/02-function-calling.ipynb` - Tools API
- [ ] `notebooks/03-fine-tuning-overview.ipynb` - Fine-tuning intro
- [ ] `exercises/01-structured-extractor.py` - JSON extraction
- [ ] `exercises/02-tool-agent.py` - Agent with tools
- [ ] `docs/FINE_TUNING_GUIDE.md` - Fine-tuning reference
- [ ] `tests/test_advanced_features.py` - Feature tests
- [ ] Solutions

### Verification:
- JSON mode produces valid JSON
- Tools are called correctly
- Fine-tuning workflow is clear
- Examples work with real API

---

## Plan 03-08: Integration & Real-World Applications
**Requirements:** All Phase 3 requirements
**Estimated Effort:** 3-4 hours
**Dependencies:** All previous plans (03-01 through 03-07)

### Tasks:
1. Create comprehensive example applications
   - Chatbot with conversation history
   - Content generator with templates
   - Data extractor with JSON mode
   - Multi-tool agent
2. Build mini-project: AI Writing Assistant
   - Uses system prompts
   - Implements streaming
   - Tracks costs
   - Has conversation memory
3. Create verification script for Phase 3
   - Test all notebooks run
   - Test all exercises have tests
   - Verify API integration works
   - Check cost tracking integration
4. Update module README with all content
5. Create Phase 3 completion guide
6. Document common patterns and anti-patterns

### Deliverables:
- [ ] `notebooks/99-complete-applications.ipynb` - Full app examples
- [ ] `projects/ai-writing-assistant/` - Complete mini-project
- [ ] `scripts/verify_phase3.py` - Verification script
- [ ] Updated module README
- [ ] `docs/PHASE_3_COMPLETION.md` - Completion guide
- [ ] `docs/OPENAI_PATTERNS.md` - Best practices
- [ ] Integration tests

### Verification:
- All notebooks run without errors
- Mini-project is fully functional
- All 5 success criteria demonstrable
- All 13 requirements complete
- Ready for Phase 4

---

## Summary

**Total Plans:** 8
**Estimated Total Effort:** 18-25 hours
**Critical Path:** 03-01 → 03-02 → 03-04 → 03-07 → 03-08

**Key Deliverables:**
- 15+ interactive Jupyter notebooks
- 12+ hands-on exercises
- Complete mini-project (AI Writing Assistant)
- Comprehensive test suite
- Integration with Phase 1-2 infrastructure

**Success Criteria Mapping:**
- Criterion 1 (pre-trained vs fine-tuning): Plan 03-01, 03-07
- Criterion 2 (Chat API + streaming): Plans 03-02, 03-03
- Criterion 3 (prompt engineering): Plan 03-04
- Criterion 4 (token management): Plan 03-05
- Criterion 5 (Playground): Plan 03-06
- Integration: Plan 03-08

**Phase 3 Completion:** When all 8 plans delivered and verified, Phase 3 requirements (AI-01 to AI-07, OAI-01 to OAI-06) will be complete, and learners will be ready to build real AI applications.
