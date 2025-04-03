# Week 3, Lesson 3: Python Web Development with Flask

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Logic puzzle

  Four people need to cross a bridge at night. They have only one flashlight, and the bridge can only hold two people at a time. The four people take 1, 2, 5, and 10 minutes respectively to cross the bridge. When two people cross together, they move at the speed of the slower person. What is the minimum time needed for all four people to cross the bridge?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 9 - Queries with expressions](https://sqlbolt.com/lesson/select_queries_with_expressions)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

# Break (10 minutes)

# Python Web Development with Flask (35 minutes)

## Introduction to Web Development with Python

Web development with Python typically involves creating server-side applications that handle HTTP requests, interact with databases, and generate dynamic web content.

### Popular Python Web Frameworks

- **Flask**: Lightweight, flexible, and easy to learn
- **Django**: Full-featured, batteries-included framework
- **FastAPI**: Modern, high-performance framework for building APIs
- **Pyramid**: Flexible framework that scales with your application

## Introduction to Flask

Flask is a micro web framework for Python that's simple to use yet powerful enough for production applications.

### Key Features of Flask

- Lightweight and modular design
- Built-in development server and debugger
- RESTful request dispatching
- Jinja2 templating engine
- Support for secure cookies
- WSGI compliant
- Extensive documentation and community support

## Setting Up Flask

```bash
# Install Flask
pip install flask
```

## Creating a Basic Flask Application

```python
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

## Flask Routes and Views

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About Page'

# Dynamic routes with parameters
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

# Specifying HTTP methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        return 'Processing login'
    else:
        # Show login form
        return 'Please log in'

if __name__ == '__main__':
    app.run(debug=True)
```

## Templates with Jinja2

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/hello.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>Hello Page</title>
  </head>
  <body>
    <h1>Hello, {{ name }}!</h1>

    {% if name == 'admin' %}
    <p>Welcome, administrator!</p>
    {% else %}
    <p>Welcome, user!</p>
    {% endif %}

    <ul>
      {% for i in range(5) %}
      <li>Item {{ i + 1 }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

## Handling Forms

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        # Process the form data
        return f'Form submitted! Name: {name}, Email: {email}'

    # If it's a GET request, show the form
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/form.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>Form Example</title>
  </head>
  <body>
    <h1>Submit Form</h1>
    <form method="POST">
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required />
      </div>
      <button type="submit">Submit</button>
    </form>
  </body>
</html>
```

## Working with Databases

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.id}: {self.content}>'

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    content = request.form.get('content')
    new_task = Task(content=content)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

## Exercises

For this lesson, we have exercises to practice web development with Flask:

1. `basic_flask_app.py`: Create a simple Flask application with multiple routes
2. `flask_todo_app/`: Build a more complex Flask application (a todo list app)

### Running the Exercises

1. Navigate to the exercises directory:

   ```bash
   cd week-3/lesson-3/exercises
   ```

2. Complete the code in each file by replacing the `pass` statements with your code.

3. Run the basic Flask app:

   ```bash
   python basic_flask_app.py
   ```

4. Run the todo list app:
   ```bash
   cd flask_todo_app
   python app.py
   ```

## Wrap-up (10 minutes)

- Wrap-up (10 min): Best practices for Flask development
- Discuss Flask vs. other web frameworks
- Review solutions to the exercises

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Real Python - Flask Tutorials](https://realpython.com/tutorials/flask/)
- [Flask Web Development with Python Tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA)
