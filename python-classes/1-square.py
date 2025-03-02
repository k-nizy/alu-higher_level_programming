#!/usr/bin/python3
"""
Module: 1-square
Defines a class Square with a private instance attribute 'size'.
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square (private instance attribute).
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
