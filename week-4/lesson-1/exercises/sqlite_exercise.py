"""
Exercise: Work with SQLite directly using the sqlite3 module
"""
import sqlite3
import os

def create_database():
    """
    Create a new SQLite database with tables for a library management system
    
    Tables:
    - books: id, title, author, published_year, isbn
    - members: id, name, email, join_date
    - loans: id, book_id, member_id, loan_date, return_date
    
    Returns:
        The database connection and cursor
    """
    # Your code here
    # 1. Connect to a database file named 'library.db'
    # 2. Create the tables if they don't exist
    # 3. Return the connection and cursor
    pass

def insert_sample_data(conn, cursor):
    """
    Insert sample data into the database
    
    Args:
        conn: The database connection
        cursor: The database cursor
    """
    # Your code here
    # 1. Insert at least 3 books
    # 2. Insert at least 2 members
    # 3. Insert at least 2 loans
    # 4. Commit the changes
    pass

def query_books(cursor):
    """
    Query all books and print them
    
    Args:
        cursor: The database cursor
    """
    # Your code here
    # 1. Execute a query to select all books
    # 2. Fetch all results
    # 3. Print each book's information
    pass

def query_loans(cursor):
    """
    Query all loans with book and member information
    
    Args:
        cursor: The database cursor
    """
    # Your code here
    # 1. Execute a JOIN query to get loan information along with book title and member name
    # 2. Fetch all results
    # 3. Print each loan's information
    pass

def update_book(conn, cursor, book_id, new_title):
    """
    Update a book's title
    
    Args:
        conn: The database connection
        cursor: The database cursor
        book_id: The ID of the book to update
        new_title: The new title for the book
    """
    # Your code here
    # 1. Execute an UPDATE query to change the book's title
    # 2. Commit the changes
    # 3. Print a confirmation message
    pass

def delete_book(conn, cursor, book_id):
    """
    Delete a book from the database
    
    Args:
        conn: The database connection
        cursor: The database cursor
        book_id: The ID of the book to delete
    """
    # Your code here
    # 1. Execute a DELETE query to remove the book
    # 2. Commit the changes
    # 3. Print a confirmation message
    pass

def main():
    """Main function to run the exercise"""
    # Remove the database file if it exists
    if os.path.exists('library.db'):
        os.remove('library.db')
    
    # Create the database and tables
    conn, cursor = create_database()
    
    # Insert sample data
    insert_sample_data(conn, cursor)
    
    # Query and display books
    print("\nAll Books:")
    query_books(cursor)
    
    # Query and display loans
    print("\nAll Loans:")
    query_loans(cursor)
    
    # Update a book
    print("\nUpdating Book:")
    update_book(conn, cursor, 1, "Updated Book Title")
    
    # Query books again to see the update
    print("\nBooks after update:")
    query_books(cursor)
    
    # Delete a book
    print("\nDeleting Book:")
    delete_book(conn, cursor, 2)
    
    # Query books again to see the deletion
    print("\nBooks after deletion:")
    query_books(cursor)
    
    # Close the connection
    conn.close()
    print("\nDatabase connection closed.")

if __name__ == "__main__":
    main() 