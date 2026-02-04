# Datasets Directory

This directory is for storing datasets used in your machine learning journey.

## 📁 Organization

Organize your datasets by module or project:

```
datasets/
├── module_01/
│   ├── titanic.csv
│   ├── iris.csv
│   └── housing.csv
├── module_03/
│   ├── classification/
│   └── regression/
├── module_05/
│   ├── images/
│   └── sequences/
└── projects/
    ├── capstone/
    └── research/
```

## 📥 Data Sources

### Beginner-Friendly Datasets
1. **[Kaggle Datasets](https://www.kaggle.com/datasets)**
   - Titanic: Survival prediction
   - Iris: Flower classification
   - MNIST: Handwritten digits
   - Housing Prices: Regression

2. **[UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)**
   - Classic ML datasets
   - Well-documented
   - Various domains

3. **[Google Dataset Search](https://datasetsearch.research.google.com/)**
   - Search across repositories
   - Research datasets

### Intermediate Datasets
1. **[CIFAR-10/100](https://www.cs.toronto.edu/~kriz/cifar.html)**
   - Image classification
   - 10 or 100 classes

2. **[ImageNet](https://www.image-net.org/)**
   - Large-scale image dataset
   - 1000+ classes

3. **[IMDB Reviews](https://ai.stanford.edu/~amaas/data/sentiment/)**
   - Sentiment analysis
   - NLP tasks

### Advanced Datasets
1. **[COCO](https://cocodataset.org/)**
   - Object detection
   - Segmentation
   - Keypoint detection

2. **[SQuAD](https://rajpurkar.github.io/SQuAD-explorer/)**
   - Question answering
   - Reading comprehension

3. **[Common Crawl](https://commoncrawl.org/)**
   - Large text corpus
   - NLP research

## 💾 Data Management Best Practices

### 1. Version Control
- Use DVC (Data Version Control) for large datasets
- Track data versions alongside code
- Document data sources and preprocessing

### 2. Storage
```bash
# Install DVC
pip install dvc

# Initialize DVC
dvc init

# Track large files
dvc add datasets/large_dataset.csv
git add datasets/large_dataset.csv.dvc .gitignore
```

### 3. Data Organization
- Keep raw data separate from processed data
- Document preprocessing steps
- Use consistent naming conventions

### 4. Data Privacy
- ⚠️ Never commit sensitive data to Git
- Use `.gitignore` to exclude private data
- Anonymize personal information
- Follow GDPR/privacy regulations

## 📝 Dataset Documentation Template

Create a `README.md` for each dataset:

```markdown
# Dataset Name

## Source
[Link to original source]

## Description
Brief description of the dataset

## Features
- Feature 1: Description
- Feature 2: Description

## Target Variable
Description of what you're predicting

## Size
- Rows: X
- Columns: Y
- File size: Z MB

## Preprocessing
1. Handling missing values
2. Feature engineering
3. Normalization/scaling

## Usage
```python
import pandas as pd
df = pd.read_csv('dataset.csv')
```

## License
Dataset license information
```

## 🔒 .gitignore Recommendations

Add to your `.gitignore`:
```
# Large datasets
*.csv
*.tsv
*.json
*.parquet
*.h5
*.hdf5

# Except small example files
!datasets/examples/*.csv

# Image datasets
*.jpg
*.png
*.jpeg
*.gif

# Compressed files
*.zip
*.tar.gz
*.7z

# DVC files (keep .dvc files, not actual data)
!*.dvc
```

## 🌐 Cloud Storage Options

For large datasets:
1. **Google Drive**: Free 15GB
2. **AWS S3**: Pay per use
3. **Google Cloud Storage**: Free tier + paid
4. **Kaggle**: Built-in dataset hosting
5. **Hugging Face Hub**: ML dataset hosting

## 📊 Example Download Scripts

```python
# download_data.py
import kaggle

# Download from Kaggle
def download_kaggle_dataset(dataset_name, path='./datasets/'):
    kaggle.api.dataset_download_files(
        dataset_name, 
        path=path, 
        unzip=True
    )

# Example usage
if __name__ == '__main__':
    download_kaggle_dataset('titanic')
```

---

**Note**: Always check dataset licenses before using them in your projects!
