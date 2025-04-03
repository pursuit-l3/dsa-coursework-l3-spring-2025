"""
Exercise for making asynchronous web requests in Python
"""
import asyncio
import time

# You'll need to install aiohttp: pip install aiohttp
import aiohttp

async def fetch_url(session, url):
    """
    Fetch the content of a URL asynchronously.
    
    Args:
        session: aiohttp ClientSession
        url: URL to fetch
    
    Returns:
        Tuple of (url, status_code, content_length)
    """
    # Your code here
    pass

async def fetch_multiple_urls(urls):
    """
    Fetch multiple URLs concurrently and return their results.
    
    Args:
        urls: List of URLs to fetch
    
    Returns:
        List of results from fetch_url
    """
    # Your code here
    pass

async def fetch_with_progress(urls):
    """
    Fetch multiple URLs and print progress as each completes.
    
    Args:
        urls: List of URLs to fetch
    
    Returns:
        List of results from fetch_url, in the order they complete
    """
    # Your code here
    pass

async def main():
    """
    Main function to run the exercises
    """
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.wikipedia.org"
    ]
    
    print("Exercise 1: Fetching a single URL")
    async with aiohttp.ClientSession() as session:
        result = await fetch_url(session, urls[0])
        print(f"Result: {result}\n")
    
    print("Exercise 2: Fetching multiple URLs concurrently")
    start_time = time.time()
    results = await fetch_multiple_urls(urls)
    elapsed = time.time() - start_time
    
    for result in results:
        print(f"URL: {result[0]}, Status: {result[1]}, Size: {result[2]} bytes")
    print(f"Total time: {elapsed:.2f} seconds\n")
    
    print("Exercise 3: Fetching with progress updates")
    start_time = time.time()
    results = await fetch_with_progress(urls)
    elapsed = time.time() - start_time
    print(f"All URLs fetched in {elapsed:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main()) 