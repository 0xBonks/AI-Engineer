"""
Exercise 02: Rate-Limited Async Processing

Implement rate limiting for API calls using semaphores and retry logic.

Learning Objectives:
- Control concurrency with semaphores
- Implement exponential backoff
- Handle rate limit errors
- Track progress in long-running operations

Success Criteria:
- Process URLs with configurable rate limit
- Retry failed requests with backoff
- Don't exceed rate limit
- Show progress during processing
"""

import asyncio
import time
from typing import List, Dict
import httpx


# TODO: Implement this class
class RateLimitedProcessor:
    """
    Process requests with rate limiting and retry logic.
    
    Requirements:
    1. Use semaphore to limit concurrent requests
    2. Implement retry with exponential backoff
    3. Track progress
    4. Handle timeouts
    """
    
    def __init__(
        self,
        max_concurrent: int = 5,
        max_retries: int = 3,
        timeout: float = 10.0
    ):
        """
        Initialize processor.
        
        Args:
            max_concurrent: Max number of concurrent requests
            max_retries: Max retry attempts
            timeout: Request timeout in seconds
        """
        # TODO: Create semaphore
        # TODO: Store config
        # TODO: Initialize counters
        pass
    
    async def fetch_with_retry(self, url: str) -> Dict:
        """
        Fetch URL with retry logic.
        
        Args:
            url: URL to fetch
        
        Returns:
            Result dictionary with success status
        """
        # TODO: Use semaphore
        # TODO: Implement retry loop with exponential backoff
        # TODO: Handle timeouts
        # TODO: Return result dict
        pass
    
    async def process_batch(self, urls: List[str]) -> List[Dict]:
        """
        Process multiple URLs with progress tracking.
        
        Args:
            urls: List of URLs to process
        
        Returns:
            List of results
        """
        # TODO: Use asyncio.gather()
        # TODO: Track and print progress
        # TODO: Return results
        pass


def test_rate_limited_processor():
    """Test the rate-limited processor."""
    # Test URLs (JSONPlaceholder API)
    urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 21)]
    
    print(f"Processing {len(urls)} URLs with rate limiting...\n")
    
    # TODO: Create processor with max 5 concurrent
    # processor = RateLimitedProcessor(max_concurrent=5, max_retries=2)
    
    # TODO: Process URLs
    # results = asyncio.run(processor.process_batch(urls))
    
    # TODO: Print summary
    # successful = sum(1 for r in results if r["success"])
    # print(f"\nResults: {successful}/{len(results)} successful")
    
    print("\n⚠ TODO: Implement RateLimitedProcessor class")


if __name__ == "__main__":
    test_rate_limited_processor()
