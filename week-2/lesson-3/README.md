# Week 2, Lesson 3: Python Testing and Debugging

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Logic puzzle

  A farmer needs to cross a river with a fox, a chicken, and a sack of grain. The boat is only large enough for the farmer and one item. If left alone, the fox will eat the chicken, and the chicken will eat the grain. How can the farmer get everything across safely?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 6 - Multi-table queries with JOINs](https://sqlbolt.com/lesson/select_queries_with_joins)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)

# Break (10 minutes)

# Python Testing and Debugging (35 minutes)

## Introduction to Testing

Testing is a critical part of software development that helps ensure your code works as expected and continues to work as you make changes.

### Types of Tests

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test how components work together
- **Functional Tests**: Test complete functionality from a user's perspective
- **Regression Tests**: Ensure that new changes don't break existing functionality

## Unit Testing with unittest

Python's built-in `unittest` framework provides tools for creating and running tests:

```python
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

### Test Fixtures

```python
import unittest
import os

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # This runs before each test
        self.test_file = 'test_data.txt'
        with open(self.test_file, 'w') as f:
            f.write('Test data')

    def tearDown(self):
        # This runs after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.test_file))

    def test_file_content(self):
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Test data')
```

### Test Assertions

The `unittest` module provides various assertion methods:

- `assertEqual(a, b)`: a == b
- `assertNotEqual(a, b)`: a != b
- `assertTrue(x)`: bool(x) is True
- `assertFalse(x)`: bool(x) is False
- `assertIs(a, b)`: a is b
- `assertIsNot(a, b)`: a is not b
- `assertIsNone(x)`: x is None
- `assertIsNotNone(x)`: x is not None
- `assertIn(a, b)`: a in b
- `assertNotIn(a, b)`: a not in b
- `assertRaises(exc, func, *args, **kwargs)`: func(\*args, \*\*kwargs) raises exc

## Debugging Techniques

### Using print() Statements

The simplest debugging technique is to add print statements to your code:

```python
def complex_function(x, y):
    print(f"Inputs: x={x}, y={y}")
    result = x * 2
    print(f"After first operation: {result}")
    result += y
    print(f"Final result: {result}")
    return result
```

### Using the Python Debugger (pdb)

Python's built-in debugger allows you to step through code execution:

```python
import pdb

def buggy_function():
    x = 5
    y = 0
    pdb.set_trace()  # Execution stops here and enters debugger
    z = x / y  # This will cause a ZeroDivisionError
    return z

buggy_function()
```

Common pdb commands:

- `n` (next): Execute the current line and move to the next one
- `s` (step): Step into a function call
- `c` (continue): Continue execution until the next breakpoint
- `p expression` (print): Print the value of an expression
- `q` (quit): Quit the debugger

### Using try-except Blocks

```python
def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        result = None
    except TypeError:
        print("Error: Invalid types for division")
        result = None
    else:
        print("Division successful")
    finally:
        print("Division operation completed")
    return result
```

## Exercises

For this lesson, we have exercises to practice testing and debugging in Python:

1. `buggy_functions.py`: Debug and fix functions with various issues
2. `test_string_utils.py`: Write tests for a string utility module

### Running the Exercises

1. Navigate to the exercises directory:

   ```bash
   cd week-2/lesson-3/exercises
   ```

2. Debug and fix the functions in `buggy_functions.py`.

3. Complete the test cases in `test_string_utils.py`.

4. Run the tests:
   ```bash
   python -m unittest test_string_utils.py
   ```

## Wrap-up (10 minutes)

- Wrap-up (10 min): Best practices for testing and debugging
- Discuss test-driven development (TDD)
- Review solutions to the exercises

## Additional Resources

- [Python Documentation - unittest](https://docs.python.org/3/library/unittest.html)
- [Python Documentation - pdb](https://docs.python.org/3/library/pdb.html)
- [Real Python - Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [Python Testing with pytest](https://realpython.com/pytest-python-testing/)
