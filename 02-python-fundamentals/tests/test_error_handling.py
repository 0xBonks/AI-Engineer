"""Tests for error handling exercises."""
import pytest
import asyncio
import logging

def test_exception_handling():
    """Test basic exception handling."""
    def risky_operation(should_fail: bool):
        if should_fail:
            raise ValueError("Test error")
        return "success"
    
    # Should not raise
    try:
        result = risky_operation(False)
        assert result == "success"
    except ValueError:
        pytest.fail("Should not raise")
    
    # Should raise
    with pytest.raises(ValueError):
        risky_operation(True)

@pytest.mark.asyncio
async def test_retry_logic():
    """Test retry with exponential backoff."""
    attempts = []
    
    async def flaky_func():
        attempts.append(1)
        if len(attempts) < 3:
            raise Exception("Retry me")
        return "success"
    
    # Should succeed after 3 attempts
    result = await retry_with_backoff(flaky_func, max_retries=3)
    assert result == "success"
    assert len(attempts) == 3

async def retry_with_backoff(func, max_retries=3):
    """Helper for testing."""
    for attempt in range(max_retries):
        try:
            return await func()
        except Exception:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(0.1)
