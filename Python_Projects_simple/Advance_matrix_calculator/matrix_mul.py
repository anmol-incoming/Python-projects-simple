import numpy as np
def matrix_multiplication(matrix1,matrix2):
    if np.shape(matrix1)[1]==np.shape(matrix2)[0]:
        mat_mul=np.dot(matrix1,matrix2)
        return mat_mul
    else:
        message="Invalid matrix"
        return message