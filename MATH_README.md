# Math Operations Library

A simple Python library providing classes for performing various mathematical operations.

## Features

This library includes two main classes:

### 1. MathOperations
Provides basic mathematical operations:
- **add(a, b)**: Add two numbers
- **subtract(a, b)**: Subtract b from a
- **multiply(a, b)**: Multiply two numbers
- **divide(a, b)**: Divide a by b (with zero division protection)

### 2. AdvancedMath
Provides advanced mathematical operations:
- **power(base, exponent)**: Raise base to the power of exponent
- **square_root(n)**: Calculate the square root of a number (with negative number protection)
- **modulo(a, b)**: Calculate the remainder of a divided by b (with zero divisor protection)
- **absolute(n)**: Calculate the absolute value of a number

## Usage

### Basic Operations

```python
from math_operations import MathOperations

# Addition
result = MathOperations.add(5, 3)  # Returns 8

# Subtraction
result = MathOperations.subtract(10, 3)  # Returns 7

# Multiplication
result = MathOperations.multiply(4, 5)  # Returns 20

# Division
result = MathOperations.divide(10, 2)  # Returns 5.0
```

### Advanced Operations

```python
from math_operations import AdvancedMath

# Power
result = AdvancedMath.power(2, 3)  # Returns 8

# Square Root
result = AdvancedMath.square_root(16)  # Returns 4.0

# Modulo
result = AdvancedMath.modulo(10, 3)  # Returns 1

# Absolute Value
result = AdvancedMath.absolute(-5)  # Returns 5
```

## Error Handling

The library includes proper error handling for common edge cases:

- **Division by zero**: Raises `ValueError` when attempting to divide by zero
- **Square root of negative numbers**: Raises `ValueError` when attempting to calculate square root of negative numbers
- **Modulo by zero**: Raises `ValueError` when attempting to perform modulo with zero divisor

### Error Handling Examples

```python
from math_operations import MathOperations, AdvancedMath

try:
    result = MathOperations.divide(10, 0)
except ValueError as e:
    print(e)  # "Cannot divide by zero"

try:
    result = AdvancedMath.square_root(-4)
except ValueError as e:
    print(e)  # "Cannot calculate square root of negative number"
```

## Testing

The library includes comprehensive unit tests. To run the tests:

```bash
python test_math_operations.py
```

Or using unittest discovery:

```bash
python -m unittest test_math_operations.py
```

## Requirements

- Python 3.x (no external dependencies)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
