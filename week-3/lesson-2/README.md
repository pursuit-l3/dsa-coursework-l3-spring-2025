# Week 3, Lesson 2: Python Data Visualization

## Warm-up (30 minutes)

### Brain Teaser (15 minutes)

- Brain Teaser (15 min): Combinatorial problem

  In how many ways can you arrange the letters in the word "MISSISSIPPI"?

### SQL Exercise (15 minutes)

- SQL Exercise (15 min): [SQLBolt Lesson 8 - A short note on NULLs](https://sqlbolt.com/lesson/select_queries_with_nulls)

## Technical Training (90 minutes)

### LeetCode Problem (45 minutes)

- LeetCode Problem (45 min): [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

# Break (10 minutes)

# Python Data Visualization (35 minutes)

## Introduction to Data Visualization

Data visualization is the graphical representation of information and data. It helps to communicate complex data relationships and data-driven insights in a visual way that is easier to understand.

### Why Data Visualization?

- Quickly communicate complex information
- Identify patterns, trends, and outliers
- Make data-driven decisions
- Tell compelling stories with data

## Visualization Libraries in Python

Python offers several powerful libraries for data visualization:

- **Matplotlib**: The foundation for most Python plotting libraries
- **Seaborn**: Statistical data visualization based on matplotlib
- **Plotly**: Interactive, web-based visualizations
- **Bokeh**: Interactive visualizations for modern web browsers
- **Altair**: Declarative statistical visualization library

## Matplotlib Basics

```python
import matplotlib.pyplot as plt
import numpy as np

# Basic line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()

# Multiple plots
plt.figure(figsize=(10, 6))
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 8))
axs[0].plot(x, np.sin(x))
axs[0].set_title('Sine Wave')
axs[0].set_ylabel('sin(x)')
axs[0].grid(True)

axs[1].plot(x, np.cos(x))
axs[1].set_title('Cosine Wave')
axs[1].set_xlabel('x')
axs[1].set_ylabel('cos(x)')
axs[1].grid(True)

plt.tight_layout()
plt.show()
```

## Common Plot Types

```python
# Bar plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 55, 15]

plt.figure(figsize=(10, 6))
plt.bar(categories, values)
plt.title('Bar Plot')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Color')
plt.show()

# Histogram
data = np.random.randn(1000)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()

# Pie chart
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 25, 10, 20]
explode = (0, 0.1, 0, 0, 0)  # explode the 2nd slice

plt.figure(figsize=(10, 6))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Pie Chart')
plt.show()
```

## Seaborn for Statistical Visualization

```python
import seaborn as sns
import pandas as pd

# Load a sample dataset
tips = sns.load_dataset('tips')

# Distribution plot
plt.figure(figsize=(10, 6))
sns.histplot(tips['total_bill'], kde=True)
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Count')
plt.show()

# Scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='total_bill', y='tip', data=tips)
plt.title('Tip vs Total Bill')
plt.show()

# Categorical plots
plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Total Bill by Day')
plt.show()

plt.figure(figsize=(10, 6))
sns.violinplot(x='day', y='total_bill', hue='sex', data=tips, split=True)
plt.title('Total Bill by Day and Sex')
plt.show()

# Heatmap
plt.figure(figsize=(10, 8))
correlation = tips.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Pair plot
sns.pairplot(tips, hue='sex')
plt.suptitle('Pair Plot of Tips Dataset', y=1.02)
plt.show()
```

## Interactive Visualization with Plotly

```python
import plotly.express as px
import plotly.graph_objects as go

# Line plot
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life Expectancy in Canada')
fig.show()

# Scatter plot
df = px.data.gapminder().query("year==2007")
fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60,
                 title="GDP per Capita vs Life Expectancy (2007)")
fig.show()

# Bar chart
df = px.data.gapminder().query("continent=='Oceania'")
fig = px.bar(df, x="year", y="pop", color="country", title="Population of Oceania Countries")
fig.show()

# Choropleth map
df = px.data.gapminder().query("year==2007")
fig = px.choropleth(df, locations="iso_alpha", color="lifeExp", hover_name="country",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Life Expectancy by Country (2007)")
fig.show()
```

## Exercises

For this lesson, we have exercises to practice data visualization in Python:

1. `basic_visualization.py`: Create basic plots using matplotlib
2. `advanced_visualization.py`: Create advanced visualizations using seaborn and plotly

### Running the Exercises

1. Navigate to the exercises directory:

   ```bash
   cd week-3/lesson-2/exercises
   ```

2. Complete the functions in each file by replacing the `pass` statements with your code.

3. Run the exercises:
   ```bash
   python basic_visualization.py
   python advanced_visualization.py
   ```

## Wrap-up (10 minutes)

- Wrap-up (10 min): Best practices for data visualization
- Discuss choosing the right visualization for your data
- Review solutions to the exercises

## Additional Resources

- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Plotly Documentation](https://plotly.com/python/)
- [Data Visualization with Python](https://realpython.com/python-data-visualization/)
- [The Python Graph Gallery](https://python-graph-gallery.com/)
