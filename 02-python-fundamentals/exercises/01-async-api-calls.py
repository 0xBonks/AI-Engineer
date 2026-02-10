"""
Exercise 01: Async API Calls

Build a concurrent OpenAI API client that processes multiple prompts efficiently.

Learning Objectives:
- Make concurrent API calls with async/await
- Handle errors gracefully
- Measure performance improvements
- Track token usage and costs

Success Criteria:
- Process 10 prompts concurrently
- Handle API errors without crashing
- Complete 5x faster than sequential
- Track total tokens used
"""

import asyncio
import os
import time
from typing import List, Dict
from openai import AsyncOpenAI


# TODO: Implement this class
class ConcurrentOpenAIClient:
    """
    Async client for processing multiple OpenAI prompts concurrently.
    
    Requirements:
    1. Initialize with API key and max concurrent requests
    2. Process multiple prompts using asyncio.gather()
    3. Track total tokens used
    4. Handle errors without stopping other requests
    5. Measure total time taken
    """
    
    def __init__(self, api_key: str, max_concurrent: int = 5):
        """
        Initialize the client.
        
        Args:
            api_key: OpenAI API key
            max_concurrent: Maximum number of concurrent requests
        """
        # TODO: Initialize AsyncOpenAI client
        # TODO: Create a semaphore with max_concurrent
        # TODO: Initialize token counter
        pass
    
    async def generate_completion(self, prompt: str) -> Dict:
        """
        Generate completion for a single prompt.
        
        Args:
            prompt: Text prompt
        
        Returns:
            Dictionary with success status, response, and token count
        """
        # TODO: Use semaphore to limit concurrency
        # TODO: Make API call to OpenAI
        # TODO: Handle errors and return appropriate dict
        # TODO: Track tokens used
        pass
    
    async def batch_generate(self, prompts: List[str]) -> List[Dict]:
        """
        Process multiple prompts concurrently.
        
        Args:
            prompts: List of text prompts
        
        Returns:
            List of result dictionaries
        """
        # TODO: Use asyncio.gather() to process all prompts
        # TODO: Measure time taken
        # TODO: Print summary stats
        pass


def test_concurrent_client():
    """Test the concurrent client implementation."""
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("⚠ OPENAI_API_KEY not set. Skipping test.")
        return
    
    # Test prompts
    prompts = [
        "What is Python?",
        "Explain async programming.",
        "What is machine learning?",
        "How do neural networks work?",
        "What is deep learning?",
        "Explain natural language processing.",
        "What are transformers in AI?",
        "How does GPT work?",
        "What is fine-tuning?",
        "Explain embeddings.",
    ]
    
    print(f"Testing with {len(prompts)} prompts...\n")
    
    # TODO: Create client instance
    # client = ConcurrentOpenAIClient(api_key, max_concurrent=3)
    
    # TODO: Process prompts
    # results = asyncio.run(client.batch_generate(prompts))
    
    # TODO: Print results
    # for i, result in enumerate(results, 1):
    #     if result["success"]:
    #         print(f"{i}. ✓ {result['prompt'][:40]}...")
    #         print(f"   Response: {result['response'][:60]}...")
    #         print(f"   Tokens: {result['tokens']}")
    #     else:
    #         print(f"{i}. ✗ {result['prompt'][:40]}...")
    #         print(f"   Error: {result['error']}")
    
    print("\n⚠ TODO: Implement ConcurrentOpenAIClient class")


if __name__ == "__main__":
    test_concurrent_client()
