# Module 04 - Solutions

This directory contains complete, working solutions for all Module 04 exercises.

## ⚠️ Important Notes

**For Students:**
- Try to complete the exercises on your own first
- Use solutions as a learning tool, not a shortcut
- Compare your approach with the solution
- Understand WHY the code works, not just WHAT it does

**Solution Files:**

1. `01-model-selection-solution.py` - Hugging Face model research and selection
2. `02-huggingface-inference-solution.py` - Using HF Inference API with retry logic
3. `03-ollama-local-solution.py` - Local model deployment and management
4. `04-input-validation-solution.py` - Prompt injection detection and prevention
5. `05-output-filtering-solution.py` - Content moderation with OpenAI API
6. `06-adversarial-testing-solution.py` - Comprehensive security testing framework

## Running Solutions

```bash
# Setup environment
source ../../.venv/bin/activate

# Set API keys in .env file
# OPENAI_API_KEY=your_key
# HUGGINGFACE_TOKEN=your_token

# Run a solution
python 01-model-selection-solution.py
```

## Testing

All solutions include test functions. Run them to verify functionality:

```python
python -m pytest test_solutions.py -v
```

## Learning Path

1. **Start with exercises** - Attempt on your own
2. **Check tests** - Run provided tests to see if your solution works
3. **Review solution** - Compare approaches
4. **Experiment** - Modify and extend the code
5. **Apply** - Use in your own projects

## Key Concepts Demonstrated

### Security Best Practices
- Never trust user input
- Defense in depth
- Input validation + output filtering
- Logging and monitoring

### API Usage
- Error handling
- Retry logic with exponential backoff
- Rate limit management
- Efficient batch processing

### Code Quality
- Type hints
- Dataclasses for structure
- Comprehensive error handling
- Testing

## Additional Resources

- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Hugging Face Documentation](https://huggingface.co/docs)
- [Ollama Documentation](https://ollama.ai/docs)
- [OpenAI Moderation Guide](https://platform.openai.com/docs/guides/moderation)

## Getting Help

If you're stuck:
1. Read the error message carefully
2. Check the documentation
3. Review the solution code comments
4. Ask for help in discussions

---

**Remember**: The goal is to learn, not just to complete exercises. Take your time and understand each concept.
