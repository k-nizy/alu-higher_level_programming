#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys alphabetically
    for key in sorted(a_dictionary.keys()):
        # Print the key-value pair
        print("{}: {}".format(key, a_dictionary[key]))
