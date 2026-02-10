"""
Tests for Streaming Exercises

Run with: pytest test_streaming.py
"""

import pytest
from unittest.mock import Mock, patch, AsyncMock
import asyncio

class MockStreamChunk:
    """Mock stream chunk for testing."""
    def __init__(self, content: str = None, finish_reason: str = None):
        self.choices = [Mock()]
        self.choices[0].delta = Mock()
        self.choices[0].delta.content = content
        self.choices[0].finish_reason = finish_reason
        self.id = "test-id"

def create_mock_stream(content_chunks: list):
    """Create mock stream from content chunks."""
    for chunk in content_chunks:
        yield MockStreamChunk(content=chunk)
    yield MockStreamChunk(content=None, finish_reason="stop")

class TestStreamingBasics:
    """Test basic streaming functionality."""
    
    @patch('openai.OpenAI')
    def test_stream_response_building(self, mock_openai):
        """Test that streaming builds complete response."""
        # Mock stream
        chunks = ["Hello", " ", "world", "!"]
        mock_stream = create_mock_stream(chunks)
        
        # Build response
        full_content = ""
        for chunk in mock_stream:
            if chunk.choices[0].delta.content:
                full_content += chunk.choices[0].delta.content
        
        assert full_content == "Hello world!"
    
    def test_stream_chunk_structure(self):
        """Test stream chunk structure."""
        chunk = MockStreamChunk(content="test", finish_reason=None)
        
        assert chunk.choices[0].delta.content == "test"
        assert chunk.choices[0].finish_reason is None
        
        final_chunk = MockStreamChunk(content=None, finish_reason="stop")
        assert final_chunk.choices[0].delta.content is None
        assert final_chunk.choices[0].finish_reason == "stop"

class TestProgressTracking:
    """Test progress tracking functionality."""
    
    def test_token_counting_realtime(self):
        """Test real-time token counting."""
        import tiktoken
        
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        
        content = ""
        chunks = ["Hello", " ", "world"]
        token_counts = []
        
        for chunk in chunks:
            content += chunk
            token_counts.append(len(encoding.encode(content)))
        
        # Verify counts increase
        assert token_counts[0] < token_counts[1] < token_counts[2]
        assert token_counts[-1] == len(encoding.encode("Hello world"))
    
    def test_speed_calculation(self):
        """Test tokens per second calculation."""
        import time
        
        start = time.time()
        time.sleep(0.1)  # Simulate processing
        elapsed = time.time() - start
        
        tokens = 10
        speed = tokens / elapsed
        
        assert speed > 0
        assert speed < 1000  # Reasonable upper bound

class TestStreamingPatterns:
    """Test advanced streaming patterns."""
    
    @pytest.mark.asyncio
    async def test_async_streaming(self):
        """Test async streaming."""
        async def mock_async_stream():
            chunks = ["a", "b", "c"]
            for chunk in chunks:
                yield MockStreamChunk(content=chunk)
        
        content = ""
        async for chunk in mock_async_stream():
            if chunk.choices[0].delta.content:
                content += chunk.choices[0].delta.content
        
        assert content == "abc"
    
    def test_stream_cancellation(self):
        """Test stream cancellation."""
        class CancellableStream:
            def __init__(self):
                self.cancelled = False
            
            def cancel(self):
                self.cancelled = True
            
            def stream(self):
                for i in range(10):
                    if self.cancelled:
                        return f"Cancelled at {i}"
                return "Completed"
        
        stream = CancellableStream()
        stream.cancel()
        result = stream.stream()
        
        assert "Cancelled" in result
    
    def test_buffered_streaming(self):
        """Test buffered streaming."""
        chunks = ["a", "b", "c", "d", "e"]
        buffer_size = 2
        
        buffer = ""
        output_chunks = []
        
        for chunk in chunks:
            buffer += chunk
            if len(buffer) >= buffer_size:
                output_chunks.append(buffer)
                buffer = ""
        
        if buffer:  # Flush remaining
            output_chunks.append(buffer)
        
        assert len(output_chunks) == 3  # "ab", "cd", "e"
        assert "".join(output_chunks) == "abcde"

class TestProgressIndicators:
    """Test progress indicator implementations."""
    
    def test_progress_bar_generation(self):
        """Test ASCII progress bar generation."""
        def get_progress_bar(current: int, total: int, width: int = 10) -> str:
            if total == 0:
                return "[" + "░" * width + "] 0%"
            percent = current / total
            filled = int(width * percent)
            bar = "█" * filled + "░" * (width - filled)
            return f"[{bar}] {int(percent * 100)}%"
        
        assert "[░░░░░░░░░░] 0%" in get_progress_bar(0, 100)
        assert "[█████░░░░░] 50%" in get_progress_bar(50, 100)
        assert "[██████████] 100%" in get_progress_bar(100, 100)
    
    def test_typing_indicator(self):
        """Test typing indicator frames."""
        frames = ["⠋", "⠙", "⠹", "⠸"]
        
        # Verify frames cycle
        for i in range(10):
            frame = frames[i % len(frames)]
            assert frame in frames

class TestStreamingIntegration:
    """Integration tests (require real API)."""
    
    @pytest.mark.integration
    @pytest.mark.skipif(
        not os.getenv('OPENAI_API_KEY'),
        reason="No API key available"
    )
    def test_real_streaming(self):
        """Test actual streaming API call."""
        from openai import OpenAI
        import os
        
        client = OpenAI()
        
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'test'"}],
            stream=True,
            max_tokens=5
        )
        
        content = ""
        chunk_count = 0
        
        for chunk in stream:
            chunk_count += 1
            delta = chunk.choices[0].delta.content
            if delta:
                content += delta
        
        assert len(content) > 0
        assert chunk_count > 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
