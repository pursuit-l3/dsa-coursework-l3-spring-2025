# Week 3, Lesson 1: Python Data Processing with Pandas

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Probability problem

  You have a fair six-sided die. If you roll it 6 times, what is the probability of getting each number exactly once?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 7 - OUTER JOINs](https://sqlbolt.com/lesson/select_queries_with_outer_joins)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

# Break (10 minutes)

# Python Data Processing with Pandas (35 minutes)

## Introduction to Pandas

Pandas is a powerful Python library for data manipulation and analysis. It provides data structures for efficiently storing and manipulating large datasets.

### Key Features of Pandas

- **DataFrame**: 2D labeled data structure with columns of potentially different types
- **Series**: 1D labeled array capable of holding any data type
- \*\*Efficient data alignment and integrated handling of missing data
- \*\*Powerful group by functionality for aggregating and transforming data
- \*\*High-performance merging and joining of datasets
- \*\*Time series functionality

## Installing Pandas

```bash
pip install pandas
```

## Creating DataFrames

```python
import pandas as pd
import numpy as np

# Create a DataFrame from a dictionary
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
print(df)

# Create a DataFrame from a list of lists
data = [
    ['John', 28, 'New York'],
    ['Anna', 34, 'Paris'],
    ['Peter', 29, 'Berlin'],
    ['Linda', 42, 'London']
]
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)

# Create a DataFrame from a CSV file
df = pd.read_csv('data.csv')
print(df)
```

## Basic DataFrame Operations

```python
# Display basic information about the DataFrame
print(df.info())
print(df.describe())

# Access columns
print(df['Name'])
print(df[['Name', 'Age']])

# Access rows by position
print(df.iloc[0])  # First row
print(df.iloc[1:3])  # Second and third rows

# Access rows by label
print(df.loc[0])  # Row with index 0
print(df.loc[df['Age'] > 30])  # Rows where Age > 30

# Add a new column
df['Country'] = ['USA', 'France', 'Germany', 'UK']

# Modify values
df.loc[0, 'Age'] = 29

# Delete a column
df = df.drop('Country', axis=1)
```

## Data Cleaning and Preprocessing

```python
# Check for missing values
print(df.isnull().sum())

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Drop rows with missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Rename columns
df = df.rename(columns={'Name': 'Full Name'})

# Change data types
df['Age'] = df['Age'].astype(int)
```

## Data Analysis and Aggregation

```python
# Basic statistics
print(df['Age'].mean())
print(df['Age'].median())
print(df['Age'].min())
print(df['Age'].max())

# Group by and aggregate
grouped = df.groupby('City')
print(grouped['Age'].mean())

# Multiple aggregations
result = grouped.agg({
    'Age': ['mean', 'min', 'max', 'count'],
    'Name': 'count'
})
print(result)

# Pivot tables
pivot = pd.pivot_table(df, values='Age', index='City', columns='Gender', aggfunc='mean')
print(pivot)
```

## Data Visualization with Pandas

```python
import matplotlib.pyplot as plt

# Bar plot
df['Age'].plot(kind='bar')
plt.title('Age Distribution')
plt.xlabel('Index')
plt.ylabel('Age')
plt.show()

# Histogram
df['Age'].plot(kind='hist', bins=10)
plt.title('Age Histogram')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Scatter plot
df.plot(kind='scatter', x='Age', y='Salary')
plt.title('Age vs. Salary')
plt.show()
```

## Exercises

For this lesson, we have exercises to practice data processing with Pandas:

1. `data_exploration.py`: Explore and analyze a dataset
2. `data_cleaning.py`: Clean and preprocess a messy dataset

### Running the Exercises

1. Navigate to the exercises directory:

   ```bash
   cd week-3/lesson-1/exercises
   ```

2. Complete the functions in each file by replacing the `pass` statements with your code.

3. Run the exercises:
   ```bash
   python data_exploration.py
   python data_cleaning.py
   ```

## Wrap-up (10 minutes)

- Wrap-up (10 min): Best practices for data processing with Pandas
- Discuss common data cleaning challenges
- Review solutions to the exercises

## Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Real Python - Pandas Tutorial](https://realpython.com/pandas-python-explore-dataset/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
