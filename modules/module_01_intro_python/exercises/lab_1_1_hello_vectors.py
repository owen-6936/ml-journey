"""
Lab 1.1: Hello Vectors - Understanding Memory and Performance
Module 1, Week 1

This lab demonstrates the practical impact of vectorization and contiguous memory.
You'll see firsthand why NumPy is essential for machine learning.
"""

import numpy as np
import time
import sys

def lab_1_vector_creation():
    """
    Part 1: Create and explore vectors
    """
    print("=" * 70)
    print("LAB 1.1 - Part 1: Vector Creation")
    print("=" * 70)
    
    # Create two large arrays
    size = 100_000
    print(f"\nCreating two arrays of size {size:,}...")
    
    arr1 = np.random.randint(0, 100, size=size)
    arr2 = np.random.randint(0, 100, size=size)
    
    print(f"✓ arr1 shape: {arr1.shape}")
    print(f"✓ arr2 shape: {arr2.shape}")
    print(f"✓ Data type: {arr1.dtype}")
    
    # Check memory properties
    print(f"\n📊 Memory Properties:")
    print(f"   Is C-contiguous (arr1): {arr1.flags['C_CONTIGUOUS']}")
    print(f"   Is C-contiguous (arr2): {arr2.flags['C_CONTIGUOUS']}")
    print(f"   Memory usage (arr1): {arr1.nbytes / 1024:.2f} KB")
    print(f"   Strides (arr1): {arr1.strides}")
    
    return arr1, arr2

def lab_2_benchmark_addition(arr1, arr2):
    """
    Part 2: Benchmark Python loop vs NumPy vectorization
    This is the core of understanding why we use NumPy!
    """
    print("\n" + "=" * 70)
    print("LAB 1.1 - Part 2: Performance Benchmark")
    print("=" * 70)
    
    print("\n🐢 Method 1: Python for loop (like JavaScript)")
    print("   Processing each element individually...")
    
    # Method 1: Python loop
    start = time.time()
    result_loop = []
    for i in range(len(arr1)):
        result_loop.append(arr1[i] + arr2[i])
    loop_time = time.time() - start
    
    print(f"   Time: {loop_time:.6f} seconds")
    
    print("\n🚀 Method 2: NumPy vectorization")
    print("   Processing entire array in one operation...")
    
    # Method 2: NumPy
    start = time.time()
    result_numpy = arr1 + arr2
    numpy_time = time.time() - start
    
    print(f"   Time: {numpy_time:.6f} seconds")
    
    # Calculate speedup
    speedup = loop_time / numpy_time
    
    print("\n" + "=" * 70)
    print(f"📈 RESULTS:")
    print(f"   Loop:  {loop_time:.6f}s")
    print(f"   NumPy: {numpy_time:.6f}s")
    print(f"   Speedup: {speedup:.1f}x FASTER! 🎯")
    print("=" * 70)
    
    # Verify results are the same
    print(f"\n✓ Results match: {np.array_equal(result_loop, result_numpy)}")
    
    return result_numpy

def lab_3_dot_product(arr1, arr2):
    """
    Part 3: The Dot Product - Geometric Meaning
    """
    print("\n" + "=" * 70)
    print("LAB 1.1 - Part 3: The Dot Product")
    print("=" * 70)
    
    # Use smaller arrays for visualization
    v1 = np.array([3, 4])
    v2 = np.array([1, 2])
    
    print(f"\nVector v1: {v1}")
    print(f"Vector v2: {v2}")
    
    # Calculate dot product
    dot_manual = v1[0] * v2[0] + v1[1] * v2[1]
    dot_numpy = np.dot(v1, v2)
    
    print(f"\nDot product (manual): {dot_manual}")
    print(f"Dot product (NumPy):  {dot_numpy}")
    
    # Geometric interpretation
    print("\n📐 Geometric Meaning:")
    print(f"   The dot product measures how much two vectors 'agree'")
    print(f"   If vectors point in same direction: positive")
    print(f"   If vectors are perpendicular: zero")
    print(f"   If vectors point in opposite directions: negative")
    
    # Calculate magnitudes and angle
    magnitude_v1 = np.sqrt(np.sum(v1 ** 2))
    magnitude_v2 = np.sqrt(np.sum(v2 ** 2))
    
    print(f"\n   |v1| = {magnitude_v1:.2f}")
    print(f"   |v2| = {magnitude_v2:.2f}")
    
    # Dot product for large arrays
    print(f"\n🚀 Dot product for large arrays ({len(arr1):,} elements):")
    start = time.time()
    dot_large = np.dot(arr1, arr2)
    dot_time = time.time() - start
    
    print(f"   Result: {dot_large:,}")
    print(f"   Time: {dot_time:.6f} seconds")
    print(f"   (Try doing this with a loop! 😅)")

def lab_4_simd_demonstration():
    """
    Part 4: Understanding SIMD Operations
    """
    print("\n" + "=" * 70)
    print("LAB 1.1 - Part 4: SIMD Demonstration")
    print("=" * 70)
    
    print("\n💡 SIMD = Single Instruction, Multiple Data")
    print("   Your CPU can process multiple numbers at once!")
    
    # Create arrays of different sizes to show scaling
    sizes = [1_000, 10_000, 100_000, 1_000_000]
    
    print("\n📊 Scaling Analysis:")
    print(f"{'Size':>12} {'Loop Time':>15} {'NumPy Time':>15} {'Speedup':>10}")
    print("-" * 70)
    
    for size in sizes:
        a = np.random.randint(0, 100, size=size)
        b = np.random.randint(0, 100, size=size)
        
        # Loop method
        start = time.time()
        result = [a[i] + b[i] for i in range(size)]
        loop_time = time.time() - start
        
        # NumPy method
        start = time.time()
        result = a + b
        numpy_time = time.time() - start
        
        speedup = loop_time / numpy_time if numpy_time > 0 else 0
        
        print(f"{size:>12,} {loop_time:>15.6f}s {numpy_time:>15.6f}s {speedup:>10.1f}x")
    
    print("\n💡 Notice: As arrays get larger, the speedup becomes more dramatic!")
    print("   This is why ML uses GPUs with massive SIMD capabilities.")

