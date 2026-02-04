# Module 1: Python & NumPy Fundamentals 🐍

**Duration**: Weeks 1-2  
**Difficulty**: Beginner

## 📋 Overview

This module introduces you to the fundamentals of Python programming and essential libraries used in machine learning. You'll set up your development environment and learn the tools needed for data manipulation and analysis. **Emphasis on understanding the hardware-software bridge** that makes ML performant.

## 🎯 Learning Objectives

By the end of this module, you will:
- **Hardware Awareness**: Understand how memory layout (contiguous vs. non-contiguous) affects AI performance
- **Vectorization Mastery**: Learn to replace slow for loops with high-speed NumPy operations
- **Research Literacy**: Begin a habit of reading foundational technical notes and viewing expert visualizations
- Set up a Python ML development environment
- Master NumPy for numerical computing
- Use Pandas for data manipulation
- Create visualizations with Matplotlib and Seaborn
- Understand basic ML concepts and terminology

## 📚 Week 1: The Hardware-Software Bridge

### 📚 Research Assignment: The Memory Bottleneck

**Goal**: Prove why "Continuous Space" (Contiguous Memory) is the backbone of ML.

**Core Question**: In your `research/` folder, create a document explaining the **"Hotel vs. Scattered Houses" analogy**:
- **NumPy Arrays (Hotel)**: All data stored in adjacent memory locations - the CPU can fetch entire blocks at once
- **Python Lists (Scattered Houses)**: Each element might be stored anywhere in memory - the CPU must make individual trips

**Key Concept - SIMD (Single Instruction, Multiple Data)**:
Research how your CPU/GPU uses SIMD to process blocks of numbers simultaneously. This is why NumPy can perform operations on entire arrays in one instruction, while Python loops must process elements one at a time.

**Assignment**: Write a 1-2 page explanation in `research/week1_memory_bottleneck.md` covering:
1. The difference between contiguous and non-contiguous memory
2. How SIMD enables parallel processing
3. Why this matters for machine learning performance
4. Include diagrams or ASCII art to illustrate the concepts

### 🧪 Lab 1.1: Hello Vectors

**Goal**: Practical implementation of vector operations with performance benchmarking.

**Tasks**:

1. **Creation**: Build two 1D arrays of size 100,000 using `np.random.randint`
2. **Benchmark**: Add these arrays using:
   - Standard Python `for` loop
   - NumPy's `+` operator
   - Use the `time` library to record the difference
3. **The Dot Product**: Compute the dot product and explain its geometric meaning (scaling and direction)

**Expected Code**:
```python
import numpy as np
import time

# Create arrays
arr1 = np.random.randint(0, 100, size=100000)
arr2 = np.random.randint(0, 100, size=100000)

# Method 1: Python loop
start = time.time()
result_loop = []
for i in range(len(arr1)):
    result_loop.append(arr1[i] + arr2[i])
loop_time = time.time() - start

# Method 2: NumPy vectorization
start = time.time()
result_numpy = arr1 + arr2
numpy_time = time.time() - start

print(f"Loop time: {loop_time:.6f}s")
print(f"NumPy time: {numpy_time:.6f}s")
print(f"Speedup: {loop_time/numpy_time:.1f}x")
```

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
   - **Memory layout and performance implications**

3. **NumPy for JS Developers** 🆕
   - Array methods: `.map()`, `.filter()`, `.reduce()` → NumPy vectorization
   - Understanding vectorized operations vs loops
   - Performance comparison: for loops vs NumPy
   - Common JS patterns translated to NumPy

4. **Pandas Basics**
   - DataFrames and Series
   - Reading/writing data (CSV, Excel, JSON)
   - Basic data exploration

### Exercises
- [ ] Exercise 1.1: Set up Python environment
- [ ] Exercise 1.2: Research Assignment - Write "Memory Bottleneck" explanation
- [ ] Exercise 1.3: Lab 1.1 - Hello Vectors with benchmarking
- [ ] Exercise 1.4: NumPy array operations
- [ ] Exercise 1.5: NumPy for JS Developers - Translate JS patterns to NumPy
- [ ] Exercise 1.6: Create and manipulate Pandas DataFrames
- [ ] Exercise 1.7: Load and explore a dataset

### 🔗 Essential Resources

#### 📺 Watch (Visual Foundations)

**Must-Watch Videos**:
1. **[Computerphile] Why NumPy is Faster Than Lists**
   - Link: Search "Computerphile NumPy faster" on YouTube
   - Essential for understanding the "Valet" (CPU) and how it fetches memory
   - Explains contiguous memory and cache efficiency

2. **[3Blue1Brown] Linear Algebra - Vectors**
   - Link: https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
   - A masterpiece in visualizing what a vector actually represents in space
   - Watch at least Chapters 1-3 (Vectors, Linear combinations, Matrix multiplication)

3. **[Two Minute Papers] Why AI Needs GPUs**
   - Explains parallel processing and why matrix operations are so important

#### 📖 Read (Research & Documentation)

**Foundational Research**:
1. **"A Few Useful Things to Know About Machine Learning" by Pedro Domingos**
   - Link: https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf
   - **Must-read** for beginners to avoid common pitfalls
   - Read pages 1-5 focusing on the introduction and overfitting section
   - Create notes in your `research/` folder

