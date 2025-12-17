"""
Unit tests for the math operations module.
"""

import unittest
from math_operations import MathOperations, AdvancedMath


class TestMathOperations(unittest.TestCase):
    """Test cases for the MathOperations class."""
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(MathOperations.add(5, 3), 8)
        self.assertEqual(MathOperations.add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(MathOperations.add(-5, -3), -8)
        self.assertEqual(MathOperations.add(-5, 3), -2)
    
    def test_add_floats(self):
        """Test addition of floating point numbers."""
        self.assertAlmostEqual(MathOperations.add(5.5, 3.2), 8.7)
    
    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(MathOperations.subtract(10, 3), 7)
        self.assertEqual(MathOperations.subtract(3, 10), -7)
        self.assertEqual(MathOperations.subtract(-5, -3), -2)
    
    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(MathOperations.multiply(5, 3), 15)
        self.assertEqual(MathOperations.multiply(-5, 3), -15)
        self.assertEqual(MathOperations.multiply(-5, -3), 15)
        self.assertEqual(MathOperations.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division."""
        self.assertEqual(MathOperations.divide(10, 2), 5)
        self.assertEqual(MathOperations.divide(15, 3), 5)
        self.assertAlmostEqual(MathOperations.divide(10, 3), 3.333333333)
    
    def test_divide_by_zero(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            MathOperations.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")


class TestAdvancedMath(unittest.TestCase):
    """Test cases for the AdvancedMath class."""
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(AdvancedMath.power(2, 3), 8)
        self.assertEqual(AdvancedMath.power(5, 2), 25)
        self.assertEqual(AdvancedMath.power(10, 0), 1)
        self.assertEqual(AdvancedMath.power(2, -1), 0.5)
    
    def test_square_root(self):
        """Test square root calculation."""
        self.assertEqual(AdvancedMath.square_root(4), 2)
        self.assertEqual(AdvancedMath.square_root(9), 3)
        self.assertEqual(AdvancedMath.square_root(0), 0)
        self.assertAlmostEqual(AdvancedMath.square_root(2), 1.414213562)
    
    def test_square_root_negative(self):
        """Test that square root of negative number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            AdvancedMath.square_root(-4)
        self.assertEqual(str(context.exception), 
                        "Cannot calculate square root of negative number")
    
    def test_modulo(self):
        """Test modulo operation."""
        self.assertEqual(AdvancedMath.modulo(10, 3), 1)
        self.assertEqual(AdvancedMath.modulo(15, 4), 3)
        self.assertEqual(AdvancedMath.modulo(20, 5), 0)
    
    def test_modulo_by_zero(self):
        """Test that modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            AdvancedMath.modulo(10, 0)
        self.assertEqual(str(context.exception), 
                        "Cannot perform modulo with zero divisor")
    
    def test_absolute(self):
        """Test absolute value calculation."""
        self.assertEqual(AdvancedMath.absolute(-5), 5)
        self.assertEqual(AdvancedMath.absolute(5), 5)
        self.assertEqual(AdvancedMath.absolute(0), 0)
        self.assertAlmostEqual(AdvancedMath.absolute(-3.5), 3.5)


if __name__ == '__main__':
    unittest.main()
