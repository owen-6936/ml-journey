# Module 4: Unsupervised Learning

**Duration**: Weeks 9-10  
**Difficulty**: Intermediate

## 📋 Overview

Unsupervised learning discovers hidden patterns in data without labeled outputs. This module covers clustering algorithms and dimensionality reduction techniques essential for data exploration and preprocessing.

## 🎯 Learning Objectives

By the end of this module, you will:
- Implement and apply clustering algorithms
- Understand dimensionality reduction techniques
- Perform feature extraction and selection
- Apply unsupervised learning to real-world problems
- Evaluate unsupervised learning results

## 📚 Week 9: Clustering Algorithms

### Topics Covered
1. **K-Means Clustering**
   - K-means algorithm
   - Choosing K (elbow method, silhouette score)
   - K-means++ initialization
   - Mini-batch K-means

2. **Hierarchical Clustering**
   - Agglomerative clustering
   - Dendrogram interpretation
   - Linkage methods (single, complete, average, Ward)
   - Cutting dendrograms

3. **Other Clustering Methods**
   - DBSCAN (density-based)
   - Gaussian Mixture Models (GMM)
   - Mean Shift
   - Spectral clustering

4. **Clustering Evaluation**
   - Silhouette coefficient
   - Davies-Bouldin index
   - Calinski-Harabasz index
   - Internal vs external validation

### Exercises
- [ ] Exercise 9.1: Implement K-means from scratch
- [ ] Exercise 9.2: Hierarchical clustering with dendrograms
- [ ] Exercise 9.3: DBSCAN for anomaly detection
- [ ] Exercise 9.4: Compare clustering algorithms

### Code Implementation

```python
# File: exercises/week9_kmeans.py
class KMeans:
    def __init__(self, n_clusters=3, max_iters=100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.centroids = None
        
    def fit(self, X):
        # Initialize centroids
        # Assign points to clusters
        # Update centroids
        # Repeat until convergence
        pass
    
    def predict(self, X):
        # Assign new points to nearest centroid
        pass
```

### Resources
- [StatQuest: K-means](https://www.youtube.com/watch?v=4b5d3muPQmA)
- [StatQuest: Hierarchical Clustering](https://www.youtube.com/watch?v=7xHsRkOdVwo)
- Scikit-learn Clustering Documentation

### Project
**Customer Segmentation**: Segment customers based on purchasing behavior for targeted marketing.

## 📚 Week 10: Dimensionality Reduction

### Topics Covered
1. **Principal Component Analysis (PCA)**
   - Covariance matrix
   - Eigenvalue decomposition
   - Variance explained
   - Choosing number of components
   - PCA for visualization

2. **t-SNE (t-Distributed Stochastic Neighbor Embedding)**
   - High-dimensional visualization
   - Perplexity parameter
   - Limitations and best practices

3. **Other Techniques**
   - Linear Discriminant Analysis (LDA)
   - Autoencoders (preview to deep learning)
   - UMAP (Uniform Manifold Approximation)
   - Factor Analysis

4. **Feature Selection**
   - Filter methods (correlation, mutual information)
   - Wrapper methods (RFE)
   - Embedded methods (Lasso, tree importance)

### Exercises
- [ ] Exercise 10.1: Implement PCA from scratch
- [ ] Exercise 10.2: Visualize high-dimensional data with t-SNE
- [ ] Exercise 10.3: Feature selection comparison
- [ ] Exercise 10.4: Apply PCA before supervised learning

### Code Implementation

```python
# File: exercises/week10_pca.py
class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None
        
    def fit(self, X):
        # Center the data
        # Compute covariance matrix
        # Find eigenvalues and eigenvectors
        # Select top n_components
        pass
    
    def transform(self, X):
        # Project data onto principal components
        pass
```

### Resources
- [StatQuest: PCA](https://www.youtube.com/watch?v=FgakZw6K1QQ)
- [Distill.pub: How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/)
- Scikit-learn Dimensionality Reduction

### Project
**High-Dimensional Data Visualization**: Visualize a complex dataset (e.g., MNIST, gene expression data).

## 🔧 Required Libraries

```bash
pip install umap-learn hdbscan plotly
```

## 📝 Assignments

### Assignment 1: Clustering Analysis (Week 9)
Perform comprehensive clustering analysis:
1. Apply at least 3 clustering algorithms
2. Determine optimal number of clusters
3. Evaluate and compare results
4. Visualize clusters
5. Interpret business meaning

**Dataset**: Customer, genomic, or image data

### Assignment 2: Dimensionality Reduction Pipeline (Week 10)
Create a complete pipeline:
1. Start with high-dimensional data (100+ features)
2. Apply multiple dimensionality reduction techniques
3. Compare visualization quality
4. Use reduced features in supervised learning
5. Compare performance with/without reduction

**Due**: End of Week 10

## 📖 Research & Reading

- **Paper**: "A Tutorial on Principal Component Analysis" by Jonathon Shlens
- **Paper**: "Visualizing Data using t-SNE" by van der Maaten & Hinton
- **Article**: "The Unreasonable Effectiveness of PCA"

## 💡 Practical Tips

### When to Use Each Algorithm

**K-Means**:
- Well-separated, spherical clusters
- Know approximate number of clusters
- Fast computation needed

**Hierarchical**:
- Don't know number of clusters
- Need cluster hierarchy
- Small to medium datasets

**DBSCAN**:
- Arbitrary-shaped clusters
- Outlier detection needed
- Don't know number of clusters

**PCA**:
- Linear relationships
- Visualization
- Preprocessing for supervised learning

**t-SNE**:
- Visualization only (2D/3D)
- Non-linear relationships
- Smaller datasets (< 10k points)

## 🎯 Real-World Applications

1. **Customer Segmentation**: Group customers for marketing
2. **Image Compression**: Reduce image dimensions
3. **Anomaly Detection**: Find outliers in data
4. **Document Clustering**: Group similar documents
5. **Gene Expression Analysis**: Identify cell types
6. **Recommender Systems**: User/item grouping

## ✅ Module Completion Checklist

- [ ] Implemented K-means from scratch
- [ ] Implemented PCA from scratch
- [ ] Understand hierarchical clustering
- [ ] Can use DBSCAN for anomaly detection
- [ ] Master t-SNE for visualization
- [ ] Can evaluate clustering quality
- [ ] Completed all projects
- [ ] Finished both assignments

## 🎓 Capstone Project: Unsupervised Learning Pipeline

Create a complete unsupervised learning analysis:
1. Choose a complex, unlabeled dataset
2. Perform EDA
3. Apply clustering (compare multiple algorithms)
4. Apply dimensionality reduction
5. Visualize results
6. Extract meaningful insights
7. Create a detailed report with visualizations

Suggested datasets:
- Credit card transactions (anomaly detection)
- Customer behavior data (segmentation)
- Gene expression data (cell type discovery)
- Image datasets (compression, clustering)

## ➡️ Next Steps

Once you complete this module, proceed to [Module 5: Deep Learning & Neural Networks](../module_05_deep_learning/README.md)

---

**Notes**: Unsupervised learning is often exploratory. Be creative with your analysis and focus on extracting meaningful insights.
