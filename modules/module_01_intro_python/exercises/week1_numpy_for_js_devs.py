"""
Module 1, Week 1: NumPy for JavaScript Developers
Learn to translate your JS array manipulation skills to NumPy's vectorized operations
"""

import numpy as np
import time

def demo_map_to_vectorization():
    """
    Exercise 1: .map() → NumPy Vectorization
    Learn how JS .map() translates to NumPy operations
    """
    print("=" * 60)
    print("Exercise 1: JavaScript .map() → NumPy Vectorization")
    print("=" * 60)
    
    # Sample data
    arr = np.array([1, 2, 3, 4, 5])
    
    print("Original array:", arr)
    print()
    
    # TODO: Double each element (like arr.map(x => x * 2))
    # In NumPy, you can just use: arr * 2
    doubled = None  # Your code here
    
    # TODO: Square each element (like arr.map(x => x ** 2))
    squared = None  # Your code here
    
    # TODO: Apply function to each element (like arr.map(x => x * 2 + 1))
    transformed = None  # Your code here
    
    print("Doubled:", doubled)
    print("Squared:", squared)
    print("Transformed (x * 2 + 1):", transformed)
    print()

def demo_filter_to_boolean_indexing():
    """
    Exercise 2: .filter() → Boolean Indexing
    Learn how JS .filter() translates to NumPy boolean indexing
    """
    print("=" * 60)
    print("Exercise 2: JavaScript .filter() → Boolean Indexing")
    print("=" * 60)
    
    arr = np.array([1, 5, 3, 8, 2, 9, 4, 7, 6])
    print("Original array:", arr)
    print()
    
    # TODO: Filter elements > 5 (like arr.filter(x => x > 5))
    # In NumPy: arr[arr > 5]
    greater_than_5 = None  # Your code here
    
    # TODO: Filter even numbers (like arr.filter(x => x % 2 === 0))
    # Hint: Use arr % 2 == 0
    even_numbers = None  # Your code here
    
    # TODO: Filter elements between 3 and 7 (like arr.filter(x => x >= 3 && x <= 7))
    # Hint: Use & operator: (arr >= 3) & (arr <= 7)
    between_3_and_7 = None  # Your code here
    
    print("Greater than 5:", greater_than_5)
    print("Even numbers:", even_numbers)
    print("Between 3 and 7:", between_3_and_7)
    print()

def demo_reduce_to_aggregations():
    """
    Exercise 3: .reduce() → NumPy Aggregations
    Learn how JS .reduce() translates to NumPy aggregation functions
    """
    print("=" * 60)
    print("Exercise 3: JavaScript .reduce() → Aggregations")
    print("=" * 60)
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Original array:", arr)
    print()
    
    # TODO: Sum all elements (like arr.reduce((acc, x) => acc + x, 0))
    # In NumPy: arr.sum()
    total = None  # Your code here
    
    # TODO: Find product of all elements (like arr.reduce((acc, x) => acc * x, 1))
    # Hint: arr.prod()
    product = None  # Your code here
    
    # TODO: Find maximum (like arr.reduce((acc, x) => Math.max(acc, x)))
    # Hint: arr.max()
    maximum = None  # Your code here
    
    # TODO: Find average (not directly .reduce in JS, but common operation)
    # Hint: arr.mean()
    average = None  # Your code here
    
    print("Sum:", total)
    print("Product:", product)
    print("Maximum:", maximum)
    print("Average:", average)
    print()

def demo_chaining_operations():
    """
    Exercise 4: Chaining Operations (JS method chaining → NumPy)
    """
    print("=" * 60)
    print("Exercise 4: Chaining Operations")
    print("=" * 60)
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Original array:", arr)
    print()
    
    # In JavaScript, you might write:
    # arr.filter(x => x > 3).map(x => x * 2).reduce((acc, x) => acc + x, 0)
    
    # TODO: Filter elements > 3, double them, then sum
    # Step by step:
    # 1. filtered = arr[arr > 3]
    # 2. doubled = filtered * 2
    # 3. result = doubled.sum()
    # Or in one line: (arr[arr > 3] * 2).sum()
    
    result = None  # Your code here
    
    print("Filter > 3, double, then sum:", result)
    print("(Should be: 4*2 + 5*2 + 6*2 + 7*2 + 8*2 + 9*2 + 10*2 = 98)")
    print()

