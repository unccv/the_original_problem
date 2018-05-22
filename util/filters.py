## ------------------------- ##
##
## filter.py
## Basic image processing utilties.
## 
##
## ------------------------- ##
import numpy as np


def roberts_cross(x):
    '''

    Compute Robert's Cross of input image x.
    Args: x: (nxm) grayscale floating point image
    Returns: (n-1) x (m-1) edge image. 

    '''

    #Confirm that x is 2-dimensional
    if x.ndim != 2:
        print('Input must be 2-dimensional, not processing!')
        return None
    
    edges = np.zeros((x.shape[0]-1,x.shape[1]-1)) #Our output will image will be one pixel smaller than our image

    for i in range(x.shape[0]-1):
        for j in range(x.shape[1]-1):
            #Grab Appropriate (2x2) image patch
            image_patch = x[i:i+2, j:j+2]
            # Compute Robert's Cross for image patch
            edges[i, j] = np.sqrt((image_patch[0,0] - image_patch[1, 1])**2 + 
                                   (image_patch[1, 0] - image_patch[0, 1])**2)
            
    return edges