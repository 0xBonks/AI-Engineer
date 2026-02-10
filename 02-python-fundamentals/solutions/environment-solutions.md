# Environment Management Solutions

## Virtual Environments

Best practices:
1. Always use virtual environments
2. Never commit venv/ directory
3. Keep requirements.txt updated
4. Document Python version requirement

## Multi-Environment Config

```python
import os
from pydantic import BaseModel

class Config(BaseModel):
    env: str
    api_key: str
    debug: bool
    
    @classmethod
    def from_env(cls):
        return cls(
            env=os.getenv("ENV", "dev"),
            api_key=os.getenv("API_KEY"),
            debug=os.getenv("DEBUG", "false").lower() == "true"
        )
```
