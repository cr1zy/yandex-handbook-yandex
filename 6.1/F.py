def multiplication_matrix(number):
    import numpy as np
    numbers = np.arange(1, number + 1)
    matrix = np.outer(numbers, numbers)
    return matrix

print(multiplication_matrix(3))
print(multiplication_matrix(5))