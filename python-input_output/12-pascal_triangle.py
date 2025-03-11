#!/usr/bin/python3

"""
This module provides a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the last row in the triangle
        new_row = [1]  # Start the new row with 1

        # Calculate the middle values
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # End the new row with 1
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle


# Example usage:
# print(pascal_triangle(5))
