import numpy as np
def matrix_inverse(matrix1,matrix2):
    choose_inverse=int(input("""Choose the matrix you want to make inverse of :-
                                    1.Matrix 1
                                    2.Matrix 2:-"""))
    if choose_inverse==1:
        try:
            mat_inv=np.linalg.inv(matrix1)
            return mat_inv
        except np.linalg.LinAlgError:
            print("Matrix is singular or not a square matirx.Thus returning pseudoinverse Value.")
            mat_inv=np.linalg.pinv(matrix1)
            return mat_inv


    elif choose_inverse==2:
        try:
            mat_inv=np.linalg.inv(matrix2)
            return mat_inv
        except np.linalg.LinAlgError:
            print("Matrix is singular or not a square matirx.Thus returning pseudoinverse Value.")
            mat_inv=np.linalg.pinv(matrix2)
            return mat_inv
    else:
        message="Invalid Input"
        return message
        
            
    