"""
String utility functions for testing exercise
"""

def reverse_string(s):
    """
    Reverse a string
    
    Args:
        s: The string to reverse
        
    Returns:
        The reversed string
    """
    return s[::-1]

def count_vowels(s):
    """
    Count the number of vowels in a string
    
    Args:
        s: The string to check
        
    Returns:
        The number of vowels in the string
    """
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in s:
        if char in vowels:
            count += 1
    
    return count

def capitalize_words(s):
    """
    Capitalize the first letter of each word in a string
    
    Args:
        s: The string to capitalize
        
    Returns:
        The string with each word capitalized
    """
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    """
    Remove all punctuation from a string
    
    Args:
        s: The string to process
        
    Returns:
        The string without punctuation
    """
    import string
    translator = str.maketrans('', '', string.punctuation)
    return s.translate(translator)

def is_palindrome(s, ignore_case=True, ignore_spaces=True, ignore_punctuation=True):
    """
    Check if a string is a palindrome
    
    Args:
        s: The string to check
        ignore_case: Whether to ignore case differences
        ignore_spaces: Whether to ignore spaces
        ignore_punctuation: Whether to ignore punctuation
        
    Returns:
        True if the string is a palindrome, False otherwise
    """
    if ignore_case:
        s = s.lower()
    
    if ignore_spaces:
        s = s.replace(' ', '')
    
    if ignore_punctuation:
        s = remove_punctuation(s)
    
    return s == s[::-1]

def word_frequency(s):
    """
    Count the frequency of each word in a string
    
    Args:
        s: The string to analyze
        
    Returns:
        A dictionary mapping words to their frequencies
    """
    words = s.lower().split()
    frequency = {}
    
    for word in words:
        # Remove punctuation from the word
        word = remove_punctuation(word)
        if word:  # Skip empty strings
            frequency[word] = frequency.get(word, 0) + 1
    
    return frequency 