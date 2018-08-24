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

def filter_2d(im, kernel):
    '''
    Filter an image by taking the dot product of each 
    image neighborhood with the kernel matrix.
    Args:
    im = (H x W) grayscale floating point image
    kernel = (M x N) matrix, smaller than im
    Returns: 
    (H-M+1 x W-N+1) filtered image.
    '''

    M = kernel.shape[0] 
    N = kernel.shape[1]
    H = im.shape[0]
    W = im.shape[1]
    
    filtered_image = np.zeros((H-M+1, W-N+1), dtype = 'float64')
    
    for i in range(filtered_image.shape[0]):
        for j in range(filtered_image.shape[1]):
            image_patch = im[i:i+M, j:j+N]
            filtered_image[i, j] = np.sum(np.multiply(image_patch, kernel))
            
    return filtered_image

def make_gaussian_kernel(size, sigma):
    '''
    Create a gaussian kernel of size x size. 
    Args: 
    size = must be an odd positive number
    sigma = standard deviation of gaussian in pixels
    Returns: A floating point (size x size) guassian kernel 
    ''' 
    #Make kernel of zeros:
    kernel = np.zeros((size, size))

    #Handle sigma = 0 case (will result in dividing by zero below if unchecked)
    if sigma == 0:
        return kernel 
    
    #Helpful for indexing:
    k = int((size-1)/2)
    
    for i in range(size):
        for j in range(size):
            kernel[i, j] = (1/(2*np.pi*sigma**2))*np.exp(-((i-k)**2 + (j-k)**2)/(2*sigma**2))
            
    return kernel
