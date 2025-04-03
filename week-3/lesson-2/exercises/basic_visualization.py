"""
Exercise: Create basic plots using matplotlib
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def create_line_plot():
    """
    Create a line plot of sine and cosine functions
    
    Returns:
        None (displays the plot)
    """
    # Your code here
    # 1. Create x values from 0 to 2π
    # 2. Calculate sin(x) and cos(x)
    # 3. Create a line plot with both functions
    # 4. Add title, labels, legend, and grid
    pass

def create_bar_plot():
    """
    Create a bar plot of programming language popularity
    
    Returns:
        None (displays the plot)
    """
    # Your code here
    # 1. Define languages and their popularity scores
    # 2. Create a bar plot
    # 3. Add title, labels, and customize colors
    pass

def create_scatter_plot():
    """
    Create a scatter plot with random data
    
    Returns:
        None (displays the plot)
    """
    # Your code here
    # 1. Generate random x and y values
    # 2. Create a scatter plot with varying colors and sizes
    # 3. Add title, labels, and a colorbar
    pass

def create_histogram():
    """
    Create a histogram of normally distributed data
    
    Returns:
        None (displays the plot)
    """
    # Your code here
    # 1. Generate random data from a normal distribution
    # 2. Create a histogram
    # 3. Add title, labels, and customize appearance
    pass

def create_pie_chart():
    """
    Create a pie chart of market share data
    
    Returns:
        None (displays the plot)
    """
    # Your code here
    # 1. Define categories and their values
    # 2. Create a pie chart
    # 3. Add title, labels, and customize appearance
    pass

def create_subplots():
    """
    Create a figure with multiple subplots
    
    Returns:
        None (displays the plot)
    """
    # Your code here
    # 1. Create a 2x2 grid of subplots
    # 2. Add a different plot type to each subplot
    # 3. Add titles and labels to each subplot
    # 4. Adjust layout for better spacing
    pass

def main():
    """Main function to run the exercise"""
    print("Creating Line Plot...")
    create_line_plot()
    
    print("Creating Bar Plot...")
    create_bar_plot()
    
    print("Creating Scatter Plot...")
    create_scatter_plot()
    
    print("Creating Histogram...")
    create_histogram()
    
    print("Creating Pie Chart...")
    create_pie_chart()
    
    print("Creating Subplots...")
    create_subplots()

if __name__ == "__main__":
    main() 