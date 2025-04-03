"""
Tests for the list_operations module
"""
import unittest
from list_operations import filter_even_numbers, double_values, find_max_value, count_occurrences

class TestListOperations(unittest.TestCase):
    """Test cases for the list_operations module"""
    
    def setUp(self):
        """Set up test data"""
        self.test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.test_items = ["apple", "banana", "apple", "orange", "banana", "apple"]
    
    def test_filter_even_numbers(self):
        """Test filtering even numbers from a list"""
        expected = [2, 4, 6, 8, 10]
        self.assertEqual(filter_even_numbers(self.test_numbers), expected)
        self.assertEqual(filter_even_numbers([]), [])  # Empty list
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])  # No even numbers
    
    def test_double_values(self):
        """Test doubling values in a list"""
        expected = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        self.assertEqual(double_values(self.test_numbers), expected)
        self.assertEqual(double_values([]), [])  # Empty list
    
    def test_find_max_value(self):
        """Test finding the maximum value in a list"""
        self.assertEqual(find_max_value(self.test_numbers), 10)
        self.assertEqual(find_max_value([5]), 5)  # Single item
        with self.assertRaises(ValueError):  # Empty list should raise ValueError
            find_max_value([])
    
    def test_count_occurrences(self):
        """Test counting occurrences of items in a list"""
        expected = {"apple": 3, "banana": 2, "orange": 1}
        self.assertEqual(count_occurrences(self.test_items), expected)
        self.assertEqual(count_occurrences([]), {})  # Empty list

if __name__ == "__main__":
    unittest.main() 