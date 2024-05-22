#!/usr/bin/python3
"""Defines a 'Square' class with a private instance attribute"""


class Square:
    """Definition of 'Square'"""
    def __init__(self, size=0):
        """Inits Square with 'size' private instance attribute

            Args:
                size: An integer size of the square.

            Raises:
                TypeError: The size argument is not an integer.
                Value Error: The size argument is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size