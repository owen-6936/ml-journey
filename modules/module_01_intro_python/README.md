# Module 1: Introduction to ML & Python Fundamentals

**Duration**: Weeks 1-2  
**Difficulty**: Beginner

## 📋 Overview

This module introduces you to the fundamentals of Python programming and essential libraries used in machine learning. You'll set up your development environment and learn the tools needed for data manipulation and analysis.

## 🎯 Learning Objectives

By the end of this module, you will:
- Set up a Python ML development environment
- Master NumPy for numerical computing
- Use Pandas for data manipulation
- Create visualizations with Matplotlib and Seaborn
- Understand basic ML concepts and terminology

## 📚 Week 1: Python Setup & NumPy/Pandas Basics

### Topics Covered
1. **Python Environment Setup**
   - Installing Python 3.8+
   - Setting up virtual environments
   - Installing Jupyter Notebook
   - IDE setup (VS Code/PyCharm)

2. **NumPy Fundamentals**
   - Arrays and array operations
   - Broadcasting
   - Linear algebra operations
   - Random number generation

3. **Pandas Basics**
   - DataFrames and Series
   - Reading/writing data (CSV, Excel, JSON)
   - Basic data exploration

### Exercises
- [ ] Exercise 1.1: Set up Python environment
- [ ] Exercise 1.2: NumPy array operations
- [ ] Exercise 1.3: Create and manipulate Pandas DataFrames
- [ ] Exercise 1.4: Load and explore a dataset

### Resources
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

### Coding Exercises

```python
# Exercise 1: NumPy Arrays
# Create exercises/week1_numpy_basics.py
# Topics: array creation, indexing, slicing, operations

# Exercise 2: Pandas DataFrames
# Create exercises/week1_pandas_basics.py
# Topics: data loading, filtering, grouping, aggregation
```

## 📚 Week 2: Data Manipulation & Visualization

### Topics Covered
1. **Advanced Pandas**
   - Data cleaning and preprocessing
   - Handling missing data
   - Merging and joining datasets
   - GroupBy operations

2. **Matplotlib**
   - Basic plots (line, scatter, bar)
   - Subplots and figures
   - Customization

3. **Seaborn**
   - Statistical visualizations
   - Distribution plots
   - Categorical plots

4. **Introduction to ML Concepts**
   - What is Machine Learning?
   - Types of ML: Supervised, Unsupervised, Reinforcement
   - ML workflow overview

### Exercises
- [ ] Exercise 2.1: Clean a messy dataset
- [ ] Exercise 2.2: Create visualizations with Matplotlib
- [ ] Exercise 2.3: Statistical plots with Seaborn
- [ ] Exercise 2.4: Exploratory Data Analysis (EDA) mini-project

### Resources
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Kaggle Learn: Data Visualization](https://www.kaggle.com/learn/data-visualization)

### Mini-Project: Exploratory Data Analysis

**Project**: Analyze a real-world dataset (e.g., Titanic, Iris, or Housing prices)

Requirements:
1. Load and clean the data
2. Perform statistical analysis
3. Create at least 5 different visualizations
4. Write insights from your analysis

## 🔧 Setup Instructions

```bash
# Create a virtual environment
python -m venv ml-env

# Activate the environment
# On Windows:
ml-env\Scripts\activate
# On macOS/Linux:
source ml-env/bin/activate

# Install required packages
pip install numpy pandas matplotlib seaborn jupyter scikit-learn

# Launch Jupyter Notebook
jupyter notebook
```

## 📝 Assignments

### Assignment 1: NumPy & Pandas Mastery (Week 1)
Create a notebook that demonstrates:
1. 10 different NumPy operations
2. Data loading from multiple formats
3. Data filtering and selection
4. Basic statistics calculation

**Due**: End of Week 1

### Assignment 2: Data Analysis Project (Week 2)
Choose a dataset from [Kaggle](https://www.kaggle.com/datasets) or [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php) and:
1. Perform complete EDA
2. Clean the data
3. Create meaningful visualizations
4. Document your findings in a Jupyter notebook

**Due**: End of Week 2

## 📖 Research & Reading

- **Paper**: "A Few Useful Things to Know About Machine Learning" by Pedro Domingos
- **Article**: Understanding the basics of ML workflows
- **Documentation**: Read Python's data model documentation

## ✅ Module Completion Checklist

- [ ] Python environment set up
- [ ] NumPy basics mastered
- [ ] Pandas operations comfortable
- [ ] Can create various plot types
- [ ] Completed all exercises
- [ ] Finished both assignments
- [ ] Understand basic ML concepts

## 🎓 Assessment

To pass this module:
1. Complete all exercises
2. Submit both assignments
3. Score 80%+ on the module quiz (create your own or use online resources)

## ➡️ Next Steps

Once you complete this module, proceed to [Module 2: Mathematical Foundations](../module_02_math_foundations/README.md)

---

**Notes**: Keep your code organized in the exercises/ directory. Document your learning in a personal journal.
