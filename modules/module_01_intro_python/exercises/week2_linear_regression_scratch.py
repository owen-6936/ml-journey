"""
Module 1, Week 2: Your First ML Algorithm - Linear Regression from Scratch
Build gradient descent using only vanilla Python (no ML libraries!)

For JS/TS developers: This shows how a simple loop can "learn" optimal parameters.
"""

import random
import matplotlib.pyplot as plt

def linear_regression_scratch(X, y, learning_rate=0.01, iterations=1000, verbose=True):
    """
    Implement Linear Regression using Gradient Descent
    
    Goal: Find the best line y = mx + b that fits the data
    
    Parameters:
    - X: list of input values
    - y: list of output values
    - learning_rate: how big of steps to take when updating parameters
    - iterations: how many times to update parameters
    - verbose: whether to print progress
    
    Returns:
    - m: slope
    - b: intercept
    - errors: list of errors at each iteration (for plotting)
    """
    # Initialize parameters randomly
    m = 0.0  # slope
    b = 0.0  # intercept
    n = len(X)
    errors = []
    
    print(f"Starting training with {iterations} iterations...")
    print(f"Learning rate: {learning_rate}")
    print()
    
    for i in range(iterations):
        # Step 1: Make predictions using current m and b
        y_pred = [m * x + b for x in X]
        
        # Step 2: Calculate error (Mean Squared Error)
        # This measures how far off our predictions are
        error = sum([(pred - actual) ** 2 for pred, actual in zip(y_pred, y)]) / n
        errors.append(error)
        
        # Step 3: Calculate gradients
        # These tell us which direction to adjust m and b
        # dm: how much error changes with respect to m
        # db: how much error changes with respect to b
        dm = sum([2 * x * (pred - actual) for x, pred, actual in zip(X, y_pred, y)]) / n
        db = sum([2 * (pred - actual) for pred, actual in zip(y_pred, y)]) / n
        
        # Step 4: Update parameters
        # Move in the direction that reduces error
        m = m - learning_rate * dm
        b = b - learning_rate * db
        
        # Print progress every 100 iterations
        if verbose and (i % 100 == 0 or i == iterations - 1):
            print(f"Iteration {i:4d}: Error = {error:.6f}, m = {m:.4f}, b = {b:.4f}")
    
    print()
    print(f"✅ Training complete!")
    print(f"Final equation: y = {m:.4f}x + {b:.4f}")
    
    return m, b, errors

