# Lesson 1: Python Fundamentals

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Tower of Hanoi puzzle with 3 disks

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 1 - SELECT basics](https://sqlbolt.com/lesson/select_queries_introduction)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 minutes): [Two Sum](https://leetcode.com/problems/two-sum/)

#### Discuss Approach to the problem by going through interview process:

- Discuss the problem statement: Put the problem into your own words.
- Identify the input and output: What are the inputs? What do you need to return?
- Discuss the constraints: What are the limits on the input? Are there any edge cases?
- Check assumptions: Are there any assumptions you are making about the input?
- Discuss examples: Walk through a few examples to clarify the problem.
  - Example 1: Input: nums = [2,7,11,15], target = 9; Output: [0,1]
  - Example 2: Input: nums = [3,2,4], target = 6; Output: [1,2]
  - Example 3: Input: nums = [3,3], target = 6; Output: [0,1]
- Discuss edge cases: What if the input array is empty? What if there are no two numbers that add up to the target?
- Discuss the approach: What is your plan to solve the problem?
  - Brute Force:
    - What does brute force mean?
    - What would the brute force solution look like?
      - Using a nested loop to check each pair of numbers
      - Time complexity: O(n²)
      - Space complexity: O(1)
  - Optimized Approach:
    - What is the optimized approach?
    - Using a dictionary to store the difference between the target and each number
      - Time complexity: O(n)
      - Space complexity: O(n)
- Pseudo code your response to the prompt
  - Tips for Pseudo code:
    - Use clear variable names
    - Keep it simple and readable
    - Indent when appropriate
    - Code a complete solution, not just a snippet
- Code your solution.
- Walk through your code with an example.
- Discuss time and space complexity of your solution.

# Break (10 minutes)

# Getting Started (20 minutes)

### Step 1: Fork the Repository

To ensure your contributions are tracked on your GitHub profile (those valuable green squares!), you need to fork this repository properly:

1. Click the "Fork" button at the top right of this repository page
2. Select your personal GitHub account as the destination
3. Wait for the forking process to complete
4. Clone YOUR forked repository to your local machine:

```bash
git clone https://github.com/YOUR-USERNAME/dsa-coursework-l3-spring-2025.git
cd dsa-coursework-l3-spring-2025
```

5. Set up the original repository as a remote to fetch updates:

```bash
git remote add upstream https://github.com/joinpursuit/dsa-coursework-l3-spring-2025.git
```

### Step 2: Install Dependencies

To set up Python for this training, follow these steps:

1. Ensure you have Python installed on your machine. You can download it from the official Python website: https://www.python.org/downloads/

2. Verify the installation by running the following command in your terminal:

```bash
python --version
```

### Python Fundamentals (35 minutes)

#### Variable Types in Python

Python is a dynamically-typed language, which means variable types are determined at runtime. Let's explore the different variable types in Python:

##### Basic Data Types

1. **Integers**: Whole numbers without a decimal point

   ```python
   age = 25
   count = -10
   ```

2. **Floating-point numbers**: Numbers with a decimal point

   ```python
   price = 19.99
   pi = 3.14159
   ```

3. **Strings**: Sequences of characters

   ```python
   name = "Alice"
   message = 'Hello, Python!'
   multiline = """This is a
   multiline string"""
   ```

4. **Booleans**: True or False values

   ```python
   is_active = True
   has_permission = False
   ```

5. **None**: Represents the absence of a value
   ```python
   result = None
   ```

## Exercises

### Hello World Exercise

In this exercise, you'll run a simple "Hello World" program and learn how to execute Python code.

#### Running the Hello World Program

1. Navigate to the exercises directory:

   ```bash
   cd week-1/lesson-1/exercises
   ```

2. Run the hello_world.py script:

   ```bash
   python hello_world.py
   ```

   You should see the output:

   ```
   Hello, World!
   ```

3. Try modifying the script to greet yourself by changing the `main()` function:

   ```python
   def main():
       print(say_hello("Your Name"))
   ```

4. Run the modified script to see your personalized greeting.

#### Running the Tests

The exercise includes unit tests to verify the functionality of the `say_hello()` function.

1. Run the tests using the unittest module:

   ```bash
   python -m unittest test_hello_world.py
   ```

2. You should see output indicating that all tests have passed:

   ```
   ...
   ----------------------------------------------------------------------
   Ran 3 tests in 0.001s

   OK
   ```

3. Try adding your own test case to test_hello_world.py:

   ```python
   def test_your_custom_test(self):
       """Add your own test description here"""
       self.assertEqual(say_hello("Python Learner"), "Hello, Python Learner!")
   ```

4. Run the tests again to verify your new test passes.

## Wrap-up (10 minutes)

- Wrap-up (10 min): Solution review and implementation alternatives

## Additional Resources

- [Python Documentation - Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Documentation - Variables and Names](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
- [Real Python - Variables in Python](https://realpython.com/python-variables/)

---
