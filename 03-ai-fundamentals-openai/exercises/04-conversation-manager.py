"""
Exercise: Conversation Manager with Context Window Management

OBJECTIVE:
Build a robust ConversationManager class that handles:
- Message history
- Token counting
- Automatic context window trimming
- Conversation persistence

REQUIREMENTS:
Implement all TODO sections in the class below.
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
    Manages multi-turn conversations with OpenAI Chat API.
    
    Features:
    - Maintains conversation history
    - Tracks token usage
    - Automatically trims old messages when approaching context limit
    - Can save/load conversations
    """
    
    def __init__(
        self,
        system_prompt: str = "You are a helpful assistant.",
        model: str = "gpt-3.5-turbo",
        max_context_tokens: int = 3000,
        temperature: float = 1.0
    ):
        """
        Initialize conversation manager.
        
        Args:
            system_prompt: Initial system message
            model: OpenAI model to use
            max_context_tokens: Max tokens to keep in context
            temperature: Response randomness (0-2)
        """
        self.model = model
        self.max_context_tokens = max_context_tokens
        self.temperature = temperature
        self.client = OpenAI()
        
        # TODO: Initialize encoding for token counting
        self.encoding = None  # Use tiktoken.encoding_for_model()
        
        # TODO: Initialize messages list with system prompt
        self.messages: List[Dict[str, str]] = []
        
        # TODO: Track total tokens used across conversation
        self.total_tokens_used = 0
    
    def count_tokens(self, text: str = None) -> int:
        """
        Count tokens in text or entire conversation.
        
        Args:
            text: Optional text to count. If None, counts all messages.
        
        Returns:
            Token count
        """
        # TODO: Implement token counting
        # If text provided, count tokens in text
        # If no text, count tokens in all messages
        return 0
    
    def trim_history(self) -> int:
        """
        Remove old messages if approaching token limit.
        Always keep system prompt (index 0).
        
        Returns:
            Number of messages removed
        """
        # TODO: Implement history trimming
        # 1. Count current tokens
        # 2. While over limit and more than 2 messages:
        #    - Remove oldest user/assistant pair (indices 1-2)
        # 3. Return count of removed messages
        removed = 0
        return removed
    
    def add_message(self, role: str, content: str):
        """Add a message to conversation history."""
        # TODO: Append message dict to self.messages
        pass
    
    def send_message(self, user_message: str) -> Dict:
        """
        Send a message and get response.
        
        Args:
            user_message: User's message
        
        Returns:
            Dict with response and metadata:
            {
                'content': str,
                'tokens_used': int,
                'finish_reason': str,
                'model': str
            }
        """
        # TODO: Implement message sending
        # 1. Add user message to history
        # 2. Trim history if needed
        # 3. Make API call
        # 4. Extract response
        # 5. Add assistant response to history
        # 6. Update total_tokens_used
        # 7. Return response dict
        
        try:
            # TODO: Make API call
            response = None
            
            # TODO: Extract and return response info
            return {
                'content': "",
                'tokens_used': 0,
                'finish_reason': "",
                'model': self.model
            }
        except Exception as e:
            raise Exception(f"API call failed: {e}")
    
    def get_history(self) -> List[Dict[str, str]]:
        """Return full conversation history."""
        return self.messages
    
    def clear_history(self):
        """Clear conversation history (keep system prompt)."""
        # TODO: Reset messages to just system prompt
        pass
    
    def save_conversation(self, filepath: str):
        """
        Save conversation to JSON file.
        
        Args:
            filepath: Path to save file
        """
        # TODO: Implement saving
        # Save messages and metadata to JSON
        data = {
            'model': self.model,
            'total_tokens': self.total_tokens_used,
            'messages': self.messages
        }
        pass
    
    def load_conversation(self, filepath: str):
        """
        Load conversation from JSON file.
        
        Args:
            filepath: Path to JSON file
        """
        # TODO: Implement loading
        # Load messages and metadata from JSON
        pass
    
    def get_stats(self) -> Dict:
        """
        Get conversation statistics.
        
        Returns:
            Dict with stats: turn_count, total_tokens, message_count
        """
        # TODO: Calculate and return stats
        return {
            'turn_count': 0,
            'total_tokens': self.total_tokens_used,
            'message_count': len(self.messages),
            'current_context_tokens': self.count_tokens()
        }


def test_conversation_manager():
    """Test the ConversationManager implementation."""
    print("Testing ConversationManager...")
    print("=" * 50)
    
    # Test 1: Basic conversation
    print("\n1. Basic Conversation:")
    conv = ConversationManager(
        system_prompt="You are a helpful math tutor.",
        max_context_tokens=500  # Small for testing
    )
    
    response = conv.send_message("What is 2+2?")
    print(f"Response: {response['content']}")
    print(f"Tokens: {response['tokens_used']}")
    
    # Test 2: Context memory
    print("\n2. Testing Context Memory:")
    response = conv.send_message("What was my first question?")
    print(f"Response: {response['content']}")
    
    # Test 3: Statistics
    print("\n3. Conversation Stats:")
    stats = conv.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Test 4: Save/Load
    print("\n4. Save/Load Test:")
    conv.save_conversation("test_conversation.json")
    print("  Saved conversation")
    
    new_conv = ConversationManager()
    new_conv.load_conversation("test_conversation.json")
    print(f"  Loaded {len(new_conv.messages)} messages")
    
    # Test 5: Context trimming
    print("\n5. Context Trimming Test:")
    for i in range(10):
        conv.send_message(f"Tell me about number {i}")
    print(f"  After 10 messages: {len(conv.messages)} messages kept")
    print(f"  Current tokens: {conv.count_tokens()}")
    
    print("\n✅ All tests complete!")


if __name__ == "__main__":
    test_conversation_manager()

"""
SUCCESS CRITERIA:
- [ ] All TODO sections implemented
- [ ] Token counting works correctly
- [ ] History trimming prevents context overflow
- [ ] Conversation can be saved and loaded
- [ ] Statistics accurately reflect conversation state
- [ ] All test cases pass

BONUS CHALLENGES:
1. Add method to get conversation summary (use GPT to summarize)
2. Implement conversation branching (save state, try different paths)
3. Add support for multiple conversations (session management)
4. Implement token budget warnings (alert when approaching limit)
5. Add method to export conversation as markdown
"""
