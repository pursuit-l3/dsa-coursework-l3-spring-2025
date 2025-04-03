# Lesson 2: Python Collections and List Comprehensions

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Binary number pattern recognition

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 2 - Constraints (WHERE clauses)](https://sqlbolt.com/lesson/select_queries_with_constraints)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

#### Approach to the problem:

1. **Understand the problem**:

   - We need to determine if a string is a palindrome
   - A palindrome reads the same forward and backward
   - Consider only alphanumeric characters and ignore case

2. **Discuss possible approaches**:

   - Two-pointer technique (start from both ends and move inward)
   - Clean the string first, then compare with its reverse
   - Handle edge cases like empty strings or strings with only non-alphanumeric characters

3. **Implement the solution in Python**:

   ```python
   def is_palindrome(s: str) -> bool:
       # Convert to lowercase and remove non-alphanumeric characters
       s = ''.join(char.lower() for char in s if char.isalnum())

       # Empty string is considered a palindrome
       if not s:
           return True

       # Check if the string equals its reverse
       return s == s[::-1]

       # Alternative: Two-pointer approach
       """
       left, right = 0, len(s) - 1

       while left < right:
           if s[left] != s[right]:
               return False
           left += 1
           right -= 1

       return True
       """
   ```

4. **Analyze time and space complexity**:
   - Time Complexity: O(n) where n is the length of the string
   - Space Complexity: O(n) for the cleaned string

# Break (10 minutes)

# Python Collections and List Comprehensions (35 minutes)

## Python Collections Overview

Python provides several built-in collection types that are powerful and flexible:

### 1. Lists

Lists are ordered, mutable collections that can contain elements of different types.

```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]

# Accessing elements (indexing starts at 0)
first_fruit = fruits[0]  # "apple"
last_number = numbers[-1]  # 5

# Slicing
first_two_fruits = fruits[0:2]  # ["apple", "banana"]
first_three_numbers = numbers[:3]  # [1, 2, 3]
last_two_numbers = numbers[-2:]  # [4, 5]

# Modifying lists
fruits.append("orange")  # Add to the end
fruits.insert(1, "blueberry")  # Insert at index 1
fruits.remove("banana")  # Remove by value
popped_fruit = fruits.pop()  # Remove and return the last item
fruits[0] = "avocado"  # Replace an item

# List operations
combined = fruits + numbers  # Concatenation
repeated = fruits * 2  # Repetition
length = len(fruits)  # Length of the list
```

### 2. Dictionaries

Dictionaries are collections of key-value pairs, similar to maps or associative arrays in other languages.

```python
# Creating dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values
name = person["name"]  # "John"
age = person.get("age")  # 30
# Using get with a default value
country = person.get("country", "Unknown")  # "Unknown"

# Modifying dictionaries
person["email"] = "john@example.com"  # Add a new key-value pair
person["age"] = 31  # Update a value
del person["city"]  # Remove a key-value pair
email = person.pop("email")  # Remove and return a value

# Dictionary methods
keys = person.keys()  # Get all keys
values = person.values()  # Get all values
items = person.items()  # Get all key-value pairs as tuples
```

### 3. Sets

Sets are unordered collections of unique elements.

```python
# Creating sets
fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}

# Adding and removing elements
fruits_set.add("orange")
fruits_set.remove("banana")  # Raises an error if not found
fruits_set.discard("kiwi")  # No error if not found

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union = set_a | set_b  # {1, 2, 3, 4, 5, 6}
intersection = set_a & set_b  # {3, 4}
difference = set_a - set_b  # {1, 2}
symmetric_difference = set_a ^ set_b  # {1, 2, 5, 6}
```

### 4. Tuples

Tuples are ordered, immutable collections.

```python
# Creating tuples
coordinates = (10, 20)
rgb = (255, 0, 0)

# Accessing elements
x = coordinates[0]  # 10
red = rgb[0]  # 255

# Tuple operations
combined = coordinates + rgb  # (10, 20, 255, 0, 0)
repeated = coordinates * 2  # (10, 20, 10, 20)
```

## List Comprehensions

List comprehensions provide a concise way to create lists based on existing lists.

### Basic Syntax

```python
[expression for item in iterable if condition]
```

### Examples

```python
# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # [1, 4, 9, 16, 25]

# With a condition
even_squares = [x**2 for x in numbers if x % 2 == 0]  # [4, 16]

# With a more complex expression
formatted = [f"Number {x}" for x in numbers]  # ["Number 1", "Number 2", ...]

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Dictionary Comprehensions

Similar to list comprehensions, but for creating dictionaries.

```python
# Basic dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With a condition
even_squares_dict = {x: x**2 for x in numbers if x % 2 == 0}  # {2: 4, 4: 16}
```

### Set Comprehensions

Creating sets using comprehensions.

```python
# Basic set comprehension
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in numbers}  # {1, 4, 9, 16, 25}
```

## Exercises

For this lesson, we have two sets of exercises to practice working with Python collections and list comprehensions:

### Exercise 1: List Operations

In this exercise, you'll implement basic list operations using traditional Python methods.

File: `list_operations.py`

Functions to implement:

- `filter_even_numbers(numbers)`: Filter a list to include only even numbers
- `double_values(numbers)`: Create a new list with each value doubled
- `find_max_value(numbers)`: Find the maximum value in a list
- `count_occurrences(items)`: Count the occurrences of each item in a list

### Exercise 2: List Comprehensions

In this exercise, you'll implement the same operations using list comprehensions for more concise code.

File: `list_comprehensions.py`

Functions to implement:

- `squares_of_evens(numbers)`: Create a list of squares of even numbers
- `filter_strings_by_length(strings, min_length)`: Filter strings by minimum length
- `extract_first_char(strings)`: Extract the first character of each string
- `create_word_lengths_dict(words)`: Create a dictionary mapping words to their lengths

### Running the Exercises and Tests

1. Navigate to the exercises directory:

   ```bash
   cd week-1/lesson-2/exercises
   ```

2. Complete the functions in each file by replacing the `pass` statements with your code.

3. Run the exercises to see if your implementations work:

   ```bash
   python list_operations.py
   python list_comprehensions.py
   ```

4. Run the tests to verify your implementations:

   ```bash
   python -m unittest test_list_operations.py
   python -m unittest test_list_comprehensions.py
   ```

5. You should see output indicating that all tests have passed:

   ```
   ....
   ----------------------------------------------------------------------
   Ran 4 tests in 0.001s

   OK
   ```

6. If you see failures, review the error messages to understand what went wrong and fix your implementations.

## Wrap-up (10 minutes)

- Wrap-up (10 min): Review of Python collections and list comprehensions
- Discuss the advantages of list comprehensions over traditional loops
- Share solutions to the exercises

## Additional Resources

- [Python Documentation - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python Documentation - List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Real Python - Python List Comprehensions](https://realpython.com/list-comprehension-python/)
- [Real Python - Dictionaries in Python](https://realpython.com/python-dicts/)
