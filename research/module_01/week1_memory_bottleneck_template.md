# Week 1 Research Assignment: The Memory Bottleneck

**Author**: [Your Name]  
**Date**: [Today's Date]  
**Module**: 1 - Python & NumPy Fundamentals

---

## The Hotel vs. Scattered Houses Analogy

### NumPy Arrays: The Hotel 🏨

[Explain how NumPy arrays store data in contiguous memory]

**Visual Representation**:
```
Memory Address: [1000][1001][1002][1003][1004][1005]
Array Data:     [  10][  20][  30][  40][  50][  60]
                  ↑
                  Single block - CPU can fetch all at once!
```

### Python Lists: Scattered Houses 🏘️

[Explain how Python lists store references to scattered objects]

**Visual Representation**:
```
List (References):  [→1000][→2500][→1200][→3000][→1800]
Actual Data:         [10]    [20]    [30]    [40]    [50]
                      ↑       ↑       ↑       ↑       ↑
                   Different memory locations - CPU must make individual trips!
```

---

## SIMD: Single Instruction, Multiple Data

### What is SIMD?

[Your explanation here]

SIMD is a technique where:
- **Single Instruction**: One CPU operation (e.g., "add")
- **Multiple Data**: Applied to multiple data elements simultaneously

### How NumPy Uses SIMD

```python
# Without SIMD (Python loop):
for i in range(len(arr)):
    result[i] = arr1[i] + arr2[i]  # Each addition is a separate instruction

# With SIMD (NumPy):
result = arr1 + arr2  # Single instruction processes entire arrays!
```

**CPU Perspective**:
```
Without SIMD:          With SIMD:
Instruction 1: a[0]+b[0]   Instruction 1: [a[0]+b[0], a[1]+b[1], a[2]+b[2], a[3]+b[3]]
Instruction 2: a[1]+b[1]   ↑
Instruction 3: a[2]+b[2]   One instruction, four operations!
Instruction 4: a[3]+b[3]
```

---

## Why This Matters for Machine Learning

### Performance Impact

1. **Training Speed**: [Your explanation]
2. **Real-time Inference**: [Your explanation]
3. **Scaling to Large Datasets**: [Your explanation]

### Practical Examples

**Example 1: Image Processing**
- An image is 1920x1080 pixels = 2,073,600 numbers
- Processing each pixel individually (loop): ~2 million operations
- Processing with vectorization (NumPy): Single operation on the entire array!

**Example 2: Neural Networks**
- Forward pass through a layer with 1000 neurons
- Matrix multiplication with contiguous arrays: Fast!
- Element-by-element loops: Extremely slow!

---

## Memory Layout: Contiguous vs. Non-Contiguous

### What is Contiguous Memory?

[Your explanation here]

**Key Points**:
- Elements stored in adjacent memory locations
- Can be accessed as a continuous block
- Enables cache-friendly access patterns

### Why It Matters

1. **Cache Efficiency**: [Explain CPU cache]
2. **Prefetching**: [Explain how CPU predicts next memory access]
3. **SIMD Operations**: [Explain why SIMD requires contiguous data]

### Demonstrating the Difference

```python
import numpy as np
import time

# Contiguous array
arr_contiguous = np.arange(1000000)
print(f"Is contiguous: {arr_contiguous.flags['C_CONTIGUOUS']}")

# Non-contiguous array (view with stride)
arr_sliced = arr_contiguous[::2]  # Every second element
print(f"Is contiguous: {arr_sliced.flags['C_CONTIGUOUS']}")

# Performance comparison
# [Add your benchmarking code here]
```

---

## Conclusion

**Key Takeaways**:
1. [Your first key point]
2. [Your second key point]
3. [Your third key point]

**Why I Should Care as a JS/TS Developer**:
[Your reflection on how this applies to your background and goals]

**How This Relates to Module 2**:
[Explain how understanding memory layout will help with linear algebra and gradient descent]

---

## References

1. Pedro Domingos - "A Few Useful Things to Know About Machine Learning"
2. NumPy Documentation - Internal Memory Layout
3. [Computerphile Video] - Why NumPy is Faster
4. [3Blue1Brown] - Linear Algebra Series
5. [Add any other sources you used]

---

## Personal Notes & Questions

[Keep track of questions that arise during your research]
[Note connections to concepts you already know from JS/TS]
[Ideas for future exploration]
