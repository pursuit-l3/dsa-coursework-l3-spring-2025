"""
Exercise: Use SQLAlchemy ORM to interact with a database
"""
import os
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date

# Create a base class for declarative class definitions
Base = declarative_base()

class Product(Base):
    """Product model for an e-commerce system"""
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    category = Column(String)
    
    # Relationship with OrderItem
    order_items = relationship("OrderItem", back_populates="product")
    
    def __repr__(self):
        return f"<Product(name='{self.name}', price=${self.price:.2f})>"

class Customer(Base):
    """Customer model for an e-commerce system"""
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    address = Column(String)
    
    # Relationship with Order
    orders = relationship("Order", back_populates="customer")
    
    def __repr__(self):
        return f"<Customer(name='{self.name}', email='{self.email}')>"

class Order(Base):
    """Order model for an e-commerce system"""
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(Date, nullable=False)
    
    # Relationships
    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
    
    def __repr__(self):
        return f"<Order(id={self.id}, date='{self.order_date}')>"

class OrderItem(Base):
    """OrderItem model for an e-commerce system"""
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)
    
    # Relationships
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
    
    def __repr__(self):
        return f"<OrderItem(product_id={self.product_id}, quantity={self.quantity})>"

def create_database():
    """
    Create a new SQLite database with tables for an e-commerce system
    
    Returns:
        The database engine and session
    """
    # Your code here
    # 1. Create an engine that connects to a database file named 'ecommerce.db'
    # 2. Create all tables
    # 3. Create and return a session
    pass

def insert_sample_data(session):
    """
    Insert sample data into the database
    
    Args:
        session: The database session
    """
    # Your code here
    # 1. Create and add at least 3 products
    # 2. Create and add at least 2 customers
    # 3. Create and add at least 2 orders with order items
    # 4. Commit the session
    pass

def query_products(session):
    """
    Query all products and print them
    
    Args:
        session: The database session
    """
    # Your code here
    # 1. Query all products
    # 2. Print each product's information
    pass

def query_customer_orders(session, customer_id):
    """
    Query all orders for a specific customer
    
    Args:
        session: The database session
        customer_id: The ID of the customer
    """
    # Your code here
    # 1. Query the customer and their orders
    # 2. Print the customer's information
    # 3. Print each order's information, including the order items and products
    pass

def update_product(session, product_id, new_price):
    """
    Update a product's price
    
    Args:
        session: The database session
        product_id: The ID of the product to update
        new_price: The new price for the product
    """
    # Your code here
    # 1. Query the product
    # 2. Update its price
    # 3. Commit the session
    # 4. Print a confirmation message
    pass

def delete_order(session, order_id):
    """
    Delete an order and its order items
    
    Args:
        session: The database session
        order_id: The ID of the order to delete
    """
    # Your code here
    # 1. Query the order
    # 2. Delete all order items associated with the order
    # 3. Delete the order
    # 4. Commit the session
    # 5. Print a confirmation message
    pass

def main():
    """Main function to run the exercise"""
    # Remove the database file if it exists
    if os.path.exists('ecommerce.db'):
        os.remove('ecommerce.db')
    
    # Create the database and tables
    engine, session = create_database()
    
    # Insert sample data
    insert_sample_data(session)
    
    # Query and display products
    print("\nAll Products:")
    query_products(session)
    
    # Query and display customer orders
    print("\nCustomer Orders:")
    query_customer_orders(session, 1)
    
    # Update a product
    print("\nUpdating Product:")
    update_product(session, 1, 29.99)
    
    # Query products again to see the update
    print("\nProducts after update:")
    query_products(session)
    
    # Delete an order
    print("\nDeleting Order:")
    delete_order(session, 2)
    
    # Query customer orders again to see the deletion
    print("\nCustomer Orders after deletion:")
    query_customer_orders(session, 1)
    
    # Close the session
    session.close()
    print("\nDatabase session closed.")

if __name__ == "__main__":
    main() 