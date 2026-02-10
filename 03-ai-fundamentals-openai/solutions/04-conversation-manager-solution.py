"""
Solution: Conversation Manager

Complete implementation of ConversationManager class with all features.
"""

from openai import OpenAI
from dotenv import load_dotenv
import tiktoken
import json
from typing import List, Dict, Optional
from pathlib import Path

load_dotenv()


class ConversationManager:
    """
    Robust conversation manager with context window management.
    
    Features:
    - Maintains conversation history
    - Tracks token usage
    - Automatic history trimming
    - Save/load conversations
    - Statistics tracking
    """
    
    def __init__(
        self,
        system_prompt: str = "You are a helpful assistant.",
        model: str = "gpt-3.5-turbo",
        max_context_tokens: int = 3000,
        temperature: float = 1.0
    ):
        self.model = model
        self.max_context_tokens = max_context_tokens
        self.temperature = temperature
        self.client = OpenAI()
        
        # Initialize encoding for token counting
        self.encoding = tiktoken.encoding_for_model(model)
        
        # Initialize messages with system prompt
        self.messages: List[Dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]
        
        # Track total tokens
        self.total_tokens_used = 0
    
    def count_tokens(self, text: str = None) -> int:
        """Count tokens in text or entire conversation."""
        if text is not None:
            # Count tokens in specific text
            return len(self.encoding.encode(text))
        else:
            # Count tokens in all messages
            total = 0
            for msg in self.messages:
                total += len(self.encoding.encode(msg['content']))
            return total
    
    def trim_history(self) -> int:
        """Remove old messages if over token limit."""
        removed = 0
        
        while self.count_tokens() > self.max_context_tokens and len(self.messages) > 2:
            # Keep system prompt (index 0), remove oldest user/assistant pair
            if len(self.messages) > 1:
                self.messages.pop(1)  # Remove second message
                removed += 1
        
        return removed
    
    def add_message(self, role: str, content: str):
        """Add a message to conversation history."""
        self.messages.append({"role": role, "content": content})
    
    def send_message(self, user_message: str) -> Dict:
        """
        Send a message and get response with metadata.
        
        Returns:
            Dict with: content, tokens_used, finish_reason, model
        """
        # Add user message
        self.add_message("user", user_message)
        
        # Trim if needed
        trimmed = self.trim_history()
        if trimmed > 0:
            print(f"⚠️  Trimmed {trimmed} old messages to stay within context limit")
        
        try:
            # Make API call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=self.temperature
            )
            
            # Extract response
            assistant_message = response.choices[0].message.content
            finish_reason = response.choices[0].finish_reason
            tokens_used = response.usage.total_tokens
            
            # Add assistant response to history
            self.add_message("assistant", assistant_message)
            
            # Update total tokens
            self.total_tokens_used += tokens_used
            
            return {
                'content': assistant_message,
                'tokens_used': tokens_used,
                'finish_reason': finish_reason,
                'model': response.model
            }
            
        except Exception as e:
            # Remove user message on error
            self.messages.pop()
            raise Exception(f"API call failed: {e}")
    
    def get_history(self) -> List[Dict[str, str]]:
        """Return full conversation history."""
        return self.messages.copy()
    
    def clear_history(self):
        """Clear conversation history (keep system prompt)."""
        system_prompt = self.messages[0]
        self.messages = [system_prompt]
        self.total_tokens_used = 0
    
    def save_conversation(self, filepath: str):
        """Save conversation to JSON file."""
        data = {
            'model': self.model,
            'temperature': self.temperature,
            'total_tokens': self.total_tokens_used,
            'messages': self.messages
        }
        
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"💾 Saved to {filepath}")
    
    def load_conversation(self, filepath: str):
        """Load conversation from JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        self.model = data.get('model', self.model)
        self.temperature = data.get('temperature', self.temperature)
        self.total_tokens_used = data.get('total_tokens', 0)
        self.messages = data['messages']
        
        print(f"📂 Loaded from {filepath}")
    
    def get_stats(self) -> Dict:
        """Get conversation statistics."""
        # Count turns (user/assistant pairs)
        turn_count = sum(1 for msg in self.messages if msg['role'] == 'user')
        
        return {
            'turn_count': turn_count,
            'total_tokens': self.total_tokens_used,
            'message_count': len(self.messages),
            'current_context_tokens': self.count_tokens()
        }


def test_conversation_manager():
    """Comprehensive test of ConversationManager."""
    print("🧪 Testing ConversationManager...")
    print("=" * 50)
    
    # Test 1: Basic conversation
    print("\n1️⃣  Basic Conversation:")
    conv = ConversationManager(
        system_prompt="You are a helpful math tutor.",
        max_context_tokens=500
    )
    
    response = conv.send_message("What is 2+2?")
    print(f"Q: What is 2+2?")
    print(f"A: {response['content']}")
    print(f"Tokens: {response['tokens_used']}")
    
    # Test 2: Context memory
    print("\n2️⃣  Testing Context Memory:")
    response = conv.send_message("What was my first question?")
    print(f"Q: What was my first question?")
    print(f"A: {response['content']}")
    
    # Test 3: Statistics
    print("\n3️⃣  Conversation Stats:")
    stats = conv.get_stats()
    for key, value in stats.items():
        print(f"  • {key}: {value}")
    
    # Test 4: Save/Load
    print("\n4️⃣  Save/Load Test:")
    test_file = "test_conversation.json"
    conv.save_conversation(test_file)
    
    new_conv = ConversationManager()
    new_conv.load_conversation(test_file)
    print(f"  Loaded {len(new_conv.messages)} messages")
    
    # Verify loaded correctly
    response = new_conv.send_message("Do you remember my questions?")
    print(f"  Continuation works: {bool(response['content'])}")
    
    # Test 5: Context trimming
    print("\n5️⃣  Context Trimming Test:")
    trim_conv = ConversationManager(max_context_tokens=200)
    
    for i in range(10):
        trim_conv.send_message(f"Tell me about number {i}")
    
    print(f"  After 10 messages: {len(trim_conv.messages)} messages kept")
    print(f"  Current tokens: {trim_conv.count_tokens()}/{trim_conv.max_context_tokens}")
    
    # Test 6: Clear history
    print("\n6️⃣  Clear History Test:")
    conv.clear_history()
    stats = conv.get_stats()
    print(f"  Messages after clear: {stats['message_count']}")
    print(f"  (Should be 1 - just system prompt)")
    
    print("\n✅ All tests complete!")
    
    # Cleanup
    import os
    if os.path.exists(test_file):
        os.remove(test_file)


def interactive_demo():
    """Interactive demo of ConversationManager."""
    print("💬 Interactive Conversation Manager Demo")
    print("Commands: /stats, /save, /load, /clear, quit")
    print("=" * 50)
    
    conv = ConversationManager(
        system_prompt="You are a helpful, friendly assistant."
    )
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("👋 Goodbye!")
            break
        
        if user_input == '/stats':
            stats = conv.get_stats()
            print("\n📊 Statistics:")
            for key, value in stats.items():
                print(f"  • {key}: {value}")
            continue
        
        if user_input.startswith('/save'):
            parts = user_input.split()
            filename = parts[1] if len(parts) > 1 else "conversation.json"
            conv.save_conversation(filename)
            continue
        
        if user_input.startswith('/load'):
            parts = user_input.split()
            filename = parts[1] if len(parts) > 1 else "conversation.json"
            try:
                conv.load_conversation(filename)
            except FileNotFoundError:
                print(f"❌ File not found: {filename}")
            continue
        
        if user_input == '/clear':
            conv.clear_history()
            print("🗑️  Conversation cleared!")
            continue
        
        if not user_input:
            continue
        
        try:
            response = conv.send_message(user_input)
            print(f"\nAssistant: {response['content']}")
            print(f"📊 {response['tokens_used']} tokens")
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        interactive_demo()
    else:
        test_conversation_manager()
