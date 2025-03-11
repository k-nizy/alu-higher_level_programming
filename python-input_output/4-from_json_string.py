#!/usr/bin/python3

"""
This module provides a function to convert a JSON string into a Python object.

T function `from_json_string` takes a JSON string and returns the corresponding
Python object using the `json.loads` method.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to a Python object.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)


# Example usage:
# s_my_list = "[1, 2, 3]"
# my_list = from_json_string(s_my_list)
# print(my_list)
# print(type(my_list))
