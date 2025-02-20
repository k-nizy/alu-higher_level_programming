#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []
    for element in my_list:
        # Replace 'search' with 'replace' if the element matches
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
