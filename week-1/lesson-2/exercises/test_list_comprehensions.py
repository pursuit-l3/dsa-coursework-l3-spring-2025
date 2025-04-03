"""
Tests for the list_comprehensions module
"""
import unittest
from list_comprehensions import (
    squares_of_evens, 
    filter_strings_by_length, 
    extract_first_char, 
    create_word_lengths_dict
)

class TestListComprehensions(unittest.TestCase):
    """Test cases for the list_comprehensions module"""
    
    def setUp(self):
        """Set up test data"""
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.strings = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
    
    def test_squares_of_evens(self):
        """Test creating a list of squares of even numbers"""
        expected = [4, 16, 36, 64, 100]
        self.assertEqual(squares_of_evens(self.numbers), expected)
        self.assertEqual(squares_of_evens([]), [])  # Empty list
        self.assertEqual(squares_of_evens([1, 3, 5]), [])  # No even numbers
    
    def test_filter_strings_by_length(self):
        """Test filtering strings by minimum length"""
        expected = ["apple", "banana", "cherry", "elderberry"]
        self.assertEqual(filter_strings_by_length(self.strings, 5), expected)
        self.assertEqual(filter_strings_by_length(self.strings, 10), ["elderberry"])  # Only one match
        self.assertEqual(filter_strings_by_length(self.strings, 20), [])  # No matches
        self.assertEqual(filter_strings_by_length([], 5), [])  # Empty list
    
    def test_extract_first_char(self):
        """Test extracting the first character of each string"""
        expected = ["a", "b", "c", "d", "e", "f"]
        self.assertEqual(extract_first_char(self.strings), expected)
        self.assertEqual(extract_first_char([]), [])  # Empty list
        
        # Test with empty strings
        with_empty = ["", "test"]
        self.assertEqual(extract_first_char(with_empty), ["", "t"])
    
    def test_create_word_lengths_dict(self):
        """Test creating a dictionary mapping words to their lengths"""
        expected = {
            "apple": 5, 
            "banana": 6, 
            "cherry": 6, 
            "date": 4, 
            "elderberry": 10, 
            "fig": 3
        }
        self.assertEqual(create_word_lengths_dict(self.strings), expected)
        self.assertEqual(create_word_lengths_dict([]), {})  # Empty list

if __name__ == "__main__":
    unittest.main() 