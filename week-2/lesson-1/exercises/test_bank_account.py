"""
Tests for the bank_account module
"""
import unittest
from bank_account import BankAccount, SavingsAccount

class TestBankAccount(unittest.TestCase):
    """Test cases for the BankAccount class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.account = BankAccount("1234567890", "John Doe", 1000)
    
    def test_initialization(self):
        """Test account initialization"""
        self.assertEqual(self.account.account_number, "******7890")
        self.assertEqual(self.account.owner_name, "John Doe")
        self.assertEqual(self.account.balance, 1000)
    
    def test_deposit(self):
        """Test deposit functionality"""
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500)
        self.assertEqual(self.account.balance, 1500)
        
        # Test negative deposit
        with self.assertRaises(ValueError):
            self.account.deposit(-100)
    
    def test_withdraw(self):
        """Test withdrawal functionality"""
        new_balance = self.account.withdraw(500)
        self.assertEqual(new_balance, 500)
        self.assertEqual(self.account.balance, 500)
        
        # Test negative withdrawal
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)
        
        # Test insufficient funds
        with self.assertRaises(ValueError):
            self.account.withdraw(1000)
    
    def test_owner_name_setter(self):
        """Test setting the owner name"""
        self.account.owner_name = "Jane Doe"
        self.assertEqual(self.account.owner_name, "Jane Doe")
        
        # Test empty name
        with self.assertRaises(ValueError):
            self.account.owner_name = ""
    
    def test_string_representation(self):
        """Test string representation of the account"""
        account_str = str(self.account)
        self.assertIn("******7890", account_str)
        self.assertIn("John Doe", account_str)
        self.assertIn("1000", account_str)

class TestSavingsAccount(unittest.TestCase):
    """Test cases for the SavingsAccount class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.savings = SavingsAccount("9876543210", "Jane Smith", 2000, 0.025)
    
    def test_initialization(self):
        """Test savings account initialization"""
        self.assertEqual(self.savings.account_number, "******3210")
        self.assertEqual(self.savings.owner_name, "Jane Smith")
        self.assertEqual(self.savings.balance, 2000)
        self.assertEqual(self.savings.interest_rate, 0.025)
    
    def test_interest_rate_setter(self):
        """Test setting the interest rate"""
        self.savings.interest_rate = 0.03
        self.assertEqual(self.savings.interest_rate, 0.03)
        
        # Test negative interest rate
        with self.assertRaises(ValueError):
            self.savings.interest_rate = -0.01
    
    def test_add_interest(self):
        """Test adding interest to the account"""
        # Interest should be balance * interest_rate
        expected_interest = 2000 * 0.025
        interest_added = self.savings.add_interest()
        
        self.assertEqual(interest_added, expected_interest)
        self.assertEqual(self.savings.balance, 2000 + expected_interest)
    
    def test_string_representation(self):
        """Test string representation of the savings account"""
        account_str = str(self.savings)
        self.assertIn("******3210", account_str)
        self.assertIn("Jane Smith", account_str)
        self.assertIn("2000", account_str)
        self.assertIn("2.5%", account_str)  # Should show interest rate as percentage

if __name__ == "__main__":
    unittest.main() 