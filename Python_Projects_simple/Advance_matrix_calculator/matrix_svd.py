import numpy as np
def matrix_svd(matrix1,matrix2):
    choose_svd=int(input("""Enter which matrix do you wanna perfrom svd on:-
                                    1.Matrix 1
                                    2.Matrix 2:-"""))
    if choose_svd==1:
        U,S,VT=np.linalg.svd(matrix1)
        return f"""U:\n{U}\nS:\n{S}\nVT:\n{VT} """
    elif choose_svd==2:
        U,S,VT=np.linalg.svd(matrix2)
        return f"""U:\n{U}\nS:\n{S}\nVT:\n{VT} """
    
    else:
        message="Invalid Input"
        return message 