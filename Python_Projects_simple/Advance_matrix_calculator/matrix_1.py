import numpy as np
def matrix_1():
    matrix1=[]
    row=int(input("enter the number of rows you need for First matrix:-"))
    column=int(input("enter the number of columns you need for First matrix:-"))
    
    for i in range(row):
        count=0
        mat1_row=int(input(f"enter the number of {i+1},{count+1} elemnt in the matrix 1:-")) 
        matrix1.append(mat1_row)      
        for j in range(column-1):
            mat1_column=int(input(f"enter the number of {i+1},{j+2} elemnt in the matrix 1:-"))
            matrix1.append(mat1_column) 
    print("Matrix 1 is created sucessfully!!!!")
    matrix1=np.array(matrix1).reshape(row,column)
    return matrix1


