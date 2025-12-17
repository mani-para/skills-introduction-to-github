"""
Demonstration script for the Math Operations library.

This script shows examples of using the MathOperations and AdvancedMath classes.
"""

from math_operations import MathOperations, AdvancedMath


def demonstrate_basic_operations():
    """Demonstrate basic mathematical operations."""
    print("=" * 60)
    print("BASIC MATH OPERATIONS")
    print("=" * 60)
    
    # Addition
    result = MathOperations.add(15, 7)
    print(f"Addition: 15 + 7 = {result}")
    
    # Subtraction
    result = MathOperations.subtract(20, 8)
    print(f"Subtraction: 20 - 8 = {result}")
    
    # Multiplication
    result = MathOperations.multiply(6, 7)
    print(f"Multiplication: 6 × 7 = {result}")
    
    # Division
    result = MathOperations.divide(50, 5)
    print(f"Division: 50 ÷ 5 = {result}")
    
    # Division with float result
    result = MathOperations.divide(10, 3)
    print(f"Division: 10 ÷ 3 = {result:.4f}")
    
    # Error handling: Division by zero
    print("\nTrying to divide by zero...")
    try:
        result = MathOperations.divide(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print()


def demonstrate_advanced_operations():
    """Demonstrate advanced mathematical operations."""
    print("=" * 60)
    print("ADVANCED MATH OPERATIONS")
    print("=" * 60)
    
    # Power
    result = AdvancedMath.power(2, 8)
    print(f"Power: 2^8 = {result}")
    
    # Square root
    result = AdvancedMath.square_root(144)
    print(f"Square Root: √144 = {result}")
    
    result = AdvancedMath.square_root(50)
    print(f"Square Root: √50 = {result:.4f}")
    
    # Modulo
    result = AdvancedMath.modulo(17, 5)
    print(f"Modulo: 17 % 5 = {result}")
    
    # Absolute value
    result = AdvancedMath.absolute(-42)
    print(f"Absolute: |-42| = {result}")
    
    result = AdvancedMath.absolute(42)
    print(f"Absolute: |42| = {result}")
    
    # Error handling: Square root of negative number
    print("\nTrying to calculate square root of negative number...")
    try:
        result = AdvancedMath.square_root(-16)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Error handling: Modulo by zero
    print("\nTrying to perform modulo with zero divisor...")
    try:
        result = AdvancedMath.modulo(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print()


def demonstrate_combined_operations():
    """Demonstrate combining multiple operations."""
    print("=" * 60)
    print("COMBINED OPERATIONS")
    print("=" * 60)
    
    # Calculate: (10 + 5) × 3
    step1 = MathOperations.add(10, 5)
    result = MathOperations.multiply(step1, 3)
    print(f"(10 + 5) × 3 = {result}")
    
    # Calculate: √(16 + 9)
    step1 = MathOperations.add(16, 9)
    result = AdvancedMath.square_root(step1)
    print(f"√(16 + 9) = {result}")
    
    # Calculate: 2^4 ÷ 2
    step1 = AdvancedMath.power(2, 4)
    result = MathOperations.divide(step1, 2)
    print(f"2^4 ÷ 2 = {result}")
    
    # Calculate: |(-5 × 3)|
    step1 = MathOperations.multiply(-5, 3)
    result = AdvancedMath.absolute(step1)
    print(f"|(-5 × 3)| = {result}")
    
    print()


if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "MATH OPERATIONS LIBRARY DEMO" + " " * 20 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    demonstrate_basic_operations()
    demonstrate_advanced_operations()
    demonstrate_combined_operations()
    
    print("=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)
    print()
