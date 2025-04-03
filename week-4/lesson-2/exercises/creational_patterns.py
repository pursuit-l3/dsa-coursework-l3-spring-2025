"""
Exercise: Implement Singleton and Factory patterns
"""

# Part 1: Singleton Pattern
class DatabaseConnection:
    """
    Implement a Singleton pattern for a database connection
    
    This class should ensure that only one database connection exists
    throughout the application.
    """
    # Your code here
    # 1. Implement the Singleton pattern
    # 2. Add methods for connecting and querying the database
    pass

# Part 2: Factory Method Pattern
class Document:
    """Base document class"""
    def __init__(self, name):
        self.name = name
    
    def open(self):
        pass
    
    def save(self):
        pass

class PDFDocument(Document):
    """PDF document implementation"""
    def open(self):
        return f"Opening PDF document: {self.name}.pdf"
    
    def save(self):
        return f"Saving PDF document: {self.name}.pdf"

class WordDocument(Document):
    """Word document implementation"""
    def open(self):
        return f"Opening Word document: {self.name}.docx"
    
    def save(self):
        return f"Saving Word document: {self.name}.docx"

class SpreadsheetDocument(Document):
    """Spreadsheet document implementation"""
    def open(self):
        return f"Opening Spreadsheet document: {self.name}.xlsx"
    
    def save(self):
        return f"Saving Spreadsheet document: {self.name}.xlsx"

class DocumentFactory:
    """
    Implement a Factory Method pattern for creating documents
    
    This class should create different types of documents based on the file extension
    or document type specified.
    """
    # Your code here
    # 1. Implement the Factory Method pattern
    # 2. Add a method to create documents based on document type or file extension
    pass

def test_singleton():
    """Test the Singleton pattern implementation"""
    print("\n=== Testing Singleton Pattern ===")
    
    # Create two instances of DatabaseConnection
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    # Check if they are the same instance
    print(f"db1 is db2: {db1 is db2}")
    
    # Test some methods
    print(db1.connect("example_db"))
    print(db1.query("SELECT * FROM users"))
    print(db2.query("SELECT * FROM products"))

def test_factory():
    """Test the Factory Method pattern implementation"""
    print("\n=== Testing Factory Method Pattern ===")
    
    factory = DocumentFactory()
    
    # Create documents using the factory
    pdf = factory.create_document("Report", "pdf")
    word = factory.create_document("Letter", "word")
    spreadsheet = factory.create_document("Budget", "spreadsheet")
    
    # Test the documents
    print(pdf.open())
    print(pdf.save())
    
    print(word.open())
    print(word.save())
    
    print(spreadsheet.open())
    print(spreadsheet.save())
    
    # Test with file extensions
    pdf2 = factory.create_document("AnotherReport", ".pdf")
    word2 = factory.create_document("AnotherLetter", ".docx")
    spreadsheet2 = factory.create_document("AnotherBudget", ".xlsx")
    
    print(pdf2.open())
    print(word2.open())
    print(spreadsheet2.open())

def main():
    """Main function to run the exercise"""
    test_singleton()
    test_factory()

if __name__ == "__main__":
    main() 