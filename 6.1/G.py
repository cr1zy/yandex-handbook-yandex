def make_board(number):
    import numpy as np
    matrix = np.zeros((number, number), dtype="int8")
    matrix[::2, ::2] = 1
    matrix[1::2, 1::2] = 1
    return(matrix)


print(make_board(10))