"""
Module 04 - Exercise 03: Ollama Local Deployment
=================================================

Task: Set up Ollama and run models locally with Python SDK.

Learning Objectives:
- Interact with Ollama using Python
- Manage local models programmatically
- Implement streaming responses
- Compare local vs cloud performance

Prerequisites:
--------------
- Ollama installed (https://ollama.ai)
- At least one model pulled (ollama pull llama3.2:3b)

Instructions:
-------------
1. Complete the OllamaManager class
2. Implement conversation management
3. Create performance benchmarks
4. Build a local chat interface

Success Criteria:
-----------------
- Successfully connect to Ollama
- Run inference on local models
- Implement streaming
- Compare performance metrics
"""

import ollama
import time
from typing import List, Dict, Optional, Generator
from dataclasses import dataclass, field


@dataclass
class Message:
    """Chat message."""
    role: str  # 'user', 'assistant', or 'system'
    content: str


@dataclass
class OllamaResponse:
    """Response from Ollama."""
    model: str
    message: str
    time_seconds: float
    tokens_per_second: Optional[float] = None


class OllamaManager:
    """Manage Ollama models and inference."""
    
    def __init__(self):
        """Initialize Ollama manager."""
        self.default_model = "llama3.2:3b"
    
    def list_models(self) -> List[str]:
        """
        List all locally available models.
        
        Returns:
            List of model names
        
        TODO: Implement this method
        - Use ollama.list()
        - Extract model names from response
        - Return as list of strings
        """
        # Your code here
        pass
    
    def is_available(self, model: str) -> bool:
        """
        Check if a model is available locally.
        
        Args:
            model: Model name
        
        Returns:
            True if model exists locally
        
        TODO: Implement this method
        - Get list of models
        - Check if model is in list
        """
        # Your code here
        pass
    
    def generate(
        self,
        prompt: str,
        model: Optional[str] = None,
        system: Optional[str] = None
    ) -> OllamaResponse:
        """
        Generate text using a local model.
        
        Args:
            prompt: User input
            model: Model name (defaults to self.default_model)
            system: System prompt
        
        Returns:
            OllamaResponse with generated text
        
        TODO: Implement this method
        - Use ollama.chat() or ollama.generate()
        - Measure execution time
        - Extract response text
        - Calculate tokens per second if available
        """
        # Your code here
        pass
    
    def stream_generate(
        self,
        prompt: str,
        model: Optional[str] = None
    ) -> Generator[str, None, None]:
        """
        Stream generated text token by token.
        
        Args:
            prompt: User input
            model: Model name
        
        Yields:
            Text tokens as they're generated
        
        TODO: Implement this method
        - Use ollama.chat() with stream=True
        - Yield tokens as they arrive
        - Handle the streaming response format
        """
        # Your code here
        pass
    
    def show_model_info(self, model: str) -> Dict:
        """
        Get detailed information about a model.
        
        Args:
            model: Model name
        
        Returns:
            Dictionary with model information
        
        TODO: Implement this method
        - Use ollama.show()
        - Return model details
        - Handle errors for non-existent models
        """
        # Your code here
        pass


class ConversationManager:
    """Manage multi-turn conversations with Ollama."""
    
    def __init__(self, model: str = "llama3.2:3b", system: Optional[str] = None):
        """
        Initialize conversation manager.
        
        Args:
            model: Model name
            system: System prompt
        """
        self.model = model
        self.messages: List[Message] = []
        
        if system:
            self.messages.append(Message(role="system", content=system))
    
    def add_message(self, role: str, content: str) -> None:
        """
        Add a message to conversation history.
        
        TODO: Implement this method
        - Create Message object
        - Append to self.messages
        """
        # Your code here
        pass
    
    def get_response(self, user_input: str) -> str:
        """
        Get response for user input.
        
        Args:
            user_input: User's message
        
        Returns:
            Assistant's response
        
        TODO: Implement this method
        - Add user message to history
        - Format messages for ollama.chat()
        - Get response from model
        - Add assistant response to history
        - Return response text
        """
        # Your code here
        pass
    
    def reset(self) -> None:
        """
        Reset conversation history.
        
        TODO: Implement this method
        - Clear messages
        - Keep system message if it exists
        """
        # Your code here
        pass
    
    def get_history(self) -> List[Message]:
        """
        Get conversation history.
        
        TODO: Implement this method
        - Return copy of messages
        """
        # Your code here
        pass


class PerformanceBenchmark:
    """Benchmark local model performance."""
    
    def __init__(self, manager: OllamaManager):
        self.manager = manager
    
    def benchmark_model(
        self,
        model: str,
        prompts: List[str]
    ) -> Dict[str, float]:
        """
        Benchmark a model's performance.
        
        Args:
            model: Model name
            prompts: List of test prompts
        
        Returns:
            Dictionary with performance metrics
        
        TODO: Implement this method
        - Run each prompt through the model
        - Collect timing data
        - Calculate statistics:
            - Average response time
            - Min/max response time
            - Average tokens per second
        - Return metrics dictionary
        """
        # Your code here
        pass
    
    def compare_models(
        self,
        models: List[str],
        prompt: str
    ) -> Dict[str, OllamaResponse]:
        """
        Compare multiple models on the same prompt.
        
        Args:
            models: List of model names
            prompt: Test prompt
        
        Returns:
            Dictionary mapping model names to responses
        
        TODO: Implement this method
        - Generate with each model
        - Collect responses
        - Return comparison dict
        """
        # Your code here
        pass


def interactive_chat(model: str = "llama3.2:3b"):
    """
    Interactive chat interface with local model.
    
    Args:
        model: Model name
    
    TODO: Implement this function
    - Create ConversationManager
    - Loop for user input
    - Display responses
    - Handle 'quit', 'reset', 'history' commands
    - Show token/sec if available
    """
    # Your code here
    pass


def test_ollama_manager():
    """Test the OllamaManager class."""
    
    manager = OllamaManager()
    
    # Test 1: List models
    print("Test 1: Listing models...")
    models = manager.list_models()
    assert isinstance(models, list), "Should return a list"
    print(f"✓ Found {len(models)} models")
    
    if not models:
        print("⚠️  No models found. Run: ollama pull llama3.2:3b")
        return
    
    test_model = models[0]
    
    # Test 2: Check availability
    print("\nTest 2: Checking model availability...")
    available = manager.is_available(test_model)
    assert available is True, "Should find the model"
    print(f"✓ {test_model} is available")
    
    # Test 3: Generate text
    print("\nTest 3: Generating text...")
    response = manager.generate("Say hello!", model=test_model)
    assert response is not None, "Should return response"
    assert len(response.message) > 0, "Should have content"
    print(f"✓ Generated response in {response.time_seconds:.2f}s")
    
    # Test 4: Streaming
    print("\nTest 4: Testing streaming...")
    tokens = list(manager.stream_generate("Count to 3", model=test_model))
    assert len(tokens) > 0, "Should stream tokens"
    print(f"✓ Streamed {len(tokens)} tokens")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # TODO: Complete the implementation and run tests
    # test_ollama_manager()
    
    # Example usage:
    # manager = OllamaManager()
    # response = manager.generate("Hello!")
    # print(response.message)
    
    # Interactive chat:
    # interactive_chat()
    
    print("TODO: Implement the OllamaManager and related classes")
    print("Make sure Ollama is running: ollama serve")
    print("Pull a model first: ollama pull llama3.2:3b")
    print("Run test_ollama_manager() when complete")
