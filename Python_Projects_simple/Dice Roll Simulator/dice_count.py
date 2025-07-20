import numpy as np
def dice_count(m):
    dice_total=np.bincount(m,minlength=7)[1:]
    return dice_total