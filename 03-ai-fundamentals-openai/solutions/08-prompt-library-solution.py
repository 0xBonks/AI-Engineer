"""
Solution: Production-Ready Prompt Library
"""

from openai import OpenAI
from dotenv import load_dotenv
from typing import Dict, List

load_dotenv()
client = OpenAI()

class PromptLibrary:
    """Professional prompt library for common tasks."""
    
    ROLES = {
        "code_reviewer": """You are a senior code reviewer. Analyze code for:
- Bugs and logic errors
- Performance and efficiency
- Security vulnerabilities
- Code style and best practices
Provide constructive, specific feedback.""",
        
        "teacher": """You are a patient, encouraging teacher. 
- Explain concepts clearly with examples
- Check for understanding
- Build on prior knowledge
- Never give direct homework answers
- Encourage critical thinking""",
        
        "writer": """You are a creative writer specializing in [genre].
- Use vivid, engaging language
- Show, don't tell
- Maintain consistent voice
- Create compelling narratives""",
        
        "analyst": """You are a data analyst. 
- Interpret data objectively
- Identify patterns and trends
- Provide actionable insights
- Support conclusions with evidence"""
    }
    
    TEMPLATES = {
        "summarize": """Summarize the following {content_type}:
{content}

Requirements:
- {length} summary
- Focus on key points
- Maintain objectivity
- Use bullet points if > 3 points""",
        
        "extract": """Extract {data_type} from:
{text}

Output format: {format}
If information missing: {missing_value}""",
        
        "compare": """Compare {item1} and {item2}:

Provide:
1. Key similarities
2. Key differences
3. Use cases for each
4. Recommendation for {context}"""
    }
    
    FEW_SHOT = {
        "sentiment": [
            {"role": "user", "content": "Review: Loved it!"},
            {"role": "assistant", "content": "Positive"},
            {"role": "user", "content": "Review: Disappointing."},
            {"role": "assistant", "content": "Negative"}
        ],
        
        "extract_json": [
            {"role": "user", "content": "Extract: John, 30, NYC"},
            {"role": "assistant", "content": '{"name":"John","age":30,"city":"NYC"}'},
            {"role": "user", "content": "Extract: Sarah, 25, LA"},
            {"role": "assistant", "content": '{"name":"Sarah","age":25,"city":"LA"}'}
        ]
    }
    
    @staticmethod
    def build_prompt(template: str, **kwargs) -> str:
        """Build prompt from template."""
        return PromptLibrary.TEMPLATES[template].format(**kwargs)
    
    @staticmethod
    def get_few_shot(task: str) -> List[Dict]:
        """Get few-shot examples."""
        return PromptLibrary.FEW_SHOT.get(task, [])
    
    @staticmethod
    def create_messages(role: str = None, few_shot: str = None, user_message: str = "") -> List[Dict]:
        """Build complete message array."""
        messages = []
        
        if role:
            messages.append({"role": "system", "content": PromptLibrary.ROLES[role]})
        
        if few_shot:
            messages.extend(PromptLibrary.get_few_shot(few_shot))
        
        if user_message:
            messages.append({"role": "user", "content": user_message})
        
        return messages

# Example usage
if __name__ == "__main__":
    # Code review
    messages = PromptLibrary.create_messages(
        role="code_reviewer",
        user_message="Review: def add(x,y): return x+y"
    )
    
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    print("CODE REVIEW:")
    print(response.choices[0].message.content)
    
    # Sentiment with few-shot
    messages = PromptLibrary.create_messages(
        few_shot="sentiment",
        user_message="Review: It was okay, I guess."
    )
    
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    print("\n\nSENTIMENT ANALYSIS:")
    print(response.choices[0].message.content)
