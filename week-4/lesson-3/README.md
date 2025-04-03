# Week 4, Lesson 3: Python Data Science and Machine Learning

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Probability problem

  You have three cards: one card is red on both sides, one card is black on both sides, and one card is red on one side and black on the other. You pick a card at random and look at one side only, which is red. What is the probability that the other side is also red?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 12 - Order of execution of a Query](https://sqlbolt.com/lesson/select_queries_order_of_execution)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

# Break (10 minutes)

# Python Data Science and Machine Learning (35 minutes)

## Introduction to Data Science with Python

Data Science is an interdisciplinary field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data.

### Key Python Libraries for Data Science

- **NumPy**: Fundamental package for scientific computing with Python
- **Pandas**: Data manipulation and analysis library
- **Matplotlib/Seaborn**: Data visualization libraries
- **Scikit-learn**: Machine learning library
- **TensorFlow/PyTorch**: Deep learning frameworks

## NumPy Basics

NumPy is the fundamental package for scientific computing in Python. It provides support for arrays, matrices, and many mathematical functions.

```python
import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros((3, 3))
arr3 = np.ones((2, 4))
arr4 = np.random.random((2, 2))

# Array operations
print(arr1 * 2)  # Element-wise multiplication
print(arr1 + 10)  # Element-wise addition

# Matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print(np.dot(matrix1, matrix2))  # Matrix multiplication
print(matrix1 @ matrix2)  # Matrix multiplication (Python 3.5+)

# Statistical functions
print(np.mean(arr1))
print(np.median(arr1))
print(np.std(arr1))
```

## Introduction to Machine Learning with Scikit-learn

Machine Learning is a subset of artificial intelligence that provides systems the ability to automatically learn and improve from experience without being explicitly programmed.

### Types of Machine Learning

- **Supervised Learning**: Training on labeled data
- **Unsupervised Learning**: Finding patterns in unlabeled data
- **Reinforcement Learning**: Learning through trial and error with rewards

### Supervised Learning Example: Classification

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
```

### Unsupervised Learning Example: Clustering

```python
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Create and train the model
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Get cluster centers and labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.5)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
plt.title('K-means Clustering')
plt.show()
```

## Introduction to Deep Learning

Deep Learning is a subset of machine learning that uses neural networks with many layers (deep neural networks) to analyze various factors of data.

### Simple Neural Network with TensorFlow/Keras

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Generate sample data
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, random_state=42)

# Split and scale the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create a model
model = Sequential([
    Dense(64, activation='relu', input_shape=(20,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=0)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")
```

## Exercises

For this lesson, we have exercises to practice data science and machine learning in Python:

1. `numpy_pandas_exercise.py`: Practice with NumPy and Pandas for data manipulation
2. `ml_classification_exercise.py`: Implement a classification model using Scikit-learn
3. `ml_regression_exercise.py`: Implement a regression model using Scikit-learn

### Running the Exercises

1. Navigate to the exercises directory:

   ```bash
   cd week-4/lesson-3/exercises
   ```

2. Complete the functions in each file by replacing the `pass` statements with your code.

3. Run the exercises:
   ```bash
   python numpy_pandas_exercise.py
   python ml_classification_exercise.py
   python ml_regression_exercise.py
   ```

## Wrap-up (10 minutes)

- Wrap-up (10 min): Best practices for data science and machine learning in Python
- Discuss the machine learning workflow
- Review solutions to the exercises

## Additional Resources

- [NumPy Documentation](https://numpy.org/doc/stable/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [TensorFlow Documentation](https://www.tensorflow.org/api_docs)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [Kaggle - Learn Data Science](https://www.kaggle.com/learn)
- [Real Python - Data Science Tutorials](https://realpython.com/tutorials/data-science/)
