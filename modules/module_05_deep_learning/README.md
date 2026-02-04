# Module 5: Deep Learning & Neural Networks

**Duration**: Weeks 11-14  
**Difficulty**: Advanced

## 📋 Overview

Deep learning has revolutionized AI and machine learning. This module covers neural networks from basics to advanced architectures including CNNs, RNNs, and transfer learning.

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand neural network fundamentals
- Implement backpropagation from scratch
- Build and train CNNs for computer vision
- Use RNNs and LSTMs for sequential data
- Apply transfer learning
- Use TensorFlow/Keras and PyTorch

## 📚 Week 11: Neural Network Basics & Backpropagation

### Topics Covered
1. **Neural Network Fundamentals**
   - Perceptron and multi-layer perceptron (MLP)
   - Activation functions (ReLU, Sigmoid, Tanh, Softmax)
   - Forward propagation
   - Loss functions (MSE, Cross-Entropy)

2. **Backpropagation**
   - Chain rule in neural networks
   - Gradient computation
   - Weight updates
   - Computational graphs

3. **Training Neural Networks**
   - Batch normalization
   - Dropout for regularization
   - Learning rate schedules
   - Optimization algorithms (SGD, Adam, RMSprop)

4. **Implementation Frameworks**
   - Introduction to TensorFlow/Keras
   - Introduction to PyTorch
   - Choosing between frameworks

### Exercises
- [ ] Exercise 11.1: Implement a neural network from scratch
- [ ] Exercise 11.2: Backpropagation by hand (small network)
- [ ] Exercise 11.3: Build MLP with Keras
- [ ] Exercise 11.4: Compare activation functions

### Code Implementation

```python
# File: exercises/week11_neural_network.py
import numpy as np

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.weights = []
        self.biases = []
        self._initialize_parameters()
    
    def _initialize_parameters(self):
        # Initialize weights and biases
        pass
    
    def forward(self, X):
        # Forward propagation
        pass
    
    def backward(self, X, y):
        # Backpropagation
        pass
    
    def train(self, X, y, epochs, learning_rate):
        # Training loop
        pass
```