2. **NumPy Internals - Memory Layout**
   - Link: https://numpy.org/doc/stable/reference/internals.html
   - Pay close attention to the definition of **Strides**
   - Understand how NumPy knows where each element is located

3. **Understanding NumPy's ndarray**
   - Link: https://numpy.org/doc/stable/reference/arrays.ndarray.html
   - Read the "Internal memory layout" section
   - Understand the difference between C-contiguous and Fortran-contiguous arrays

**Visual Aids**:
- **Python Tutor**: http://pythontutor.com/ - Visualize how Python executes code step-by-step
- **NumPy Illustrated**: https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d

### Resources
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

### Coding Exercises

```python
# Exercise 1: NumPy Arrays
# Create exercises/week1_numpy_basics.py
# Topics: array creation, indexing, slicing, operations

# Exercise 2: NumPy for JS Developers
# Create exercises/week1_numpy_for_js_devs.py
# Topics: vectorization, translating .map/.filter/.reduce to NumPy

# Exercise 3: Pandas DataFrames
# Create exercises/week1_pandas_basics.py
# Topics: data loading, filtering, grouping, aggregation
```

### Special Section: NumPy for JavaScript Developers 💻

If you're coming from JavaScript/TypeScript, this section will help you leverage your array manipulation skills:

**JS `.map()` → NumPy vectorization**
```python
# JavaScript
const doubled = arr.map(x => x * 2);

# Python/NumPy - NO loops needed!
doubled = arr * 2
```

**JS `.filter()` → NumPy boolean indexing**
```python
# JavaScript
const filtered = arr.filter(x => x > 5);

# Python/NumPy
filtered = arr[arr > 5]
```

**JS `.reduce()` → NumPy aggregations**
```python
# JavaScript
const sum = arr.reduce((acc, x) => acc + x, 0);

# Python/NumPy
sum = arr.sum()
```

**Why this matters**: NumPy operations are 10-100x faster because they avoid Python loops and use optimized C code under the hood. As a JS dev who thinks algorithmically, you'll appreciate the elegance and performance!

**Exercise**: Create `exercises/week1_numpy_for_js_devs.py` to practice these translations.

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

5. **Your First ML Algorithm: Linear Regression from Scratch** 🆕
   - Understanding the concept: fitting a line to data
   - Implementing gradient descent with vanilla Python (no ML libraries!)
   - Seeing how a simple loop can "learn"
   - Why this matters before diving into math in Module 2

### Exercises
- [ ] Exercise 2.1: Clean a messy dataset
- [ ] Exercise 2.2: Create visualizations with Matplotlib
- [ ] Exercise 2.3: Statistical plots with Seaborn
- [ ] Exercise 2.4: Build Linear Regression from scratch (vanilla Python)
- [ ] Exercise 2.5: Exploratory Data Analysis (EDA) mini-project

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

### 🚀 Special Challenge: Build Your First ML Algorithm (No Libraries!)

**Why do this?** As someone who likes building from scratch, seeing how a simple loop can "learn" will make the complex math in Module 2 feel relevant and concrete.

**The Challenge**: Implement Linear Regression using only vanilla Python (no scikit-learn, no ML libraries!)

```python
# File: exercises/week2_linear_regression_scratch.py
"""
Your First ML Algorithm: Linear Regression from Scratch

Goal: Fit a line y = mx + b to data points using gradient descent
You'll see how a loop can iteratively "learn" the best m and b!
"""

def linear_regression_scratch(X, y, learning_rate=0.01, iterations=1000):
    """
    Implement gradient descent to find m and b
    
    For JS devs: This is like using a loop to minimize error!
    Each iteration adjusts m and b to reduce prediction error.
    """
    m = 0  # slope
    b = 0  # intercept
    n = len(X)
    
    for i in range(iterations):
        # Make predictions
        y_pred = [m * x + b for x in X]
        
        # Calculate error (Mean Squared Error)
        error = sum([(pred - actual) ** 2 for pred, actual in zip(y_pred, y)]) / n
        
        # Calculate gradients (how much to adjust m and b)
        dm = sum([2 * x * (pred - actual) for x, pred, actual in zip(X, y_pred, y)]) / n
        db = sum([2 * (pred - actual) for pred, actual in zip(y_pred, y)]) / n
        
        # Update parameters
        m = m - learning_rate * dm
        b = b - learning_rate * db
        
        if i % 100 == 0:
            print(f"Iteration {i}: Error = {error:.4f}")
    
    return m, b

# Test it!
X = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]  # Perfect line: y = 2x
m, b = linear_regression_scratch(X, y)
print(f"Learned: y = {m:.2f}x + {b:.2f}")
```

**What you'll learn:**
- How machine learning is just optimization (finding best parameters)
- Why we need gradient descent (cannot solve directly for complex problems)
- The intuition behind "training" a model
- This prepares you perfectly for Module 2's math!

**Bonus**: After implementing this, the calculus and linear algebra in Module 2 will feel like "oh, this is WHY it works!" instead of abstract math.

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
