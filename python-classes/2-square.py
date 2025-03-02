#!/usr/bin/python3
"""
Module: 2-square
Defines a class Square with a private instance attribute 'size' and validation.
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private instance attribute).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
