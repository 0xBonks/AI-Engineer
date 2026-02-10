"""
Solution: Stream Progress Indicators

Complete implementations of various progress indicator types.
"""

from openai import OpenAI
from dotenv import load_dotenv
import tiktoken
import time
import sys

load_dotenv()
client = OpenAI()

class ProgressTracker:
    """Track streaming progress with multiple indicators."""
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model
        self.encoding = tiktoken.encoding_for_model(model)
        self.client = OpenAI()
        self.reset()
    
    def reset(self):
        """Reset all counters."""
        self.start_time = None
        self.token_count = 0
        self.word_count = 0
        self.char_count = 0
        self.content = ""
    
    def start(self):
        """Start tracking."""
        self.start_time = time.time()
    
    def update(self, delta: str):
        """Update progress with new content."""
        if delta:
            self.content += delta
            self.char_count += len(delta)
            self.word_count += len(delta.split())
            self.token_count = len(self.encoding.encode(self.content))
    
    def get_speed(self) -> float:
        """Calculate tokens per second."""
        if not self.start_time:
            return 0.0
        elapsed = time.time() - self.start_time
        return self.token_count / elapsed if elapsed > 0 else 0.0
    
    def get_progress_bar(self, current: int, total: int, width: int = 30) -> str:
        """Generate ASCII progress bar."""
        if total == 0:
            return "[" + "░" * width + "] 0%"
        
        percent = current / total
        filled = int(width * percent)
        bar = "█" * filled + "░" * (width - filled)
        return f"[{bar}] {int(percent * 100)}%"
    
    def display_inline(self):
        """Display progress inline (same line)."""
        speed = self.get_speed()
        elapsed = time.time() - self.start_time if self.start_time else 0
        
        stats = (
            f"\r📊 {self.token_count}t | "
            f"{self.word_count}w | "
            f"{speed:.1f} tok/s | "
            f"{elapsed:.1f}s"
        )
        
        sys.stdout.write(stats)
        sys.stdout.flush()

def stream_with_token_counter(message: str):
    """Stream with simple token counter."""
    tracker = ProgressTracker()
    tracker.start()
    
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        stream=True
    )
    
    print("Response: ", end='', flush=True)
    
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            tracker.update(delta)
            print(delta, end='', flush=True)
    
    print(f"\n[{tracker.token_count} tokens]")

def stream_with_speed_indicator(message: str):
    """Stream with speed indicator."""
    tracker = ProgressTracker()
    tracker.start()
    
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        stream=True
    )
    
    print("Response: ", end='', flush=True)
    
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            tracker.update(delta)
            print(delta, end='', flush=True)
    
    speed = tracker.get_speed()
    print(f"\n[{tracker.token_count} tokens, {speed:.1f} tok/s]")

def stream_with_progress_bar(message: str, estimated_tokens: int = 100):
    """Stream with progress bar."""
    tracker = ProgressTracker()
    tracker.start()
    
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        stream=True
    )
    
    print("Response: ", end='', flush=True)
    content_lines = []
    
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            tracker.update(delta)
            content_lines.append(delta)
            
            # Update progress bar
            bar = tracker.get_progress_bar(tracker.token_count, estimated_tokens)
            sys.stdout.write(f"\r{bar} ({tracker.token_count}/{estimated_tokens})")
            sys.stdout.flush()
    
    print("\n\nResponse:", "".join(content_lines))

def stream_with_all_indicators(message: str):
    """Stream with comprehensive progress display."""
    tracker = ProgressTracker()
    tracker.start()
    
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}],
        stream=True
    )
    
    print("Streaming...\n")
    
    # Display content on first line, stats on second
    content_displayed = 0
    
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            tracker.update(delta)
            
            # Display new content
            sys.stdout.write(delta)
            sys.stdout.flush()
            content_displayed += len(delta)
            
            # Update stats line
            if content_displayed % 20 == 0:  # Update every ~20 chars
                elapsed = time.time() - tracker.start_time
                speed = tracker.get_speed()
                
                # Move to stats line
                sys.stdout.write(f"\n📊 {tracker.token_count}t | {tracker.word_count}w | {speed:.1f}tok/s | {elapsed:.1f}s")
                # Move back to content line
                sys.stdout.write("\033[F")  # Move cursor up one line
                sys.stdout.flush()
    
    # Final stats
    elapsed = time.time() - tracker.start_time
    speed = tracker.get_speed()
    print(f"\n\n✅ Final: {tracker.token_count} tokens, {tracker.word_count} words, {speed:.1f} tok/s, {elapsed:.1f}s")

def compare_indicators():
    """Demo all indicator types."""
    test_message = "Explain how transformers work in machine learning in 2-3 sentences."
    
    print("\n" + "="*60)
    print("1. TOKEN COUNTER")
    print("="*60)
    stream_with_token_counter(test_message)
    
    time.sleep(1)
    
    print("\n" + "="*60)
    print("2. SPEED INDICATOR")
    print("="*60)
    stream_with_speed_indicator(test_message)
    
    time.sleep(1)
    
    print("\n" + "="*60)
    print("3. PROGRESS BAR")
    print("="*60)
    stream_with_progress_bar(test_message, estimated_tokens=150)
    
    time.sleep(1)
    
    print("\n" + "="*60)
    print("4. ALL INDICATORS")
    print("="*60)
    stream_with_all_indicators(test_message)

if __name__ == "__main__":
    compare_indicators()
