## ------------------------- ##
##
## hough_accumulator.py
## Hough acumulator class
## 
##
## ------------------------- ##

import numpy as np


class HoughAccumulator(object):
    def __init__(self, theta_bins: int, phi_bins: int, phi_min: int, phi_max: int):
        '''
        Simple class to implement an accumalator for the hough transform. 
        Args: 
        theta_bins = number of bins to use for theta
        phi_bins = number of bins to use for phi
        phi_max = maximum phi value to accumulate
        phi_min = minimu phi value to acumulate
        '''
        self.theta_bins = theta_bins
        self.phi_bins = phi_bins
        self.accumulator = np.zeros((self.phi_bins, self.theta_bins))

        # This covers all possible lines:
        theta_min = 0
        theta_max = np.pi

        # Compute the phi and theta values for the grids in our accumulator:
        self.rhos = np.linspace(phi_min, phi_max, self.accumulator.shape[0])
        self.thetas = np.linspace(theta_min, theta_max, self.accumulator.shape[1])

    def accumulate(self, x_coords: list, y_coords: list):
        '''
        Iterate through x and y coordinates, accumulate in hough space, and return. 
        Args: 
        x_coords = x-coordinates of points to transform
        y_coords = y-coordinats of points to transform

        Returns:
        accumulator = numpy array of accumulated values. 
        '''

        for i in range(len(x_coords)):
            # Grab a single point
            x = x_coords[i]  # TODO This was originally called 'x_coords_scaled'. Verify if a method needs to used to scale
            y = y_coords[i]  # TODO This was originally called 'y_coords_scaled'. Verify if a method needs to used to scale

            # Actually do transform!
            curve_prho = x * np.cos(self.thetas) + y * np.sin(self.thetas)

            for j in range(len(self.thetas)):
                # Make sure that the part of the curve falls within our accumulator
                if np.min(abs(curve_prho[j] - self.rhos)) <= 1.0:
                    # Find the cell our curve goes through:
                    rho_index = np.argmin(abs(curve_prho[j] - self.rhos))
                    self.accumulator[rho_index, j] += 1

        return self.accumulator

    def clear_accumulator(self):
        '''
        Zero out accumulator
        '''
        self.accumulator = np.zeros((self.phi_bins, self.theta_bins))
