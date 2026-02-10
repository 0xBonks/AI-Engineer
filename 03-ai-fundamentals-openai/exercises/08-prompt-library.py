"""
Exercise: Build a Reusable Prompt Library

Create a library of reusable, production-ready prompts.
"""

from openai import OpenAI
from dotenv import load_dotenv
from typing import Dict, List

load_dotenv()

class PromptLibrary:
    """Collection of reusable prompts for common tasks."""
    
    # TODO: Add system prompts for different roles
    ROLES = {
        "code_reviewer": "TODO: Add code review prompt",
        "teacher": "TODO: Add teaching prompt",
        "writer": "TODO: Add creative writing prompt",
        "analyst": "TODO: Add data analysis prompt"
    }
    
    # TODO: Add prompt templates
    TEMPLATES = {
        "summarize": "TODO: Summarization template",
        "extract": "TODO: Data extraction template",
        "compare": "TODO: Comparison template"
    }
    
    @staticmethod
    def build_prompt(template: str, **kwargs) -> str:
        """Build prompt from template with variables."""
        # TODO: Implement template variable substitution
        pass
    
    @staticmethod
    def few_shot_examples(task: str) -> List[Dict]:
        """Get few-shot examples for common tasks."""
        # TODO: Return appropriate examples
        pass

# TODO: Implement methods and add more prompts
