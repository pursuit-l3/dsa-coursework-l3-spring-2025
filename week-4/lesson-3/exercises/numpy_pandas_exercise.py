"""
Exercise: Practice with NumPy and Pandas for data manipulation
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def numpy_array_operations():
    """
    Perform basic NumPy array operations
    
    Returns:
        None (prints results to console)
    """
    # Your code here
    # 1. Create a 3x3 matrix with random values
    # 2. Create a 3x3 identity matrix
    # 3. Perform matrix multiplication between them
    # 4. Calculate the determinant of the result
    # 5. Calculate the inverse of the random matrix
    # 6. Calculate the eigenvalues and eigenvectors of the random matrix
    # 7. Print all results
    pass

def numpy_statistical_operations():
    """
    Perform statistical operations with NumPy
    
    Returns:
        None (prints results to console)
    """
    # Your code here
    # 1. Create an array of 1000 random numbers from a normal distribution
    # 2. Calculate mean, median, standard deviation
    # 3. Find the minimum and maximum values
    # 4. Calculate the 25th, 50th, and 75th percentiles
    # 5. Create a histogram of the data
    # 6. Print all results
    pass

def pandas_data_manipulation():
    """
    Perform data manipulation with Pandas
    
    Returns:
        None (prints results to console)
    """
    # Your code here
    # 1. Create a DataFrame with columns: 'Name', 'Age', 'City', 'Salary'
    # 2. Add at least 5 rows of sample data
    # 3. Calculate basic statistics for numeric columns
    # 4. Filter rows where Age > 30
    # 5. Group by City and calculate mean Salary
    # 6. Sort the DataFrame by Salary in descending order
    # 7. Add a new column 'Salary_Category' based on Salary (High, Medium, Low)
    # 8. Print all results
    pass

def pandas_data_cleaning():
    """
    Perform data cleaning with Pandas
    
    Returns:
        None (prints results to console)
    """
    # Your code here
    # 1. Create a DataFrame with some missing values
    # 2. Identify and count missing values
    # 3. Fill missing values with appropriate methods
    # 4. Remove duplicates if any
    # 5. Convert data types if needed
    # 6. Create a new column derived from existing columns
    # 7. Print all results
    pass

def pandas_data_visualization():
    """
    Visualize data with Pandas and Matplotlib
    
    Returns:
        None (displays plots)
    """
    # Your code here
    # 1. Create a DataFrame with time series data
    # 2. Create a line plot of the time series
    # 3. Create a bar plot for categorical data
    # 4. Create a scatter plot for two numerical columns
    # 5. Create a histogram for a numerical column
    # 6. Create a box plot to show distribution
    # 7. Add titles, labels, and legends to all plots
    pass

def main():
    """Main function to run the exercise"""
    print("\n=== NumPy Array Operations ===")
    numpy_array_operations()
    
    print("\n=== NumPy Statistical Operations ===")
    numpy_statistical_operations()
    
    print("\n=== Pandas Data Manipulation ===")
    pandas_data_manipulation()
    
    print("\n=== Pandas Data Cleaning ===")
    pandas_data_cleaning()
    
    print("\n=== Pandas Data Visualization ===")
    pandas_data_visualization()

if __name__ == "__main__":
    main() 