def demo_performance_comparison():
    """
    Exercise 5: Performance - Why Vectorization Matters
    See the dramatic speed difference between loops and vectorization
    """
    print("=" * 60)
    print("Exercise 5: Performance Comparison")
    print("=" * 60)
    
    # Create large array
    large_arr = np.random.randint(0, 100, size=1_000_000)
    
    # Method 1: Python loop (like JavaScript)
    start = time.time()
    result_loop = []
    for x in large_arr:
        if x > 50:
            result_loop.append(x * 2)
    end = time.time()
    loop_time = end - start
    
    # Method 2: NumPy vectorization
    start = time.time()
    result_numpy = large_arr[large_arr > 50] * 2
    end = time.time()
    numpy_time = end - start
    
    print(f"Array size: {len(large_arr):,} elements")
    print(f"\nPython loop (JS-style): {loop_time:.4f} seconds")
    print(f"NumPy vectorization:    {numpy_time:.4f} seconds")
    print(f"\nSpeedup: {loop_time / numpy_time:.1f}x faster! 🚀")
    print("\nThis is why we avoid loops in NumPy!")
    print()

def bonus_2d_arrays():
    """
    Bonus Exercise: Working with 2D Arrays
    Arrays of arrays in JS → NumPy matrices
    """
    print("=" * 60)
    print("Bonus: 2D Arrays (Matrix Operations)")
    print("=" * 60)
    
    # In JS: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    print("Matrix:")
    print(matrix)
    print()
    
    # TODO: Get all elements in first row
    # Like matrix[0] in JS
    first_row = None  # Your code here
    
    # TODO: Get all elements in first column
    # In JS, you'd need matrix.map(row => row[0])
    # In NumPy, just: matrix[:, 0]
    first_column = None  # Your code here
    
    # TODO: Filter all elements > 5 (flattens the result)
    greater_than_5 = None  # Your code here
    
    # TODO: Double every element in the matrix
    doubled_matrix = None  # Your code here
    
    print("First row:", first_row)
    print("First column:", first_column)
    print("Elements > 5:", greater_than_5)
    print("\nDoubled matrix:")
    print(doubled_matrix)
    print()

def practical_example():
    """
    Practical Example: Processing User Data
    A realistic scenario you might encounter
    """
    print("=" * 60)
    print("Practical Example: Processing User Data")
    print("=" * 60)
    
    # Simulated user ages
    ages = np.array([25, 30, 18, 45, 22, 35, 50, 28, 31, 19, 42, 38])
    
    print("User ages:", ages)
    print()
    
    # TODO: Calculate average age
    avg_age = None  # Your code here
    
    # TODO: Find how many users are adults (age >= 18)
    # Hint: Use .sum() on boolean array
    num_adults = None  # Your code here
    
    # TODO: Get ages of users in their 20s (20-29)
    twenties = None  # Your code here
    
    # TODO: Categorize users: add 10 years to everyone's age
    ages_plus_10 = None  # Your code here
    
    print(f"Average age: {avg_age}")
    print(f"Number of adults: {num_adults}")
    print(f"Users in their 20s: {twenties}")
    print(f"Ages in 10 years: {ages_plus_10}")
    print()

def main():
    """Run all exercises"""
    print("\n" + "=" * 60)
    print("NUMPY FOR JAVASCRIPT DEVELOPERS")
    print("=" * 60 + "\n")
    
    print("As a JS/TS developer, you already know how to think about")
    print("array operations. NumPy just makes them MUCH faster!")
    print()
    
    demo_map_to_vectorization()
    demo_filter_to_boolean_indexing()
    demo_reduce_to_aggregations()
    demo_chaining_operations()
    demo_performance_comparison()
    bonus_2d_arrays()
    practical_example()
    
    print("\n" + "=" * 60)
    print("Key Takeaways:")
    print("=" * 60)
    print("1. .map()    → Just use math operators: arr * 2")
    print("2. .filter() → Boolean indexing: arr[arr > 5]")
    print("3. .reduce() → Built-in functions: arr.sum(), arr.mean()")
    print("4. Avoid loops - use vectorization for 10-100x speedup!")
    print("5. NumPy is your friend for ML performance")
    print("\n✅ Now you're thinking in NumPy, not loops!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
