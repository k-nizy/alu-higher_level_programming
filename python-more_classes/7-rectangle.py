#!/usr/bin/python3
"""
Module: 7-rectangle
Defines a class Rectangle with private instance attributes 'width' and 'height',
getters and setters for both attributes, public class attributes
'number_of_instances' and 'print_symbol', methods to calculate the area and
perimeter, custom string representations, and a custom destructor.
"""


class Rectangle:
    """
    A class that defines a rectangle by its width and height.

    Attributes:
        __width (int): The width of the rectangle (private instance attribute).
        __height (int): The height of the rectangle (private instance attribute).
        number_of_instances (int): The number of Rectangle instances (public class attribute).
        print_symbol (any): The symbol used for string representation (public class attribute).
    """

    number_of_instances = 0  # Public class attribute
    print_symbol = "#"  # Public class attribute

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width  # Use the setter to validate the width
        self.height = height  # Use the setter to validate the height
        Rectangle.number_of_instances += 1  # Increment the number of instances

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the symbol stored
        in `print_symbol`.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append(str(self.print_symbol) * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """
        Returns a string representation of the rectangle for `repr()`.

        Returns:
            str: The string representation of the rectangle object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted and decrements
        the number of instances.
        """
        Rectangle.number_of_instances -= 1  # Decrement the number of instances
        print("Bye rectangle...")
