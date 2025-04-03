# Lesson 3: Asynchronous Python

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Logic grid puzzle

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 3 - SQL Queries with constraints](https://sqlbolt.com/lesson/select_queries_with_constraints_pt_2)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

# Break (10 minutes)

# Asynchronous Python (35 minutes)

## Introduction to Asynchronous Programming

Asynchronous programming allows code to execute without blocking the main thread, which is especially useful for I/O-bound operations like network requests or file operations.

### Why Asynchronous Programming?

- **Improved Performance**: Handle multiple operations concurrently
- **Better Resource Utilization**: Don't waste CPU cycles waiting for I/O
- **Enhanced Responsiveness**: Keep your application responsive while waiting for slow operations

### Synchronous vs. Asynchronous

**Synchronous (Blocking) Code**:

- Operations execute one after another
- Each operation must complete before the next one starts
- Simple to write and understand, but can be inefficient

**Asynchronous (Non-blocking) Code**:

- Operations can run concurrently
- Start an operation and continue with other tasks
- More complex to write, but can be much more efficient

## Asynchronous Approaches in Python

Python offers several approaches to asynchronous programming:

1. **Threading**: Multiple threads within a process
2. **Multiprocessing**: Multiple processes
3. **Asyncio**: Coroutines and event loops (Python's modern approach)

### Threading vs. Asyncio

- **Threading**: Good for I/O-bound tasks, but limited by the Global Interpreter Lock (GIL)
- **Asyncio**: Cooperative multitasking with a single thread, excellent for I/O-bound tasks

## Python's Asyncio Framework

Asyncio is Python's built-in library for writing concurrent code using the `async`/`await` syntax.

### Key Concepts

1. **Coroutines**: Functions defined with `async def` that can be paused and resumed
2. **Awaitables**: Objects that can be used with the `await` keyword
3. **Event Loop**: Manages and distributes the execution of different tasks

### Basic Asyncio Example

```python
import asyncio

async def say_hello(name, delay):
    await asyncio.sleep(delay)  # Non-blocking sleep
    print(f"Hello, {name}!")
    return f"Done greeting {name}"

async def main():
    # Run coroutines concurrently
    results = await asyncio.gather(
        say_hello("Alice", 1),
        say_hello("Bob", 2),
        say_hello("Charlie", 3)
    )
    print(results)

# Run the main coroutine
asyncio.run(main())
```

### Creating and Running Tasks

```python
import asyncio
import time

async def fetch_data(name, delay):
    print(f"Starting to fetch data for {name}...")
    await asyncio.sleep(delay)  # Simulate network delay
    print(f"Finished fetching data for {name}")
    return f"Data for {name}"

async def main():
    start_time = time.time()

    # Create and schedule tasks
    task1 = asyncio.create_task(fetch_data("resource1", 2))
    task2 = asyncio.create_task(fetch_data("resource2", 1))

    # Wait for both tasks to complete
    result1 = await task1
    result2 = await task2

    elapsed = time.time() - start_time
    print(f"Completed in {elapsed:.2f} seconds")
    print(f"Results: {result1}, {result2}")

asyncio.run(main())
```

### Error Handling in Asyncio

```python
import asyncio

async def risky_operation(name):
    await asyncio.sleep(1)
    if name == "error":
        raise ValueError(f"Error processing {name}")
    return f"Processed {name} successfully"

async def main():
    try:
        # This will raise an exception
        result = await risky_operation("error")
        print(result)
    except ValueError as e:
        print(f"Caught an error: {e}")

    # This will succeed
    result = await risky_operation("data")
    print(result)

asyncio.run(main())
```

## Exercises

For this lesson, we have exercises to practice asynchronous programming in Python using the asyncio library. The exercises are in the following files:

1. `async_basics.py`: Basic asyncio operations
2. `async_web_requests.py`: Making asynchronous web requests

### Running the Exercises

1. Navigate to the exercises directory:

   ```bash
   cd week-1/lesson-3/exercises
   ```

2. Complete the functions in each file by replacing the `pass` statements with your code.

3. Run the exercises:

   ```bash
   python async_basics.py
   python async_web_requests.py
   ```

4. Run the tests to verify your implementations:
   ```bash
   python -m unittest test_async_basics.py
   ```

## Wrap-up (10 minutes)

- Wrap-up (10 min): Common pitfalls and best practices in asynchronous Python
- Discuss when to use asyncio vs. threading vs. multiprocessing
- Review solutions to the exercises

## Additional Resources

- [Python Documentation - asyncio](https://docs.python.org/3/library/asyncio.html)
- [Real Python - Async IO in Python](https://realpython.com/async-io-python/)
- [Python Documentation - Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)
- [Asyncio for the Working Python Developer](https://yeray.dev/python/asyncio/asyncio-for-the-working-python-developer)
