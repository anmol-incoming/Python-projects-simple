from matrix_1 import matrix_1
from matrix_2 import matrix_2
from menu import menu

def main():
    matrix1,matrix2=matrix_1(),matrix_2()
    result=menu(matrix1,matrix2)
    print(result)
    
run=main()




