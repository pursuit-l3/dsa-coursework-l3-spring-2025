# Week 4, Lesson 1: Python and Databases

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Probability problem

  Three prisoners are told that one of them will be executed and the other two will be freed. The guard knows which prisoner will be executed but won't tell. Prisoner A asks the guard to tell him privately which of the other two prisoners will be freed, arguing that this reveals no information about his own fate. The guard tells him that Prisoner B will be freed. What is Prisoner A's probability of being executed now?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 10 - Queries with aggregates](https://sqlbolt.com/lesson/select_queries_with_aggregates)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

# Break (10 minutes)

# Python and Databases (35 minutes)

## Introduction to Databases with Python

Python can interact with various database systems, from simple file-based databases to complex relational database management systems (RDBMS).

### Types of Databases

- **Relational Databases**: SQLite, MySQL, PostgreSQL
- **NoSQL Databases**: MongoDB, Redis, Cassandra
- **Object-Oriented Databases**: ZODB
- **File-based Databases**: JSON, CSV, Pickle

## SQLite with Python

SQLite is a lightweight, disk-based database that doesn't require a separate server process. It's included with Python through the `sqlite3` module.

```python
import sqlite3

# Connect to a database (creates it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER
)
''')

# Insert data
cursor.execute('''
INSERT INTO users (name, email, age) VALUES (?, ?, ?)
''', ('Alice', 'alice@example.com', 30))

# Commit changes
conn.commit()

# Query data
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
for user in users:
    print(user)

# Close the connection
conn.close()
```

## SQLAlchemy: Python SQL Toolkit and ORM

SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library that gives application developers the full power and flexibility of SQL.

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create an engine that connects to the database
engine = create_engine('sqlite:///example.db', echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a User class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer)
    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}', age={self.age})>"

# Define a Post class
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post(title='{self.title}')>"

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a user
new_user = User(name='Bob', email='bob@example.com', age=25)
session.add(new_user)
session.commit()

# Add a post for the user
new_post = Post(title='My First Post', content='Hello, world!', author=new_user)
session.add(new_post)
session.commit()

# Query data
users = session.query(User).all()
for user in users:
    print(user)
    for post in user.posts:
        print(f"  {post}")

# Close the session
session.close()
```

## MongoDB with PyMongo

MongoDB is a popular NoSQL database that stores data in flexible, JSON-like documents.

```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Get or create a database
db = client['example_db']

# Get or create a collection
users = db['users']

# Insert a document
user_data = {
    'name': 'Charlie',
    'email': 'charlie@example.com',
    'age': 35,
    'interests': ['Python', 'Databases', 'Web Development']
}
result = users.insert_one(user_data)
print(f"Inserted user with ID: {result.inserted_id}")

# Query documents
for user in users.find({'age': {'$gt': 30}}):
    print(user)

# Update a document
users.update_one(
    {'name': 'Charlie'},
    {'$set': {'age': 36}}
)

# Delete a document
users.delete_one({'name': 'Charlie'})

# Close the connection
client.close()
```

## Exercises

For this lesson, we have exercises to practice working with databases in Python:

1. `sqlite_exercise.py`: Work with SQLite directly using the sqlite3 module
2. `sqlalchemy_exercise.py`: Use SQLAlchemy ORM to interact with a database

### Running the Exercises

1. Navigate to the exercises directory:

   ```bash
   cd week-4/lesson-1/exercises
   ```

2. Complete the functions in each file by replacing the `pass` statements with your code.

3. Run the exercises:
   ```bash
   python sqlite_exercise.py
   python sqlalchemy_exercise.py
   ```

## Wrap-up (10 minutes)

- Wrap-up (10 min): Best practices for database interactions in Python
- Discuss when to use different database systems
- Review solutions to the exercises

## Additional Resources

- [Python SQLite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PyMongo Documentation](https://pymongo.readthedocs.io/)
- [Real Python - Python and SQLite](https://realpython.com/python-sqlite-sqlalchemy/)
- [MongoDB with Python](https://realpython.com/introduction-to-mongodb-and-python/)
