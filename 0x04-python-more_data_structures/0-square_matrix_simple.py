#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return(None)
    else:
        newmatrix = [[(r[i]**2)for i in range(len(matrix))] for r in matrix]
    return(newmatrix)
