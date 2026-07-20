def snake(width, height, direction="H"):
    import numpy as np
    arange = np.arange(1, width * height + 1, dtype="int16")
    matrix = arange.reshape(height, width)
    if direction == "H":
        matrix[1::2, ::] = matrix[1::2, ::-1]
    else:
        matrix = matrix.transpose()
        matrix.resize(height, width)
        matrix[::, 1::2] = matrix[::-1, 1::2]
    return matrix



print(snake(5, 3))