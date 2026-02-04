# Research Papers & Notes

This directory contains research papers, summaries, and implementation notes.

## 📚 Organization

```
research/
├── module_01/                  # Module 1 research assignments
│   └── week1_memory_bottleneck_template.md
├── module_02/                  # Module 2 research
├── papers/
│   ├── foundational/
│   ├── computer_vision/
│   ├── nlp/
│   └── recent/
├── summaries/
│   └── paper_notes.md
├── implementations/
│   └── paper_code/
└── reading_list.md
```

## 📝 Module Research Assignments

As part of this curriculum, you'll complete research assignments that deepen your understanding of core concepts. These are not just reading exercises - you'll write detailed explanations in your own words to solidify learning.

### Module 1: Week 1 - The Memory Bottleneck

**Assignment**: Explain why contiguous memory is critical for ML performance
- Use the template in `module_01/week1_memory_bottleneck_template.md`
- Create your completed version as `module_01/week1_memory_bottleneck.md`
- Include the "Hotel vs Scattered Houses" analogy
- Research and explain SIMD operations
- This prepares you for understanding why NumPy is essential

**Resources**:
1. Pedro Domingos - "A Few Useful Things to Know About Machine Learning"
2. NumPy Documentation - Internal Memory Layout
3. Computerphile videos on memory and performance

**Deliverable**: 1-2 page markdown document with diagrams and code examples

## 🎯 How to Read Research Papers

### Three-Pass Method

#### First Pass (5-10 minutes)
- Read title, abstract, and introduction
- Read section headings
- Read conclusion
- Glance at references

**Goal**: Get the gist of the paper

#### Second Pass (1 hour)
- Read carefully but skip proofs
- Note key points and figures
- Mark references to read

**Goal**: Understand main contributions

#### Third Pass (4-5 hours)
- Read thoroughly, understand every detail
- Re-implement key algorithms
- Compare with related work

**Goal**: Deep understanding

## 📝 Paper Summary Template

Create a markdown file for each paper:

```markdown
# [Paper Title]

## Metadata
- **Authors**: [Author names]
- **Year**: [Year]
- **Conference/Journal**: [Venue]
- **Link**: [ArXiv or paper link]
- **Code**: [GitHub repo if available]

## Problem Statement
What problem does this paper address?

## Key Contributions
1. Contribution 1
2. Contribution 2
3. Contribution 3

## Methodology
How do they solve the problem?

### Architecture/Algorithm
- Describe the model/algorithm
- Key innovations

### Experiments
- Datasets used
- Baselines
- Evaluation metrics

## Results
- Main findings
- Performance improvements
- Ablation studies

## Strengths
- What did they do well?
- Novel ideas?

## Limitations
- What could be improved?
- Assumptions made?

## Personal Notes
- How can I use this?
- Questions for further research
- Ideas for improvements

## Implementation Notes
- Key equations
- Hyperparameters
- Training details

## Related Work
- Similar papers
- Follow-up research
```

## 📖 Essential ML Papers (Reading List)

### Foundational Papers

#### Classical Machine Learning
1. **"A Few Useful Things to Know About Machine Learning"** - Pedro Domingos (2012)
   - Great overview of ML principles

2. **"Random Forests"** - Leo Breiman (2001)
   - Introduction to ensemble methods

3. **"Support-Vector Networks"** - Cortes & Vapnik (1995)
   - Original SVM paper

#### Deep Learning Foundations
1. **"Deep Learning"** - LeCun, Bengio, Hinton (2015)
   - Nature paper overview

2. **"ImageNet Classification with Deep CNNs"** - Krizhevsky et al. (2012)
   - AlexNet, started deep learning revolution

3. **"Deep Residual Learning for Image Recognition"** - He et al. (2015)
   - ResNet architecture

### Computer Vision

1. **"You Only Look Once: Unified Real-Time Object Detection"** - Redmon et al. (2016)
   - YOLO object detection

2. **"Mask R-CNN"** - He et al. (2017)
   - Instance segmentation

3. **"An Image is Worth 16x16 Words"** - Dosovitskiy et al. (2020)
   - Vision Transformers (ViT)

### Natural Language Processing

1. **"Attention Is All You Need"** - Vaswani et al. (2017)
   - Transformer architecture

2. **"BERT: Pre-training of Deep Bidirectional Transformers"** - Devlin et al. (2018)
   - BERT model

3. **"Language Models are Few-Shot Learners"** - Brown et al. (2020)
   - GPT-3

4. **"Improving Language Understanding by Generative Pre-Training"** - Radford et al. (2018)
   - GPT

