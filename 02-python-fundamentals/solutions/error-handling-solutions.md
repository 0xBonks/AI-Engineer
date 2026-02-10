# Error Handling Solutions

## Exercise 1: Robust API Client

```python
import asyncio
import logging
from typing import Dict, Any
import httpx

logger = logging.getLogger(__name__)

class RobustAPIClient:
    """API client with comprehensive error handling."""
    
    def __init__(self, max_retries: int = 3, timeout: float = 30.0):
        self.max_retries = max_retries
        self.timeout = timeout
    
    async def call_api(self, url: str) -> Dict[str, Any]:
        """Make API call with retry and error handling."""
        for attempt in range(self.max_retries):
            try:
                async with httpx.AsyncClient() as client:
                    response = await asyncio.wait_for(
                        client.get(url),
                        timeout=self.timeout
                    )
                    response.raise_for_status()
                    return {"success": True, "data": response.json()}
            
            except httpx.HTTPStatusError as e:
                logger.error(f"HTTP {e.response.status_code}: {url}")
                if e.response.status_code >= 500 and attempt < self.max_retries - 1:
                    delay = 2 ** attempt
                    await asyncio.sleep(delay)
                    continue
                return {"success": False, "error": str(e)}
            
            except asyncio.TimeoutError:
                logger.error(f"Timeout: {url}")
                if attempt < self.max_retries - 1:
                    continue
                return {"success": False, "error": "timeout"}
            
            except Exception as e:
                logger.exception(f"Unexpected error: {url}")
                return {"success": False, "error": str(e)}
```

## Exercise 2: Production Logging

```python
import logging
from logging.handlers import RotatingFileHandler
import sys

def setup_logger(name: str, log_file: str = "app.log") -> logging.Logger:
    """Configure production logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Console handler
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    console_fmt = logging.Formatter('%(levelname)s: %(message)s')
    console.setFormatter(console_fmt)
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_fmt = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(file_fmt)
    
    logger.addHandler(console)
    logger.addHandler(file_handler)
    
    return logger
```

## Exercise 3: Retry Decorator

```python
from functools import wraps
import asyncio

def retry_async(max_retries: int = 3, base_delay: float = 1.0):
    """Decorator for retry with exponential backoff."""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    delay = base_delay * (2 ** attempt)
                    logging.warning(f"Retry {attempt + 1}/{max_retries} after {delay}s")
                    await asyncio.sleep(delay)
        return wrapper
    return decorator

# Usage
@retry_async(max_retries=3, base_delay=1.0)
async def api_call():
    # Your API call here
    pass
```
