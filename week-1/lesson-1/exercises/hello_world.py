"""
A simple Hello World program in Python
This is the traditional first program for learning any programming language
"""

def say_hello(name="World"):
    """
    Returns a greeting message with the given name.
    If no name is provided, defaults to "World".
    
    Args:
        name (str, optional): The name to greet. Defaults to "World".
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"

def main():
    """
    Main function that prints a greeting to the console
    """
    print(say_hello())

if __name__ == "__main__":
    # This block only executes when the script is run directly
    # (not when imported as a module)
    main() 