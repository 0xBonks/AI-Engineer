"""
Exercise: Streaming Chat Application

OBJECTIVE:
Build a chat application that streams responses in real-time with progress indicators.

REQUIREMENTS:
1. Stream responses token-by-token
2. Display typing indicator before response starts
3. Show real-time token count
4. Handle streaming errors
5. Maintain conversation history
6. Support cancellation (bonus)

STARTER CODE:
"""

from openai import OpenAI
from dotenv import load_dotenv
import tiktoken
import time
import sys

load_dotenv()
client = OpenAI()

def typing_indicator(duration: float = 1.0):
    """
    Show a typing indicator animation.
    
    TODO: Implement typing animation
    - Display "..." with animation
    - Run for specified duration
    - Clear when done
    """
    pass

def stream_with_progress(messages: list, model: str = "gpt-3.5-turbo"):
    """
    Stream response with real-time progress indicators.
    
    TODO: Implement streaming with:
    1. Show typing indicator
    2. Stream tokens as they arrive
    3. Count tokens in real-time
    4. Display progress every N tokens
    5. Return full response and token count
    
    Returns:
        Tuple of (content, token_count)
    """
    # TODO: Initialize encoding
    encoding = None
    
    # TODO: Show typing indicator
    
    # TODO: Create streaming request
    
    # TODO: Process stream chunks
    full_content = ""
    token_count = 0
    
    # TODO: Return results
    return full_content, token_count

def streaming_chat():
    """
    Main chat loop with streaming.
    
    TODO: Implement chat loop with:
    - Conversation history
    - Streaming responses
    - Progress indicators
    - Error handling
    - Commands: /clear, /stats, quit
    """
    print("💬 Streaming Chat (type 'quit' to exit)")
    print("Commands: /clear, /stats")
    print("=" * 50)
    
    # TODO: Initialize conversation
    messages = []
    
    # TODO: Implement chat loop
    pass

def main():
    streaming_chat()

if __name__ == "__main__":
    main()

"""
SUCCESS CRITERIA:
- [ ] Responses stream token-by-token
- [ ] Typing indicator shows before response
- [ ] Token count updates in real-time
- [ ] Conversation history maintained
- [ ] Errors handled gracefully
- [ ] Clean UI with progress indicators

BONUS CHALLENGES:
1. Add async streaming for better performance
2. Implement "Stop" button to cancel mid-stream
3. Add word-per-second (WPS) speed indicator
4. Buffer tokens for smoother display
5. Color-code user vs assistant messages
"""
