# Solutions for Async Programming Exercises

## Exercise 01: Concurrent OpenAI Client

### Complete Solution

```python
import asyncio
import os
import time
from typing import List, Dict
from openai import AsyncOpenAI


class ConcurrentOpenAIClient:
    """Async client for processing multiple OpenAI prompts concurrently."""
    
    def __init__(self, api_key: str, max_concurrent: int = 5):
        self.client = AsyncOpenAI(api_key=api_key)
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.total_tokens = 0
        self.completed = 0
    
    async def generate_completion(self, prompt: str) -> Dict:
        """Generate completion for a single prompt with error handling."""
        async with self.semaphore:  # Limit concurrency
            try:
                response = await self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=50
                )
                
                self.total_tokens += response.usage.total_tokens
                self.completed += 1
                
                return {
                    "success": True,
                    "prompt": prompt,
                    "response": response.choices[0].message.content,
                    "tokens": response.usage.total_tokens
                }
            
            except Exception as e:
                return {
                    "success": False,
                    "prompt": prompt,
                    "error": str(e)
                }
    
    async def batch_generate(self, prompts: List[str]) -> List[Dict]:
        """Process multiple prompts concurrently."""
        print(f"Processing {len(prompts)} prompts (max {self.semaphore._value} concurrent)...\\n")
        
        start = time.time()
        results = await asyncio.gather(*[self.generate_completion(p) for p in prompts])
        elapsed = time.time() - start
        
        successful = sum(1 for r in results if r["success"])
        
        print(f"\\nCompleted: {successful}/{len(prompts)} successful")
        print(f"Time: {elapsed:.2f}s ({len(prompts)/elapsed:.1f} prompts/sec)")
        print(f"Total tokens: {self.total_tokens}")
        print(f"Est. cost: ${self.total_tokens * 0.0000015:.4f}")
        
        return results
```

### Key Concepts:

1. **Semaphore**: `asyncio.Semaphore(max_concurrent)` limits concurrent requests
2. **Error Handling**: Individual try/except so one failure doesn't stop others
3. **Token Tracking**: Accumulate tokens from all requests
4. **asyncio.gather**: Run all requests concurrently

---

## Exercise 02: Rate-Limited Processor

### Complete Solution

```python
import asyncio
import time
from typing import List, Dict
import httpx


class RateLimitedProcessor:
    """Process requests with rate limiting and retry logic."""
    
    def __init__(
        self,
        max_concurrent: int = 5,
        max_retries: int = 3,
        timeout: float = 10.0
    ):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.max_retries = max_retries
        self.timeout = timeout
        self.completed = 0
        self.failed = 0
    
    async def fetch_with_retry(self, url: str) -> Dict:
        """Fetch URL with retry logic and exponential backoff."""
        async with self.semaphore:
            for attempt in range(self.max_retries + 1):
                try:
                    async with httpx.AsyncClient() as client:
                        response = await asyncio.wait_for(
                            client.get(url, timeout=self.timeout),
                            timeout=self.timeout
                        )
                        response.raise_for_status()
                        self.completed += 1
                        return {
                            "success": True,
                            "url": url,
                            "status": response.status_code,
                            "data": response.json()
                        }
                
                except (httpx.HTTPError, asyncio.TimeoutError) as e:
                    if attempt < self.max_retries:
                        # Exponential backoff
                        delay = 1.0 * (2 ** attempt)
                        print(f"Retry {attempt + 1}/{self.max_retries} for {url[-20:]} in {delay}s...")
                        await asyncio.sleep(delay)
                    else:
                        self.failed += 1
                        return {
                            "success": False,
                            "url": url,
                            "error": str(e),
                            "attempts": attempt + 1
                        }
    
    async def process_batch(self, urls: List[str]) -> List[Dict]:
        """Process multiple URLs with progress tracking."""
        print(f"Processing {len(urls)} URLs...")
        print(f"Settings: max_concurrent={self.semaphore._value}, max_retries={self.max_retries}\\n")
        
        start = time.time()
        results = await asyncio.gather(*[self.fetch_with_retry(url) for url in urls])
        elapsed = time.time() - start
        
        print(f"\\nResults: {self.completed} successful, {self.failed} failed")
        print(f"Time: {elapsed:.2f}s ({len(urls)/elapsed:.1f} req/sec)")
        
        return results
```

### Key Concepts:

1. **Exponential Backoff**: `delay = base * (2 ** attempt)` - 1s, 2s, 4s, 8s...
2. **Retry Loop**: Attempt up to `max_retries` times
3. **Timeout Handling**: Use `asyncio.wait_for()` to enforce timeouts
4. **Progress Tracking**: Count completed and failed requests

---

## Testing Your Solutions

### Run Tests
```bash
# Run all tests
pytest test_async_exercises.py -v

# Run specific test
pytest test_async_exercises.py::TestConcurrentAPIClient -v

# Run with coverage
pytest test_async_exercises.py --cov=exercises --cov-report=html
```

### Manual Testing

```python
# Test Exercise 01
client = ConcurrentOpenAIClient(api_key=os.getenv("OPENAI_API_KEY"), max_concurrent=3)
prompts = ["What is Python?", "What is async?", "What is AI?"]
results = asyncio.run(client.batch_generate(prompts))

# Test Exercise 02
processor = RateLimitedProcessor(max_concurrent=5, max_retries=2)
urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 11)]
results = asyncio.run(processor.process_batch(urls))
```

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Not using semaphore
```python
# Wrong: All requests run at once
results = await asyncio.gather(*[fetch(url) for url in urls])
```

```python
# Right: Semaphore limits concurrency
async with semaphore:
    result = await fetch(url)
```

### ❌ Mistake 2: No error handling
```python
# Wrong: One error stops everything
results = await asyncio.gather(*tasks)
```

```python
# Right: Handle errors individually
try:
    result = await task()
except Exception as e:
    result = {"error": str(e)}
```

### ❌ Mistake 3: Linear retry delays
```python
# Wrong: Same delay each time
await asyncio.sleep(1.0)
```

```python
# Right: Exponential backoff
delay = base_delay * (2 ** attempt)
await asyncio.sleep(delay)
```

---

## Performance Benchmarks

### Expected Results:

**Exercise 01 (10 prompts, max_concurrent=3):**
- Sequential (hypothetical): ~50s
- Concurrent: ~15s
- **Speedup**: ~3x

**Exercise 02 (20 URLs, max_concurrent=5):**
- Sequential: ~10s
- Concurrent: ~2s
- **Speedup**: ~5x

---

## Next Steps

1. ✅ Understand semaphore pattern
2. ✅ Implement retry with backoff
3. ✅ Handle timeouts properly
4. ➡️ **Module 02-02**: Add type hints with Pydantic
5. ➡️ **Module 02-03**: Add proper logging

---

## Additional Resources

- [asyncio documentation](https://docs.python.org/3/library/asyncio.html)
- [httpx async client](https://www.python-httpx.org/async/)
- [OpenAI rate limits](https://platform.openai.com/docs/guides/rate-limits)
- [Retry patterns](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)
