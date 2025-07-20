from dice_input import dice_input
from dice_vec import dice_vectoriztion
from dice_count import dice_count
import numpy as np
def main():
    n=dice_input()
    m=dice_vectoriztion(n)
    result=dice_count(m)
    print(f'The dice of 1 to 6 after running {n} simulation of rolling the result came out as :-')
    for i,j in enumerate(result,1):
        print(f'''{i} = {j}''')
    
main()