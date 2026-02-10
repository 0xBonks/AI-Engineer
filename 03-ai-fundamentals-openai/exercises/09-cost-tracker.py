"""Exercise: Build Cost Tracking System"""
from openai import OpenAI
import tiktoken

class CostTracker:
    def __init__(self):
        self.total_cost = 0
        self.calls = []
    
    def track_call(self, prompt_tokens, completion_tokens, model="gpt-3.5-turbo"):
        """Track an API call and calculate cost."""
        # TODO: Implement cost calculation and tracking
        pass
    
    def get_stats(self):
        """Get usage statistics."""
        # TODO: Return total cost, calls, average cost
        pass

# TODO: Implement and test
