#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        print()
    else:
        newmatrix = []
        newmatrix = [[(row[i]**2)for i in range(len(matrix))] for row \
                    in matrix]
    return(newmatrix)
