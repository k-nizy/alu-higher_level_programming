#!/usr/bin/python3

"""
This module   function to convert a Python object into its JSON representation.

The function `to_json_string` takes a Python object and returns its JSON string
representation using the `json.dumps` method.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The Python object to convert to JSON.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)


# Example usage:
# my_list = [1, 2, 3]
# s_my_list = to_json_string(my_list)
# print(s_my_list)
# print(type(s_my_list))
