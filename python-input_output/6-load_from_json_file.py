#!/usr/bin/python3

"""
This module provides a function to create an object from a JSON file.

The function `load_from_json_file` ds a JSON file and returns the corresponding
Python object using the `json.load` method.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)


# Example usage:
# my_list = load_from_json_file("my_list.json")
# print(my_list)
# print(type(my_list))
