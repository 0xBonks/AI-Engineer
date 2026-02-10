"""
Exercise: Build Reusable AI Components

TODO: Implement LLMClient base class with implementations
Success Criteria:
- Abstract base class
- OpenAI implementation
- Cost tracking decorator
- Session context manager
"""

from abc import ABC, abstractmethod

class LLMClient(ABC):
    """Base class for LLM clients."""
    
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        pass

# TODO: Implement OpenAIClient
# TODO: Implement cost_tracker decorator  
# TODO: Implement APISession context manager

if __name__ == "__main__":
    print("TODO: Implement AI components")
