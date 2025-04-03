"""
Basic asyncio exercises to practice asynchronous programming in Python
"""
import asyncio
import time

async def delay_message(message, delay_seconds):
    """
    Print a message after a specified delay.
    
    Args:
        message: The message to print
        delay_seconds: How long to wait before printing (in seconds)
    
    Returns:
        The message that was printed
    """
    # Your code here
    pass

async def process_concurrent_tasks():
    """
    Run three delay_message tasks concurrently and return their results.
    
    The tasks should be:
    1. "Task 1" with a 2-second delay
    2. "Task 2" with a 1-second delay
    3. "Task 3" with a 3-second delay
    
    Returns:
        A list of the results from all three tasks
    """
    # Your code here
    pass

async def fetch_data_with_timeout(resource_id, delay_seconds, timeout_seconds):
    """
    Simulate fetching data with a timeout.
    
    If the operation takes longer than timeout_seconds, it should be cancelled.
    
    Args:
        resource_id: ID of the resource to fetch
        delay_seconds: How long the fetch operation takes
        timeout_seconds: Maximum time to wait before timing out
    
    Returns:
        f"Data from resource {resource_id}" if successful
        f"Timed out fetching resource {resource_id}" if timed out
    """
    # Your code here
    pass

async def main():
    """
    Main function to run the exercises
    """
    print("Exercise 1: Delayed Messages")
    result = await delay_message("Hello, Async World!", 1)
    print(f"Result: {result}\n")
    
    print("Exercise 2: Concurrent Tasks")
    start_time = time.time()
    results = await process_concurrent_tasks()
    elapsed = time.time() - start_time
    print(f"Results: {results}")
    print(f"Total time: {elapsed:.2f} seconds (should be ~3 seconds)\n")
    
    print("Exercise 3: Timeouts")
    # This should succeed (delay < timeout)
    result1 = await fetch_data_with_timeout(1, 1, 2)
    print(result1)
    
    # This should time out (delay > timeout)
    result2 = await fetch_data_with_timeout(2, 3, 1)
    print(result2)

if __name__ == "__main__":
    asyncio.run(main()) 