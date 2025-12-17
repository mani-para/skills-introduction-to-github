"""
Basic Math Operations Module

This module provides classes for performing various mathematical operations.
"""


class MathOperations:
    """
    A class that provides basic mathematical operations.
    """
    
    @staticmethod
    def add(a, b):
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """
        Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return a * b
    
    @staticmethod
    def divide(a, b):
        """
        Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class AdvancedMath:
    """
    A class that provides advanced mathematical operations.
    """
    
    @staticmethod
    def power(base, exponent):
        """
        Raise base to the power of exponent.
        
        Args:
            base: The base number
            exponent: The exponent
            
        Returns:
            base raised to the power of exponent
        """
        return base ** exponent
    
    @staticmethod
    def square_root(n):
        """
        Calculate the square root of a number.
        
        Args:
            n: The number
            
        Returns:
            Square root of n
            
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return n ** 0.5
    
    @staticmethod
    def modulo(a, b):
        """
        Calculate the remainder of a divided by b.
        
        Args:
            a: The dividend
            b: The divisor
            
        Returns:
            Remainder of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot perform modulo with zero divisor")
        return a % b
    
    @staticmethod
    def absolute(n):
        """
        Calculate the absolute value of a number.
        
        Args:
            n: The number
            
        Returns:
            Absolute value of n
        """
        return abs(n)
