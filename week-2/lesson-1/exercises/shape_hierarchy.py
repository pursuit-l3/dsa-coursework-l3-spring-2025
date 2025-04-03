"""
Exercise: Implement a hierarchy of shape classes
"""

class Shape:
    """Base class for all shapes"""
    
    def __init__(self, name):
        """
        Initialize a shape with a name
        
        Args:
            name: The name of the shape
        """
        self.name = name
    
    def area(self):
        """
        Calculate the area of the shape
        
        Returns:
            The area of the shape
        """
        # This is an abstract method that should be overridden by subclasses
        raise NotImplementedError("Subclasses must implement area()")
    
    def perimeter(self):
        """
        Calculate the perimeter of the shape
        
        Returns:
            The perimeter of the shape
        """
        # This is an abstract method that should be overridden by subclasses
        raise NotImplementedError("Subclasses must implement perimeter()")
    
    def __str__(self):
        """
        Return a string representation of the shape
        
        Returns:
            A string describing the shape
        """
        return f"{self.name} with area {self.area()} and perimeter {self.perimeter()}"


class Circle(Shape):
    """Circle shape"""
    
    def __init__(self, radius):
        """
        Initialize a circle with a radius
        
        Args:
            radius: The radius of the circle
        """
        # Your code here
        pass
    
    def area(self):
        """
        Calculate the area of the circle
        
        Returns:
            The area of the circle (π * r²)
        """
        # Your code here
        pass
    
    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle
        
        Returns:
            The perimeter of the circle (2 * π * r)
        """
        # Your code here
        pass


class Rectangle(Shape):
    """Rectangle shape"""
    
    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height
        
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        # Your code here
        pass
    
    def area(self):
        """
        Calculate the area of the rectangle
        
        Returns:
            The area of the rectangle (width * height)
        """
        # Your code here
        pass
    
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle
        
        Returns:
            The perimeter of the rectangle (2 * width + 2 * height)
        """
        # Your code here
        pass


class Square(Rectangle):
    """Square shape (special case of rectangle)"""
    
    def __init__(self, side_length):
        """
        Initialize a square with a side length
        
        Args:
            side_length: The length of each side of the square
        """
        # Your code here - hint: use the parent class's __init__
        pass
    
    def __str__(self):
        """
        Return a string representation of the square
        
        Returns:
            A string describing the square
        """
        # Your code here - override the parent's __str__ to specify it's a square
        pass


# Test your implementation
if __name__ == "__main__":
    # Create some shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    square = Square(4)
    
    # Print information about the shapes
    print(circle)
    print(rectangle)
    print(square)
    
    # Test polymorphism with a list of shapes
    shapes = [circle, rectangle, square]
    
    print("\nAll shapes:")
    for shape in shapes:
        print(f"{shape.name}: Area = {shape.area()}, Perimeter = {shape.perimeter()}") 