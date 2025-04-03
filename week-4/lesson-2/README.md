# Week 4, Lesson 2: Python Design Patterns

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Logic puzzle

  A man walks into a bar and asks for a glass of water. The bartender pulls out a gun and points it at the man. The man says "Thank you" and leaves. What happened?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 11 - Queries with aggregates Pt. 2](https://sqlbolt.com/lesson/select_queries_with_aggregates_pt_2)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Design HashMap](https://leetcode.com/problems/design-hashmap/)

# Break (10 minutes)

# Python Design Patterns (35 minutes)

## Introduction to Design Patterns

Design patterns are typical solutions to common problems in software design. They represent best practices evolved over time by experienced software developers.

### Categories of Design Patterns

- **Creational Patterns**: Deal with object creation mechanisms
- **Structural Patterns**: Deal with object composition
- **Behavioral Patterns**: Deal with object interaction and responsibility

## Creational Patterns

### Singleton Pattern

Ensures a class has only one instance and provides a global point of access to it.

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Put any initialization here
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True - both variables reference the same instance
```

### Factory Method Pattern

Defines an interface for creating an object, but lets subclasses decide which class to instantiate.

```python
from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creator
class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
```

## Structural Patterns

### Adapter Pattern

Allows objects with incompatible interfaces to collaborate.

```python
# Existing class with incompatible interface
class OldSystem:
    def old_operation(self, data):
        return f"Processing {data} using old system"

# Target interface
class NewSystem:
    def new_operation(self, data):
        return f"Processing {data} using new system"

# Adapter
class SystemAdapter(NewSystem):
    def __init__(self, old_system):
        self.old_system = old_system

    def new_operation(self, data):
        # Adapt the old operation to the new interface
        return self.old_system.old_operation(data)

# Usage
old_system = OldSystem()
adapter = SystemAdapter(old_system)
result = adapter.new_operation("data")
print(result)  # Processing data using old system
```

### Decorator Pattern

Attaches additional responsibilities to an object dynamically.

```python
# Component interface
class Coffee:
    def cost(self):
        return 5

    def description(self):
        return "Basic coffee"

# Decorator base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

    def description(self):
        return self.coffee.description()

# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 1

    def description(self):
        return self.coffee.description() + ", milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 0.5

    def description(self):
        return self.coffee.description() + ", sugar"

# Usage
coffee = Coffee()
coffee_with_milk = MilkDecorator(coffee)
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)

print(f"{coffee_with_milk_and_sugar.description()}: ${coffee_with_milk_and_sugar.cost()}")
# Basic coffee, milk, sugar: $6.5
```

## Behavioral Patterns

### Observer Pattern

Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

class Observer:
    def update(self, subject, *args, **kwargs):
        pass

# Concrete subject
class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify()

# Concrete observer
class TemperatureDisplay(Observer):
    def update(self, subject, *args, **kwargs):
        print(f"Temperature Display: {subject.temperature}°C")

class FanController(Observer):
    def update(self, subject, *args, **kwargs):
        if subject.temperature > 25:
            print("Fan: Turning on")
        else:
            print("Fan: Turning off")

# Usage
weather_station = WeatherStation()
display = TemperatureDisplay()
fan = FanController()

weather_station.attach(display)
weather_station.attach(fan)

weather_station.temperature = 20
# Temperature Display: 20°C
# Fan: Turning off

weather_station.temperature = 30
# Temperature Display: 30°C
# Fan: Turning on
```

### Strategy Pattern

Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

```python
from abc import ABC, abstractmethod

# Strategy interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# Concrete strategies
class QuickSort(SortStrategy):
    def sort(self, data):
        print("Sorting using quick sort")
        # Implementation of quick sort
        return sorted(data)

class MergeSort(SortStrategy):
    def sort(self, data):
        print("Sorting using merge sort")
        # Implementation of merge sort
        return sorted(data)

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Sorting using bubble sort")
        # Implementation of bubble sort
        return sorted(data)

# Context
class Sorter:
    def __init__(self, strategy=None):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def sort(self, data):
        if self._strategy is None:
            raise ValueError("Strategy not set")
        return self._strategy.sort(data)

# Usage
data = [5, 3, 1, 4, 2]
sorter = Sorter()

sorter.strategy = QuickSort()
result = sorter.sort(data)
print(result)

sorter.strategy = MergeSort()
result = sorter.sort(data)
print(result)
```

## Exercises

For this lesson, we have exercises to practice implementing design patterns in Python:

1. `creational_patterns.py`: Implement Singleton and Factory patterns
2. `structural_patterns.py`: Implement Adapter and Decorator patterns
3. `behavioral_patterns.py`: Implement Observer and Strategy patterns

### Running the Exercises

1. Navigate to the exercises directory:

   ```bash
   cd week-4/lesson-2/exercises
   ```

2. Complete the implementations in each file by replacing the `pass` statements with your code.

3. Run the exercises:
   ```bash
   python creational_patterns.py
   python structural_patterns.py
   python behavioral_patterns.py
   ```

## Wrap-up (10 minutes)

- Wrap-up (10 min): Best practices for using design patterns
- Discuss when to use different patterns
- Review solutions to the exercises

## Additional Resources

- [Python Design Patterns](https://refactoring.guru/design-patterns/python)
- [Python Patterns](https://github.com/faif/python-patterns)
- [Design Patterns in Python](https://www.toptal.com/python/python-design-patterns)
- [Real Python - Python Design Patterns](https://realpython.com/factory-method-python/)
- [Python 3 Patterns, Recipes and Idioms](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/)
