#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_set = set(my_list)
    # Sum the unique integers
    return sum(unique_set)
