"""
Exercise: Prompt Engineering Challenges

OBJECTIVE:
Master prompt engineering by solving real-world challenges.

Complete each challenge by creating effective prompts.
"""

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# CHALLENGE 1: Data Extraction
def challenge_extract_data():
    """
    Extract structured data from unstructured text.
    
    Input: "Contact John at john@email.com or call 555-1234"
    Expected Output: {"name": "John", "email": "john@email.com", "phone": "555-1234"}
    
    TODO: Create system prompt + few-shot examples to extract contact info as JSON
    """
    pass

# CHALLENGE 2: Sentiment with Reasoning
def challenge_sentiment_analysis():
    """
    Classify sentiment AND explain why.
    
    Input: "The product works but shipping took forever."
    Expected: "Mixed - positive about product, negative about shipping"
    
    TODO: Use chain-of-thought to get sentiment + reasoning
    """
    pass

# CHALLENGE 3: Format Enforcement
def challenge_force_format():
    """
    Get EXACTLY the format you want.
    
    Expected format: "PRO: [benefit]\nCON: [drawback]\nVERDICT: [conclusion]"
    
    TODO: Create prompt that enforces this exact format
    """
    pass

# CHALLENGE 4: Creative Constraints
def challenge_creative_writing():
    """
    Creative writing with multiple constraints.
    
    Requirements:
    - Write a story
    - Exactly 50 words
    - Must include: robot, coffee, mystery
    - End with a cliffhanger
    
    TODO: System prompt with all constraints
    """
    pass

# CHALLENGE 5: Multi-Step Reasoning
def challenge_complex_reasoning():
    """
    Solve complex problem requiring multiple reasoning steps.
    
    Problem: "If Alice can paint a room in 3 hours and Bob in 2 hours, 
              how long together?"
    
    TODO: Use chain-of-thought to solve step-by-step
    """
    pass

if __name__ == "__main__":
    print("Prompt Engineering Challenges")
    print("=" * 60)
    print("\nImplement each challenge function!")
    print("Run tests: pytest tests/test_prompts.py")
