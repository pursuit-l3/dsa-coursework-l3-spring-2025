"""
Tests for the shape_hierarchy module
"""
import unittest
import math
from shape_hierarchy import Shape, Circle, Rectangle, Square

class TestShapeHierarchy(unittest.TestCase):
    """Test cases for the shape hierarchy classes"""
    
    def test_shape_base_class(self):
        """Test that the Shape base class is abstract"""
        # We can't instantiate Shape directly
        with self.assertRaises(NotImplementedError):
            shape = Shape("Generic Shape")
            shape.area()
        
        with self.assertRaises(NotImplementedError):
            shape = Shape("Generic Shape")
            shape.perimeter()
    
    def test_circle(self):
        """Test the Circle class"""
        radius = 5
        circle = Circle(radius)
        
        # Test name
        self.assertEqual(circle.name, "Circle")
        
        # Test area calculation
        expected_area = math.pi * radius ** 2
        self.assertAlmostEqual(circle.area(), expected_area)
        
        # Test perimeter calculation
        expected_perimeter = 2 * math.pi * radius
        self.assertAlmostEqual(circle.perimeter(), expected_perimeter)
        
        # Test string representation
        self.assertIn("Circle", str(circle))
        self.assertIn(str(round(expected_area, 2)), str(circle))
    
    def test_rectangle(self):
        """Test the Rectangle class"""
        width, height = 4, 6
        rectangle = Rectangle(width, height)
        
        # Test name
        self.assertEqual(rectangle.name, "Rectangle")
        
        # Test area calculation
        expected_area = width * height
        self.assertEqual(rectangle.area(), expected_area)
        
        # Test perimeter calculation
        expected_perimeter = 2 * (width + height)
        self.assertEqual(rectangle.perimeter(), expected_perimeter)
        
        # Test string representation
        self.assertIn("Rectangle", str(rectangle))
        self.assertIn(str(expected_area), str(rectangle))
    
    def test_square(self):
        """Test the Square class"""
        side = 4
        square = Square(side)
        
        # Test name
        self.assertEqual(square.name, "Square")
        
        # Test inheritance from Rectangle
        self.assertIsInstance(square, Rectangle)
        
        # Test area calculation
        expected_area = side ** 2
        self.assertEqual(square.area(), expected_area)
        
        # Test perimeter calculation
        expected_perimeter = 4 * side
        self.assertEqual(square.perimeter(), expected_perimeter)
        
        # Test string representation
        self.assertIn("Square", str(square))
        self.assertIn(str(expected_area), str(square))

if __name__ == "__main__":
    unittest.main() 