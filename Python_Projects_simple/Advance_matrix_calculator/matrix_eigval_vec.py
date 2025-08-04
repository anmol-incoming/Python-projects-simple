import numpy as np
def matrix_eigen(matrix1,matrix2):
    choose_eigen=int(input("""Choose the matrix of which you want to calcuate eigen value and vector of :-
                                1.Matrix 1
                                2.Matrix 2"""))
    if choose_eigen==1:
        if np.shape(matrix1)[0]==np.shape(matrix1)[1]:
            value,vector=np.linalg.eig(matrix1)
            return f"""Eigen Values:- \n{value} \nEigen Vector:- \n{vector} """
        else:
            error_message="The Matrix Is not a square matrix try SVD instead."
            return error_message
    elif choose_eigen==2:
        if np.shape(matrix2)[0]==np.shape(matrix2)[1]:
            value,vector=np.linalg.eig(matrix2)
            return f"""Eigen Values:-\n{value}\nEigen Vector:- \n{vector} """
        else:
            error_message="The Matrix Is not a square matrix try SVD instead."
            return error_message
        
    else:
        message="Invalid Input"
        return message

        