"""
Exercise: Implement a classification model using Scikit-learn
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

def load_and_prepare_data():
    """
    Load and prepare the breast cancer dataset
    
    Returns:
        X_train, X_test, y_train, y_test: Split and scaled data
    """
    # Your code here
    # 1. Load the breast cancer dataset
    # 2. Split the data into training and testing sets
    # 3. Scale the features
    # 4. Return the prepared data
    pass

def train_logistic_regression(X_train, y_train):
    """
    Train a logistic regression model
    
    Args:
        X_train: Training features
        y_train: Training labels
        
    Returns:
        The trained model
    """
    # Your code here
    # 1. Create a logistic regression model
    # 2. Train the model on the training data
    # 3. Return the trained model
    pass

def train_knn(X_train, y_train):
    """
    Train a K-Nearest Neighbors model
    
    Args:
        X_train: Training features
        y_train: Training labels
        
    Returns:
        The trained model
    """
    # Your code here
    # 1. Create a KNN model
    # 2. Train the model on the training data
    # 3. Return the trained model
    pass

def train_svm(X_train, y_train):
    """
    Train a Support Vector Machine model
    
    Args:
        X_train: Training features
        y_train: Training labels
        
    Returns:
        The trained model
    """
    # Your code here
    # 1. Create an SVM model
    # 2. Train the model on the training data
    # 3. Return the trained model
    pass

def train_random_forest(X_train, y_train):
    """
    Train a Random Forest model
    
    Args:
        X_train: Training features
        y_train: Training labels
        
    Returns:
        The trained model
    """
    # Your code here
    # 1. Create a Random Forest model
    # 2. Train the model on the training data
    # 3. Return the trained model
    pass

def evaluate_model(model, X_test, y_test, model_name):
    """
    Evaluate a model on the test data
    
    Args:
        model: The trained model
        X_test: Test features
        y_test: Test labels
        model_name: Name of the model for display
        
    Returns:
        The accuracy score
    """
    # Your code here
    # 1. Make predictions on the test data
    # 2. Calculate accuracy
    # 3. Print classification report
    # 4. Create and display confusion matrix
    # 5. Return the accuracy score
    pass

def perform_cross_validation(model, X, y, model_name):
    """
    Perform cross-validation on a model
    
    Args:
        model: The model to evaluate
        X: Features
        y: Labels
        model_name: Name of the model for display
        
    Returns:
        The mean cross-validation score
    """
    # Your code here
    # 1. Perform 5-fold cross-validation
    # 2. Print the cross-validation scores
    # 3. Return the mean cross-validation score
    pass

def tune_hyperparameters(X_train, y_train):
    """
    Tune hyperparameters for the Random Forest model
    
    Args:
        X_train: Training features
        y_train: Training labels
        
    Returns:
        The best model
    """
    # Your code here
    # 1. Create a parameter grid for Random Forest
    # 2. Perform grid search with cross-validation
    # 3. Print the best parameters
    # 4. Return the best model
    pass

def main():
    """Main function to run the exercise"""
    # Load and prepare data
    X_train, X_test, y_train, y_test = load_and_prepare_data()
    
    # Train models
    print("\n=== Training Logistic Regression ===")
    lr_model = train_logistic_regression(X_train, y_train)
    
    print("\n=== Training K-Nearest Neighbors ===")
    knn_model = train_knn(X_train, y_train)
    
    print("\n=== Training Support Vector Machine ===")
    svm_model = train_svm(X_train, y_train)
    
    print("\n=== Training Random Forest ===")
    rf_model = train_random_forest(X_train, y_train)
    
    # Evaluate models
    print("\n=== Evaluating Logistic Regression ===")
    lr_accuracy = evaluate_model(lr_model, X_test, y_test, "Logistic Regression")
    
    print("\n=== Evaluating K-Nearest Neighbors ===")
    knn_accuracy = evaluate_model(knn_model, X_test, y_test, "K-Nearest Neighbors")
    
    print("\n=== Evaluating Support Vector Machine ===")
    svm_accuracy = evaluate_model(svm_model, X_test, y_test, "Support Vector Machine")
    
    print("\n=== Evaluating Random Forest ===")
    rf_accuracy = evaluate_model(rf_model, X_test, y_test, "Random Forest")
    
    # Compare models
    print("\n=== Model Comparison ===")
    models = ["Logistic Regression", "K-Nearest Neighbors", "Support Vector Machine", "Random Forest"]
    accuracies = [lr_accuracy, knn_accuracy, svm_accuracy, rf_accuracy]
    
    for model, accuracy in zip(models, accuracies):
        print(f"{model}: {accuracy:.4f}")
    
    best_model_index = np.argmax(accuracies)
    print(f"\nBest model: {models[best_model_index]} with accuracy {accuracies[best_model_index]:.4f}")
    
    # Cross-validation for the best model
    if best_model_index == 0:
        best_model = lr_model
    elif best_model_index == 1:
        best_model = knn_model
    elif best_model_index == 2:
        best_model = svm_model
    else:
        best_model = rf_model
    
    print("\n=== Cross-Validation for Best Model ===")
    X = np.vstack((X_train, X_test))
    y = np.hstack((y_train, y_test))
    cv_score = perform_cross_validation(best_model, X, y, models[best_model_index])
    
    # Hyperparameter tuning for Random Forest
    print("\n=== Hyperparameter Tuning for Random Forest ===")
    best_rf = tune_hyperparameters(X_train, y_train)
    
    print("\n=== Evaluating Tuned Random Forest ===")
    tuned_rf_accuracy = evaluate_model(best_rf, X_test, y_test, "Tuned Random Forest")
    
    print(f"\nTuned Random Forest accuracy: {tuned_rf_accuracy:.4f}")
    print(f"Improvement over base Random Forest: {tuned_rf_accuracy - rf_accuracy:.4f}")

if __name__ == "__main__":
    main() 