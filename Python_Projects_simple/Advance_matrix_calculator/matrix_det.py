import numpy as np
def matrix_determinant(matrix1,matrix2):
    choose_determinant=int(input("""Choose the matrix whoose determinant you want to calculate:-
                                        1.Matrix 1
                                        2.Matrix 2:-"""))
    if choose_determinant==1:
        if np.shape(matrix1)[0]==np.shape(matrix1)[1]:
            return np.linalg.det(matrix1)
        else:
            error_message="For calculating determinant it should be a square martix eg-2,2 or 3,3 etc..."
            return error_message
    elif choose_determinant==2:
        if np.shape(matrix2)[0]==np.shape(matrix2)[1]:
            return np.linalg.det(matrix2)
        else:
            error_message="For calculating determinant it should be a square martix eg-2,2 or 3,3 etc..."
            return error_message
    else:
        message="Invalid Input"
        return message