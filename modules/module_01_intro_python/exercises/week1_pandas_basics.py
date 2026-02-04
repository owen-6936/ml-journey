"""
Module 1, Week 1: Pandas Basics Exercises
Complete these exercises to master Pandas fundamentals
"""

import pandas as pd
import numpy as np

def exercise_1_series_basics():
    """
    Exercise 1: Pandas Series
    Create and manipulate Series
    """
    print("=" * 50)
    print("Exercise 1: Pandas Series")
    print("=" * 50)
    
    # TODO: Create a Series from a list
    data = [10, 20, 30, 40, 50]
    series = None  # Your code here
    
    # TODO: Create a Series with custom index
    custom_series = None  # Your code here (use index=['a', 'b', 'c', 'd', 'e'])
    
    # TODO: Access element at index 'c'
    element = None  # Your code here
    
    print("Basic Series:\n", series)
    print("\nSeries with custom index:\n", custom_series)
    print(f"\nElement at 'c': {element}")
    print()

def exercise_2_dataframe_creation():
    """
    Exercise 2: DataFrame Creation
    Create DataFrames from different sources
    """
    print("=" * 50)
    print("Exercise 2: DataFrame Creation")
    print("=" * 50)
    
    # TODO: Create a DataFrame from a dictionary
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
        'Salary': [70000, 80000, 75000, 65000, 90000]
    }
    df = None  # Your code here
    
    # TODO: Display first 3 rows
    first_three = None  # Your code here
    
    # TODO: Get DataFrame info (shape, columns, dtypes)
    shape = None  # Your code here
    columns = None  # Your code here
    
    print("DataFrame:\n", df)
    print("\nFirst 3 rows:\n", first_three)
    print(f"\nShape: {shape}")
    print(f"Columns: {list(columns)}")
    print()

def exercise_3_data_selection():
    """
    Exercise 3: Selecting Data
    Access data using different methods
    """
    print("=" * 50)
    print("Exercise 3: Data Selection")
    print("=" * 50)
    
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]
    })
    
    print("Original DataFrame:\n", df)
    
    # TODO: Select column 'A'
    col_a = None  # Your code here
    
    # TODO: Select multiple columns ['A', 'C']
    cols_ac = None  # Your code here
    
    # TODO: Select row at index 2
    row_2 = None  # Your code here (use .loc or .iloc)
    
    # TODO: Select rows where column 'B' > 20
    filtered = None  # Your code here
    
    # TODO: Select value at row 3, column 'C'
    value = None  # Your code here
    
    print("\nColumn 'A':\n", col_a)
    print("\nColumns A and C:\n", cols_ac)
    print("\nRow 2:\n", row_2)
    print("\nRows where B > 20:\n", filtered)
    print(f"\nValue at (3, 'C'): {value}")
    print()

def exercise_4_data_operations():
    """
    Exercise 4: Data Operations
    Perform operations on DataFrames
    """
    print("=" * 50)
    print("Exercise 4: Data Operations")
    print("=" * 50)
    
    df = pd.DataFrame({
        'Product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B'],
        'Sales': [100, 150, 200, 120, 180, 210, 90, 160],
        'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West']
    })
    
    print("Sales DataFrame:\n", df)
    
    # TODO: Calculate total sales
    total_sales = None  # Your code here
    
    # TODO: Calculate average sales
    avg_sales = None  # Your code here
    
    # TODO: Group by 'Product' and calculate sum of sales
    sales_by_product = None  # Your code here
    
    # TODO: Group by 'Region' and calculate mean sales
    sales_by_region = None  # Your code here
    
    # TODO: Sort by 'Sales' in descending order
    sorted_df = None  # Your code here
    
    print(f"\nTotal Sales: {total_sales}")
    print(f"Average Sales: {avg_sales}")
    print("\nSales by Product:\n", sales_by_product)
    print("\nAverage Sales by Region:\n", sales_by_region)
    print("\nSorted by Sales (desc):\n", sorted_df)
    print()

