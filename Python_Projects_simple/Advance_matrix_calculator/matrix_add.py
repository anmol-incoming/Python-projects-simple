import numpy as np
def matrix_addition(matrix1,matrix2):
    if np.shape(matrix1)!=np.shape(matrix2):
        message="Should have same number of rows and column in both the matrices."
        return message
    else:
        add_opp=matrix1+matrix2
        return add_opp
