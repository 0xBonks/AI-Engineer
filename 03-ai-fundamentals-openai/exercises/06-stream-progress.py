"""
Exercise: Stream Progress Indicators

OBJECTIVE:
Build various progress indicators for streaming responses.

REQUIREMENTS:
Create multiple progress indicator types:
1. Token counter
2. Word counter  
3. Progress bar
4. Speed indicator (tokens/second)
5. Estimated time remaining

STARTER CODE:
"""

from openai import OpenAI
from dotenv import load_dotenv
import tiktoken
import time
import sys

load_dotenv()
client = OpenAI()

class ProgressTracker:
    """
    Track streaming progress with various indicators.
    """
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model
        self.encoding = tiktoken.encoding_for_model(model)
        self.client = OpenAI()
        
        # TODO: Initialize tracking variables
        self.start_time = None
        self.token_count = 0
        self.word_count = 0
        self.char_count = 0
    
    def start(self):
        """Start tracking."""
        # TODO: Initialize start time
        pass
    
    def update(self, delta: str):
        """
        Update progress with new content.
        
        TODO: Update all counters based on delta
        """
        pass
    
    def get_speed(self) -> float:
        """
        Calculate tokens per second.
        
        Returns:
            Tokens per second
        """
        # TODO: Calculate speed
        return 0.0
    
    def get_progress_bar(self, current: int, total: int, width: int = 30) -> str:
        """
        Generate ASCII progress bar.
        
        Args:
            current: Current progress
            total: Total expected
            width: Bar width in characters
        
        Returns:
            Progress bar string
        """
        # TODO: Generate progress bar
        # Example: [████████░░░░░░] 60%
        return ""
    
    def display_inline(self):
        """
        Display progress inline (updates same line).
        
        TODO: Use \\r to overwrite line with current stats
        """
        pass

def stream_with_token_counter(message: str):
    """
    Stream with simple token counter.
    
    TODO: Implement streaming with inline token count
    Display format: "Response text here... [50 tokens]"
    """
    pass

def stream_with_speed_indicator(message: str):
    """
    Stream with speed indicator.
    
    TODO: Implement streaming with tokens/second display
    Display format: "Response... [35 tokens, 12.5 tok/s]"
    """
    pass

def stream_with_progress_bar(message: str, estimated_tokens: int = 100):
    """
    Stream with progress bar.
    
    TODO: Implement streaming with progress bar
    Display format: "[████████░░] 80% (80/100 tokens)"
    
    Args:
        message: User message
        estimated_tokens: Estimated response length for progress bar
    """
    pass

def stream_with_all_indicators(message: str):
    """
    Stream with all progress indicators.
    
    TODO: Implement comprehensive progress display:
    - Token count
    - Word count
    - Speed (tokens/sec)
    - Elapsed time
    - Display all indicators inline (same line updates)
    """
    pass

def compare_indicators():
    """
    Demo all indicator types side by side.
    
    TODO: Run same query with different indicators
    """
    test_message = "Explain how transformers work in machine learning."
    
    print("\\n1. Token Counter:")
    stream_with_token_counter(test_message)
    
    print("\\n\\n2. Speed Indicator:")
    stream_with_speed_indicator(test_message)
    
    print("\\n\\n3. Progress Bar:")
    stream_with_progress_bar(test_message, estimated_tokens=150)
    
    print("\\n\\n4. All Indicators:")
    stream_with_all_indicators(test_message)

if __name__ == "__main__":
    compare_indicators()

"""
SUCCESS CRITERIA:
- [ ] Token counter updates in real-time
- [ ] Speed indicator shows tokens/second
- [ ] Progress bar displays correctly
- [ ] All indicators update inline (no scrolling)
- [ ] Accurate calculations

BONUS CHALLENGES:
1. Add estimated time remaining (ETA)
2. Create animated spinner during streaming
3. Show cumulative cost in real-time
4. Add color coding (green=fast, yellow=slow, red=very slow)
5. Create dashboard view with multiple concurrent streams

TIPS:
- Use \\r to return to line start (overwrite)
- Use flush=True for immediate display
- Use \\033[K to clear to end of line
- ANSI codes for colors: \\033[32m (green), \\033[33m (yellow), \\033[0m (reset)
"""
