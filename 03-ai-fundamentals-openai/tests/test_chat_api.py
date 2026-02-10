"""
Tests for Chat API Exercises

Run with: pytest test_chat_api.py
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add exercises directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../exercises'))


class TestSimpleChat:
    """Tests for simple chat exercise."""
    
    @patch('exercises.03-simple-chat.client')
    def test_chat_maintains_history(self, mock_client):
        """Test that conversation history is maintained."""
        # TODO: Implement test
        pass
    
    @patch('exercises.03-simple-chat.client')
    def test_quit_command(self, mock_client):
        """Test that 'quit' exits the chat."""
        # TODO: Implement test
        pass


class TestConversationManager:
    """Tests for ConversationManager class."""
    
    def test_initialization(self):
        """Test that manager initializes correctly."""
        from exercises['04-conversation-manager'] import ConversationManager
        
        manager = ConversationManager(
            system_prompt="Test prompt",
            model="gpt-3.5-turbo"
        )
        
        assert len(manager.messages) == 1
        assert manager.messages[0]['role'] == 'system'
        assert manager.messages[0]['content'] == "Test prompt"
    
    def test_token_counting(self):
        """Test token counting functionality."""
        from exercises['04-conversation-manager'] import ConversationManager
        
        manager = ConversationManager()
        
        # Test counting specific text
        count = manager.count_tokens("Hello world")
        assert count > 0
        assert isinstance(count, int)
    
    @patch('openai.OpenAI')
    def test_send_message(self, mock_openai):
        """Test sending a message."""
        from exercises['04-conversation-manager'] import ConversationManager
        
        # Mock API response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Test response"
        mock_response.choices[0].finish_reason = "stop"
        mock_response.usage.total_tokens = 20
        mock_response.model = "gpt-3.5-turbo"
        
        mock_client = Mock()
        mock_client.chat.completions.create.return_value = mock_response
        
        with patch('exercises.04-conversation-manager.OpenAI', return_value=mock_client):
            manager = ConversationManager()
            response = manager.send_message("Test message")
            
            assert response['content'] == "Test response"
            assert response['tokens_used'] == 20
            assert len(manager.messages) == 3  # system + user + assistant
    
    def test_history_trimming(self):
        """Test that old messages are trimmed."""
        from exercises['04-conversation-manager'] import ConversationManager
        
        manager = ConversationManager(max_context_tokens=100)
        
        # Add messages until trimming occurs
        initial_count = len(manager.messages)
        
        # Simulate adding many messages
        for i in range(20):
            manager.add_message("user", f"Message {i}" * 20)
            manager.add_message("assistant", f"Response {i}" * 20)
        
        manager.trim_history()
        
        # Should have trimmed some messages
        assert manager.count_tokens() <= manager.max_context_tokens
        # Should keep system prompt
        assert manager.messages[0]['role'] == 'system'
    
    def test_save_load_conversation(self, tmp_path):
        """Test saving and loading conversations."""
        from exercises['04-conversation-manager'] import ConversationManager
        
        # Create and populate conversation
        manager1 = ConversationManager(system_prompt="Test")
        manager1.add_message("user", "Hello")
        manager1.add_message("assistant", "Hi there")
        
        # Save
        filepath = tmp_path / "test_conv.json"
        manager1.save_conversation(str(filepath))
        
        # Load into new manager
        manager2 = ConversationManager()
        manager2.load_conversation(str(filepath))
        
        # Verify loaded correctly
        assert len(manager2.messages) == len(manager1.messages)
        assert manager2.messages[-1]['content'] == "Hi there"
    
    def test_get_stats(self):
        """Test conversation statistics."""
        from exercises['04-conversation-manager'] import ConversationManager
        
        manager = ConversationManager()
        manager.add_message("user", "Test")
        manager.add_message("assistant", "Response")
        
        stats = manager.get_stats()
        
        assert 'turn_count' in stats
        assert 'total_tokens' in stats
        assert 'message_count' in stats
        assert stats['message_count'] >= 3  # system + user + assistant


class TestChatAPIIntegration:
    """Integration tests (require real API key)."""
    
    @pytest.mark.integration
    def test_real_api_call(self):
        """Test actual API call (only if API key available)."""
        if not os.getenv('OPENAI_API_KEY'):
            pytest.skip("No API key available")
        
        from openai import OpenAI
        
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'test'"}],
            max_tokens=5
        )
        
        assert response.choices[0].message.content
        assert response.usage.total_tokens > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
