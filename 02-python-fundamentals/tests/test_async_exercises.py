"""
Tests for async programming exercises.

Run with: pytest test_async_exercises.py -v
"""

import pytest
import asyncio
import time
from unittest.mock import AsyncMock, patch


class TestAsyncBasics:
    """Test basic async understanding."""
    
    @pytest.mark.asyncio
    async def test_async_function_returns_coroutine(self):
        """Test that async functions return coroutines."""
        async def simple_async():
            return "result"
        
        result = simple_async()
        assert asyncio.iscoroutine(result)
        await result  # Clean up
    
    @pytest.mark.asyncio
    async def test_concurrent_faster_than_sequential(self):
        """Test that concurrent execution is faster."""
        async def task():
            await asyncio.sleep(0.1)
            return "done"
        
        # Sequential
        start = time.time()
        for _ in range(5):
            await task()
        seq_time = time.time() - start
        
        # Concurrent
        start = time.time()
        await asyncio.gather(*[task() for _ in range(5)])
        conc_time = time.time() - start
        
        assert conc_time < seq_time
        assert conc_time < 0.2  # Should be ~0.1s not 0.5s


class TestConcurrentAPIClient:
    """Test concurrent API client (Exercise 01)."""
    
    @pytest.mark.asyncio
    async def test_semaphore_limits_concurrency(self):
        """Test that semaphore limits concurrent operations."""
        active_count = 0
        max_active = 0
        semaphore = asyncio.Semaphore(3)
        
        async def task():
            nonlocal active_count, max_active
            async with semaphore:
                active_count += 1
                max_active = max(max_active, active_count)
                await asyncio.sleep(0.1)
                active_count -= 1
        
        await asyncio.gather(*[task() for _ in range(10)])
        
        assert max_active == 3  # Should never exceed semaphore limit
    
    @pytest.mark.asyncio
    async def test_error_handling_doesnt_stop_other_tasks(self):
        """Test that one error doesn't stop other tasks."""
        async def task(should_fail: bool):
            if should_fail:
                raise ValueError("Test error")
            await asyncio.sleep(0.1)
            return "success"
        
        # Mix of successful and failing tasks
        tasks = [task(i % 2 == 0) for i in range(10)]
        
        # Use return_exceptions=True to continue on errors
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Count successes and failures
        successes = sum(1 for r in results if r == "success")
        failures = sum(1 for r in results if isinstance(r, Exception))
        
        assert successes == 5
        assert failures == 5


class TestRateLimiting:
    """Test rate limiting implementation (Exercise 02)."""
    
    @pytest.mark.asyncio
    async def test_exponential_backoff_delays(self):
        """Test that retry delays increase exponentially."""
        delays = []
        
        async def task_with_retry(max_retries=3, base_delay=0.1):
            for attempt in range(max_retries):
                delay = base_delay * (2 ** attempt)
                delays.append(delay)
                await asyncio.sleep(delay)
        
        await task_with_retry()
        
        # Check delays: 0.1, 0.2, 0.4
        assert len(delays) == 3
        assert delays[0] == 0.1
        assert delays[1] == 0.2
        assert delays[2] == 0.4
    
    @pytest.mark.asyncio
    async def test_timeout_handling(self):
        """Test that timeouts are handled correctly."""
        async def slow_task():
            await asyncio.sleep(10)  # Too slow
            return "done"
        
        with pytest.raises(asyncio.TimeoutError):
            await asyncio.wait_for(slow_task(), timeout=0.1)


class TestProgressTracking:
    """Test progress tracking."""
    
    @pytest.mark.asyncio
    async def test_progress_counter(self):
        """Test progress tracking during async operations."""
        completed = 0
        total = 10
        
        async def task():
            nonlocal completed
            await asyncio.sleep(0.1)
            completed += 1
        
        await asyncio.gather(*[task() for _ in range(total)])
        
        assert completed == total


# Helper function to run async tests
def test_async_performance_improvement():
    """Test that async provides performance improvement."""
    # This is a sync test that runs async code
    
    async def measure_sequential():
        start = time.time()
        for _ in range(5):
            await asyncio.sleep(0.1)
        return time.time() - start
    
    async def measure_concurrent():
        start = time.time()
        await asyncio.gather(*[asyncio.sleep(0.1) for _ in range(5)])
        return time.time() - start
    
    seq_time = asyncio.run(measure_sequential())
    conc_time = asyncio.run(measure_concurrent())
    
    # Concurrent should be ~5x faster
    assert seq_time > 0.4  # ~0.5s
    assert conc_time < 0.2  # ~0.1s
    assert seq_time / conc_time > 3  # At least 3x speedup
