"""
Exercise: Create Pydantic models for OpenAI API

TODO: Implement complete models for OpenAI Chat Completions API
Success Criteria:
- All fields properly typed
- Validation works
- JSON parsing works
- Helper methods included
"""

from pydantic import BaseModel, Field
from typing import List, Optional

# TODO: Implement these models
class Message(BaseModel):
    pass

class ChatCompletion(BaseModel):
    pass

# Test your implementation
if __name__ == "__main__":
    print("TODO: Implement OpenAI models")
