#!/usr/bin/python3

"""
his module provides a function to write an object to a text file using its JSON
representation.

The nction `save_to_json_file` takes a Python object and a filename, serializes
the object into a JSON string, and writes it to the file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to serialize and write to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


# Example usage:
# my_list = [1, 2, 3]
# save_to_json_file(my_list, "my_list.json")
