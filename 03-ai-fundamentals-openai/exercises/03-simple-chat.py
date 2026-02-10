"""
Exercise: Build a Simple Chat Interface

OBJECTIVE:
Build a command-line chat interface that maintains conversation history.

REQUIREMENTS:
1. Accept user input in a loop
2. Send to OpenAI Chat Completions API
3. Display assistant's response
4. Maintain conversation history
5. Type 'quit' to exit
6. Track and display token usage

STARTER CODE:
"""

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

def simple_chat():
    """
    Simple chat interface with OpenAI.
    
    TODO: Implement the following:
    1. Initialize empty messages list with system prompt
    2. Create main loop that:
       - Gets user input
       - Breaks if input is 'quit'
       - Adds user message to history
       - Calls OpenAI API
       - Displays assistant response
       - Adds assistant response to history
    3. Display token usage after each turn
    4. Handle errors gracefully
    """
    print("Chat Interface (type 'quit' to exit)")
    print("=" * 50)
    
    # TODO: Initialize messages with system prompt
    messages = []
    
    while True:
        # TODO: Get user input
        user_input = ""
        
        # TODO: Check for quit command
        
        # TODO: Add user message to messages list
        
        # TODO: Make API call
        try:
            pass  # Replace with API call
        except Exception as e:
            print(f"Error: {e}")
            continue
        
        # TODO: Extract and display response
        
        # TODO: Add assistant response to messages
        
        # TODO: Display token usage

def main():
    simple_chat()

if __name__ == "__main__":
    main()

"""
SUCCESS CRITERIA:
- [ ] Chat interface runs without errors
- [ ] Conversation history is maintained (bot remembers context)
- [ ] Token usage displayed after each turn
- [ ] Exits cleanly when user types 'quit'
- [ ] Errors handled gracefully

BONUS CHALLENGES:
1. Add command '/clear' to reset conversation
2. Add command '/history' to show full conversation
3. Add command '/save <filename>' to save conversation to JSON
4. Color code user vs assistant messages (use colorama library)
5. Add typing animation for assistant responses
"""
