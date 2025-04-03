"""
Tests for the hello_world module
"""
import unittest
from hello_world import say_hello

class TestHelloWorld(unittest.TestCase):
    """Test cases for the hello_world module"""
    
    def test_default_greeting(self):
        """Test the default greeting (no name provided)"""
        self.assertEqual(say_hello(), "Hello, World!")
    
    def test_custom_greeting(self):
        """Test greeting with a custom name"""
        self.assertEqual(say_hello("Python"), "Hello, Python!")
    
    def test_empty_name(self):
        """Test greeting with an empty name"""
        self.assertEqual(say_hello(""), "Hello, !")

if __name__ == "__main__":
    unittest.main() 