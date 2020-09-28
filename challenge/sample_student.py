## ---------------------------- ##
## 
## sample_student.py
##
## Example student submission for programming challenge. A few things: 
## 1. Before submitting, change the name of this file to your firstname_lastname.py.
## 2. Be sure not to change the name of the method below, classify.py
## 3. In this challenge, you are only permitted to import numpy and methods from 
##    the util module in this repository. Note that if you make any changes to your local 
##    util module, these won't be reflected in the util module that is imported by the 
##    auto grading algorithm. 
## 4. Anti-plagarism checks will be run on your submission
##
##
## ---------------------------- ##


import numpy as np
#It's kk to import whatever you want from the local util module if you would like:
#from util.X import ... 

def classify(im):
    '''
    Example submission for coding challenge. 
    
    Args: im (nxmx3) unsigned 8-bit color image 
    Returns: One of three strings: 'brick', 'ball', or 'cylinder'
    
    '''
    #im = imread(r"C:\Users\haris\images\ball_5.jpg");
    def convert_to_grayscale_image(im):
        gray_image=np.mean(im,axis=2);
        return gray_image;
    gray_img=convert_to_grayscale_image(im/255.)
    def make_gaussian_kernel(size, sigma):
    
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
    gaussian_kernel = make_gaussian_kernel(size = 40, sigma = 1.0)
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

        M, N = kernel.shape
        H, W = im.shape
        filtered_image = np.zeros((H-M+1, W-N+1), dtype = 'float64')

        for i in range(filtered_image.shape[0]):
            for j in range(filtered_image.shape[1]):
                image_patch = im[i:i+M, j:j+N]
                filtered_image[i, j] = np.sum(np.multiply(image_patch, kernel))

        return filtered_image
    
    filterd_image = filter_2d(gray_img,gaussian_kernel)
    
    #Implement Sobel kernels as numpy arrays
    Kx = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]])

    Ky = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]])
    Gx = filter_2d(filterd_image, Kx)

    Gy = filter_2d(filterd_image, Ky)

    G = np.sqrt(Gx**2+Gy**2)
    magnitude_sum=np.sum(G)
    
    G_direction = np.arctan2(Gy, Gx)
    
    def tune_thresh(thresh = 0):
        fig = figure(0, (8,8))
        imshow(G > thresh)
    
    thresh = 0.30
    edges_and_angles = np.zeros(G.shape)*np.NaN #Create empty array of NaNs
    #Replace pixels with gradient estimates above thresh with the direction of the gradient estimate:
    edges_and_angles[G>thresh] = G_direction[G>thresh]
    

    
    

    #Let's guess randomly! Maybe we'll get lucky.
    labels = ['brick', 'ball', 'cylinder']

    if magnitude_sum>4000:
        output_result = 'brick'
    elif 1800  <= magnitude_sum < 2800:
        output_result = 'ball'
    else:
        output_result = 'cylinder'
    
    return output_result
