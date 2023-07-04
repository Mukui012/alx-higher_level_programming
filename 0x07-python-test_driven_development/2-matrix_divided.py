#!/usr/bin/python3
"""
Definition of module matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg_type)

    new_matrix = []
    len_m = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(msg_type)
        if len(lists) != len_m:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(msg_type)
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
