# Getting Started with Your ML Journey

Welcome! This guide will help you set up your environment and start learning machine learning.

## 🚀 Quick Start

### 1. Prerequisites

Before starting, ensure you have:
- Python 3.8 or higher installed
- Git installed
- A code editor (VS Code, PyCharm, or similar)
- At least 10GB of free disk space

Check your Python version:
```bash
python --version
# or
python3 --version
```

### 2. Clone or Fork This Repository

If you haven't already:
```bash
git clone https://github.com/owen-6936/ml-journey.git
cd ml-journey
```

### 3. Set Up Virtual Environment

**Important**: Always use a virtual environment to avoid conflicts!

#### On Windows:
```bash
python -m venv ml-env
ml-env\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv ml-env
source ml-env/bin/activate
```

You should see `(ml-env)` in your terminal prompt.

### 4. Install Dependencies

Start with core dependencies:
```bash
pip install --upgrade pip
pip install numpy pandas matplotlib seaborn jupyter scikit-learn
```

For full installation (this may take a while):
```bash
pip install -r requirements.txt
```

**Note**: If you encounter issues with TensorFlow or PyTorch, install them separately:
```bash
# TensorFlow
pip install tensorflow

# PyTorch (visit pytorch.org for your specific system)
pip install torch torchvision
```

### 5. Verify Installation

Create a test script to verify:
```python
# test_setup.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import tensorflow as tf

print("✅ NumPy:", np.__version__)
print("✅ Pandas:", pd.__version__)
print("✅ Scikit-learn:", sklearn.__version__)
print("✅ TensorFlow:", tf.__version__)
print("\n🎉 All core libraries installed successfully!")
```

Run it:
```bash
python test_setup.py
```

### 6. Set Up Jupyter Notebook

```bash
# Install Jupyter if not already installed
pip install jupyter

# Launch Jupyter Notebook
jupyter notebook

# Or use JupyterLab (modern interface)
jupyter lab
```

Your browser should open automatically. Navigate to the `notebooks/` directory.

## 📚 Learning Path

### Week 1-2: Module 1 - Python & Basics
Start here: [Module 1 README](modules/module_01_intro_python/README.md)

1. Create your first notebook in `notebooks/module_01/`
2. Follow along with exercises
3. Practice with small datasets
4. Complete the assignments

### Week 3-4: Module 2 - Math Foundations
Continue to: [Module 2 README](modules/module_02_math_foundations/README.md)

1. Review linear algebra concepts
2. Implement mathematical operations
3. Understand calculus for ML
4. Practice probability and statistics

### Week 5+: Continue Through Modules
Follow the structured path through all modules!

## 🛠️ Development Setup

### Recommended VS Code Extensions
- Python (Microsoft)
- Jupyter (Microsoft)
- Pylance
- GitLens
- Black Formatter

### Recommended Settings

Create `.vscode/settings.json`:
```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.defaultInterpreterPath": "./ml-env/bin/python"
}
```

## 🔑 Setting Up Gemini 3 API (Module 6)

You'll need this for Module 6. Get started early!

1. Go to [Google AI Studio](https://makersuite.google.com/)
2. Sign in with your Google account
3. Create an API key
4. Store it securely

Create a `.env` file (never commit this!):
```bash
GEMINI_API_KEY=your_api_key_here
```

Add to `.gitignore`:
```bash
echo ".env" >> .gitignore
```

Use in your code:
```python
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
```

## 📊 GPU Setup (Optional but Recommended)

For deep learning (Module 5), GPU acceleration is highly recommended.

### Option 1: Use Google Colab (Free!)
- Go to [Google Colab](https://colab.research.google.com/)
- Runtime > Change runtime type > GPU
- Upload your notebooks
- Free GPU access!

### Option 2: Local GPU Setup
If you have an NVIDIA GPU:
```bash
# Install CUDA-enabled TensorFlow
pip install tensorflow[and-cuda]

# Or for PyTorch, visit pytorch.org for your specific CUDA version
```

### Option 3: Cloud Platforms
- AWS SageMaker
- Google Cloud AI Platform
- Azure ML
- Kaggle Kernels (free GPU)

## 📁 Organizing Your Work

### Daily Workflow
1. Activate virtual environment
2. Navigate to appropriate module
3. Create or open notebooks
4. Code, experiment, learn!
5. Commit your changes

### Git Workflow
```bash
# Check status
git status

# Add changes
git add .

# Commit
git commit -m "Completed Module 1 Week 1 exercises"

# Push to your fork
git push origin main
```

## 📖 Additional Resources

### Online Learning
- [Kaggle Learn](https://www.kaggle.com/learn) - Free micro-courses
- [Fast.ai](https://www.fast.ai/) - Practical deep learning
- [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)

### Practice Platforms
- [Kaggle](https://www.kaggle.com/) - Competitions and datasets
- [LeetCode](https://leetcode.com/) - Coding practice
- [HackerRank](https://www.hackerrank.com/domains/ai) - ML challenges

### Communities
- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/)
- [r/learnmachinelearning](https://www.reddit.com/r/learnmachinelearning/)
- [Kaggle Forums](https://www.kaggle.com/discussion)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/machine-learning)

## 🆘 Troubleshooting

### Common Issues

**Problem**: `ImportError: No module named 'numpy'`
**Solution**: Install the package: `pip install numpy`

**Problem**: Jupyter kernel keeps dying
**Solution**: Reduce batch size or use smaller datasets

**Problem**: Out of memory errors
**Solution**: 
- Use smaller datasets initially
- Reduce batch size
- Use Google Colab for free GPU/RAM

**Problem**: TensorFlow installation issues
**Solution**: Try installing specific version: `pip install tensorflow==2.13.0`

### Getting Help
1. Check the module README files
2. Search Stack Overflow
3. Ask in ML communities
4. Check package documentation
5. Create an issue in this repo (if it's a structural problem)

## ✅ Initial Setup Checklist

- [ ] Python 3.8+ installed
- [ ] Git installed
- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] Core packages installed (numpy, pandas, matplotlib)
- [ ] Jupyter Notebook working
- [ ] Can run test script successfully
- [ ] Read Module 1 README
- [ ] Created first notebook

## 🎯 Learning Tips

1. **Practice Daily**: Even 30 minutes helps
2. **Code Everything**: Don't just read, implement
3. **Start Simple**: Master basics before advanced topics
4. **Build Projects**: Apply what you learn
5. **Join Community**: Learn from others
6. **Be Patient**: ML has a learning curve
7. **Document**: Keep notes of what you learn
8. **Review**: Regularly revisit previous modules

## 🚀 Next Steps

1. ✅ Complete this setup
2. 📖 Read the main [README.md](README.md)
3. 🎓 Start [Module 1](modules/module_01_intro_python/README.md)
4. 💻 Create your first notebook
5. 🏃 Begin your ML journey!

---

**You're all set! Happy learning! 🎉**

If you have questions, refer to the module READMEs or search online communities. You've got this! 💪
