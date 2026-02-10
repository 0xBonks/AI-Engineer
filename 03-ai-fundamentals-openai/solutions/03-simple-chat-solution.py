"""
Solution: Simple Chat Interface

This is a complete, working implementation of the simple chat exercise.
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

def simple_chat():
    """
    Simple chat interface with OpenAI Chat Completions API.
    
    Features:
    - Maintains conversation history
    - Displays token usage
    - Handles errors
    - Clean exit with 'quit'
    """
    print("💬 Chat Interface (type 'quit' to exit)")
    print("=" * 50)
    
    # Initialize messages with system prompt
    messages = [
        {"role": "system", "content": "You are a helpful, friendly assistant."}
    ]
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check for quit command
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Add user message to history
        messages.append({"role": "user", "content": user_input})
        
        # Make API call
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7
            )
            
            # Extract response
            assistant_message = response.choices[0].message.content
            
            # Display response
            print(f"\nAssistant: {assistant_message}")
            
            # Add assistant response to history
            messages.append({"role": "assistant", "content": assistant_message})
            
            # Display token usage
            usage = response.usage
            print(f"\n📊 Tokens - Prompt: {usage.prompt_tokens}, "
                  f"Completion: {usage.completion_tokens}, "
                  f"Total: {usage.total_tokens}")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            # Remove the user message that caused error
            messages.pop()
            continue


def enhanced_chat():
    """
    Enhanced version with additional commands.
    
    Commands:
    - /clear: Reset conversation
    - /history: Show conversation history
    - quit: Exit
    """
    print("💬 Enhanced Chat Interface")
    print("Commands: /clear, /history, quit")
    print("=" * 50)
    
    system_prompt = "You are a helpful, friendly assistant."
    messages = [{"role": "system", "content": system_prompt}]
    
    while True:
        user_input = input("\nYou: ").strip()
        
        # Handle commands
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!")
            break
        
        if user_input == '/clear':
            messages = [{"role": "system", "content": system_prompt}]
            print("🗑️  Conversation cleared!")
            continue
        
        if user_input == '/history':
            print("\n📜 Conversation History:")
            for i, msg in enumerate(messages):
                role = msg['role'].title()
                content = msg['content'][:100]  # Truncate long messages
                print(f"  {i}. {role}: {content}")
            continue
        
        if not user_input:
            continue
        
        # Normal chat flow
        messages.append({"role": "user", "content": user_input})
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            
            assistant_message = response.choices[0].message.content
            print(f"\nAssistant: {assistant_message}")
            
            messages.append({"role": "assistant", "content": assistant_message})
            
            usage = response.usage
            print(f"\n📊 {usage.total_tokens} tokens")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            messages.pop()


def main():
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--enhanced':
        enhanced_chat()
    else:
        simple_chat()


if __name__ == "__main__":
    main()
