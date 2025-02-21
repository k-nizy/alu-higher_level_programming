#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is empty or None
    if not a_dictionary:
        return None

    # Find the key with the maximum value
    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key
