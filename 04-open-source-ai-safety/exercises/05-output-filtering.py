"""
Module 04 - Exercise 05: Output Filtering
==========================================

Task: Use OpenAI Moderation API to filter harmful content.

Learning Objectives:
- Implement content moderation
- Handle moderation results
- Build safe AI applications
- Balance safety and usability

Instructions:
-------------
1. Complete the ContentModerator class
2. Implement filtering logic
3. Create user-friendly feedback
4. Test with various content types

Success Criteria:
-----------------
- Successfully moderate input and output
- Block harmful content
- Provide clear user feedback
- Log violations appropriately
"""

import os
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
from dataclasses import dataclass
from enum import Enum

load_dotenv()


class ModerationAction(Enum):
    """Actions to take on flagged content."""
    ALLOW = "allow"
    WARN = "warn"
    BLOCK = "block"


@dataclass
class ModerationResult:
    """Result of content moderation."""
    text: str
    flagged: bool
    categories: Dict[str, bool]
    category_scores: Dict[str, float]
    action: ModerationAction
    message: Optional[str] = None


@dataclass
class ViolationLog:
    """Log entry for content violations."""
    timestamp: datetime
    user_id: str
    text: str
    categories: List[str]
    action_taken: str


class ContentModerator:
    """Moderate content using OpenAI Moderation API."""
    
    # Category severity levels (higher = more severe)
    SEVERITY = {
        "violence": 5,
        "violence/graphic": 5,
        "self-harm": 5,
        "self-harm/intent": 5,
        "self-harm/instructions": 5,
        "sexual/minors": 5,
        "hate": 4,
        "hate/threatening": 5,
        "harassment": 3,
        "harassment/threatening": 4,
        "sexual": 2,
    }
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        strict_mode: bool = False
    ):
        """
        Initialize content moderator.
        
        Args:
            api_key: OpenAI API key
            strict_mode: If True, block on any flag
        """
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.strict_mode = strict_mode
        self.violation_log: List[ViolationLog] = []
    
    def moderate(self, text: str) -> ModerationResult:
        """
        Moderate content using OpenAI API.
        
        Args:
            text: Content to moderate
        
        Returns:
            ModerationResult
        
        TODO: Implement this method
        - Call client.moderations.create()
        - Extract results
        - Convert to ModerationResult
        - Handle API errors gracefully
        """
        # Your code here
        pass
    
    def determine_action(self, result: ModerationResult) -> ModerationAction:
        """
        Determine what action to take based on moderation result.
        
        Args:
            result: ModerationResult from moderate()
        
        Returns:
            ModerationAction (ALLOW, WARN, or BLOCK)
        
        TODO: Implement this method
        - If strict_mode and flagged: BLOCK
        - If not flagged: ALLOW
        - Check flagged categories
        - Use SEVERITY to determine action:
            - Severity 5: BLOCK
            - Severity 3-4: WARN or BLOCK based on score
            - Severity 1-2: WARN
        - Return appropriate action
        """
        # Your code here
        pass
    
    def get_user_message(self, result: ModerationResult) -> str:
        """
        Generate user-friendly feedback message.
        
        Args:
            result: ModerationResult
        
        Returns:
            Message to show the user
        
        TODO: Implement this method
        - If ALLOW: return empty string or positive message
        - If WARN: return gentle warning
        - If BLOCK: return clear explanation without details
        - Don't reveal specific categories (privacy/gaming)
        - Be respectful and helpful
        """
        # Your code here
        pass
    
    def log_violation(
        self,
        user_id: str,
        text: str,
        result: ModerationResult
    ) -> None:
        """
        Log a content violation.
        
        Args:
            user_id: User identifier
            text: Violating content
            result: ModerationResult
        
        TODO: Implement this method
        - Extract flagged categories
        - Create ViolationLog entry
        - Append to self.violation_log
        - Consider truncating text for privacy
        """
        # Your code here
        pass
    
    def get_violations(
        self,
        user_id: Optional[str] = None,
        limit: int = 10
    ) -> List[ViolationLog]:
        """
        Retrieve violation logs.
        
        Args:
            user_id: Filter by user (None for all)
            limit: Maximum number of logs to return
        
        Returns:
            List of ViolationLog entries
        
        TODO: Implement this method
        - Filter by user_id if provided
        - Sort by timestamp (newest first)
        - Limit results
        - Return list
        """
        # Your code here
        pass


