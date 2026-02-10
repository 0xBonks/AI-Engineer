# OOP and Advanced Patterns Solutions

## LLM Client Hierarchy

```python
from abc import ABC, abstractmethod
from openai import AsyncOpenAI

class LLMClient(ABC):
    """Abstract base for LLM clients."""
    
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        pass

class OpenAIClient(LLMClient):
    """OpenAI implementation."""
    
    def __init__(self, api_key: str):
        self.client = AsyncOpenAI(api_key=api_key)
    
    async def generate(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
```

## Cost Tracking Decorator

```python
def track_cost(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        # Track tokens and cost
        return result
    return wrapper
```
