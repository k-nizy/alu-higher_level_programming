#!/usr/bin/python3

"""
This module provides a function  return the dictionary description of an object
for JSON serialization.

The function `class_to_json` taes an object and returns a dictionary containing
all its serializable attributes.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing the object's serializable attributes.
    """
    return obj.__dict__


# Example usage:
# m = MyClass("John")
# mj = class_to_json(m)
# print(mj)
