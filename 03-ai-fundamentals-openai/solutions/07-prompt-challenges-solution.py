"""
Solution: Prompt Engineering Challenges
"""

from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI()

def challenge_extract_data():
    """Extract structured data using few-shot learning."""
    messages = [
        {"role": "system", "content": "Extract contact information as JSON with keys: name, email, phone. If field missing, use null."},
        # Few-shot examples
        {"role": "user", "content": "Contact Sarah at sarah@test.com"},
        {"role": "assistant", "content": '{"name": "Sarah", "email": "sarah@test.com", "phone": null}'},
        {"role": "user", "content": "Call Mike at 555-9999"},
        {"role": "assistant", "content": '{"name": "Mike", "email": null, "phone": "555-9999"}'},
        # Actual task
        {"role": "user", "content": "Contact John at john@email.com or call 555-1234"}
    ]
    
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return json.loads(response.choices[0].message.content)

def challenge_sentiment_analysis():
    """Sentiment with chain-of-thought reasoning."""
    messages = [{
        "role": "user",
        "content": """Analyze sentiment of: "The product works but shipping took forever."
        
Let's think step by step:
1. Identify positive aspects
2. Identify negative aspects
3. Determine overall sentiment
4. Provide reasoning"""
    }]
    
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content

def challenge_force_format():
    """Enforce exact output format."""
    messages = [
        {"role": "system", "content": """You MUST respond in this EXACT format:
PRO: [one benefit]
CON: [one drawback]
VERDICT: [one sentence conclusion]

Never deviate from this format."""},
        {"role": "user", "content": "Analyze remote work"}
    ]
    
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content

def challenge_creative_writing():
    """Creative writing with constraints."""
    messages = [{
        "role": "system",
        "content": """Write a story with these requirements:
- Exactly 50 words (count carefully!)
- Must include: robot, coffee, mystery
- Must end with a cliffhanger question
- Be creative and engaging"""
    }, {
        "role": "user",
        "content": "Write the story now."
    }]
    
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, temperature=1.2)
    return response.choices[0].message.content

def challenge_complex_reasoning():
    """Multi-step math reasoning."""
    messages = [{
        "role": "user",
        "content": """Problem: If Alice can paint a room in 3 hours and Bob in 2 hours, how long together?

Let's solve step by step:
1. Calculate Alice's rate (rooms per hour)
2. Calculate Bob's rate (rooms per hour)
3. Add their rates together
4. Calculate time = 1 room / combined rate
5. State the final answer"""
    }]
    
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content

def run_all_challenges():
    """Run all challenges and display results."""
    print("CHALLENGE 1: Data Extraction")
    print("="*60)
    result = challenge_extract_data()
    print(json.dumps(result, indent=2))
    
    print("\n\nCHALLENGE 2: Sentiment Analysis")
    print("="*60)
    print(challenge_sentiment_analysis())
    
    print("\n\nCHALLENGE 3: Format Enforcement")
    print("="*60)
    print(challenge_force_format())
    
    print("\n\nCHALLENGE 4: Creative Writing")
    print("="*60)
    story = challenge_creative_writing()
    print(story)
    print(f"\nWord count: {len(story.split())}")
    
    print("\n\nCHALLENGE 5: Complex Reasoning")
    print("="*60)
    print(challenge_complex_reasoning())

if __name__ == "__main__":
    run_all_challenges()
