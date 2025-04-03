"""
Exercise: Debug and fix the following functions
"""

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers
    
    Args:
        numbers: A list of numbers
        
    Returns:
        The average of the numbers
    """
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
    
    # Bug: This will cause a ZeroDivisionError if numbers is empty
    return total / count

def find_largest_element(matrix):
    """
    Find the largest element in a 2D matrix
    
    Args:
        matrix: A list of lists representing a 2D matrix
        
    Returns:
        The largest element in the matrix
    """
    largest = matrix[0][0]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Bug: Using > instead of < will not find the largest element
            if matrix[i][j] > largest:
                largest = matrix[i][j]
    
    return largest

def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries
    
    Args:
        dict1: First dictionary
        dict2: Second dictionary
        
    Returns:
        A new dictionary containing all key-value pairs from both dictionaries
    """
    result = dict1
    
    # Bug: This modifies dict1 instead of creating a new dictionary
    for key, value in dict2.items():
        result[key] = value
    
    return result

def filter_even_numbers(numbers):
    """
    Filter a list to include only even numbers
    
    Args:
        numbers: A list of integers
        
    Returns:
        A new list containing only the even numbers
    """
    result = []
    
    for num in numbers:
        # Bug: This checks if the index is even, not the number itself
        if numbers.index(num) % 2 == 0:
            result.append(num)
    
    return result

def parse_csv_line(line):
    """
    Parse a CSV line into a list of values
    
    Args:
        line: A string representing a line of CSV data
        
    Returns:
        A list of values from the CSV line
    """
    # Bug: This doesn't handle quoted values with commas inside them
    return line.split(',')

def is_palindrome(text):
    """
    Check if a string is a palindrome (reads the same forwards and backwards)
    
    Args:
        text: The string to check
        
    Returns:
        True if the string is a palindrome, False otherwise
    """
    # Bug: This doesn't handle spaces or case sensitivity
    return text == text[::-1] 