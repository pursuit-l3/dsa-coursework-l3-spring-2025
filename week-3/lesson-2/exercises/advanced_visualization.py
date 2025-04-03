"""
Exercise: Create advanced visualizations using seaborn and plotly
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Optional: If plotly is installed
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    print("Plotly is not installed. Skipping plotly visualizations.")

def load_dataset():
    """
    Load a dataset for visualization
    
    Returns:
        A pandas DataFrame
    """
    # Try to load a seaborn dataset
    try:
        # Load the Titanic dataset
        titanic = sns.load_dataset('titanic')
        return titanic
    except:
        # If seaborn datasets are not available, create a synthetic dataset
        np.random.seed(42)
        
        # Create synthetic data
        n = 500
        data = {
            'age': np.random.normal(30, 10, n),
            'fare': np.random.exponential(50, n),
            'survived': np.random.choice([0, 1], size=n, p=[0.6, 0.4]),
            'class': np.random.choice(['First', 'Second', 'Third'], size=n, p=[0.2, 0.3, 0.5]),
            'sex': np.random.choice(['male', 'female'], size=n),
            'embark_town': np.random.choice(['Southampton', 'Cherbourg', 'Queenstown'], size=n, p=[0.7, 0.2, 0.1]),
            'alone': np.random.choice([True, False], size=n),
        }
        
        return pd.DataFrame(data)

def create_seaborn_distribution_plot(df):
    """
    Create a distribution plot using seaborn
    
    Args:
        df: The pandas DataFrame to visualize
        
    Returns:
        None (displays the plot)
    """
    # Your code here
    # 1. Create a distribution plot of a numeric column (e.g., 'age')
    # 2. Add title and labels
    # 3. Customize the appearance
    pass

def create_seaborn_categorical_plot(df):
    """
    Create categorical plots using seaborn
    
    Args:
        df: The pandas DataFrame to visualize
        
    Returns:
        None (displays the plot)
    """
    # Your code here
    # 1. Create a box plot showing a numeric variable across categories
    # 2. Create a violin plot showing the same data
    # 3. Add titles and labels
    pass

def create_seaborn_heatmap(df):
    """
    Create a correlation heatmap using seaborn
    
    Args:
        df: The pandas DataFrame to visualize
        
    Returns:
        None (displays the plot)
    """
    # Your code here
    # 1. Calculate the correlation matrix of numeric columns
    # 2. Create a heatmap of the correlation matrix
    # 3. Add title and customize appearance
    pass

def create_seaborn_pairplot(df):
    """
    Create a pair plot using seaborn
    
    Args:
        df: The pandas DataFrame to visualize
        
    Returns:
        None (displays the plot)
    """
    # Your code here
    # 1. Create a pair plot of numeric columns, colored by a categorical variable
    # 2. Customize the appearance
    pass

def create_plotly_interactive_plot(df):
    """
    Create an interactive plot using plotly
    
    Args:
        df: The pandas DataFrame to visualize
        
    Returns:
        None (displays the plot)
    """
    if not PLOTLY_AVAILABLE:
        print("Plotly is not available. Skipping this visualization.")
        return
    
    # Your code here
    # 1. Create an interactive scatter plot
    # 2. Add hover information
    # 3. Customize appearance
    pass

def create_plotly_dashboard(df):
    """
    Create a simple dashboard with multiple plotly visualizations
    
    Args:
        df: The pandas DataFrame to visualize
        
    Returns:
        None (displays the plots)
    """
    if not PLOTLY_AVAILABLE:
        print("Plotly is not available. Skipping this visualization.")
        return
    
    # Your code here
    # 1. Create a subplot with 2x2 grid
    # 2. Add different plot types to each cell
    # 3. Customize appearance and add titles
    pass

def main():
    """Main function to run the exercise"""
    # Load the dataset
    df = load_dataset()
    print("Dataset loaded successfully.")
    print(df.head())
    print("\n" + "-"*50 + "\n")
    
    print("Creating Seaborn Distribution Plot...")
    create_seaborn_distribution_plot(df)
    
    print("Creating Seaborn Categorical Plot...")
    create_seaborn_categorical_plot(df)
    
    print("Creating Seaborn Heatmap...")
    create_seaborn_heatmap(df)
    
    print("Creating Seaborn Pair Plot...")
    create_seaborn_pairplot(df)
    
    if PLOTLY_AVAILABLE:
        print("Creating Plotly Interactive Plot...")
        create_plotly_interactive_plot(df)
        
        print("Creating Plotly Dashboard...")
        create_plotly_dashboard(df)

if __name__ == "__main__":
    main() 