### Resources
- [3Blue1Brown: Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- [Deep Learning Specialization (Coursera)](https://www.coursera.org/specializations/deep-learning)
- TensorFlow Tutorials: [tensorflow.org](https://www.tensorflow.org/tutorials)
- PyTorch Tutorials: [pytorch.org](https://pytorch.org/tutorials/)

### Project
**MNIST Digit Classification**: Build a neural network to classify handwritten digits.

## 📚 Week 12: Convolutional Neural Networks (CNNs)

### Topics Covered
1. **CNN Fundamentals**
   - Convolution operation
   - Filters/kernels
   - Stride and padding
   - Pooling layers (Max, Average)

2. **CNN Architectures**
   - LeNet-5
   - AlexNet
   - VGGNet
   - ResNet (residual connections)
   - Modern architectures (EfficientNet, Vision Transformers)

3. **CNN Applications**
   - Image classification
   - Object detection
   - Image segmentation
   - Style transfer

4. **Best Practices**
   - Data augmentation
   - Batch normalization in CNNs
   - Transfer learning preparation

### Exercises
- [ ] Exercise 12.1: Implement convolution from scratch
- [ ] Exercise 12.2: Build a simple CNN
- [ ] Exercise 12.3: Data augmentation techniques
- [ ] Exercise 12.4: Visualize CNN filters and activations

### Code Implementation

```python
# File: exercises/week12_cnn.py
from tensorflow import keras
from tensorflow.keras import layers

def create_cnn_model(input_shape, num_classes):
    model = keras.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model
```

### Resources
- [CS231n: CNNs for Visual Recognition](http://cs231n.stanford.edu/)
- [Deep Learning for Computer Vision (fast.ai)](https://course.fast.ai/)
- Keras CNN Examples

### Project
**Image Classification**: Build a CNN for CIFAR-10 or your own image dataset.

## 📚 Week 13: Recurrent Neural Networks (RNNs) & LSTMs

### Topics Covered
1. **Sequence Modeling**
   - Sequential data characteristics
   - Temporal dependencies
   - Sequence-to-sequence problems

2. **RNN Architecture**
   - Vanilla RNN
   - Vanishing/exploding gradients
   - Backpropagation through time (BPTT)

3. **Advanced RNN Variants**
   - Long Short-Term Memory (LSTM)
   - Gated Recurrent Unit (GRU)
   - Bidirectional RNNs
   - Attention mechanism

4. **Applications**
   - Time series prediction
   - Natural language processing
   - Speech recognition
   - Video analysis

### Exercises
- [ ] Exercise 13.1: Implement simple RNN
- [ ] Exercise 13.2: LSTM for sequence prediction
- [ ] Exercise 13.3: Text generation with RNN
- [ ] Exercise 13.4: Time series forecasting

### Code Implementation

```python
# File: exercises/week13_rnn.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding

def create_lstm_model(vocab_size, embedding_dim, max_length):
    model = Sequential([
        Embedding(vocab_size, embedding_dim, input_length=max_length),
        LSTM(128, return_sequences=True),
        LSTM(64),
        Dense(64, activation='relu'),
        Dense(vocab_size, activation='softmax')
    ])
    return model
```

### Resources
- [Understanding LSTM Networks (Colah's Blog)](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [The Unreasonable Effectiveness of RNNs](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- TensorFlow RNN Guide

### Project
**Stock Price Prediction** or **Text Generation**: Use LSTM for sequential data prediction.

## 📚 Week 14: Transfer Learning & Fine-Tuning

### Topics Covered
1. **Transfer Learning Concepts**
   - Pre-trained models
   - Feature extraction
   - Fine-tuning strategies
   - When to use transfer learning

2. **Popular Pre-trained Models**
   - Image: ResNet, VGG, InceptionV3, EfficientNet
   - Text: BERT, GPT, Word2Vec, GloVe
   - Multi-modal: CLIP

3. **Fine-Tuning Techniques**
   - Freezing layers
   - Layer-wise learning rates
   - Progressive unfreezing
   - Domain adaptation

4. **Practical Applications**
   - Custom image classification
   - Object detection (YOLO, Faster R-CNN)
   - Semantic segmentation
   - NLP tasks

### Exercises
- [ ] Exercise 14.1: Use pre-trained ResNet for image classification
- [ ] Exercise 14.2: Fine-tune BERT for text classification
- [ ] Exercise 14.3: Feature extraction vs fine-tuning comparison
- [ ] Exercise 14.4: Build a custom object detector

### Code Implementation

```python
# File: exercises/week14_transfer_learning.py
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D

def create_transfer_model(num_classes):
    # Load pre-trained model
    base_model = ResNet50(weights='imagenet', include_top=False)
    
    # Freeze base model layers
    base_model.trainable = False
    
    # Add custom layers
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    
    model = Model(inputs=base_model.input, outputs=predictions)
    return model
```

### Resources
- [Transfer Learning Guide (TensorFlow)](https://www.tensorflow.org/tutorials/images/transfer_learning)
- [CS231n Transfer Learning Notes](http://cs231n.github.io/transfer-learning/)
- Hugging Face Transformers Library

### Project
**Custom Image Classifier**: Use transfer learning to build a classifier for your own image dataset.

## 🔧 Required Libraries

```bash
# TensorFlow/Keras
pip install tensorflow keras

# PyTorch (alternative)
pip install torch torchvision torchaudio

# Additional tools
pip install tensorboard opencv-python pillow
```

## 📝 Major Assignments

### Assignment 1: Neural Network from Scratch (Week 11)
Implement a complete neural network library:
1. Support multiple layers
2. Multiple activation functions
3. Backpropagation
4. Different optimizers
5. Train on real dataset
6. Compare with Keras implementation

### Assignment 2: Deep Learning Competition (Weeks 12-14)
Participate in a computer vision or NLP competition:
1. Choose a Kaggle competition or dataset
2. Experiment with different architectures
3. Apply transfer learning
4. Optimize hyperparameters
5. Create ensemble models
6. Document your approach

**Due**: End of Week 14

## 📖 Research & Reading

- **Paper**: "ImageNet Classification with Deep CNNs" (AlexNet)
- **Paper**: "Deep Residual Learning for Image Recognition" (ResNet)
- **Paper**: "Attention Is All You Need" (Transformers)
- **Paper**: "BERT: Pre-training of Deep Bidirectional Transformers"
- **Book**: "Deep Learning" by Goodfellow, Bengio, and Courville

## 💡 Training Tips

1. **Start Simple**: Begin with small models, then scale up
2. **Monitor Training**: Use TensorBoard for visualization
3. **Regularization**: Use dropout, batch norm, data augmentation
4. **Learning Rate**: Critical hyperparameter, try different schedules
5. **GPU Usage**: Deep learning requires GPU for efficiency
6. **Debugging**: Check gradients, visualize activations

## 🎯 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Overfitting | More data, dropout, regularization |
| Underfitting | Bigger model, more training, better features |
| Slow training | Better optimization, learning rate tuning, GPU |
| Vanishing gradients | ReLU, batch norm, residual connections |
| Exploding gradients | Gradient clipping, better initialization |

## ✅ Module Completion Checklist

- [ ] Implemented neural network from scratch
- [ ] Understand backpropagation deeply
- [ ] Built and trained CNNs
- [ ] Worked with RNNs/LSTMs
- [ ] Applied transfer learning successfully
- [ ] Comfortable with TensorFlow/Keras or PyTorch
- [ ] Completed all projects
- [ ] Finished both assignments

## 🎓 Capstone: Deep Learning Project

Build a complete deep learning application:
1. Define a challenging problem (computer vision or NLP)
2. Collect or find a suitable dataset
3. Design and implement architecture
4. Train with proper validation
5. Evaluate thoroughly
6. Deploy the model (web app or API)
7. Create comprehensive documentation

## ➡️ Next Steps

Once you complete this module, proceed to [Module 6: Advanced Topics & Gemini 3 Integration](../module_06_advanced_topics/README.md)

---

**Notes**: Deep learning requires significant computational resources. Consider using Google Colab (free GPU) or Kaggle Kernels for training.
