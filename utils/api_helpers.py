"""
API helper utilities for robust AI API interactions.

This module provides:
- Retry logic with exponential backoff
- Rate limiting utilities
- Error handling patterns
- Logging integration
- Response validation helpers

Example usage:
    from utils.api_helpers import retry_with_backoff, RateLimiter
    
    # Retry decorator
    @retry_with_backoff(max_retries=3)
    def call_api():
        return client.chat.completions.create(...)
    
    # Rate limiter
    rate_limiter = RateLimiter(max_requests=60, time_window=60)
    with rate_limiter:
        response = client.chat.completions.create(...)
"""

import time
import logging
from typing import Callable, Optional, Any, TypeVar, Dict
from functools import wraps
from datetime import datetime, timedelta
import asyncio
from collections import deque


# Configure logging
logger = logging.getLogger(__name__)


T = TypeVar('T')


class APIError(Exception):
    """Base exception for API errors."""
    pass


class RateLimitError(APIError):
    """Exception raised when rate limit is exceeded."""
    pass


class RetryableError(APIError):
    """Exception for errors that should trigger a retry."""
    pass


def retry_with_backoff(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    max_delay: float = 60.0,
    exponential_base: float = 2.0,
    jitter: bool = True,
    retryable_exceptions: tuple = (Exception,)
):
    """
    Decorator that implements exponential backoff retry logic.
    
    Args:
        max_retries: Maximum number of retry attempts
        initial_delay: Initial delay in seconds
        max_delay: Maximum delay in seconds
        exponential_base: Base for exponential backoff
        jitter: Add random jitter to prevent thundering herd
        retryable_exceptions: Tuple of exceptions that should trigger retry
    
    Example:
        @retry_with_backoff(max_retries=3, initial_delay=1.0)
        def api_call():
            return client.chat.completions.create(...)
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            delay = initial_delay
            
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                
                except retryable_exceptions as e:
                    if attempt == max_retries:
                        logger.error(f"Max retries ({max_retries}) exceeded for {func.__name__}")
                        raise
                    
                    # Calculate delay with exponential backoff
                    if jitter:
                        import random
                        actual_delay = delay * (0.5 + random.random())
                    else:
                        actual_delay = delay
                    
                    actual_delay = min(actual_delay, max_delay)
                    
                    logger.warning(
                        f"Attempt {attempt + 1}/{max_retries} failed for {func.__name__}: {e}. "
                        f"Retrying in {actual_delay:.2f}s..."
                    )
                    
                    time.sleep(actual_delay)
                    delay *= exponential_base
        
        return wrapper
    return decorator


def async_retry_with_backoff(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    max_delay: float = 60.0,
    exponential_base: float = 2.0,
    jitter: bool = True,
    retryable_exceptions: tuple = (Exception,)
):
    """
    Async version of retry_with_backoff decorator.
    
    Args:
        Same as retry_with_backoff
    
    Example:
        @async_retry_with_backoff(max_retries=3)
        async def async_api_call():
            return await client.chat.completions.create(...)
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> T:
            delay = initial_delay
            
            for attempt in range(max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                
                except retryable_exceptions as e:
                    if attempt == max_retries:
                        logger.error(f"Max retries ({max_retries}) exceeded for {func.__name__}")
                        raise
                    
                    # Calculate delay with exponential backoff
                    if jitter:
                        import random
                        actual_delay = delay * (0.5 + random.random())
                    else:
                        actual_delay = delay
                    
                    actual_delay = min(actual_delay, max_delay)
                    
                    logger.warning(
                        f"Attempt {attempt + 1}/{max_retries} failed for {func.__name__}: {e}. "
                        f"Retrying in {actual_delay:.2f}s..."
                    )
                    
                    await asyncio.sleep(actual_delay)
                    delay *= exponential_base
        
        return wrapper
    return decorator


class RateLimiter:
    """
    Token bucket rate limiter for API calls.
    
    Example:
        rate_limiter = RateLimiter(max_requests=60, time_window=60)
        
        # As context manager
        with rate_limiter:
            response = call_api()
        
        # Or manually
        rate_limiter.acquire()
        response = call_api()
    """
    
    def __init__(
        self,
        max_requests: int = 60,
        time_window: float = 60.0
    ):
        """
        Initialize rate limiter.
        
        Args:
            max_requests: Maximum number of requests allowed
            time_window: Time window in seconds
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests: deque = deque()
    
    def acquire(self) -> None:
        """Acquire permission to make a request, blocking if necessary."""
        now = time.time()
        
        # Remove old requests outside time window
        while self.requests and self.requests[0] < now - self.time_window:
            self.requests.popleft()
        
        # Check if we've exceeded the rate limit
        if len(self.requests) >= self.max_requests:
            # Calculate how long to wait
            oldest_request = self.requests[0]
            wait_time = self.time_window - (now - oldest_request)
            
            if wait_time > 0:
                logger.info(f"Rate limit reached. Waiting {wait_time:.2f}s...")
                time.sleep(wait_time)
                # Recursively try again
                return self.acquire()
        
        # Record this request
        self.requests.append(time.time())
    
    def __enter__(self):
        """Context manager entry."""
        self.acquire()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        pass


class AsyncRateLimiter:
    """
    Async version of RateLimiter.
    
    Example:
        rate_limiter = AsyncRateLimiter(max_requests=60, time_window=60)
        
        async with rate_limiter:
            response = await call_api_async()
    """
    
    def __init__(
        self,
        max_requests: int = 60,
        time_window: float = 60.0
    ):
        """
        Initialize async rate limiter.
        
        Args:
            max_requests: Maximum number of requests allowed
            time_window: Time window in seconds
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests: deque = deque()
        self.lock = asyncio.Lock()
    
    async def acquire(self) -> None:
        """Acquire permission to make a request, blocking if necessary."""
        async with self.lock:
            now = time.time()
            
            # Remove old requests outside time window
            while self.requests and self.requests[0] < now - self.time_window:
                self.requests.popleft()
            
            # Check if we've exceeded the rate limit
            if len(self.requests) >= self.max_requests:
                # Calculate how long to wait
                oldest_request = self.requests[0]
                wait_time = self.time_window - (now - oldest_request)
                
                if wait_time > 0:
                    logger.info(f"Rate limit reached. Waiting {wait_time:.2f}s...")
                    await asyncio.sleep(wait_time)
                    # Try again after waiting
                    await self.acquire()
                    return
            
            # Record this request
            self.requests.append(time.time())
    
    async def __aenter__(self):
        """Async context manager entry."""
        await self.acquire()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        pass


def validate_response(
    response: Any,
    required_fields: Optional[list] = None
) -> bool:
    """
    Validate an API response has required fields.
    
    Args:
        response: API response object or dict
        required_fields: List of required field names
    
    Returns:
        True if valid, raises ValueError if invalid
    
    Example:
        response = client.chat.completions.create(...)
        validate_response(response, required_fields=['choices', 'usage'])
    """
    if required_fields is None:
        return True
    
    for field in required_fields:
        if isinstance(response, dict):
            if field not in response:
                raise ValueError(f"Response missing required field: {field}")
        else:
            if not hasattr(response, field):
                raise ValueError(f"Response missing required field: {field}")
    
    return True


def handle_api_error(error: Exception) -> Optional[str]:
    """
    Handle common API errors and return user-friendly message.
    
    Args:
        error: Exception from API call
    
    Returns:
        User-friendly error message or None
    """
    error_msg = str(error)
    
    # OpenAI-specific error handling
    if "insufficient_quota" in error_msg or "quota" in error_msg.lower():
        return (
            "API quota exceeded. Please check your billing settings and usage limits. "
            "Visit https://platform.openai.com/account/billing"
        )
    
    elif "invalid_api_key" in error_msg or "authentication" in error_msg.lower():
        return (
            "Invalid API key. Please check your .env file and ensure OPENAI_API_KEY is correct. "
            "Get your key from https://platform.openai.com/api-keys"
        )
    
    elif "rate_limit" in error_msg.lower():
        return (
            "Rate limit exceeded. Please wait a moment and try again. "
            "Consider implementing rate limiting in your code."
        )
    
    elif "timeout" in error_msg.lower():
        return (
            "Request timed out. Please check your internet connection and try again."
        )
    
    elif "model_not_found" in error_msg or "model" in error_msg.lower():
        return (
            "Model not found or not accessible. Please verify the model name and your API access. "
            "List available models: https://platform.openai.com/docs/models"
        )
    
    else:
        return f"API error: {error_msg}"


def log_api_call(
    model: str,
    prompt_tokens: int,
    completion_tokens: int,
    latency: float,
    metadata: Optional[Dict] = None
) -> None:
    """
    Log API call details for monitoring and debugging.
    
    Args:
        model: Model name
        prompt_tokens: Number of prompt tokens
        completion_tokens: Number of completion tokens
        latency: Request latency in seconds
        metadata: Optional metadata to include
    """
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "model": model,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
        "latency_seconds": round(latency, 3),
        "metadata": metadata or {}
    }
    
    logger.info(f"API call: {log_data}")


class RequestTimer:
    """
    Context manager to time API requests.
    
    Example:
        with RequestTimer() as timer:
            response = client.chat.completions.create(...)
        print(f"Request took {timer.elapsed:.2f}s")
    """
    
    def __init__(self):
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.elapsed: Optional[float] = None
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed = self.end_time - self.start_time


# Global rate limiter instance
_global_rate_limiter: Optional[RateLimiter] = None


def get_global_rate_limiter() -> RateLimiter:
    """Get or create global rate limiter from environment config."""
    global _global_rate_limiter
    
    if _global_rate_limiter is None:
        import os
        max_requests = int(os.getenv("MAX_REQUESTS_PER_MINUTE", "60"))
        _global_rate_limiter = RateLimiter(max_requests=max_requests, time_window=60.0)
    
    return _global_rate_limiter


def with_rate_limiting(func: Callable[..., T]) -> Callable[..., T]:
    """
    Decorator to add rate limiting to a function.
    
    Uses global rate limiter configured from environment variables.
    
    Example:
        @with_rate_limiting
        def call_api():
            return client.chat.completions.create(...)
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> T:
        rate_limiter = get_global_rate_limiter()
        with rate_limiter:
            return func(*args, **kwargs)
    
    return wrapper
