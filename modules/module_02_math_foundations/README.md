# Module 2: Mathematical Foundations

**Duration**: Weeks 3-4  
**Difficulty**: Intermediate

## 📋 Overview

Understanding the mathematics behind machine learning is crucial for building intuition about how algorithms work. This module covers essential linear algebra, calculus, probability, and statistics needed for ML.

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand vectors, matrices, and their operations
- Apply calculus concepts to ML (derivatives, gradients)
- Use probability theory in ML contexts
- Perform statistical analysis
- Implement mathematical concepts in Python

## 📚 Week 3: Linear Algebra

### Topics Covered
1. **Vectors and Vector Operations**
   - Vector addition, subtraction, scalar multiplication
   - Dot product and cross product
   - Vector norms (L1, L2)
   - Unit vectors and normalization

2. **Matrices**
   - Matrix operations (addition, multiplication)
   - Transpose, inverse
   - Determinant and rank
   - Eigenvalues and eigenvectors

3. **Applications in ML**
   - Data representation as matrices
   - Linear transformations
   - Dimensionality and vector spaces

### Exercises
- [ ] Exercise 3.1: Vector operations in NumPy
- [ ] Exercise 3.2: Matrix multiplication and properties
- [ ] Exercise 3.3: Eigenvalue decomposition
- [ ] Exercise 3.4: Implement PCA from scratch (simplified)

### Resources
- [3Blue1Brown: Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [MIT OCW: Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/)
- Khan Academy: Linear Algebra

### Coding Exercises

```python
# Exercise 1: Vector Operations
# Implement dot product, cross product, norms
# File: exercises/week3_vectors.py

# Exercise 2: Matrix Operations
# Implement matrix multiplication, inverse, determinant
# File: exercises/week3_matrices.py
```

## 📚 Week 4: Calculus, Probability & Statistics

### Topics Covered
1. **Calculus Basics**
   - Derivatives and partial derivatives
   - Chain rule (crucial for backpropagation)
   - Gradient and gradient descent
   - Optimization basics

2. **Probability Theory**
   - Probability distributions (Normal, Bernoulli, Binomial)
   - Conditional probability and Bayes' theorem
   - Expected value and variance
   - Maximum Likelihood Estimation (MLE)

3. **Statistics**
   - Descriptive statistics (mean, median, mode, std)
   - Hypothesis testing
   - Confidence intervals
   - Correlation and covariance

### Exercises
- [ ] Exercise 4.1: Calculate derivatives using SymPy
- [ ] Exercise 4.2: Implement gradient descent from scratch
- [ ] Exercise 4.3: Work with probability distributions
- [ ] Exercise 4.4: Statistical hypothesis testing

### Resources
- [3Blue1Brown: Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
- [Khan Academy: Probability and Statistics](https://www.khanacademy.org/math/statistics-probability)
- StatQuest YouTube Channel

### Coding Exercises

```python
# Exercise 1: Gradient Descent
# Implement gradient descent for a simple function
# File: exercises/week4_gradient_descent.py

# Exercise 2: Probability Distributions
# Work with scipy.stats and visualize distributions
# File: exercises/week4_probability.py
```

## 🔧 Additional Libraries

```bash
pip install scipy sympy
```

## 📝 Assignments

### Assignment 1: Linear Algebra in Practice (Week 3)
Implement the following from scratch using NumPy:
1. Matrix multiplication (don't use @)
2. Matrix inverse using Gaussian elimination
3. QR decomposition
4. A simple image transformation using matrices

**Due**: End of Week 3

### Assignment 2: Optimization Project (Week 4)
Create a notebook that:
1. Implements gradient descent for multiple functions
2. Visualizes the optimization process
3. Compares different learning rates
4. Applies gradient descent to a simple ML problem (linear regression)

**Due**: End of Week 4

## 📖 Research & Reading

- **Paper**: "The Matrix Calculus You Need For Deep Learning" by Parr & Howard
- **Book Chapter**: Read Chapter 2 of "Deep Learning" by Goodfellow (Linear Algebra)
- **Article**: Understanding Gradient Descent and Backpropagation

## 🧮 Key Formulas to Master

### Linear Algebra
```
Dot product: a · b = Σ(ai * bi)
Matrix multiplication: C = AB, where Cij = Σ(Aik * Bkj)
Norm: ||x|| = √(Σxi²)
```

### Calculus
```
Gradient: ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]
Chain rule: d/dx[f(g(x))] = f'(g(x)) * g'(x)
Gradient descent: θ := θ - α∇J(θ)
```

### Probability
```
Bayes' theorem: P(A|B) = P(B|A)P(A) / P(B)
Expected value: E[X] = Σ(xi * P(xi))
Variance: Var(X) = E[(X - μ)²]
```

## 💡 Practical Tips

1. **Visualize Everything**: Use matplotlib to visualize vectors, matrices, gradients
2. **Implement from Scratch First**: Then use library implementations
3. **Connect to ML**: Always ask "how is this used in ML?"
4. **Practice Daily**: Math requires consistent practice

## ✅ Module Completion Checklist

- [ ] Understand vector and matrix operations
- [ ] Can compute derivatives and gradients
- [ ] Implemented gradient descent from scratch
- [ ] Understand probability distributions
- [ ] Can perform statistical analysis
- [ ] Completed all exercises
- [ ] Finished both assignments
- [ ] Can explain math concepts in ML context

## 🎓 Assessment

Create a Jupyter notebook that demonstrates:
1. Linear algebra operations with visualizations
2. Gradient descent implementation
3. Probability calculations
4. Statistical analysis of a dataset

Minimum score: 80%

## ➡️ Next Steps

Once you complete this module, proceed to [Module 3: Supervised Learning](../module_03_supervised_learning/README.md)

---

**Notes**: Math is the foundation of ML. Take your time with this module. Revisit concepts as needed.
