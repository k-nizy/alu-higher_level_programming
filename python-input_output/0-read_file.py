#!/usr/bin/python3

"""
This module provides a function to read and print the contents of a text file.

The function `read_file` reads a file specified by the filename and prints its
contents to standard output. It uses the `with` statement to ensure proper file
handling and does not require any external modules.

Example:
    To use this module, import it and call the `read_file` function with the
    filename as an argument.

    ```python
    read_file = __import__('0-read_file').read_file
    read_file("my_file_0.txt")
    ```
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')


# Example usage:
# read_file("my_file_0.txt")
