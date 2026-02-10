# Type Safety Solutions

## Exercise 1: OpenAI Models

```python
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str

class Choice(BaseModel):
    index: int
    message: Message
    finish_reason: str

class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

class ChatCompletion(BaseModel):
    id: str
    model: str
    choices: List[Choice]
    usage: Usage
    
    def get_content(self) -> str:
        """Extract message content."""
        return self.choices[0].message.content
    
    def get_total_tokens(self) -> int:
        """Get total tokens used."""
        return self.usage.total_tokens
```

## Exercise 2: Config Validation

```python
from pydantic import BaseModel, Field, field_validator
from typing import Optional

class AIConfig(BaseModel):
    api_key: str = Field(min_length=20, description="OpenAI API key")
    model: str = "gpt-3.5-turbo"
    max_tokens: int = Field(gt=0, le=4000, default=100)
    temperature: float = Field(ge=0.0, le=2.0, default=0.7)
    timeout: float = Field(gt=0, default=30.0)
    
    @field_validator('api_key')
    @classmethod
    def validate_api_key(cls, v: str) -> str:
        if not v.startswith('sk-'):
            raise ValueError('API key must start with sk-')
        return v
```

## Best Practices

1. Always use Pydantic for API responses
2. Add field validators for business logic
3. Use Field() for constraints
4. Run mypy in CI/CD
5. Document models with docstrings
