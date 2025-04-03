"""
Exercise: Clean and preprocess a messy dataset using Pandas
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_messy_dataset():
    """
    Load a messy dataset
    
    Returns:
        A pandas DataFrame containing a messy dataset
    """
    # Create a synthetic messy dataset
    np.random.seed(42)
    
    # Create data with various issues
    data = {
        'ID': range(1, 101),
        'Name': [f'Person_{i}' for i in range(1, 101)],
        'Age': np.random.randint(18, 80, 100),
        'Income': np.random.normal(50000, 15000, 100),
        'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD', None], 100),
        'Marital_Status': np.random.choice(['Single', 'Married', 'Divorced', 'Widowed', 'S', 'M', 'D', 'W', ''], 100),
        'Date_Joined': pd.date_range(start='2020-01-01', periods=100),
        'Last_Purchase': pd.date_range(start='2020-02-01', periods=100),
    }
    
    df = pd.DataFrame(data)
    
    # Introduce missing values
    for col in ['Age', 'Income', 'Education', 'Marital_Status']:
        mask = np.random.choice([True, False], size=df.shape[0], p=[0.1, 0.9])
        df.loc[mask, col] = np.nan
    
    # Introduce outliers
    df.loc[np.random.choice(df.index, 5), 'Age'] = np.random.randint(100, 120, 5)
    df.loc[np.random.choice(df.index, 5), 'Income'] = np.random.normal(500000, 50000, 5)
    
    # Introduce inconsistent formatting
    df.loc[np.random.choice(df.index, 10), 'Name'] = df.loc[np.random.choice(df.index, 10), 'Name'].str.lower()
    
    # Introduce duplicate rows
    duplicates = np.random.choice(df.index, 5)
    df = pd.concat([df, df.loc[duplicates]], ignore_index=True)
    
    return df

def identify_issues(df):
    """
    Identify issues in the dataset
    
    Args:
        df: The pandas DataFrame to check
        
    Returns:
        None (prints information to console)
    """
    # Your code here - identify issues in the dataset
    # 1. Check for missing values
    # 2. Check for duplicates
    # 3. Check for outliers in numeric columns
    # 4. Check for inconsistent formatting
    pass

def clean_missing_values(df):
    """
    Clean missing values in the dataset
    
    Args:
        df: The pandas DataFrame to clean
        
    Returns:
        A cleaned pandas DataFrame
    """
    # Your code here - handle missing values
    # 1. Fill missing ages with the median age
    # 2. Fill missing incomes with the mean income
    # 3. Fill missing education with the mode
    # 4. Drop rows with missing marital status
    pass

def standardize_categorical_variables(df):
    """
    Standardize categorical variables
    
    Args:
        df: The pandas DataFrame to clean
        
    Returns:
        A cleaned pandas DataFrame
    """
    # Your code here - standardize categorical variables
    # 1. Standardize marital status (S -> Single, M -> Married, etc.)
    # 2. Standardize name formatting (all title case)
    pass

def handle_outliers(df):
    """
    Handle outliers in numeric columns
    
    Args:
        df: The pandas DataFrame to clean
        
    Returns:
        A cleaned pandas DataFrame
    """
    # Your code here - handle outliers
    # 1. Cap ages at a reasonable maximum (e.g., 100)
    # 2. Use IQR method to handle income outliers
    pass

def remove_duplicates(df):
    """
    Remove duplicate rows
    
    Args:
        df: The pandas DataFrame to clean
        
    Returns:
        A cleaned pandas DataFrame
    """
    # Your code here - remove duplicate rows
    pass

def create_new_features(df):
    """
    Create new features from existing data
    
    Args:
        df: The pandas DataFrame to enhance
        
    Returns:
        An enhanced pandas DataFrame
    """
    # Your code here - create new features
    # 1. Calculate days since last purchase
    # 2. Create an age group category
    # 3. Calculate membership duration in days
    pass

def main():
    """Main function to run the exercise"""
    # Load the messy dataset
    df = load_messy_dataset()
    
    # Identify issues
    print("Identifying Issues:")
    identify_issues(df)
    print("\n" + "-"*50 + "\n")
    
    # Clean the dataset
    print("Cleaning the Dataset:")
    
    # Handle missing values
    print("Handling Missing Values...")
    df = clean_missing_values(df)
    
    # Standardize categorical variables
    print("Standardizing Categorical Variables...")
    df = standardize_categorical_variables(df)
    
    # Handle outliers
    print("Handling Outliers...")
    df = handle_outliers(df)
    
    # Remove duplicates
    print("Removing Duplicates...")
    df = remove_duplicates(df)
    
    # Create new features
    print("Creating New Features...")
    df = create_new_features(df)
    
    # Show the cleaned dataset
    print("\nCleaned Dataset:")
    print(df.head())
    print(df.info())
    print(df.describe())

if __name__ == "__main__":
    main() 