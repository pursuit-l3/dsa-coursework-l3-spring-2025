"""
Exercise: Create a simple Flask application with multiple routes
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
    {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
]

@app.route('/')
def home():
    """
    Home page route
    
    Returns:
        Rendered home page template
    """
    # Your code here - render a template with a welcome message
    pass

@app.route('/about')
def about():
    """
    About page route
    
    Returns:
        Rendered about page template
    """
    # Your code here - render a template with information about the app
    pass

@app.route('/users')
def user_list():
    """
    User list page route
    
    Returns:
        Rendered user list template with all users
    """
    # Your code here - render a template with the list of users
    pass

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    """
    User detail page route
    
    Args:
        user_id: The ID of the user to display
        
    Returns:
        Rendered user detail template for the specified user
    """
    # Your code here - find the user with the given ID and render a template with their details
    # If the user doesn't exist, show an error message
    pass

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Contact form route
    
    Returns:
        If GET: Rendered contact form template
        If POST: Thank you message after form submission
    """
    # Your code here - handle both GET and POST requests
    # For GET: render a contact form
    # For POST: process the form data and show a thank you message
    pass

if __name__ == '__main__':
    app.run(debug=True) 