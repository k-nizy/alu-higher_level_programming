#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = []
    for row in matrix:
        # Square each element in the row and append to the new row
        new_row = [x ** 2 for x in row]
        new_matrix.append(new_row)
    return new_matrix