def plot_results(X, y, m, b, errors):
    """
    Visualize the results
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot 1: Data and fitted line
    ax1.scatter(X, y, color='blue', label='Actual data', s=100, alpha=0.6)
    
    # Generate line points
    x_line = [min(X), max(X)]
    y_line = [m * x + b for x in x_line]
    ax1.plot(x_line, y_line, color='red', linewidth=2, label=f'Fitted line: y = {m:.2f}x + {b:.2f}')
    
    ax1.set_xlabel('X', fontsize=12)
    ax1.set_ylabel('y', fontsize=12)
    ax1.set_title('Linear Regression: Data vs Fitted Line', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Error over iterations (learning curve)
    ax2.plot(errors, color='green', linewidth=2)
    ax2.set_xlabel('Iteration', fontsize=12)
    ax2.set_ylabel('Mean Squared Error', fontsize=12)
    ax2.set_title('Learning Curve: Error Decreasing Over Time', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('linear_regression_results.png', dpi=150, bbox_inches='tight')
    print("📊 Plot saved as 'linear_regression_results.png'")
    plt.show()

def example_1_perfect_line():
    """
    Example 1: Perfect linear relationship
    y = 2x (no noise)
    """
    print("=" * 70)
    print("Example 1: Perfect Linear Relationship (y = 2x)")
    print("=" * 70)
    
    X = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    
    print(f"Data: X = {X}")
    print(f"      y = {y}")
    print()
    
    m, b, errors = linear_regression_scratch(X, y, learning_rate=0.01, iterations=1000)
    
    # Make a prediction
    test_x = 6
    prediction = m * test_x + b
    print(f"\n🔮 Prediction for x = {test_x}: y = {prediction:.2f}")
    print(f"   (Expected: {2 * test_x})")
    print()

def example_2_with_intercept():
    """
    Example 2: Line with intercept
    y = 3x + 5
    """
    print("=" * 70)
    print("Example 2: Line with Intercept (y = 3x + 5)")
    print("=" * 70)
    
    X = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [8, 11, 14, 17, 20, 23, 26, 29]
    
    print(f"Data: X = {X}")
    print(f"      y = {y}")
    print()
    
    m, b, errors = linear_regression_scratch(X, y, learning_rate=0.01, iterations=1000)
    
    test_x = 10
    prediction = m * test_x + b
    print(f"\n🔮 Prediction for x = {test_x}: y = {prediction:.2f}")
    print(f"   (Expected: {3 * test_x + 5})")
    print()
    
    # Visualize
    plot_results(X, y, m, b, errors)

def example_3_noisy_data():
    """
    Example 3: Realistic data with noise
    Approximate relationship: y ≈ 2x + 3 (with random noise)
    """
    print("=" * 70)
    print("Example 3: Noisy Real-World Data")
    print("=" * 70)
    
    # Generate data with noise
    random.seed(42)
    X = list(range(1, 21))  # 1 to 20
    y = [2 * x + 3 + random.uniform(-2, 2) for x in X]  # y = 2x + 3 + noise
    
    print(f"Generated {len(X)} noisy data points")
    print(f"True relationship: y ≈ 2x + 3 (with noise)")
    print()
    
    m, b, errors = linear_regression_scratch(X, y, learning_rate=0.01, iterations=2000)
    
    print(f"\n📊 How close did we get?")
    print(f"   True slope: 2.0, Learned slope: {m:.4f}")
    print(f"   True intercept: 3.0, Learned intercept: {b:.4f}")
    print()
    
    # Visualize
    plot_results(X, y, m, b, errors)

def challenge_exercise():
    """
    Challenge: Experiment with different learning rates
    """
    print("=" * 70)
    print("Challenge: Understanding Learning Rate")
    print("=" * 70)
    
    X = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    
    learning_rates = [0.001, 0.01, 0.1, 0.5]
    
    print("Testing different learning rates on the same data...")
    print()
    
    for lr in learning_rates:
        print(f"Learning rate: {lr}")
        m, b, errors = linear_regression_scratch(X, y, learning_rate=lr, iterations=500, verbose=False)
        final_error = errors[-1]
        print(f"  Final error: {final_error:.6f}")
        print(f"  Final m: {m:.4f}, b: {b:.4f}")
        print()
    
    print("💡 Observations:")
    print("   - Too small learning rate (0.001): slow convergence")
    print("   - Too large learning rate (0.5): might overshoot")
    print("   - Sweet spot (0.01-0.1): good balance")
    print()

def what_you_learned():
    """
    Summary of key concepts
    """
    print("=" * 70)
    print("🎓 What You Just Learned")
    print("=" * 70)
    print()
    print("1. **Machine Learning is Optimization**")
    print("   - We want to find parameters (m, b) that minimize error")
    print("   - This is what 'training' means!")
    print()
    print("2. **Gradient Descent**")
    print("   - Start with random parameters")
    print("   - Calculate how wrong we are (error)")
    print("   - Calculate which direction to adjust (gradient)")
    print("   - Take a small step in that direction")
    print("   - Repeat until error is small enough")
    print()
    print("3. **Learning Rate Matters**")
    print("   - Too small: slow learning")
    print("   - Too large: might never converge")
    print("   - Just right: efficient learning")
    print()
    print("4. **Why This Matters**")
    print("   - This is the foundation of ALL machine learning!")
    print("   - Neural networks? Same idea, more parameters")
    print("   - Deep learning? Same idea, more layers")
    print()
    print("5. **Next Steps**")
    print("   - Module 2 will teach you the MATH behind this")
    print("   - You'll understand WHY gradient descent works")
    print("   - The calculus and linear algebra will make sense now!")
    print()
    print("=" * 70)
    print()

def main():
    """
    Run all examples
    """
    print("\n" + "=" * 70)
    print("YOUR FIRST ML ALGORITHM: LINEAR REGRESSION FROM SCRATCH")
    print("=" * 70)
    print()
    print("You're about to see how a simple Python loop can 'learn'!")
    print("No ML libraries needed - just math and iteration.")
    print()
    
    # Run examples
    example_1_perfect_line()
    input("Press Enter to continue to Example 2...")
    
    example_2_with_intercept()
    input("Press Enter to continue to Example 3...")
    
    example_3_noisy_data()
    input("Press Enter to continue to Challenge...")
    
    challenge_exercise()
    
    what_you_learned()
    
    print("🎉 Congratulations! You just built a machine learning algorithm!")
    print("💪 You're ready for Module 2: Mathematical Foundations")
    print()

if __name__ == "__main__":
    main()
