#!/usr/bin/python3

def square_matrix_map(matrix=None):
    if matrix is None:
        matrix = []

    return list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))
