import numpy as np
def dice_vectoriztion(n):

    dice_simulate=np.random.randint(1,7,size=n)# this can work also
    #dice_simulate=np.random.choice([1,2,3,4,5,6],size=10)#this can also work choose any one

    return dice_simulate
