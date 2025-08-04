import numpy as np
def matrix_transpose(matrix1,matrix2):
    choose_transpose=int(input("""Enter which matrix do you wanna transpose:-
                                    1.Matrix 1
                                    2.Matrix 2:-"""))
    if choose_transpose==1:
        return matrix1.T
    elif choose_transpose==2:
        return matrix2.T
    else:
        message="Invalid Input"
        return message
    