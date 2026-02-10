"""
Cost tracking utilities for API usage monitoring.

This module provides:
- Token counting utilities (using tiktoken)
- Cost calculation for various AI models
- Session cost tracking and reporting
- Cost estimation before API calls
- Export functionality for cost reports

Example usage:
    from utils.cost_tracker import CostTracker, estimate_cost, track_cost
    
    # Estimate before calling
    cost = estimate_cost(prompt="Your prompt here", model="gpt-4")
    print(f"Estimated cost: ${cost:.4f}")
    
    # Automatic tracking with decorator
    @track_cost
    def my_ai_function():
        # Your OpenAI API calls here
        pass
    
    # Manual tracking
    tracker = CostTracker()
    tracker.track_tokens(prompt_tokens=100, completion_tokens=50, model="gpt-3.5-turbo")
    print(tracker.get_session_report())
"""

import tiktoken
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from functools import wraps
import json
import os


# Model pricing (per 1K tokens) - Updated 2026-02-10
MODEL_PRICING = {
    # GPT-4 models
    "gpt-4": {
        "prompt": 0.03,
        "completion": 0.06,
    },
    "gpt-4-32k": {
        "prompt": 0.06,
        "completion": 0.12,
    },
    "gpt-4-turbo": {
        "prompt": 0.01,
        "completion": 0.03,
    },
    "gpt-4-turbo-preview": {
        "prompt": 0.01,
        "completion": 0.03,
    },
    
    # GPT-3.5 models
    "gpt-3.5-turbo": {
        "prompt": 0.0005,
        "completion": 0.0015,
    },
    "gpt-3.5-turbo-16k": {
        "prompt": 0.003,
        "completion": 0.004,
    },
    
    # Embedding models
    "text-embedding-3-small": {
        "prompt": 0.00002,
        "completion": 0.0,
    },
    "text-embedding-3-large": {
        "prompt": 0.00013,
        "completion": 0.0,
    },
    "text-embedding-ada-002": {
        "prompt": 0.0001,
        "completion": 0.0,
    },
    
    # Legacy models
    "davinci-002": {
        "prompt": 0.002,
        "completion": 0.002,
    },
    "babbage-002": {
        "prompt": 0.0004,
        "completion": 0.0004,
    },
}


