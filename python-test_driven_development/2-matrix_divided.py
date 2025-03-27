#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number
    
    Args:
        matrix: list of lists of integers/floats
        div: number to divide by (integer or float)
    
    Returns:
        new matrix with all elements divided by div, rounded to 2 decimal places
    
    Raises:
        TypeError: if matrix is not a list of lists of integers/floats,
                  or if rows are not the same size,
                  or if div is not a number
        ZeroDivisionError: if div is zero
    """
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if matrix is empty (should return empty list)
    if matrix == []:
        return []

    # Check if all elements are lists
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if matrix contains only empty lists (should return empty list)
    if all(len(row) == 0 for row in matrix):
        return []

    # Check if all elements are numbers
    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element by div and round to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]
