"""
Exercise: Implement a regression model using Scikit-learn
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston, fetch_california_housing
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

def load_and_prepare_data():
    """
    Load and prepare a housing dataset
    
    Returns:
        X_train, X_test, y_train, y_test: Split and scaled data
    """
    # Your code here
    # 1. Load the California housing dataset
    # 2. Split the data into training and testing sets
    # 3. Scale the features
    # 4. Return the prepared data
    pass

def train_linear_regression(X_train, y_train):
    """
    Train a linear regression model
    
    Args:
        X_train: Training features
        y_train: Training labels
        
    Returns:
        The trained model
    """
    # Your code here
    # 1. Create a linear regression model
    # 2. Train the model on the training data
    # 3. Return the trained model
    pass

def train_ridge_regression(X_train, y_train):
    """
    Train a ridge regression model
    
    Args:
        X_train: Training features
        y_train: Training labels
        
    Returns:
        The trained model
    """
    # Your code here
    # 1. Create a ridge regression model
    # 2. Train the model on the training data
    # 3. Return the trained model
    pass

def train_lasso_regression(X_train, y_train):
    """
    Train a lasso regression model
    
    Args:
        X_train: Training features
        y_train: Training labels
        
    Returns:
        The trained model
    """
    # Your code here
    # 1. Create a lasso regression model
    # 2. Train the model on the training data
    # 3. Return the trained model
    pass

def train_random_forest_regression(X_train, y_train):
    """
    Train a random forest regression model
    
    Args:
        X_train: Training features
        y_train: Training labels
        
    Returns:
        The trained model
    """
    # Your code here
    # 1. Create a random forest regression model
    # 2. Train the model on the training data
    # 3. Return the trained model
    pass

def train_gradient_boosting_regression(X_train, y_train):
    """
    Train a gradient boosting regression model
    
    Args:
        X_train: Training features
        y_train: Training labels
        
    Returns:
        The trained model
    """
    # Your code here
    # 1. Create a gradient boosting regression model
    # 2. Train the model on the training data
    # 3. Return the trained model
    pass

def evaluate_model(model, X_test, y_test, model_name):
    """
    Evaluate a regression model on the test data
    
    Args:
        model: The trained model
        X_test: Test features
        y_test: Test labels
        model_name: Name of the model for display
        
    Returns:
        The R^2 score
    """
    # Your code here
    # 1. Make predictions on the test data
    # 2. Calculate MSE, MAE, and R^2
    # 3. Print the metrics
    # 4. Return the R^2 score
    pass

def plot_predictions(model, X_test, y_test, model_name):
    """
    Plot actual vs predicted values
    
    Args:
        model: The trained model
        X_test: Test features
        y_test: Test labels
        model_name: Name of the model for display
    """
    # Your code here
    # 1. Make predictions on the test data
    # 2. Create a scatter plot of actual vs predicted values
    # 3. Add a perfect prediction line
    # 4. Add title, labels, and legend
    pass

def plot_feature_importance(model, feature_names, model_name):
    """
    Plot feature importance for tree-based models
    
    Args:
        model: The trained model
        feature_names: Names of the features
        model_name: Name of the model for display
    """
    # Your code here
    # 1. Get feature importances from the model
    # 2. Sort features by importance
    # 3. Create a horizontal bar plot
    # 4. Add title and labels
    pass

def main():
    """Main function to run the exercise"""
    # Load and prepare data
    X_train, X_test, y_train, y_test = load_and_prepare_data()
    
    # Get feature names
    try:
        # For California housing dataset
        feature_names = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
    except:
        # Fallback
        feature_names = [f'Feature {i}' for i in range(X_train.shape[1])]
    
    # Train models
    print("\n=== Training Linear Regression ===")
    lr_model = train_linear_regression(X_train, y_train)
    
    print("\n=== Training Ridge Regression ===")
    ridge_model = train_ridge_regression(X_train, y_train)
    
    print("\n=== Training Lasso Regression ===")
    lasso_model = train_lasso_regression(X_train, y_train)
    
    print("\n=== Training Random Forest Regression ===")
    rf_model = train_random_forest_regression(X_train, y_train)
    
    print("\n=== Training Gradient Boosting Regression ===")
    gb_model = train_gradient_boosting_regression(X_train, y_train)
    
    # Evaluate models
    print("\n=== Evaluating Linear Regression ===")
    lr_r2 = evaluate_model(lr_model, X_test, y_test, "Linear Regression")
    
    print("\n=== Evaluating Ridge Regression ===")
    ridge_r2 = evaluate_model(ridge_model, X_test, y_test, "Ridge Regression")
    
    print("\n=== Evaluating Lasso Regression ===")
    lasso_r2 = evaluate_model(lasso_model, X_test, y_test, "Lasso Regression")
    
    print("\n=== Evaluating Random Forest Regression ===")
    rf_r2 = evaluate_model(rf_model, X_test, y_test, "Random Forest Regression")
    
    print("\n=== Evaluating Gradient Boosting Regression ===")
    gb_r2 = evaluate_model(gb_model, X_test, y_test, "Gradient Boosting Regression")
    
    # Compare models
    print("\n=== Model Comparison ===")
    models = ["Linear Regression", "Ridge Regression", "Lasso Regression", 
              "Random Forest Regression", "Gradient Boosting Regression"]
    r2_scores = [lr_r2, ridge_r2, lasso_r2, rf_r2, gb_r2]
    
    for model, r2 in zip(models, r2_scores):
        print(f"{model}: R^2 = {r2:.4f}")
    
    best_model_index = np.argmax(r2_scores)
    print(f"\nBest model: {models[best_model_index]} with R^2 = {r2_scores[best_model_index]:.4f}")
    
    # Plot predictions for the best model
    if best_model_index == 0:
        best_model = lr_model
    elif best_model_index == 1:
        best_model = ridge_model
    elif best_model_index == 2:
        best_model = lasso_model
    elif best_model_index == 3:
        best_model = rf_model
    else:
        best_model = gb_model
    
    print("\n=== Plotting Predictions for Best Model ===")
    plot_predictions(best_model, X_test, y_test, models[best_model_index])
    
    # Plot feature importance for tree-based models
    if best_model_index in [3, 4]:  # Random Forest or Gradient Boosting
        print("\n=== Plotting Feature Importance for Best Model ===")
        plot_feature_importance(best_model, feature_names, models[best_model_index])

if __name__ == "__main__":
    main() 