def lab_5_memory_layout():
    """
    Part 5: Contiguous vs Non-Contiguous Memory
    """
    print("\n" + "=" * 70)
    print("LAB 1.1 - Part 5: Memory Layout Investigation")
    print("=" * 70)
    
    # Create contiguous array
    arr_contiguous = np.arange(1000000)
    
    # Create non-contiguous view (every 2nd element)
    arr_sliced = arr_contiguous[::2]
    
    # Create non-contiguous view (transpose)
    matrix = np.arange(1000000).reshape(1000, 1000)
    matrix_T = matrix.T
    
    print("\n1️⃣ Contiguous Array:")
    print(f"   C-contiguous: {arr_contiguous.flags['C_CONTIGUOUS']}")
    print(f"   Strides: {arr_contiguous.strides}")
    
    print("\n2️⃣ Sliced Array (every 2nd element):")
    print(f"   C-contiguous: {arr_sliced.flags['C_CONTIGUOUS']}")
    print(f"   Strides: {arr_sliced.strides}")
    print(f"   ⚠️  Not contiguous! CPU must skip elements.")
    
    print("\n3️⃣ Transposed Matrix:")
    print(f"   Original C-contiguous: {matrix.flags['C_CONTIGUOUS']}")
    print(f"   Transposed C-contiguous: {matrix_T.flags['C_CONTIGUOUS']}")
    print(f"   Transposed F-contiguous: {matrix_T.flags['F_CONTIGUOUS']}")
    
    # Benchmark the difference
    print("\n📊 Performance Impact:")
    
    # Contiguous operation
    start = time.time()
    result1 = arr_contiguous * 2
    time1 = time.time() - start
    
    # Non-contiguous operation
    start = time.time()
    result2 = arr_sliced * 2
    time2 = time.time() - start
    
    print(f"   Contiguous array operation: {time1:.6f}s")
    print(f"   Non-contiguous operation:   {time2:.6f}s")
    print(f"   Ratio: {time2/time1:.2f}x slower")
    
    print("\n💡 Takeaway: Contiguous memory = better cache usage = faster!")

def lab_6_hotel_analogy():
    """
    Part 6: Visualizing the Hotel vs Scattered Houses
    """
    print("\n" + "=" * 70)
    print("LAB 1.1 - Part 6: The Hotel Analogy")
    print("=" * 70)
    
    print("\n🏨 NumPy Array (The Hotel):")
    print("   Memory: [1000][1001][1002][1003][1004][1005]")
    print("   Data:   [  10][  20][  30][  40][  50][  60]")
    print("            ↑")
    print("   CPU Valet: 'Give me everything from 1000 to 1005!'")
    print("   → Gets entire block in ONE trip! ✅")
    
    print("\n🏘️  Python List (Scattered Houses):")
    print("   List:     [ptr1][ptr2][ptr3][ptr4][ptr5][ptr6]")
    print("              ↓     ↓     ↓     ↓     ↓     ↓")
    print("   Memory:  1000  2500  1200  3400  1800  2900")
    print("   Data:     10    20    30    40    50    60")
    print("   CPU Valet: Must make 6 individual trips! ❌")
    
    print("\n💡 For Machine Learning:")
    print("   - Processing millions/billions of numbers")
    print("   - Every memory fetch counts")
    print("   - NumPy's contiguous layout = 10-100x faster")

def main():
    """
    Run all lab exercises
    """
    print("\n" + "=" * 70)
    print("🧪 LAB 1.1: HELLO VECTORS")
    print("Understanding Memory, Performance, and Vectorization")
    print("=" * 70)
    
    # Part 1: Create vectors
    arr1, arr2 = lab_1_vector_creation()
    
    input("\nPress Enter to continue to Part 2 (Benchmark)...")
    
    # Part 2: Benchmark
    result = lab_2_benchmark_addition(arr1, arr2)
    
    input("\nPress Enter to continue to Part 3 (Dot Product)...")
    
    # Part 3: Dot product
    lab_3_dot_product(arr1, arr2)
    
    input("\nPress Enter to continue to Part 4 (SIMD)...")
    
    # Part 4: SIMD demonstration
    lab_4_simd_demonstration()
    
    input("\nPress Enter to continue to Part 5 (Memory Layout)...")
    
    # Part 5: Memory layout
    lab_5_memory_layout()
    
    input("\nPress Enter to continue to Part 6 (Hotel Analogy)...")
    
    # Part 6: Hotel analogy
    lab_6_hotel_analogy()
    
    # Summary
    print("\n" + "=" * 70)
    print("🎓 LAB COMPLETE!")
    print("=" * 70)
    print("\n📝 Key Takeaways:")
    print("   1. NumPy is 10-100x faster than Python loops")
    print("   2. Contiguous memory enables SIMD operations")
    print("   3. The 'Hotel' analogy explains why layout matters")
    print("   4. This is the foundation for all ML performance")
    print("\n📚 Next Steps:")
    print("   1. Complete the Research Assignment (week1_memory_bottleneck.md)")
    print("   2. Watch the recommended videos")
    print("   3. Read Pedro Domingos' paper")
    print("   4. Move on to NumPy for JS Developers exercises")
    print()

if __name__ == "__main__":
    main()