### Generative Models

1. **"Generative Adversarial Networks"** - Goodfellow et al. (2014)
   - Original GAN paper

2. **"Auto-Encoding Variational Bayes"** - Kingma & Welling (2013)
   - VAE

3. **"Denoising Diffusion Probabilistic Models"** - Ho et al. (2020)
   - Diffusion models

### Advanced Topics

1. **"Retrieval-Augmented Generation for Knowledge-Intensive Tasks"** - Lewis et al. (2020)
   - RAG approach

2. **"LoRA: Low-Rank Adaptation of Large Language Models"** - Hu et al. (2021)
   - Efficient fine-tuning

3. **"Constitutional AI: Harmlessness from AI Feedback"** - Bai et al. (2022)
   - AI alignment

## 🔍 Where to Find Papers

### Primary Sources
1. **[arXiv.org](https://arxiv.org/)**
   - Preprint server
   - Categories: cs.LG, cs.CV, cs.CL, cs.AI

2. **[Papers With Code](https://paperswithcode.com/)**
   - Papers + code implementations
   - Benchmarks and leaderboards

3. **[Google Scholar](https://scholar.google.com/)**
   - Search and citations
   - Follow authors

### Conferences
- **NeurIPS**: Neural Information Processing Systems
- **ICML**: International Conference on Machine Learning
- **ICLR**: International Conference on Learning Representations
- **CVPR**: Computer Vision and Pattern Recognition
- **ACL**: Association for Computational Linguistics
- **AAAI**: Association for Advancement of Artificial Intelligence

### Journals
- Journal of Machine Learning Research (JMLR)
- IEEE Transactions on Pattern Analysis and Machine Intelligence
- Nature Machine Intelligence
- Machine Learning journal

## 📱 Tools for Paper Management

### Reference Managers
1. **Zotero** (Free)
   - Open source
   - Browser integration
   - PDF management

2. **Mendeley** (Free)
   - PDF annotation
   - Citation management

3. **Notion** (Free/Paid)
   - Custom databases
   - Note-taking

### Paper Reading Apps
- **Connected Papers**: Visualize paper relationships
- **Semantic Scholar**: AI-powered search
- **ResearchGate**: Academic social network

## 💻 Implementation Strategy

### 1. Choose a Paper
- Start with well-known papers
- Has existing implementations to reference
- Matches your skill level

### 2. Understand Thoroughly
- Read multiple times
- Understand all equations
- Clarify uncertainties

### 3. Implementation Plan
```python
# 1. Implement data loading
def load_data():
    pass

# 2. Implement model architecture
class PaperModel:
    pass

# 3. Implement training loop
def train():
    pass

# 4. Implement evaluation
def evaluate():
    pass

# 5. Reproduce results
def reproduce_table_1():
    pass
```

### 4. Compare Results
- Your implementation vs paper results
- Identify discrepancies
- Debug and iterate

### 5. Document
- Write detailed README
- Document differences
- Share learnings

## ✅ Paper Review Checklist

When reviewing a paper:
- [ ] Problem is clearly defined
- [ ] Method is novel/interesting
- [ ] Experiments are thorough
- [ ] Results are convincing
- [ ] Code is available
- [ ] Reproducible
- [ ] Limitations discussed
- [ ] Ethical considerations addressed

## 🌟 Stay Current

### Newsletters
- **The Batch** (DeepLearning.AI)
- **Import AI** (Jack Clark)
- **Papers with Code Newsletter**
- **Hugging Face Newsletter**

### Social Media
- Follow researchers on Twitter/X
- Join ML Discord servers
- Reddit: r/MachineLearning
- LinkedIn ML groups

### Podcasts
- **TWIML** (This Week in Machine Learning)
- **Lex Fridman Podcast**
- **The AI Podcast** (NVIDIA)

## 📊 Tracking Progress

Create a reading log:

| Date | Paper Title | Status | Notes |
|------|-------------|---------|-------|
| 2024-01-15 | Attention Is All You Need | ✅ Read | Implemented transformer |
| 2024-01-20 | BERT | 📖 Reading | In progress |
| 2024-01-25 | ResNet | 📋 Todo | Next up |

## 🎓 Advanced Reading Topics

Once comfortable with basics:
- Reinforcement Learning (Sutton & Barto)
- Graph Neural Networks
- Meta-learning
- Federated Learning
- Explainable AI
- AI Safety and Alignment

---

**Remember**: You don't need to understand every paper completely. Focus on papers relevant to your interests and goals!
