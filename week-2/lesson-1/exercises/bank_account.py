"""
Exercise: Create a bank account class with proper encapsulation
"""

class BankAccount:
    """A class representing a bank account"""
    
    def __init__(self, account_number, owner_name, balance=0):
        """
        Initialize a bank account
        
        Args:
            account_number: The account number
            owner_name: The name of the account owner
            balance: The initial balance (default 0)
        """
        # Your code here - use proper encapsulation with private attributes
        pass
    
    @property
    def account_number(self):
        """
        Get the account number
        
        Returns:
            The account number (last 4 digits masked with *)
        """
        # Your code here - return the account number with only the last 4 digits visible
        pass
    
    @property
    def owner_name(self):
        """
        Get the owner name
        
        Returns:
            The name of the account owner
        """
        # Your code here
        pass
    
    @owner_name.setter
    def owner_name(self, new_name):
        """
        Set the owner name
        
        Args:
            new_name: The new name for the account owner
        """
        # Your code here - validate that the name is not empty
        pass
    
    @property
    def balance(self):
        """
        Get the current balance
        
        Returns:
            The current balance
        """
        # Your code here
        pass
    
    def deposit(self, amount):
        """
        Deposit money into the account
        
        Args:
            amount: The amount to deposit
            
        Returns:
            The new balance
            
        Raises:
            ValueError: If the amount is negative
        """
        # Your code here - validate that amount is positive
        pass
    
    def withdraw(self, amount):
        """
        Withdraw money from the account
        
        Args:
            amount: The amount to withdraw
            
        Returns:
            The new balance
            
        Raises:
            ValueError: If the amount is negative or greater than the balance
        """
        # Your code here - validate amount and sufficient funds
        pass
    
    def __str__(self):
        """
        Return a string representation of the account
        
        Returns:
            A string with the account details
        """
        # Your code here
        pass


class SavingsAccount(BankAccount):
    """A savings account that earns interest"""
    
    def __init__(self, account_number, owner_name, balance=0, interest_rate=0.01):
        """
        Initialize a savings account
        
        Args:
            account_number: The account number
            owner_name: The name of the account owner
            balance: The initial balance (default 0)
            interest_rate: The annual interest rate (default 1%)
        """
        # Your code here
        pass
    
    @property
    def interest_rate(self):
        """
        Get the interest rate
        
        Returns:
            The current interest rate
        """
        # Your code here
        pass
    
    @interest_rate.setter
    def interest_rate(self, rate):
        """
        Set the interest rate
        
        Args:
            rate: The new interest rate
            
        Raises:
            ValueError: If the rate is negative
        """
        # Your code here - validate that rate is not negative
        pass
    
    def add_interest(self):
        """
        Add interest to the account based on the current balance and interest rate
        
        Returns:
            The amount of interest added
        """
        # Your code here - calculate interest and add to balance
        pass
    
    def __str__(self):
        """
        Return a string representation of the savings account
        
        Returns:
            A string with the account details including interest rate
        """
        # Your code here - extend the parent's __str__ method
        pass


# Test your implementation
if __name__ == "__main__":
    # Create a regular bank account
    account1 = BankAccount("1234567890", "John Doe", 1000)
    
    # Test basic operations
    print(account1)
    account1.deposit(500)
    print(f"After deposit: {account1.balance}")
    account1.withdraw(200)
    print(f"After withdrawal: {account1.balance}")
    
    # Create a savings account
    savings = SavingsAccount("9876543210", "Jane Smith", 2000, 0.025)
    
    # Test savings account operations
    print(savings)
    interest_added = savings.add_interest()
    print(f"Interest added: ${interest_added:.2f}")
    print(f"New balance: ${savings.balance:.2f}")
    
    # Test error handling
    try:
        account1.withdraw(10000)
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        account1.deposit(-100)
    except ValueError as e:
        print(f"Error: {e}") 