"""
Module 04 - Exercise 02: Hugging Face Inference
================================================

Task: Use Hugging Face Inference API to run open source models.

Learning Objectives:
- Use the InferenceClient for text generation
- Handle API responses and errors
- Compare model outputs
- Implement retry logic for rate limits

Instructions:
-------------
1. Complete the InferenceWrapper class
2. Implement error handling and retries
3. Create comparison tools
4. Test with multiple models

Success Criteria:
-----------------
- Successfully run inference on at least 2 models
- Handle rate limits gracefully
- Compare output quality
- Measure response times
"""

import os
import time
from typing import List, Dict, Optional
from dotenv import load_dotenv
from huggingface_hub import InferenceClient, HfHubHTTPError
from dataclasses import dataclass

load_dotenv()


@dataclass
class InferenceResult:
    """Container for inference results."""
    model: str
    prompt: str
    response: str
    time_seconds: float
    error: Optional[str] = None


class InferenceWrapper:
    """Wrapper for Hugging Face Inference API with error handling."""
    
    def __init__(self, token: Optional[str] = None):
        """
        Initialize the inference wrapper.
        
        Args:
            token: Hugging Face API token
        """
        self.token = token or os.getenv("HUGGINGFACE_TOKEN")
        self.client = InferenceClient(token=self.token)
        self.max_retries = 3
    
    def generate_text(
        self,
        prompt: str,
        model: str,
        max_new_tokens: int = 100,
        temperature: float = 0.7
    ) -> InferenceResult:
        """
        Generate text using specified model.
        
        Args:
            prompt: Input text
            model: Model ID
            max_new_tokens: Maximum tokens to generate
            temperature: Sampling temperature
        
        Returns:
            InferenceResult with response and metadata
        
        TODO: Implement this method
        - Use client.text_generation()
        - Measure execution time
        - Return InferenceResult object
        - Handle exceptions and return error in result
        """
        # Your code here
        pass
    
    def generate_with_retry(
        self,
        prompt: str,
        model: str,
        max_new_tokens: int = 100
    ) -> InferenceResult:
        """
        Generate text with exponential backoff retry logic.
        
        Args:
            prompt: Input text
            model: Model ID
            max_new_tokens: Maximum tokens to generate
        
        Returns:
            InferenceResult
        
        TODO: Implement this method
        - Try to generate text
        - If rate limited, wait and retry
        - Use exponential backoff (2^attempt seconds)
        - Return error after max_retries exceeded
        
        Hint: Check for "rate limit" in error message
        """
        # Your code here
        pass
    
    def compare_models(
        self,
        prompt: str,
        models: List[str],
        max_new_tokens: int = 100
    ) -> List[InferenceResult]:
        """
        Compare multiple models on the same prompt.
        
        Args:
            prompt: Input text
            models: List of model IDs
            max_new_tokens: Maximum tokens to generate
        
        Returns:
            List of InferenceResult objects
        
        TODO: Implement this method
        - Generate with each model
        - Collect results
        - Sort by response time
        """
        # Your code here
        pass
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str,
        max_tokens: int = 500
    ) -> InferenceResult:
        """
        Chat-style completion.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            model: Model ID
            max_tokens: Maximum tokens
        
        Returns:
            InferenceResult
        
        TODO: Implement this method
        - Use client.chat_completion()
        - Extract message content from response
        - Measure time
        """
        # Your code here
        pass


class ModelTester:
    """Test and compare model performance."""
    
    def __init__(self, wrapper: InferenceWrapper):
        self.wrapper = wrapper
    
    def run_benchmark(
        self,
        prompts: List[str],
        models: List[str]
    ) -> Dict[str, Dict]:
        """
        Benchmark models across multiple prompts.
        
        Args:
            prompts: List of test prompts
            models: List of model IDs
        
        Returns:
            Dictionary with statistics per model
        
        TODO: Implement this method
        - Run each prompt through each model
        - Calculate average response time
        - Calculate success rate
        - Return summary statistics
        """
        # Your code here
        pass
    
    def quality_comparison(
        self,
        prompt: str,
        models: List[str]
    ) -> None:
        """
        Display side-by-side quality comparison.
        
        Args:
            prompt: Test prompt
            models: List of model IDs
        
        TODO: Implement this method
        - Generate responses from all models
        - Display in formatted output
        - Show response time for each
        """
        # Your code here
        pass


def test_inference_wrapper():
    """Test the InferenceWrapper class."""
    
    wrapper = InferenceWrapper()
    
    # Test 1: Basic generation
    print("Test 1: Basic text generation...")
    result = wrapper.generate_text(
        "What is artificial intelligence?",
        "mistralai/Mistral-7B-Instruct-v0.3",
        max_new_tokens=50
    )
    assert result is not None, "Should return a result"
    assert result.response or result.error, "Should have response or error"
    print("✓ Basic generation works")
    
    # Test 2: Retry logic
    print("\nTest 2: Testing retry logic...")
    result = wrapper.generate_with_retry(
        "Explain quantum computing",
        "mistralai/Mistral-7B-Instruct-v0.3"
    )
    assert result is not None, "Should return a result"
    print("✓ Retry logic works")
    
    # Test 3: Model comparison
    print("\nTest 3: Comparing models...")
    models = [
        "mistralai/Mistral-7B-Instruct-v0.3",
        "microsoft/Phi-3-mini-4k-instruct"
    ]
    results = wrapper.compare_models("Hello, how are you?", models)
    assert len(results) > 0, "Should return results"
    print(f"✓ Compared {len(results)} models")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # TODO: Complete the implementation and run tests
    # test_inference_wrapper()
    
    # Example usage:
    # wrapper = InferenceWrapper()
    # result = wrapper.generate_text("Hello", "mistralai/Mistral-7B-Instruct-v0.3")
    # print(result.response)
    
    print("TODO: Implement the InferenceWrapper class methods")
    print("Run test_inference_wrapper() when complete")
