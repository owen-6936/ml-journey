# Jupyter Notebooks Directory

This directory contains Jupyter notebooks for exercises, experiments, and exploratory data analysis.

## 📓 Notebook Organization

Organize notebooks by module:

```
notebooks/
├── module_01_intro/
│   ├── 01_numpy_basics.ipynb
│   ├── 02_pandas_intro.ipynb
│   └── 03_visualization.ipynb
├── module_02_math/
│   ├── 01_linear_algebra.ipynb
│   └── 02_calculus_stats.ipynb
├── module_03_supervised/
│   ├── 01_linear_regression.ipynb
│   ├── 02_logistic_regression.ipynb
│   └── 03_decision_trees.ipynb
└── experiments/
    └── quick_tests.ipynb
```

## 🎯 Notebook Best Practices

### 1. Naming Convention
- Use descriptive names
- Include module/week number
- Use lowercase with underscores
- Example: `03_week1_linear_regression.ipynb`

### 2. Structure
Every notebook should have:
```markdown
# Title

## 1. Introduction
Brief description and objectives

## 2. Setup
Imports and configuration

## 3. Data Loading
Load and explore data

## 4. Analysis/Implementation
Main content

## 5. Results
Findings and visualizations

## 6. Conclusions
Key takeaways and next steps
```

### 3. Code Quality
- Clear markdown explanations
- Well-commented code
- Reproducible results (set random seeds)
- Clean output (clear outputs before committing)

### 4. Visualizations
- Properly labeled axes
- Titles and legends
- Appropriate figure sizes
- Color-blind friendly palettes

## 🔧 Jupyter Setup

### Installation
```bash
# Install Jupyter
pip install jupyter notebook

# Install JupyterLab (modern interface)
pip install jupyterlab

# Install extensions
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

### Useful Extensions
1. **Table of Contents**: Easy navigation
2. **Variable Inspector**: See variable values
3. **ExecuteTime**: Track cell execution time
4. **Code Folding**: Collapse code blocks

### Launch Jupyter
```bash
# Classic Notebook
jupyter notebook

# JupyterLab
jupyter lab

# Specific port
jupyter lab --port=8889
```

## 📊 Template Notebooks

### Data Analysis Template
```python
# Standard imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration
%matplotlib inline
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Random seed for reproducibility
np.random.seed(42)

# Display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
```

### ML Model Template
```python
# ML Libraries
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# Deep Learning
import tensorflow as tf
from tensorflow import keras

# Utilities
import warnings
warnings.filterwarnings('ignore')
```

## 🎨 Visualization Tips

```python
# Set default figure size
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['figure.dpi'] = 100

# Create professional plots
def create_plot(data, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel('X Label', fontsize=12)
    ax.set_ylabel('Y Label', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig, ax
```

## 💡 Useful Magic Commands

```python
# Time a cell
%%time

# Profile a cell
%%prun

# Write cell to file
%%writefile script.py

# Load external script
%load script.py

# Show available magic commands
%lsmagic

# Reload modules automatically
%load_ext autoreload
%autoreload 2
```

## 🔍 Debugging in Notebooks

```python
# Enable interactive debugger
%pdb on

# Use IPython debugger
from IPython.core.debugger import set_trace
set_trace()  # Set breakpoint

# Display full traceback
%xmode Verbose
```

## 📱 Sharing Notebooks

### 1. GitHub
- Clear all outputs before committing
- Use `.gitignore` for large output files
- Add README with notebook descriptions

### 2. nbviewer
- Share read-only version
- URL: `https://nbviewer.org/github/user/repo/blob/main/notebook.ipynb`

### 3. Google Colab
- Upload to Google Drive
- Share with "Anyone with link"
- Enable GPU/TPU if needed

### 4. Export Options
```bash
# Convert to HTML
jupyter nbconvert --to html notebook.ipynb

# Convert to PDF (requires LaTeX)
jupyter nbconvert --to pdf notebook.ipynb

# Convert to Python script
jupyter nbconvert --to script notebook.ipynb
```

## 🚀 Performance Tips

### 1. Memory Management
```python
# Delete large objects
del large_dataframe
import gc
gc.collect()

# Monitor memory
%load_ext memory_profiler
%memit code_to_profile
```

### 2. Parallel Processing
```python
# Use joblib for parallel loops
from joblib import Parallel, delayed

results = Parallel(n_jobs=-1)(
    delayed(function)(i) for i in range(100)
)
```

### 3. Progress Bars
```python
from tqdm.notebook import tqdm

for i in tqdm(range(100)):
    # Your code here
    pass
```

## ✅ Checklist Before Sharing

- [ ] Clear all outputs (or keep only essential ones)
- [ ] Remove sensitive information
- [ ] Test notebook runs from top to bottom
- [ ] Add markdown documentation
- [ ] Include requirements.txt or environment.yml
- [ ] Check file size (GitHub limit: 100MB)

## 📚 Learning Resources

- [Jupyter Documentation](https://jupyter.org/documentation)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- [IPython Documentation](https://ipython.readthedocs.io/)
- [Real Python Jupyter Tutorial](https://realpython.com/jupyter-notebook-introduction/)

---

**Happy coding in Jupyter! 🎉**
