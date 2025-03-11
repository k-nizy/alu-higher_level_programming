#!/usr/bin/python3

"""
This module provides a function to write a string to a text file and return the
number of characters written.

The function `write_file` writes the provided text to a file specified by the
filename. If the file does not exist, it creates it. If the file exists, it
overwrites its content. The function returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and returns the number of characters written.

    Args:
        filename (str): The name of  file to write to. Defa to an empty string.
        text (str): The text to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)


# Example usage:
# nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
# print(nb_characters)
