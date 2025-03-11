#!/usr/bin/python3

"""
This script adds all command-line arguments to a Python list and saves the list
to a JSON file named `add_item.json`.

he script uses the `save_to_json_file` and `load_from_json_file` functions from
previous tasks to handle file operations.
"""

import sys
from os import path

# Import the functions from the previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Define the filename
filename = "add_item.json"

# Load the existing list from the alize an empty list if the file doesn't exist
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add the command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
