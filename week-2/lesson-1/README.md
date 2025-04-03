# Week 2, Lesson 1: Python Classes and Object-Oriented Programming

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Logical sequence completion

  What comes next in this sequence? 1, 11, 21, 1211, 111221, ?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 4 - Filtering and sorting Query results](https://sqlbolt.com/lesson/filtering_sorting_query_results)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

# Break (10 minutes)

# Python Classes and Object-Oriented Programming (35 minutes)

## Introduction to Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code. Python is a multi-paradigm language that supports OOP principles.

**Key Features of OOP:**

- **Encapsulation**: Bundling data and methods that work on that data
- **Inheritance**: Creating new classes based on existing ones
- **Polymorphism**: Using a single interface for different data types
- **Abstraction**: Hiding complex implementation details

## Creating Classes in Python

```python
class Person:
    # Class attribute (shared by all instances)
    species = "Homo sapiens"

    # Constructor method
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance method
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    # Class method
    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous", 0)

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

# Creating instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing attributes and methods
print(person1.name)  # Alice
print(person1.greet())  # Hello, my name is Alice and I am 30 years old.
print(Person.species)  # Homo sapiens
```

## Inheritance and Polymorphism

```python
class Employee(Person):
    def __init__(self, name, age, employee_id):
        # Call the parent class constructor
        super().__init__(name, age)
        self.employee_id = employee_id

    # Override the greet method
    def greet(self):
        return f"{super().greet()} I work here with ID: {self.employee_id}."

# Create an employee
employee = Employee("Charlie", 35, "E12345")

# Use inherited and overridden methods
print(employee.name)  # Charlie
print(employee.greet())  # Hello, my name is Charlie and I am 35 years old. I work here with ID: E12345.
```

## Special Methods (Dunder Methods)

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # String representation
    def __str__(self):
        return f"{self.title} by {self.author}"

    # Representation for developers
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    # Length of the book
    def __len__(self):
        return self.pages

    # Equality comparison
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self.title == other.title and
                self.author == other.author)

# Create a book
book = Book("Python Basics", "John Smith", 350)

# Using special methods
print(str(book))  # Python Basics by John Smith
print(repr(book))  # Book('Python Basics', 'John Smith', 350)
print(len(book))  # 350
```

## Properties and Encapsulation

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    # Getter
    @property
    def celsius(self):
        return self._celsius

    # Setter
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    # Property that depends on another property
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

# Create a temperature object
temp = Temperature(25)

# Use properties
print(temp.celsius)  # 25
print(temp.fahrenheit)  # 77.0

# Set temperature using properties
temp.celsius = 30
print(temp.fahrenheit)  # 86.0
```

## Exercises

For this lesson, we have exercises to practice object-oriented programming in Python:

1. `shape_hierarchy.py`: Implement a hierarchy of shape classes
2. `bank_account.py`: Create a bank account class with proper encapsulation

### Running the Exercises

1. Navigate to the exercises directory:

   ```bash
   cd week-2/lesson-1/exercises
   ```

2. Complete the classes in each file by replacing the `pass` statements with your code.

3. Run the exercises:

   ```bash
   python shape_hierarchy.py
   python bank_account.py
   ```

4. Run the tests to verify your implementations:
   ```bash
   python -m unittest test_shape_hierarchy.py
   python -m unittest test_bank_account.py
   ```

## Wrap-up (10 minutes)

- Wrap-up (10 min): OOP best practices in Python
- Discuss when to use classes vs. functions
- Review solutions to the exercises

## Additional Resources

- [Python Documentation - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [Python Documentation - Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names)
