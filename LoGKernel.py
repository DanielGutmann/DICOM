from math import pi
from scipy import ndimage
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt

import numpy as np
# LoG=LoGcontatnt*(r^2/sigma^2 -3)*e^-r^2/(2*sigma^2) ,where r is in [mm]

class LoG3D(object):
    def __init__(self, sigma):
        three_sigma = 3.0 * sigma
        self.sigma = sigma
        self.x = np.linspace(-three_sigma, three_sigma, three_sigma * 10)
        # self.y = np.arange(-three_sigma, three_sigma, 0.2)
        #self.z = np.arange(-three_sigma, three_sigma, 0.2)

        self.X, self.Y, self.Z = np.meshgrid(self.x, self.x, self.x)


    def get_LoG(self):
        sigma_square = self.sigma ** 2
        LoGcontant = 1.0 / (2.0 * pi * (sigma_square ** 2))
        R_square = self.X ** 2 + self.Y ** 2 + self.Z ** 2

        exponenta = np.exp(-R_square / (2 * sigma_square))
        LoG = LoGcontant * (R_square / sigma_square - 2) * exponenta
        LoG_normalized = LoG / np.sum(LoG)

        return LoG_normalized

    def get_grid_x_y_z(self):
        return self.x, self.x, self.x


class LoG2D(object):
    def __init__(self, sigma):
        three_sigma = 3.0 * sigma
        self.sigma = sigma
        self.x = np.linspace(-three_sigma, three_sigma, three_sigma * 10+(three_sigma-1)%2)
        # self.y = np.linspace(-three_sigma, three_sigma, three_sigma*10+(three_sigma-1)%2)

        self.X, self.Y = np.meshgrid(self.x, self.x)


    def get_LoG(self):
        sigma_square = self.sigma ** 2
        LoGcontant = 1.0 / (2.0 * pi * (sigma_square ** 2))
        R_square = self.X ** 2 + self.Y ** 2

        exponenta = np.exp(-R_square / (2 * sigma_square))
        LoG = LoGcontant * (R_square / sigma_square - 2) * exponenta
        LoG_normalized = LoG / np.sum(LoG)
        print np.sum(LoG_normalized)
        return LoG_normalized

    def get_grid_x_y(self):
        return self.x, self.x
