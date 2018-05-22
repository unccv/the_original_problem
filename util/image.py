## ------------------------- ##
##
## image.py
## Basic image processing utilties.
## 
##
## ------------------------- ##

import numpy as np


def convert_to_grayscale(im):
    '''
    Convert color image to grayscale.
    Args: im = (nxmx3) floating point color image scaled between 0 and 1
    Returns: (nxm) floating point grayscale image scaled between 0 and 1
    '''
    return np.mean(im, axis = 2)


