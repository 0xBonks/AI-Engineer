"""Solution: Cost Tracking System"""
from openai import OpenAI
import tiktoken
from typing import Dict, List

class CostTracker:
    PRICING = {
        "gpt-3.5-turbo": {"input": 0.0015, "output": 0.002},
        "gpt-4-turbo": {"input": 0.01, "output": 0.03}
    }
    
    def __init__(self):
        self.total_cost = 0.0
        self.calls: List[Dict] = []
    
    def track_call(self, prompt_tokens: int, completion_tokens: int, model: str = "gpt-3.5-turbo"):
        rates = self.PRICING.get(model, self.PRICING["gpt-3.5-turbo"])
        cost = (prompt_tokens/1000 * rates["input"]) + (completion_tokens/1000 * rates["output"])
        
        self.calls.append({
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "cost": cost,
            "model": model
        })
        self.total_cost += cost
        return cost
    
    def get_stats(self) -> Dict:
        return {
            "total_cost": self.total_cost,
            "total_calls": len(self.calls),
            "avg_cost": self.total_cost / len(self.calls) if self.calls else 0,
            "total_tokens": sum(c["prompt_tokens"] + c["completion_tokens"] for c in self.calls)
        }

# Test
tracker = CostTracker()
tracker.track_call(100, 200)
tracker.track_call(50, 100)
print(tracker.get_stats())
