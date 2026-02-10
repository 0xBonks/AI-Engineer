"""
Exercise: Multi-Environment Configuration

TODO: Create config for dev/staging/prod environments
"""

from pydantic import BaseModel
from typing import Literal

class EnvironmentConfig(BaseModel):
    env: Literal["dev", "staging", "prod"]
    api_key: str
    debug: bool = False

# TODO: Implement environment-specific configs