class SafeChatbot:
    """Chatbot with input/output moderation."""
    
    def __init__(
        self,
        openai_client: OpenAI,
        moderator: ContentModerator,
        system_prompt: str = "You are a helpful assistant."
    ):
        """
        Initialize safe chatbot.
        
        Args:
            openai_client: OpenAI client
            moderator: ContentModerator instance
            system_prompt: System instructions
        """
        self.client = openai_client
        self.moderator = moderator
        self.system_prompt = system_prompt
    
    def chat(self, user_input: str, user_id: str = "default") -> Tuple[str, bool]:
        """
        Chat with moderation on input and output.
        
        Args:
            user_input: User's message
            user_id: User identifier
        
        Returns:
            Tuple of (response, was_safe)
        
        TODO: Implement this method
        - Moderate user_input
        - If blocked, return error message
        - If warned, log but continue
        - Generate AI response
        - Moderate AI output
        - If AI output blocked, return safe fallback
        - Log violations
        - Return (response, was_safe)
        """
        # Your code here
        pass


class ModerationDashboard:
    """Analytics dashboard for moderation."""
    
    def __init__(self, moderator: ContentModerator):
        self.moderator = moderator
    
    def get_statistics(self) -> Dict[str, any]:
        """
        Get moderation statistics.
        
        Returns:
            Dictionary with stats
        
        TODO: Implement this method
        - Total violations
        - Violations by category
        - Violations by user
        - Most common violations
        - Trends over time
        """
        # Your code here
        pass
    
    def print_report(self) -> None:
        """
        Print formatted moderation report.
        
        TODO: Implement this method
        - Get statistics
        - Format nicely
        - Print to console
        - Include charts/visualizations if possible
        """
        # Your code here
        pass


def test_content_moderator():
    """Test the ContentModerator class."""
    
    moderator = ContentModerator()
    
    # Test 1: Safe content
    print("Test 1: Safe content...")
    result = moderator.moderate("I love learning about AI!")
    assert result.flagged is False, "Should not flag safe content"
    print("✓ Safe content passed")
    
    # Test 2: Harmful content
    print("\nTest 2: Harmful content...")
    result = moderator.moderate("I want to hurt people")
    assert result.flagged is True, "Should flag harmful content"
    assert any(result.categories.values()), "Should flag categories"
    print("✓ Harmful content blocked")
    
    # Test 3: Action determination
    print("\nTest 3: Action determination...")
    action = moderator.determine_action(result)
    assert action in [ModerationAction.WARN, ModerationAction.BLOCK]
    print(f"✓ Action: {action.value}")
    
    # Test 4: User message
    print("\nTest 4: User message...")
    message = moderator.get_user_message(result)
    assert len(message) > 0, "Should provide feedback"
    assert "violence" not in message.lower(), "Should not reveal categories"
    print(f"✓ Message: {message}")
    
    # Test 5: Violation logging
    print("\nTest 5: Violation logging...")
    moderator.log_violation("user123", "test content", result)
    logs = moderator.get_violations()
    assert len(logs) > 0, "Should log violations"
    print("✓ Logging works")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # TODO: Complete the implementation and run tests
    # test_content_moderator()
    
    # Example usage:
    # moderator = ContentModerator(strict_mode=False)
    # result = moderator.moderate(user_input)
    # 
    # if result.action == ModerationAction.BLOCK:
    #     print("Content blocked:", moderator.get_user_message(result))
    # else:
    #     # Process normally
    #     pass
    
    # Safe chatbot:
    # from openai import OpenAI
    # client = OpenAI()
    # moderator = ContentModerator()
    # bot = SafeChatbot(client, moderator)
    # response, safe = bot.chat("Hello!")
    # print(response)
    
    print("TODO: Implement the ContentModerator class")
    print("Run test_content_moderator() when complete")
