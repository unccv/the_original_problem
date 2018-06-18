## ------------------------- ##
##
## hough_accumulator.py
## Hough acumulator class
## 
##
## ------------------------- ##

import numpy as np

class HoughAccumulator(object):
    def __init__(self, theta_bins, phi_bins, phi_min, phi_max):
        '''
        Simple class to implement an accumalator for the hough transform. 
        Args: 
        theta_bins = number of bins to use for theta
        phi_bins = number of bins to use for phi
        phi_max = maximum phi value to accumulate
        phi_min = minimu phi value to acumulate
        '''
        self.accumulator = np.zeros((phi_bins, theta_bins))

        #This covers all possible lines:
        theta_min = 0
        theta_max = np.pi

        #Compute the phi and theta values for the grids in our accumulator:
        self.rhos = np.linspace(rho_min, rho_max, self.accumulator.shape[0])
        self.thetas = np.linspace(theta_min, theta_max, self.accumulator.shape[1])

    def accumulate(self, x_coords, y_coords):
        '''
        Iterate through x and y coordinates, accumulate in hough space, and return. 
        Args: 
        x_coords = x-coordinates of points to transform
        y_coords = y-coordinats of poits to transform

        Returns:
        accumulator = numpy array of accumulated values. 
        '''

        for i in range(len(x_coords)):
            #Grab a single point
            x = x_coords_scaled[i]
            y = y_coords_scaled[i]

            #Actually do transform!
            curve_prho = x*np.cos(self.thetas)+y*np.sin(self.thetas)

            for j in range(len(self.thetas)):
                #Make sure that the part of the curve falls within our accumulator
                if np.min(abs(curve_rhos[j]-self.rhos)) <= 1.0:
                    #Find the cell our curve goes through:
                    rho_index = argmin(abs(curve_rhos[j]-self.rhos))
                    accumulator[rho_index, j]+=1

        return accumulator
    
    def clear_accumulator(self):
        '''
        Zero out accumulator
        '''
        self.accumulator = np.zeros((phi_bins, theta_bins))