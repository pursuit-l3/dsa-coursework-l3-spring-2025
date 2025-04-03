"""
Exercise: Explore and analyze a dataset using Pandas
"""
import pandas as pd
import matplotlib.pyplot as plt

def load_dataset():
    """
    Load the Titanic dataset
    
    Returns:
        A pandas DataFrame containing the Titanic dataset
    """
    # The dataset is included with seaborn
    try:
        import seaborn as sns
        titanic = sns.load_dataset('titanic')
        return titanic
    except:
        # If seaborn is not installed, load from URL
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        return pd.read_csv(url)

def basic_exploration(df):
    """
    Perform basic exploration of the dataset
    
    Args:
        df: The pandas DataFrame to explore
        
    Returns:
        None (prints information to console)
    """
    # Your code here - explore the dataset
    # 1. Print the first 5 rows
    # 2. Print the shape of the dataset
    # 3. Print the column names
    # 4. Print basic statistics for numeric columns
    # 5. Check for missing values
    pass

def analyze_survival_by_feature(df, feature):
    """
    Analyze survival rates by a specific feature
    
    Args:
        df: The pandas DataFrame to analyze
        feature: The feature to analyze (e.g., 'sex', 'pclass', 'embarked')
        
    Returns:
        A pandas Series with survival rates by the feature
    """
    # Your code here - calculate survival rates by the feature
    pass

def visualize_survival_by_feature(df, feature):
    """
    Create a bar plot of survival rates by a specific feature
    
    Args:
        df: The pandas DataFrame to visualize
        feature: The feature to visualize (e.g., 'sex', 'pclass', 'embarked')
        
    Returns:
        None (displays the plot)
    """
    # Your code here - create a bar plot of survival rates
    pass

def analyze_fare_by_class(df):
    """
    Analyze fare statistics by passenger class
    
    Args:
        df: The pandas DataFrame to analyze
        
    Returns:
        A pandas DataFrame with fare statistics by class
    """
    # Your code here - calculate fare statistics by class
    pass

def visualize_age_distribution(df):
    """
    Create a histogram of passenger ages
    
    Args:
        df: The pandas DataFrame to visualize
        
    Returns:
        None (displays the plot)
    """
    # Your code here - create a histogram of ages
    pass

def main():
    """Main function to run the exercise"""
    # Load the dataset
    titanic = load_dataset()
    
    # Basic exploration
    print("Basic Exploration:")
    basic_exploration(titanic)
    print("\n" + "-"*50 + "\n")
    
    # Analyze survival by sex
    print("Survival Rates by Sex:")
    survival_by_sex = analyze_survival_by_feature(titanic, 'sex')
    print(survival_by_sex)
    visualize_survival_by_feature(titanic, 'sex')
    print("\n" + "-"*50 + "\n")
    
    # Analyze survival by passenger class
    print("Survival Rates by Passenger Class:")
    survival_by_class = analyze_survival_by_feature(titanic, 'pclass')
    print(survival_by_class)
    visualize_survival_by_feature(titanic, 'pclass')
    print("\n" + "-"*50 + "\n")
    
    # Analyze fare by class
    print("Fare Statistics by Passenger Class:")
    fare_by_class = analyze_fare_by_class(titanic)
    print(fare_by_class)
    print("\n" + "-"*50 + "\n")
    
    # Visualize age distribution
    print("Age Distribution:")
    visualize_age_distribution(titanic)

if __name__ == "__main__":
    main() 