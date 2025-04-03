# Week 2, Lesson 2: Python Modules and Packages

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Probability problem

  Three people check their hats at a restaurant. The attendant mixes up the hats and returns them randomly. What is the probability that none of the three people get their own hat back?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 5 - SQL Review: Simple SELECT Queries](https://sqlbolt.com/lesson/select_queries_review)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

# Break (10 minutes)

# Python Modules and Packages (35 minutes)

## Introduction to Modules and Packages

In Python, modules and packages are essential for organizing and reusing code:

- **Module**: A Python file containing code (functions, classes, variables)
- **Package**: A directory containing multiple modules and a special `__init__.py` file

## Creating and Using Modules

```python
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

PI = 3.14159
```

```python
# Using the module
import math_operations

result = math_operations.add(5, 3)
print(result)  # 8

# Import specific functions
from math_operations import multiply, PI

product = multiply(4, 7)
print(product)  # 28
print(PI)  # 3.14159

# Import with alias
import math_operations as math_ops

result = math_ops.subtract(10, 4)
print(result)  # 6
```

## Creating Packages

A package is a directory with an `__init__.py` file and one or more module files:

```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

The `__init__.py` file can be empty or can contain initialization code:

```python
# my_package/__init__.py
print("Initializing my_package")

# Import commonly used functions to make them available directly from the package
from .module1 import function1, function2
from .module2 import Class1
```

## Importing from Packages

```python
# Import the package
import my_package

# Import a specific module from the package
from my_package import module1

# Import a specific function from a module in the package
from my_package.module1 import function1

# Import from a subpackage
from my_package.subpackage import module3
```

## Standard Library Modules

Python comes with a rich standard library:

```python
# Working with file paths
import os.path

file_exists = os.path.exists("data.txt")
file_size = os.path.getsize("data.txt")
base_name = os.path.basename("/path/to/file.txt")  # "file.txt"

# Working with dates and times
import datetime

now = datetime.datetime.now()
today = datetime.date.today()
one_week = datetime.timedelta(days=7)
next_week = today + one_week

# Random numbers
import random

random_number = random.randint(1, 100)
random_choice = random.choice(["apple", "banana", "cherry"])
random.shuffle(my_list)  # Shuffle in place

# JSON handling
import json

data = {"name": "John", "age": 30}
json_string = json.dumps(data)
parsed_data = json.loads(json_string)
```

## Virtual Environments and Package Management

### Creating a Virtual Environment

```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate

# Deactivate when done
deactivate
```

### Managing Packages with pip

```bash
# Install a package
pip install requests

# Install a specific version
pip install requests==2.25.1

# Install from requirements file
pip install -r requirements.txt

# List installed packages
pip list

# Generate requirements file
pip freeze > requirements.txt
```

## Exercises

For this lesson, we have exercises to practice working with modules and packages:

1. `calculator_module.py`: Create a calculator module with various functions
2. `geometry_package/`: Create a package for geometric calculations

### Running the Exercises

1. Navigate to the exercises directory:

   ```bash
   cd week-2/lesson-2/exercises
   ```

2. Complete the module and package files by replacing the `pass` statements with your code.

3. Run the test script:
   ```bash
   python test_calculator.py
   python test_geometry.py
   ```

## Wrap-up (10 minutes)

- Wrap-up (10 min): Best practices for organizing code with modules and packages
- Discuss when to create modules vs. packages
- Review solutions to the exercises

## Additional Resources

- [Python Documentation - Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Documentation - The import system](https://docs.python.org/3/reference/import.html)
- [Real Python - Python Modules and Packages](https://realpython.com/python-modules-packages/)
- [Python Package Index (PyPI)](https://pypi.org/)
