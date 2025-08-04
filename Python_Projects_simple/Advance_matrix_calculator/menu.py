from matrix_add import  matrix_addition
from matrix_sub import matrix_subtraction
from matrix_mul import matrix_multiplication
from matrix_t import matrix_transpose
from matrix_det import matrix_determinant
from matrix_inv import matrix_inverse
from matrix_eigval_vec import matrix_eigen
from matrix_svd import matrix_svd
from sclar import sclar_multiplication
def menu(matrix1,matrix2):
    while True:
        a=int(input("""Enter the operation you want to perform:-
                        1.Matrix Addition
                        2.Matrix Subtraction
                        3.Matrix Multiplication
                        4.Matrix Transpose
                        5.Matrix Determinent
                        6.Matrix Inverse
                        7.Eigen Values and  Eigen Vetors
                        8.SVD
                        9.Sclar Multiplication
                        10.Exit / Work on new matrix:-"""))
        if a==1:
            print(matrix_addition(matrix1,matrix2) )           
        elif a==2:
            print(matrix_subtraction(matrix1,matrix2))
        elif a==3:
            print(matrix_multiplication(matrix1,matrix2))
        elif a==4:
            print(matrix_transpose(matrix1,matrix2))
        elif a==5:
            print(matrix_determinant(matrix1,matrix2))
        elif a==6:
            print(matrix_inverse(matrix1,matrix2))
        elif a==7:
            print(matrix_eigen(matrix1,matrix2))
        elif a==8:
            print(matrix_svd(matrix1,matrix2))
        elif a==9:
            print(sclar_multiplication(matrix1,matrix2))
        elif a==10:
            exit_message="Exited successfully"
            return exit_message
        else:
            print("Invalid Input")
    