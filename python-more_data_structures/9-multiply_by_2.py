#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
