def squares_of_evens(numbers):
    """
    Create a list of squares of even numbers from the input list.
    
    Args:
        numbers: A list of integers
        
    Returns:
        A list containing squares of even numbers
    """
    # Your code here - use list comprehension
    pass

def filter_strings_by_length(strings, min_length):
    """
    Filter strings by minimum length.
    
    Args:
        strings: A list of strings
        min_length: Minimum length threshold
        
    Returns:
        A list of strings with length >= min_length
    """
    # Your code here - use list comprehension
    pass

def extract_first_char(strings):
    """
    Extract the first character of each string.
    
    Args:
        strings: A list of strings
        
    Returns:
        A list of first characters
    """
    # Your code here - use list comprehension
    pass

def create_word_lengths_dict(words):
    """
    Create a dictionary mapping words to their lengths.
    
    Args:
        words: A list of strings
        
    Returns:
        A dictionary with words as keys and their lengths as values
    """
    # Your code here - use dictionary comprehension
    pass

# Test your functions
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    strings = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    
    print(f"Squares of even numbers: {squares_of_evens(numbers)}")
    print(f"Strings with length >= 5: {filter_strings_by_length(strings, 5)}")
    print(f"First characters: {extract_first_char(strings)}")
    print(f"Word lengths: {create_word_lengths_dict(strings)}") 