def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    """
    Count the number of tokens in a text string.
    
    Args:
        text: The text to count tokens for
        model: The model name (used to determine encoding)
    
    Returns:
        Number of tokens
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # Default to cl100k_base encoding (used by GPT-3.5 and GPT-4)
        encoding = tiktoken.get_encoding("cl100k_base")
    
    return len(encoding.encode(text))


def calculate_cost(
    prompt_tokens: int,
    completion_tokens: int,
    model: str = "gpt-3.5-turbo"
) -> float:
    """
    Calculate the cost of an API call.
    
    Args:
        prompt_tokens: Number of tokens in the prompt
        completion_tokens: Number of tokens in the completion
        model: The model name
    
    Returns:
        Cost in USD
    """
    pricing = MODEL_PRICING.get(model)
    
    if not pricing:
        # Try to find a partial match
        for model_name, model_pricing in MODEL_PRICING.items():
            if model_name in model:
                pricing = model_pricing
                break
        else:
            raise ValueError(f"Pricing not found for model: {model}")
    
    prompt_cost = (prompt_tokens / 1000) * pricing["prompt"]
    completion_cost = (completion_tokens / 1000) * pricing["completion"]
    
    return prompt_cost + completion_cost


def estimate_cost(
    prompt: str,
    model: str = "gpt-3.5-turbo",
    max_tokens: int = 1000
) -> float:
    """
    Estimate the cost of an API call before making it.
    
    Args:
        prompt: The prompt text
        model: The model name
        max_tokens: Maximum completion tokens
    
    Returns:
        Estimated cost in USD
    """
    prompt_tokens = count_tokens(prompt, model)
    return calculate_cost(prompt_tokens, max_tokens, model)


class CostTracker:
    """Track API costs across a session."""
    
    def __init__(self, session_name: Optional[str] = None):
        """
        Initialize cost tracker.
        
        Args:
            session_name: Optional name for this tracking session
        """
        self.session_name = session_name or f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.calls: List[Dict] = []
        self.start_time = datetime.now()
    
    def track_tokens(
        self,
        prompt_tokens: int,
        completion_tokens: int,
        model: str = "gpt-3.5-turbo",
        metadata: Optional[Dict] = None
    ) -> float:
        """
        Track tokens and calculate cost for a single API call.
        
        Args:
            prompt_tokens: Number of prompt tokens
            completion_tokens: Number of completion tokens
            model: Model name
            metadata: Optional metadata to store with this call
        
        Returns:
            Cost of this call in USD
        """
        cost = calculate_cost(prompt_tokens, completion_tokens, model)
        
        call_data = {
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
            "cost": cost,
            "metadata": metadata or {}
        }
        
        self.calls.append(call_data)
        
        # Check thresholds
        self._check_thresholds()
        
        return cost
    
    def track_from_response(self, response, model: Optional[str] = None, metadata: Optional[Dict] = None) -> float:
        """
        Track cost from an OpenAI API response object.
        
        Args:
            response: OpenAI API response object
            model: Model name (if not in response)
            metadata: Optional metadata
        
        Returns:
            Cost of this call in USD
        """
        usage = response.usage
        model_used = model or getattr(response, 'model', 'gpt-3.5-turbo')
        
        return self.track_tokens(
            prompt_tokens=usage.prompt_tokens,
            completion_tokens=usage.completion_tokens,
            model=model_used,
            metadata=metadata
        )
    
    def get_total_cost(self) -> float:
        """Get total cost for this session."""
        return sum(call["cost"] for call in self.calls)
    
    def get_total_tokens(self) -> int:
        """Get total tokens used in this session."""
        return sum(call["total_tokens"] for call in self.calls)
    
    def get_session_report(self) -> Dict:
        """
        Generate a comprehensive session report.
        
        Returns:
            Dictionary containing session statistics
        """
        if not self.calls:
            return {
                "session_name": self.session_name,
                "total_calls": 0,
                "total_cost": 0.0,
                "total_tokens": 0,
                "duration": str(datetime.now() - self.start_time)
            }
        
        total_cost = self.get_total_cost()
        total_tokens = self.get_total_tokens()
        
        # Group by model
        by_model = {}
        for call in self.calls:
            model = call["model"]
            if model not in by_model:
                by_model[model] = {
                    "calls": 0,
                    "cost": 0.0,
                    "tokens": 0
                }
            by_model[model]["calls"] += 1
            by_model[model]["cost"] += call["cost"]
            by_model[model]["tokens"] += call["total_tokens"]
        
        return {
            "session_name": self.session_name,
            "start_time": self.start_time.isoformat(),
            "end_time": datetime.now().isoformat(),
            "duration": str(datetime.now() - self.start_time),
            "total_calls": len(self.calls),
            "total_cost": round(total_cost, 4),
            "total_tokens": total_tokens,
            "by_model": by_model,
            "calls": self.calls
        }
    
    def export_report(self, filepath: str, format: str = "json") -> None:
        """
        Export session report to file.
        
        Args:
            filepath: Path to save report
            format: Export format ("json" or "csv")
        """
        report = self.get_session_report()
        
        if format == "json":
            with open(filepath, 'w') as f:
                json.dump(report, f, indent=2)
        
        elif format == "csv":
            import csv
            with open(filepath, 'w', newline='') as f:
                if not self.calls:
                    return
                
                fieldnames = ["timestamp", "model", "prompt_tokens", "completion_tokens", "total_tokens", "cost"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                writer.writeheader()
                for call in self.calls:
                    row = {k: call[k] for k in fieldnames}
                    writer.writerow(row)
        
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _check_thresholds(self) -> None:
        """Check if cost thresholds have been exceeded."""
        total_cost = self.get_total_cost()
        
        warning_threshold = float(os.getenv("COST_WARNING_THRESHOLD", "10.0"))
        max_threshold = float(os.getenv("COST_MAX_THRESHOLD", "50.0"))
        
        if total_cost >= max_threshold:
            raise CostLimitExceeded(
                f"Session cost (${total_cost:.2f}) has exceeded maximum threshold (${max_threshold:.2f})"
            )
        
        elif total_cost >= warning_threshold:
            print(f"Warning: Session cost (${total_cost:.2f}) has exceeded warning threshold (${warning_threshold:.2f})")
    
    def print_summary(self) -> None:
        """Print a formatted summary of the session."""
        report = self.get_session_report()
        
        print("\n" + "=" * 70)
        print(f"Session: {report['session_name']}")
        print("=" * 70)
        print(f"Total Calls: {report['total_calls']}")
        print(f"Total Cost: ${report['total_cost']:.4f}")
        print(f"Total Tokens: {report['total_tokens']:,}")
        print(f"Duration: {report['duration']}")
        
        if report['by_model']:
            print("\nBy Model:")
            for model, stats in report['by_model'].items():
                print(f"  {model}:")
                print(f"    Calls: {stats['calls']}")
                print(f"    Cost: ${stats['cost']:.4f}")
                print(f"    Tokens: {stats['tokens']:,}")
        
        print("=" * 70 + "\n")


class CostLimitExceeded(Exception):
    """Exception raised when cost limit is exceeded."""
    pass


# Global tracker instance
_global_tracker: Optional[CostTracker] = None


def get_global_tracker() -> CostTracker:
    """Get or create the global cost tracker."""
    global _global_tracker
    if _global_tracker is None:
        _global_tracker = CostTracker(session_name="global")
    return _global_tracker


def track_cost(func):
    """
    Decorator to automatically track costs for a function.
    
    The decorated function should return an OpenAI API response object.
    
    Example:
        @track_cost
        def my_completion(prompt):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracker = get_global_tracker()
        response = func(*args, **kwargs)
        
        # Try to track from response
        try:
            if hasattr(response, 'usage'):
                tracker.track_from_response(response, metadata={"function": func.__name__})
        except Exception as e:
            print(f"Warning: Could not track cost: {e}")
        
        return response
    
    return wrapper


# Convenience functions for common operations
def print_global_summary():
    """Print summary of global tracker."""
    get_global_tracker().print_summary()


def export_global_report(filepath: str, format: str = "json"):
    """Export global tracker report."""
    get_global_tracker().export_report(filepath, format)


def reset_global_tracker():
    """Reset the global tracker."""
    global _global_tracker
    _global_tracker = None
