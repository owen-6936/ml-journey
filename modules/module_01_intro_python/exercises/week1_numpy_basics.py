"""
Module 1, Week 1: NumPy Basics Exercises
Complete these exercises to master NumPy fundamentals
"""

import numpy as np

def exercise_1_array_creation():
    """
    Exercise 1: Array Creation
    Create different types of NumPy arrays
    """
    print("=" * 50)
    print("Exercise 1: Array Creation")
    print("=" * 50)
    
    # TODO: Create a 1D array with numbers from 0 to 9
    arr_1d = None  # Your code here
    
    # TODO: Create a 2D array (3x3) filled with zeros
    arr_zeros = None  # Your code here
    
    # TODO: Create a 2D array (2x4) filled with ones
    arr_ones = None  # Your code here
    
    # TODO: Create an identity matrix of size 4x4
    identity = None  # Your code here
    
    # TODO: Create an array with random values between 0 and 1, shape (3, 3)
    arr_random = None  # Your code here
    
    print("1D array:", arr_1d)
    print("Zeros array:\n", arr_zeros)
    print("Ones array:\n", arr_ones)
    print("Identity matrix:\n", identity)
    print("Random array:\n", arr_random)
    print()

def exercise_2_array_operations():
    """
    Exercise 2: Array Operations
    Perform mathematical operations on arrays
    """
    print("=" * 50)
    print("Exercise 2: Array Operations")
    print("=" * 50)
    
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([10, 20, 30, 40, 50])
    
    # TODO: Add arrays a and b
    sum_ab = None  # Your code here
    
    # TODO: Multiply arrays a and b (element-wise)
    product_ab = None  # Your code here
    
    # TODO: Calculate the dot product of a and b
    dot_product = None  # Your code here
    
    # TODO: Calculate the square of each element in array a
    squares = None  # Your code here
    
    # TODO: Calculate the mean of array b
    mean_b = None  # Your code here
    
    print("a:", a)
    print("b:", b)
    print("Sum:", sum_ab)
    print("Element-wise product:", product_ab)
    print("Dot product:", dot_product)
    print("Squares of a:", squares)
    print("Mean of b:", mean_b)
    print()

def exercise_3_indexing_slicing():
    """
    Exercise 3: Indexing and Slicing
    Access and modify array elements
    """
    print("=" * 50)
    print("Exercise 3: Indexing and Slicing")
    print("=" * 50)
    
    arr = np.arange(20).reshape(4, 5)
    print("Original array:\n", arr)
    
    # TODO: Get the element at row 2, column 3
    element = None  # Your code here
    
    # TODO: Get the first row
    first_row = None  # Your code here
    
    # TODO: Get the last column
    last_column = None  # Your code here
    
    # TODO: Get a 2x2 subarray from the top-left corner
    subarray = None  # Your code here
    
    # TODO: Get all elements greater than 10
    greater_than_10 = None  # Your code here
    
    print("Element at (2, 3):", element)
    print("First row:", first_row)
    print("Last column:", last_column)
    print("Top-left 2x2 subarray:\n", subarray)
    print("Elements > 10:", greater_than_10)
    print()

def exercise_4_broadcasting():
    """
    Exercise 4: Broadcasting
    Understanding NumPy broadcasting
    """
    print("=" * 50)
    print("Exercise 4: Broadcasting")
    print("=" * 50)
    
    # TODO: Create a 3x3 array with values 1 to 9
    matrix = None  # Your code here
    
    # TODO: Add 10 to every element (broadcasting)
    matrix_plus_10 = None  # Your code here
    
    # TODO: Multiply each row by [1, 2, 3] respectively
    row_multiplier = np.array([1, 2, 3])
    # Hint: You might need to reshape row_multiplier
    scaled_rows = None  # Your code here
    
    print("Original matrix:\n", matrix)
    print("Matrix + 10:\n", matrix_plus_10)
    print("Scaled rows:\n", scaled_rows)
    print()

def exercise_5_statistics():
    """
    Exercise 5: Statistical Operations
    Calculate statistics from arrays
    """
    print("=" * 50)
    print("Exercise 5: Statistical Operations")
    print("=" * 50)
    
    data = np.random.randn(100)  # 100 random numbers from standard normal distribution
    
    # TODO: Calculate mean
    mean = None  # Your code here
    
    # TODO: Calculate median
    median = None  # Your code here
    
    # TODO: Calculate standard deviation
    std = None  # Your code here
    
    # TODO: Find minimum and maximum values
    min_val = None  # Your code here
    max_val = None  # Your code here
    
    # TODO: Find the index of the maximum value
    max_index = None  # Your code here
    
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard deviation: {std}")
    print(f"Min: {min_val}, Max: {max_val}")
    print(f"Index of max value: {max_index}")
    print()

def bonus_exercise():
    """
    Bonus Exercise: Matrix Operations
    Advanced NumPy operations
    """
    print("=" * 50)
    print("Bonus Exercise: Matrix Operations")
    print("=" * 50)
    
    # TODO: Create two 3x3 matrices with random integers between 1 and 10
    A = None  # Your code here
    B = None  # Your code here
    
    # TODO: Perform matrix multiplication (use @ or np.matmul)
    C = None  # Your code here
    
    # TODO: Calculate the transpose of matrix A
    A_transpose = None  # Your code here
    
    # TODO: Calculate the inverse of matrix A (if it exists)
    # Hint: Use np.linalg.inv()
    try:
        A_inverse = None  # Your code here
    except:
        A_inverse = "Matrix is singular, cannot compute inverse"
    
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)
    print("A @ B:\n", C)
    print("Transpose of A:\n", A_transpose)
    print("Inverse of A:\n", A_inverse)
    print()

def main():
    """Run all exercises"""
    print("\n" + "=" * 50)
    print("NUMPY BASICS EXERCISES")
    print("=" * 50 + "\n")
    
    exercise_1_array_creation()
    exercise_2_array_operations()
    exercise_3_indexing_slicing()
    exercise_4_broadcasting()
    exercise_5_statistics()
    bonus_exercise()
    
    print("\n" + "=" * 50)
    print("Exercises completed!")
    print("=" * 50)
    print("\nNext steps:")
    print("1. Review your solutions")
    print("2. Try to optimize your code")
    print("3. Experiment with different array shapes and sizes")
    print("4. Move on to Pandas exercises")

if __name__ == "__main__":
    main()
