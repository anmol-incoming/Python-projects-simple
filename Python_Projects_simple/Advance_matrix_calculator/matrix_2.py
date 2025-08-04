import numpy as np
def matrix_2():
    matrix2=[]
    row=int(input("enter the number of rows you need for second matrix:-"))
    column=int(input("enter the number of columns you need for second matrix:-"))
    
    for i in range(row):
        count=0
        mat2_row=int(input(f"enter the number of {i+1},{count+1} elemnt in the matrix 2:-")) 
        matrix2.append(mat2_row)      
        for j in range(column-1):
            mat2_column=int(input(f"enter the number of {i+1},{j+2} elemnt in the matrix 2:-"))
            matrix2.append(mat2_column) 
    print("Matrix 2 is created sucessfully!!!!")
    matrix2=np.array(matrix2).reshape(row,column)
    return matrix2


