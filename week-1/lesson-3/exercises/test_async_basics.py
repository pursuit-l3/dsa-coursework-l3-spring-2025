"""
Tests for the async_basics module
"""
import asyncio
import unittest
from async_basics import delay_message, process_concurrent_tasks, fetch_data_with_timeout

class TestAsyncBasics(unittest.TestCase):
    """Test cases for the async_basics module"""
    
    def test_delay_message(self):
        """Test the delay_message function"""
        message = "Test Message"
        start_time = asyncio.run(self.measure_execution_time(delay_message, message, 0.5))
        self.assertGreaterEqual(start_time, 0.5)
        
    async def measure_execution_time(self, coro, *args):
        """Helper to measure execution time of a coroutine"""
        import time
        start = time.time()
        result = await coro(*args)
        elapsed = time.time() - start
        self.assertEqual(result, args[0])  # Check return value
        return elapsed
    
    def test_process_concurrent_tasks(self):
        """Test the process_concurrent_tasks function"""
        start_time = time.time()
        results = asyncio.run(process_concurrent_tasks())
        elapsed = time.time() - start_time
        
        # Check that it took around 3 seconds (the longest task)
        self.assertGreaterEqual(elapsed, 2.9)
        self.assertLessEqual(elapsed, 3.5)
        
        # Check that we got all three results
        self.assertEqual(len(results), 3)
        self.assertIn("Task 1", results)
        self.assertIn("Task 2", results)
        self.assertIn("Task 3", results)
    
    def test_fetch_data_with_timeout_success(self):
        """Test fetch_data_with_timeout when it succeeds"""
        result = asyncio.run(fetch_data_with_timeout(1, 0.5, 1))
        self.assertEqual(result, "Data from resource 1")
    
    def test_fetch_data_with_timeout_failure(self):
        """Test fetch_data_with_timeout when it times out"""
        result = asyncio.run(fetch_data_with_timeout(2, 1, 0.5))
        self.assertEqual(result, "Timed out fetching resource 2")

if __name__ == "__main__":
    unittest.main() 