def exercise_5_data_cleaning():
    """
    Exercise 5: Data Cleaning
    Handle missing values and data types
    """
    print("=" * 50)
    print("Exercise 5: Data Cleaning")
    print("=" * 50)
    
    # Create DataFrame with missing values
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, 4, 5],
        'C': [1, 2, 3, np.nan, 5]
    })
    
    print("DataFrame with missing values:\n", df)
    
    # TODO: Check for missing values
    missing_count = None  # Your code here
    
    # TODO: Fill missing values with 0
    df_filled = None  # Your code here
    
    # TODO: Drop rows with any missing values
    df_dropped = None  # Your code here
    
    # TODO: Fill missing values with column mean
    df_mean_filled = None  # Your code here
    
    print("\nMissing values count:\n", missing_count)
    print("\nFilled with 0:\n", df_filled)
    print("\nDropped rows with NaN:\n", df_dropped)
    print("\nFilled with column mean:\n", df_mean_filled)
    print()

def exercise_6_merging_data():
    """
    Exercise 6: Merging and Joining
    Combine multiple DataFrames
    """
    print("=" * 50)
    print("Exercise 6: Merging Data")
    print("=" * 50)
    
    df1 = pd.DataFrame({
        'ID': [1, 2, 3, 4],
        'Name': ['Alice', 'Bob', 'Charlie', 'David']
    })
    
    df2 = pd.DataFrame({
        'ID': [1, 2, 3, 5],
        'Age': [25, 30, 35, 28]
    })
    
    print("DataFrame 1:\n", df1)
    print("\nDataFrame 2:\n", df2)
    
    # TODO: Perform inner join on 'ID'
    inner_join = None  # Your code here
    
    # TODO: Perform left join on 'ID'
    left_join = None  # Your code here
    
    # TODO: Concatenate df1 and df2 vertically
    concatenated = None  # Your code here (hint: use pd.concat)
    
    print("\nInner Join:\n", inner_join)
    print("\nLeft Join:\n", left_join)
    print()

def bonus_exercise():
    """
    Bonus Exercise: Real-world Data Analysis
    Simulate analyzing a small dataset
    """
    print("=" * 50)
    print("Bonus Exercise: Mini Data Analysis")
    print("=" * 50)
    
    # Create sample sales data
    np.random.seed(42)
    df = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=30),
        'Product': np.random.choice(['A', 'B', 'C'], 30),
        'Sales': np.random.randint(50, 200, 30),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 30)
    })
    
    print("Sales Data:\n", df.head(10))
    
    # TODO: Calculate total sales per product
    sales_per_product = None  # Your code here
    
    # TODO: Find the date with highest sales
    max_sales_date = None  # Your code here
    
    # TODO: Calculate average sales by region
    avg_by_region = None  # Your code here
    
    # TODO: Add a new column 'Month' extracted from Date
    df_with_month = df.copy()
    # Your code here to add 'Month' column
    
    print("\nTotal Sales per Product:\n", sales_per_product)
    print(f"\nDate with highest sales: {max_sales_date}")
    print("\nAverage sales by Region:\n", avg_by_region)
    print()

def main():
    """Run all exercises"""
    print("\n" + "=" * 50)
    print("PANDAS BASICS EXERCISES")
    print("=" * 50 + "\n")
    
    exercise_1_series_basics()
    exercise_2_dataframe_creation()
    exercise_3_data_selection()
    exercise_4_data_operations()
    exercise_5_data_cleaning()
    exercise_6_merging_data()
    bonus_exercise()
    
    print("\n" + "=" * 50)
    print("Exercises completed!")
    print("=" * 50)
    print("\nNext steps:")
    print("1. Practice with real datasets (Kaggle, UCI ML Repository)")
    print("2. Learn about Pandas performance optimization")
    print("3. Explore advanced features like MultiIndex")
    print("4. Move on to data visualization exercises")

if __name__ == "__main__":
    main()
