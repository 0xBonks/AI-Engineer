"""
Solution: Streaming Chat Application

Complete implementation with typing indicators and progress tracking.
"""

from openai import OpenAI
from dotenv import load_dotenv
import tiktoken
import time
import sys

load_dotenv()
client = OpenAI()

def typing_indicator(duration: float = 1.0):
    """Show animated typing indicator."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    
    while time.time() < end_time:
        sys.stdout.write(f"\r{frames[i % len(frames)]} Thinking...")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    
    sys.stdout.write("\r" + " " * 20 + "\r")  # Clear line
    sys.stdout.flush()

def stream_with_progress(messages: list, model: str = "gpt-3.5-turbo"):
    """Stream response with real-time progress."""
    encoding = tiktoken.encoding_for_model(model)
    
    # Show typing indicator
    typing_indicator(0.5)
    
    # Create stream
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True
    )
    
    full_content = ""
    token_count = 0
    update_interval = 10  # Update count every N tokens
    
    print("Assistant: ", end='', flush=True)
    
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        
        if delta:
            full_content += delta
            print(delta, end='', flush=True)
            
            # Update token count periodically
            new_count = len(encoding.encode(full_content))
            if new_count >= token_count + update_interval:
                token_count = new_count
    
    # Final token count
    token_count = len(encoding.encode(full_content))
    print(f"\n\n📊 {token_count} tokens")
    
    return full_content, token_count

def streaming_chat():
    """Main streaming chat loop."""
    print("💬 Streaming Chat")
    print("Commands: /clear, /stats, quit")
    print("=" * 50)
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    total_tokens = 0
    turn_count = 0
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Handle commands
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!")
            break
        
        if user_input == '/clear':
            messages = [messages[0]]  # Keep system prompt
            total_tokens = 0
            turn_count = 0
            print("🗑️  Conversation cleared!")
            continue
        
        if user_input == '/stats':
            print(f"\n📊 Statistics:")
            print(f"  • Turns: {turn_count}")
            print(f"  • Total tokens: {total_tokens}")
            print(f"  • Messages: {len(messages)}")
            continue
        
        if not user_input:
            continue
        
        # Add user message
        messages.append({"role": "user", "content": user_input})
        
        try:
            # Stream response
            content, tokens = stream_with_progress(messages)
            
            # Add assistant response
            messages.append({"role": "assistant", "content": content})
            
            # Update stats
            total_tokens += tokens
            turn_count += 1
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            messages.pop()  # Remove user message on error
            continue

def main():
    streaming_chat()

if __name__ == "__main__":
    main()
