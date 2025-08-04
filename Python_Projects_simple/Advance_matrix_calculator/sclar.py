def sclar_multiplication(matrix1,matrix2):
    sclar_input=int(input("Enter the number you want to Multiply in your matrix:-"))
    choose_sclar=int(input("""Enter which matrix do you wanna perfrom the operation on:-
                                    1.Matrix 1
                                    2.Matrix 2:-"""))
    if choose_sclar==1:
        sclar_cal=sclar_input*matrix1
        return sclar_cal
    elif choose_sclar==2:
        sclar_cal=sclar_input*matrix2
        return sclar_cal
    else:
        message="Invalid Input"
        return message

    
