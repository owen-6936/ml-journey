# Module 3: Supervised Learning

**Duration**: Weeks 5-8  
**Difficulty**: Intermediate to Advanced

## 📋 Overview

Supervised learning is the foundation of most practical ML applications. In this module, you'll learn various algorithms for regression and classification, understanding both theory and implementation.

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand and implement linear and logistic regression
- Master gradient descent optimization
- Build decision trees and random forests
- Use Support Vector Machines effectively
- Evaluate model performance properly
- Apply cross-validation and hyperparameter tuning

## 📚 Week 5: Linear Regression & Gradient Descent

### Topics Covered
1. **Simple Linear Regression**
   - Hypothesis function
   - Cost function (MSE)
   - Normal equation
   - Assumptions of linear regression

2. **Multiple Linear Regression**
   - Feature scaling and normalization
   - Polynomial regression
   - Regularization (L1, L2)

3. **Gradient Descent**
   - Batch gradient descent
   - Stochastic gradient descent (SGD)
   - Mini-batch gradient descent
   - Learning rate selection

### Exercises
- [ ] Exercise 5.1: Implement linear regression from scratch
- [ ] Exercise 5.2: Compare gradient descent variants
- [ ] Exercise 5.3: Polynomial regression with regularization
- [ ] Exercise 5.4: Feature engineering for regression

### Code Implementation

```python
# File: exercises/week5_linear_regression.py
class LinearRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        # Implement gradient descent
        pass
    
    def predict(self, X):
        # Make predictions
        pass
```

### Resources
- Andrew Ng's ML Course: Week 1-2
- [StatQuest: Linear Regression](https://www.youtube.com/watch?v=nk2CQITm_eo)
- Scikit-learn Linear Regression documentation

### Project
**Housing Price Prediction**: Build a model to predict house prices using multiple features.

## 📚 Week 6: Logistic Regression & Classification

### Topics Covered
1. **Binary Classification**
   - Sigmoid function
   - Log loss (binary cross-entropy)
   - Decision boundary

2. **Multiclass Classification**
   - One-vs-Rest (OvR)
   - One-vs-One (OvO)
   - Softmax regression

3. **Evaluation Metrics**
   - Accuracy, Precision, Recall, F1-score
   - ROC curve and AUC
   - Confusion matrix
   - Classification report

### Exercises
- [ ] Exercise 6.1: Implement logistic regression from scratch
- [ ] Exercise 6.2: Binary classification project
- [ ] Exercise 6.3: Multiclass classification
- [ ] Exercise 6.4: ROC curve analysis

### Code Implementation

```python
# File: exercises/week6_logistic_regression.py
class LogisticRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def fit(self, X, y):
        # Implement gradient descent for logistic regression
        pass
    
    def predict(self, X):
        # Make predictions
        pass
```

### Resources
- Andrew Ng's ML Course: Week 3
- [StatQuest: Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8)
- Scikit-learn Classification Metrics

### Project
**Email Spam Detection**: Classify emails as spam or not spam using text features.

## 📚 Week 7: Decision Trees & Random Forests

### Topics Covered
1. **Decision Trees**
   - Gini impurity and entropy
   - Information gain
   - Tree building algorithm
   - Pruning techniques

2. **Random Forests**
   - Ensemble learning
   - Bagging and bootstrap
   - Feature importance
   - Out-of-bag (OOB) error

3. **Advanced Concepts**
   - Handling imbalanced data
   - Feature selection
   - Interpretability

### Exercises
- [ ] Exercise 7.1: Implement a simple decision tree
- [ ] Exercise 7.2: Build a random forest classifier
- [ ] Exercise 7.3: Feature importance analysis
- [ ] Exercise 7.4: Compare with other algorithms

### Code Implementation

```python
# File: exercises/week7_trees.py
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Implement and compare different tree-based models
```

### Resources
- [StatQuest: Decision Trees](https://www.youtube.com/watch?v=7VeUPuFGJHk)
- [StatQuest: Random Forests](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ)
- Scikit-learn Tree Algorithms

### Project
**Customer Churn Prediction**: Predict whether customers will churn using tree-based models.

## 📚 Week 8: Support Vector Machines (SVM)

### Topics Covered
1. **Linear SVM**
   - Maximum margin classifier
   - Support vectors
   - Hinge loss
   - Soft margin SVM

2. **Kernel Methods**
   - Kernel trick
   - RBF (Gaussian) kernel
   - Polynomial kernel
   - Custom kernels

3. **SVM in Practice**
   - Multi-class SVM
   - Parameter tuning (C, gamma)
   - When to use SVM

### Exercises
- [ ] Exercise 8.1: Linear SVM implementation
- [ ] Exercise 8.2: Kernel SVM experiments
- [ ] Exercise 8.3: SVM parameter tuning
- [ ] Exercise 8.4: Compare SVM with other classifiers

### Code Implementation

```python
# File: exercises/week8_svm.py
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

# Implement SVM with different kernels
# Tune hyperparameters using GridSearch
```

### Resources
- Andrew Ng's ML Course: Week 7
- [StatQuest: SVM](https://www.youtube.com/watch?v=efR1C6CvhmE)
- Scikit-learn SVM Guide

### Project
**Image Classification**: Use SVM to classify images (e.g., MNIST digits).

## 🔧 Required Libraries

```bash
pip install scikit-learn imbalanced-learn xgboost lightgbm
```

## 📝 Major Assignments

### Assignment 1: Complete ML Pipeline (Week 5-6)
Build a complete regression and classification pipeline:
1. Data loading and exploration
2. Feature engineering
3. Model training (multiple algorithms)
4. Model evaluation
5. Hyperparameter tuning
6. Final model selection

**Dataset**: Choose from Kaggle competitions

### Assignment 2: Ensemble Methods Comparison (Week 7-8)
Compare different supervised learning algorithms:
1. Implement at least 5 different algorithms
2. Perform proper cross-validation
3. Create performance comparison charts
4. Write a report on findings

**Due**: End of Week 8

## 📖 Research & Reading

- **Paper**: "Random Forests" by Leo Breiman
- **Paper**: "Support-Vector Networks" by Cortes & Vapnik
- **Book Chapter**: "Supervised Learning" from "Elements of Statistical Learning"

## 🎯 Model Evaluation Best Practices

1. **Always use train/test split** (or cross-validation)
2. **Never tune on test set**
3. **Use appropriate metrics** for the problem
4. **Check for overfitting** (train vs validation performance)
5. **Use cross-validation** for robust estimates

## ✅ Module Completion Checklist

- [ ] Implemented linear regression from scratch
- [ ] Implemented logistic regression from scratch
- [ ] Understand decision trees and random forests
- [ ] Can use SVM effectively
- [ ] Master model evaluation metrics
- [ ] Can perform hyperparameter tuning
- [ ] Completed all weekly projects
- [ ] Finished both assignments

## 🎓 Final Project: Supervised Learning Competition

Participate in a Kaggle competition or create your own project:
1. Choose a supervised learning problem
2. Complete EDA
3. Feature engineering
4. Try multiple algorithms
5. Ensemble methods
6. Submit predictions
7. Write a detailed report

## ➡️ Next Steps

Once you complete this module, proceed to [Module 4: Unsupervised Learning](../module_04_unsupervised_learning/README.md)

---

**Notes**: This is a crucial module. Take time to understand each algorithm deeply. Practice on multiple datasets.
